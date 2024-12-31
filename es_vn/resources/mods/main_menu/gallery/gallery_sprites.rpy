init python:
	spr_emo_list = [
		('guilty',       'Вина'),
		('sad',          'Грусть'),
		('angry',        'Злость'),
		('evil_smile',   'Злобная улыбка'),
		('scared',       'Испуг'),
		('dontlike',     'Недовольство'),
		('tender',       'Нежность'),
		('upset',        'Огорчение'),
		('serious',      'Серьёзность'),
		('cry',          'Слёзы'),
		('cry2',         'Слёзы2'),
		('laugh',        'Смех'),
		('laugh2',       'Смех2'),
		('shy',          'Смущение'),
		('shy2',         'Смущение2'),
		('calml',        'Спокойно'),
		('normal',       'Спокойствие'),
		('fear',         'Страх'),
		('happy',        'Счастье'),
		('surprise',     'Удивление'),
		('surprise2',    'Удивление2'),
		('surp1',        'Удивление'),
		('surp2',        'Удивление2'),
		('surp3',        'Удивление3'),
		('bukal',        'Удивление'),
		('cry_smile',    'Улыбка\nсо слезами'),
		('normal_smile', 'Улыбка2'),
		('smile',        'Улыбка'),
		('smile2',       'Улыбка2'),
		('smile3',       'Улыбка3'),
		('grin',         'Ухмылка'),
		('fingal',       'Фингал'),
		('shocked',      'Шок'),
		('rage',         'Ярость'),
	]
	
	spr_dress_list = [
		('dress',    'Платье'),
		('pioneer',  'Пионерская\nформа'),
		('pioneer2', 'Пионерская\nформа2'),
		('swim',     'Купальник'),
		('sport',    'Спортивная\nформа'),
	]

	spr_acc_list = [
		('glasses',     'Очки'),
		('panama',      'Панама'),
		('stethoscope', 'Стетоскоп'),
	]
	
	
	def parse_sprites():
		global spr_character_images
		spr_character_images = {}
		
		content = open('mods/common/sprites.rpy', 'rb').read().decode('utf-8')
		for s in content.split('\n'):
			if 'close' in s or 'far' in s: continue
			
			i = s.find('image ')
			if i == -1: continue
			
			s = s[i + len('image '):]
			i = s.find('=')
			if i == -1: continue
			
			image_name = s[:i].strip()
			if not image_was_registered(image_name): continue
			
			character_name = image_name.split(' ')[0]
			character_sprites = spr_character_images.setdefault(character_name, {})
			
			cmds = get_image(image_name)
			character_sprites[image_name] = cmds[0]
		
		t = [(name, str(globals()[name])) for name in spr_character_images]
		t.sort(key = lambda pair: pair[1])
		
		global spr_character_list, spr_character_text_list
		spr_character_list =      [name for name, text in t]
		spr_character_text_list = [text for name, text in t]
	
	def parse_sprites_on_show_gallery(screen_name):
		if screen_name == 'gallery':
			set_timeout(parse_sprites, 0.5)
	signals.add('show_screen', parse_sprites_on_show_gallery)
	
	
	choice_menu_show_db_btns = False
	in_gallery_sprite_show = False
	
	spr_character = ''
	spr_dress = ''
	spr_emo = ''
	spr_acc = ''
	
	spr_character_text = ''
	spr_dress_text = ''
	spr_emo_text = ''
	spr_acc_text = ''
	
	spr_cur_dress_list = []
	spr_cur_emo_list = []
	spr_cur_dress_text_list = []
	spr_cur_emo_text_list = []
	spr_cur_emo_image_list = []
	
	spr_character_index = None
	spr_dress_index = None
	spr_emo_index = None
	
	gallery_sprite_image = ''
	gallery_sprite_image_prev = ''
	
	def spr_ask_character():
		global choice_menu_variants, call_screen_name, call_ret_name
		choice_menu_variants = spr_character_text_list
		call_screen_name = 'choice_menu'
		call_ret_name = 'spr_character_index'
		show_screen(call_screen_name)
		
		global spr_character, spr_dress, spr_emo
		spr_character, spr_dress, spr_emo = '', '', ''
		
		global spr_character_text, spr_dress_text, spr_emo_text
		spr_character_text, spr_dress_text, spr_emo_text = '', '', ''
		
		global gallery_sprite_image
		gallery_sprite_image = ''
	
	def spr_ask_dress():
		if not spr_character or not spr_cur_dress_list:
			return
		
		global choice_menu_variants, call_screen_name, call_ret_name
		choice_menu_variants = [s.replace('\n', ' ') for s in spr_cur_dress_text_list]
		call_screen_name = 'choice_menu'
		call_ret_name = 'spr_dress_index'
		show_screen(call_screen_name)
		
		global spr_dress, spr_emo, spr_acc
		spr_dress, spr_emo, spr_acc = '', '', ''
		
		global spr_dress_text, spr_emo_text, spr_acc_text
		spr_dress_text, spr_emo_text, spr_acc_text = '', '', ''
		
		global gallery_sprite_image
		gallery_sprite_image = ''
	
	def spr_ask_emo():
		if (not spr_dress and spr_cur_dress_list) or not spr_cur_emo_list:
			return
		
		global choice_menu_variants, call_screen_name, call_ret_name
		choice_menu_variants = [s.replace('\n', ' ') for s in spr_cur_emo_text_list]
		call_screen_name = 'choice_menu'
		call_ret_name = 'spr_emo_index'
		show_screen(call_screen_name)
		
		global spr_emo, spr_emo_text
		spr_emo, spr_emo_text = '', ''
		
		global gallery_sprite_image
		gallery_sprite_image = ''
	
	
	def on_variant_selected(screen_name):
		if screen_name != 'choice_menu':
			return
		
		global spr_character_index, spr_dress_index, spr_emo_index
		
		global spr_character, spr_dress, spr_emo
		global spr_character_text, spr_dress_text, spr_emo_text
		
		global spr_cur_dress_list, spr_cur_emo_list
		global spr_cur_dress_text_list, spr_cur_emo_text_list, spr_cur_emo_image_list
		
		set_emo = False
		
		if type(spr_character_index) is int:
			spr_character      = spr_character_list[     spr_character_index]
			spr_character_text = spr_character_text_list[spr_character_index]
			spr_character_index = None
			
			t = set()
			for dress_name, dress_text in spr_dress_list:
				for image_name in spr_character_images[spr_character]:
					if dress_name in image_name:
						t.add((dress_text, dress_name))
						break
			t = sorted(t)
			spr_cur_dress_list      = [dress_name for dress_text, dress_name in t]
			spr_cur_dress_text_list = [dress_text for dress_text, dress_name in t]
			
			if not spr_cur_dress_list:
				set_emo = True
		
		
		if type(spr_dress_index) is int:
			spr_dress      = spr_cur_dress_list[     spr_dress_index]
			spr_dress_text = spr_cur_dress_text_list[spr_dress_index]
			spr_dress_index = None
			set_emo = True
		
		if set_emo:
			t = set()
			for emo_name, emo_text in spr_emo_list:
				for image_name in spr_character_images[spr_character]:
					if spr_dress   not in image_name: continue
					if spr_dress + '2' in image_name: continue
					
					if ' ' + emo_name   not in image_name: continue
					if ' ' + emo_name + '2' in image_name: continue
					if ' ' + emo_name + '3' in image_name: continue
					
					for acc_name, acc_text in spr_acc_list:
						if acc_name in image_name:
							t.add((emo_text + '\n(+' + acc_text + ')', emo_name, image_name))
							break
					else:
						t.add((emo_text, emo_name, image_name))
			
			def my_key(value):
				text = value[0]
				
				prefix = ''
				for _acc_name, acc_text in spr_acc_list:
					if acc_text in text:
						prefix = acc_text
				
				return prefix, text
			
			t = sorted(t, key = my_key)
			
			spr_cur_emo_list       = [emo_name   for emo_text, emo_name, image_name in t]
			spr_cur_emo_text_list  = [emo_text   for emo_text, emo_name, image_name in t]
			spr_cur_emo_image_list = [image_name for emo_text, emo_name, image_name in t]
		
		
		if type(spr_emo_index) is int:
			spr_emo       = spr_cur_emo_list[      spr_emo_index]
			spr_emo_text  = spr_cur_emo_text_list[ spr_emo_index]
			
			global gallery_sprite_image
			gallery_sprite_image = spr_cur_emo_image_list[spr_emo_index]
			
			spr_emo_index = None
			
			if not in_gallery_sprite_show:
				renpy.call('gallery_sprite_show')
	
	signals.add('hide_screen', on_variant_selected)
	
	
	def on_show_gallery(screen_name):
		if screen_name == 'gallery' and gallery_type == 'СПРАЙТЫ' and gallery_sprite_image:
			renpy.call('gallery_sprite_show')
	signals.add('show_screen', on_show_gallery)
	
	def spr_get_dress():
		if not spr_character:
			return ''
		if not spr_cur_dress_list:
			return 'Стандартная'
		return spr_dress_text


label gallery_sprite_show:
	$ in_gallery_sprite_show = True
	
	image transparent_scene = ''
	image gallery_sprite = gallery_sprite_image
	
	$ gallery_sprite_image_prev = ''
	while has_screen('gallery') and gallery_type == 'СПРАЙТЫ':
		if gallery_sprite_image_prev != gallery_sprite_image:
			$ gallery_sprite_image_prev = gallery_sprite_image
			scene transparent_scene
			show gallery_sprite at center
			with dspr
		pause 0.01
	
	hide gallery_sprite with dspr
	
	$ in_gallery_sprite_show = False


init:
	style spr_text is text:
		font 'CenturyGothic'
		color '#909CA3'
		text_size 32 / 1080
		
		xpos 50 / 1920
		xsize 270 / 1920
		ysize 80 / 1080
		text_valign 'center'
	
	style spr_btn is title_btn:
		anchor 0
		text_size 32 / 1080
		text_align 'left'


screen gallery_sprites:
	if gallery_type_prev != 'СПРАЙТЫ' and gallery_sprite_image:
		$ renpy.call('gallery_sprite_show')
	
	vbox:
		xpos 45 / 1920
		ypos 280 / 1080
		
		textbutton 'Спрайт':
			style 'spr_btn'
			action spr_ask_character
		
		text spr_character_text:
			style 'spr_text'
		
		textbutton 'Одежда':
			style 'spr_btn'
			action spr_ask_dress
		
		text spr_get_dress():
			style 'spr_text'
		
		textbutton 'Эмоция':
			style 'spr_btn'
			action spr_ask_emo
		
		text spr_emo_text:
			style 'spr_text'
