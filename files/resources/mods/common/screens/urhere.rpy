init python:
	urhere_text = 'Ты здесь не просто так'
	
	urhere_params = [
	#   startx endx  y  time  italic size  color
		[-0.5, 1.5, 0.3, 4.0,  True,  40, '#EEE', ],
		[-0.5, 1.5, 0.1, 3.0, False,  80, '#111', ],
		[-0.5, 1.5, 0.7, 5.0, False,  60, '#A3D', ],
		[-0.5, 1.5, 0.5, 4.0, False, 100, '#E34', ],
		[-0.5, 1.5, 0.8, 3.0, False,  50, '#D00', ],
		
		[1.0, -1.0, 0.1, 4.0,  True,  60, '#E01', ],
		[1.0, -1.0, 0.3, 3.0, False,  30, '#AD5', ],
		[1.0, -1.0, 0.8, 5.0,  True,  90, '#F54', ],
		[1.0, -1.0, 0.6, 4.0, False,  65, '#D10', ],
		[1.0, -1.0, 0.4, 3.5,  True,  30, '#EE1', ],
	]
	
	def urhere_show():
		global urhere_time_show, urhere_time_hide
		urhere_time_show = get_game_time()
		urhere_time_hide = None
		show_screen('urhere')
	def urhere_hide():
		global urhere_time_hide
		urhere_time_hide = get_game_time()
	
	urhere_appearance_time = 1.0
	urhere_disappearance_time = 1.0


screen urhere:
	python:
		if urhere_time_hide is None:
			alpha = (get_game_time() - urhere_time_show) / urhere_appearance_time
		else:
			alpha = 1 - (get_game_time() - urhere_time_hide) / urhere_disappearance_time
			if alpha < 0:
				hide_screen('urhere')
	alpha in_bounds(alpha, 0, 1)
	zorder -3
	
	image im.rect('#FFF'):
		size 1.0
	
	$ sw = get_stage_width()
	for startx, endx, y, move_time, italic, size, color in urhere_params:
		$ dtime = (get_game_time() - urhere_time_show) % move_time
		$ x = int((startx + (endx - startx) * dtime / move_time) * sw)
		
		text urhere_text:
			pos (x, y)
			
			color color
			outlinecolor 0
			
			italic italic
			text_size size