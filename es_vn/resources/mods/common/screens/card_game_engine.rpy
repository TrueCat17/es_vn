init python:
	class Card:
		def __init__(self, name, visible):
			self.name = name
			self.visible = visible
			
			self.hot = False
			self.interesting = False
			self.allow = False
			
			self.x = self.old_x = self.new_x = (screen_width  - card_width ) / 2
			self.y = self.old_y = self.new_y = (screen_height - card_height) / 2
			self.dy = 0
			self.time = None
		
		def set_pos(self, x, y):
			if (self.new_x, self.new_y) == (x, y):
				return
			
			dx = self.x - x
			dy = self.y + self.dy - y
			distance = (dx * dx + dy * dy) ** 0.5
			self.time = card_time_koef * (distance ** 0.25)
			self.start_time = get_game_time()
			
			self.old_x = self.x
			self.old_y = self.y + self.dy
			self.new_x = x
			self.new_y = y
			self.dy = 0
		
		def update(self):
			if self.time is None:
				return
			
			dtime = get_game_time() - self.start_time
			k = dtime / self.time
			if k > 1:
				k = 1
				self.time = None
			
			self.x = (self.new_x - self.old_x) * k + self.old_x
			self.y = (self.new_y - self.old_y) * k + self.old_y
	
	
	screen_width  = 1920
	screen_height = 1080
	
	n_cards    = 7
	n_xchanges = 2
	n_cycles   = 3
	
	
	card_prefix = 'images/cards/'
	card_types  = ('2ch', 'ussr', 'utan', 'uvao')
	card_suffix = '.webp'
	card_width       = 210
	card_height      = 315
	card_dx          = 225
	card_left_dx     = 50
	card_top_dy      = 50
	button_dx        = 0
	button_dy        = 0
	bottom_dy        = 0
	bottom_dy_result = 0
	
	card_size = (card_width / screen_width, card_height / screen_height)
	
	card_bottom_dy = screen_height - card_top_dy - card_height - bottom_dy
	
	cards_bg	   = im.Sepia('images/bg/int_dining_hall_day.jpg')
	cards_text_back = im.rect('#404040')
	
	card_time_koef = 1 / 7
	
	VISIBLE   = True
	INVISIBLE = False
	
	
	name_of_none = (0, 'none')
	
	def get_img(img):
		return im.Scale(card_prefix + img + card_suffix, card_width, card_height)
	
	
	arrow_width = 50
	
	ints = list(range(1, 14))
	card_img = {}
	card_img['cover'] = get_img('cover')
	card_img[name_of_none] = im.rect('#0000')
	
	for i in ints:
		for j in card_types:
			name = '%d_%s' % (i, j)
			card_img[(i, j)] = get_img(name)
	
	def generate_cards(dialogs):
		global game_interuptions
		global cards_rival
		global cards_my
		global cycles_left
		global changes_left
		global cards_state, cards_state_old
		global cards_answer
		global result_status
		
		game_interuptions = dialogs
		cycles_left  = n_cycles
		changes_left = n_xchanges
		cards_state = 'init'
		cards_state_old = None
		cards_answer = None
		result_status = 'in_progress'
		
		k = 0
		cset = []
		while k < 2 * n_cards:
			name = (renpy.random.randint(1, 13), card_types[renpy.random.randint(0, 3)])
			if not name in cset:
				cset.append(name)
				k += 1
		
		cards_rival = [Card(cset[i],		 'INVISIBLE') for i in range(n_cards)]
		cards_my	= [Card(cset[n_cards + i], 'VISIBLE') for i in range(n_cards)]
		
		cards_rival[0].name = name_of_none
		cards_my   [0].name = name_of_none
		
		renpy.music.play('sound/sfx/cardgame/new/deal_card_%s.ogg' % random.randint(1, 4), channel = 'sound')
		
		show_screen('card_engine')
	
	def move_buttons(setk, k, setj, j):
		for card in cards_rival + cards_my:
			card.interesting = False
			card.hot = False
		setk[k].hot = setj[j].hot = True
		setk[k], setj[j] = setj[j], setk[k]
	
	def xchange_cards():
		cards_my[my_card].visible = 'INVISIBLE'
		cards_rival[rival_card].visible = 'VISIBLE'
		move_buttons(cards_my, my_card, cards_rival, rival_card)
		
		renpy.music.play('sound/sfx/cardgame/new/take_card_%s.ogg' % random.randint(1, 3), channel = 'sound')
	
	def interuption_region():
		global cards_state, cards_state_old
		
		if cards_state == 'me_select_1':
			renpy.music.play('sound/sfx/cardgame/new/choose_card_2.ogg', channel = 'sound')
		
		elif cards_state == 'rival_defend':
			renpy.music.play('sound/sfx/cardgame/new/choose_card_1.ogg', channel = 'sound')
		
		position = (cycles_left, cards_state, 'call')
		if position in game_interuptions:
			cards_state_old = cards_state
			cards_state = 'interuption'
			renpy.call(game_interuptions[position])
			del game_interuptions[position]
			return True
		
		position = (cycles_left, cards_state, 'jump')
		if position in game_interuptions:
			cards_state = 'interuption'
			renpy.jump(game_interuptions[position])
			return True
		
		return False
	
	def card_value(x):
		if x.name[0] == 1:
			return 14
		return x.name[0]
	
	def what_category(cardset):
		ans = []
		summ = 0
		for card in cardset:
			card.interesting = False
		
		for len in (4, 3, 2):
			for i in range(n_cards - len + 1):
				if cardset[i].interesting:
					continue
				
				val = card_value(cardset[i])
				for j in range(i + 1, i + len):
					if card_value(cardset[j]) != card_value(cardset[i]):
						break
				else:
					for j in range(i, i + len):
						cardset[j].interesting = True
					ans.append([len, val])
					summ += len
		
		if summ:
			return summ, ans
		
		cardset[n_cards - 1].interesting = True
		return 1, [[1, card_value(cardset[n_cards - 1])]]
	
	def cmpset(a, b):
		if a[0] != b[0]:
			return b[0] - a[0]
		return b[1] - a[1]
	
	def compare_sets(result_my, gr_my, result_rival, gr_rival):
		if result_my > result_rival:
			return 'win'
		if result_my < result_rival:
			return 'fail'
		
		if len(gr_my) < len(gr_rival):
			return 'win'
		if len(gr_my) > len(gr_rival):
			return 'fail'
		
		for i in range(len(gr_my)):
			if gr_my[i][0] > gr_rival[i][0]:
				return 'win'
			if gr_my[i][0] < gr_rival[i][0]:
				return 'fail'
			
			if gr_my[i][1] > gr_rival[i][1]:
				return 'win'
			if gr_my[i][1] < gr_rival[i][1]:
				return 'fail'
		
		return 'draw'
	
	def count_score():
		from functools import cmp_to_key
		
		def cmp(a, b):
			a = card_value(a)
			b = card_value(b)
			if a < b: return -1
			if a > b: return +1
			return 0
		cards_rival.sort(key = cmp_to_key(cmp))
		cards_my.sort(key = cmp_to_key(cmp))
		
		result_my,    gr_my    = what_category(cards_my)
		result_rival, gr_rival = what_category(cards_rival)
		
		gr_my.sort(key = cmp_to_key(cmpset))
		gr_rival.sort(key = cmp_to_key(cmpset))
		
		return compare_sets(result_my, gr_my, result_rival, gr_rival)
	
	
	def get_cards_to_draw():
		cache = get_cards_to_draw.__dict__
		
		res = []
		for cards, owner in ((cards_rival, 'rival'), (cards_my, 'my')):
			for i, card in enumerate(cards):
				x = card_dx * i + card_left_dx
				y = (card_top_dy if owner == 'rival' else card_bottom_dy)
				card.set_pos(x, y)
				
				card.update()
				
				tmp_answer = None
				if owner == 'rival':
					if cards_state == 'me_select_2' and card.allow:
						tmp_answer = ('rival', i)
				else:
					if cards_state in ('me_defend_1', 'me_defend_2', 'rival_select') or (cards_state == 'me_select_2' and i == my_card):
						tmp_answer = ('my', i)
				
				if (card.visible == 'VISIBLE' and VISIBLE) or (card.visible == 'INVISIBLE' and INVISIBLE) or card.name == name_of_none:
					ground = card_img[card.name]
				else:
					ground = card_img['cover']
				
				key = (ground, tmp_answer is None)
				if not tmp_answer:
					if key not in cache:
						cache[key] = im.MatrixColor(ground, im.matrix.saturation(0.1))
					ground = hover = cache[key]
				else:
					if key not in cache:
						cache[key] = im.MatrixColor(ground, im.matrix.brightness(0.1) * im.matrix.saturation(1.5))
					hover = cache[key]
				
				if card.time:
					hover = ground
					tmp_answer = None
				
				res.append((card, ground, hover, tmp_answer))
		return res
	
	def get_game_phase():
		state = cards_state if cards_state != 'interuption' else cards_state_old
		
		if state in ('me_defend_1', 'me_defend_2', 'rival_defend'):
			return 'Защита'
		if state == 'me_select_1':
			return 'Сброс'
		if state in ('me_select_2', 'rival_select'):
			return 'Захват'
		if state in ('me_get', 'rival_get'):
			return 'Вытягивание'
		if state == 'results':
			return 'Результаты'
		return '---' # error
	
	
	def cards_update():
		global cards_state
		global cards_answer, cards_answer_prev
		global changes_left, cycles_left
		global my_card, rival_card
		
		for card in cards_rival + cards_my:
			if card.time is not None:
				return
		
		if interuption_region():
			return
		
		if cards_state == 'init':
			cards_state = 'rival_select'
			cards_answer = None
			renpy.pause(1)
			return
		
		if cards_state == 'rival_select':
			my_card = rival.pick_my_card()
			if my_card < 0:
				return
			
			for card in cards_rival + cards_my:
				card.interesting = False
			cards_my[my_card].interesting = True
			
			if rival.allow_to_defend():
				cards_state = 'me_defend_1'
			else:
				cards_state = 'rival_get'
			
			renpy.pause(1)
			return
		
		if cards_state == 'me_defend_1':
			if not cards_answer:
				return
			
			if cards_answer == 'end_of_turn':
				cards_state = 'rival_get'
			else:
				cards_state = 'me_defend_2'
				
				owner, index = cards_answer
				cards_my[index].dy = -40
				cards_answer_prev = index
			
			cards_answer = None
			return
		
		if cards_state == 'me_defend_2':
			if not cards_answer:
				return
			
			if cards_answer == 'end_of_turn':
				cards_state = 'rival_get'
			else:
				owner, index = cards_answer
				if cards_answer_prev == index:
					cards_state = 'me_defend_1'
				else:
					move_buttons(cards_my, cards_answer_prev, cards_my, index)
					changes_left -= 1
					if changes_left == 0:
						cards_state = 'rival_get'
					else:
						cards_state = 'rival_select'
			
			cards_answer = None
			return
		
		if cards_state == 'rival_get':
			if changes_left == 0:
				my_card = rival.pick_my_card_last()
			for card in cards_rival + cards_my:
				card.interesting = False
			cards_my[my_card].interesting = True
			
			for i, card in enumerate(cards_rival):
				if card.name == name_of_none:
					rival_card = i
			
			xchange_cards()
			changes_left = n_xchanges
			rival.allow_to_take()
			cards_state = 'me_select_1'
			return
		
		if cards_state == 'me_select_1':
			for i, card in enumerate(cards_my):
				if card.name == name_of_none:
					my_card = i
			cards_state = 'me_select_2'
			return
		
		if cards_state == 'me_select_2':
			if not cards_answer:
				return
			
			owner, index = cards_answer
			if owner == 'my':
				cards_state = 'me_select_1'
			else:
				rival_card = index
				for card in cards_rival + cards_my:
					card.interesting = False
				cards_rival[index].interesting = True
				cards_state = 'rival_defend'
			
			cards_answer = None
			return
		
		if cards_state == 'rival_defend':
			if changes_left == 0:
				cards_state = 'me_get'
				return
			
			if not rival.want_to_defend():
				changes_left = 0
				cards_state = 'me_get'
			else:
				changes_left -= 1
				i, j = rival.what_to_xchange()
				move_buttons(cards_rival, i, cards_rival, j)
				cards_rival[i].interesting, cards_rival[j].interesting = cards_rival[j].interesting, cards_rival[i].interesting
				cards_state = 'me_select_2'
			return
		
		if cards_state == 'me_get':
			xchange_cards()
			cycles_left -= 1
			if cycles_left:
				changes_left = n_xchanges
				cards_state = 'rival_select'
				cards_answer = None
			else:
				cards_state = 'results'
			return
		
		if cards_state == 'results':
			for card in cards_rival + cards_my:
				card.visible = 'VISIBLE'
			cards_state = '_' + count_score()
			return


label cards_gameloop:
	while True:
		$ cards_update()
		pause 0.1
		
		if cards_state_old:
			$ cards_state, cards_state_old = cards_state_old, None


init:
	style cards_text_back is image:
		xalign 0.5
		xsize 210 / 1920
		ysize 50 / 1080
	
	style cards_text is text:
		align 0.5
		color '#C8C8C8'
		text_align 'center'
		text_size 0.023

screen card_engine:
	zorder -4 if db.visible or sprites.list else 0
	
	image cards_bg:
		size 1.0
	
	for card, ground, hover, tmp_answer in get_cards_to_draw():
		button:
			action 'cards_answer = tmp_answer' if tmp_answer else None
			mouse   tmp_answer is not None
			
			corner_sizes 0
			ground ground
			hover  hover
			
			size card_size
			
			xpos card.x / screen_width
			ypos (card.y + card.dy) / screen_height
			
			if card.interesting:
				$ arrow = 'up' if card in cards_rival else 'down'
				
				image ('images/misc/' + arrow + '.webp'):
					xalign 0.5
					ypos int(((card_height + 20) if arrow == 'up' else -100) / screen_height * get_stage_height())
					
					xsize 50 / 1920
					ysize 50 / 1080
	
	if cards_state in ('_win', '_draw', '_fail'):
		python:
			if cards_state == '_win':
				tmp = 'Победа'
			elif cards_state == '_draw':
				tmp = 'Ничья'
			else:
				tmp = 'FAIL'
		
		textbutton tmp:
			align 0.5
			size (0.15, 0.08)
			
			text_size 72 / 1080
			color '#C8FFFF'
			
			ground im.rect('#000')
			hover  im.rect('#555')
			
			action 'cards_state = cards_state[1:]'
	
	if not (db.visible or sprites.list):
		use card_engine_info

screen card_engine_info:
	vbox:
		xanchor 1.0
		xpos (1920 - 65) / 1920
		ypos 65 / 1080
		spacing 15 / 1080
		
		image 'images/avatars/back.webp':
			xalign 0.5
			xsize 210 / 1920
			ysize 210 / 1080
			
			image rival.avatar:
				align 0.5
				xsize 200 / 1920
				ysize 200 / 1080
		
		image cards_text_back:
			style 'cards_text_back'
			
			text ('Соперник:\n%s' % rival.name):
				style 'cards_text'
	
	vbox:
		anchor 1.0
		xpos (1920 - 65) / 1920
		ypos (1080 - 65) / 1080
		spacing 30 / 1080
		
		image cards_text_back:
			style 'cards_text_back'
			
			python:
				if cards_state.startswith('me_'):
					tmp = 'Твой'
				elif cards_state.startswith('rival_'):
					tmp = 'Чужой'
				else:
					tmp = '---'
			text ('Чей ход:\n' + tmp):
				style 'cards_text'
		
		image cards_text_back:
			style 'cards_text_back'
			
			text ('Фаза игры:\n' + get_game_phase()):
				style 'cards_text'
			
			if cards_state in ('me_defend_1', 'me_defend_2'):
				textbutton 'X':
					ground im.rect('#00000002')
					hover  im.rect('#00000002')
					
					color '#C8FFFF'
					hover_color '#FF0000'
					
					text_size 0.025
					xsize 40 / 1920
					ysize 40 / 1080
					align (1.0, 0.5)
					
					action "cards_answer = 'end_of_turn'"
		
		image cards_text_back:
			style 'cards_text_back'
			
			text ('Кругов осталось:\n%s' % cycles_left):
				style 'cards_text'
		
		image cards_text_back:
			style 'cards_text_back'
			
			text ('Обменов осталось:\n%s' % (changes_left or '---')):
				style 'cards_text'
