init python:
	credits_text = '\n\n'.join([
		"Команда Soviet Games (IIchan Eroge Team) благодарит вас за время, уделённое игре!",
		"Благодарности:",
		"PyTom'у за движок Ren'Py.",
		"Сайту freesounds.org за бесплатные звуки.",
		"Сайтам iichan.hk и 2ch.hk.",
		"Паблику vk.com/everlasting.summer.official",
		"Всем, кто помогал работать над игрой.",
		"Всем, кто нас поддерживал все эти годы, ждал и верил!",
		"",
		"",
		"{size=80}КОНЕЦ.{/size}",
	])
	
	def show_credits():
		global credits_show_time
		credits_show_time = get_game_time()
		show_screen('credits')
	
	def get_credits_ypos():
		ystart = 1.3
		yend = -1.2
		dtime = get_game_time() - credits_show_time
		if dtime > 87:
			hide_screen('credits')
		return ystart + (yend - ystart) * dtime / 87

screen credits:
	text credits_text:
		font 'Corbel'
		text_size 50 / 1080
		
		color        '#FFF'
		outlinecolor '#000'
		
		text_align 'center'
		xalign 0.5
		xsize 0.8
		
		ypos get_credits_ypos()