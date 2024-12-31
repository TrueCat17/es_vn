init -10 python:
	pause_screen.hotspots = (
		[(0,  83, 660, 65), Function(start_mod, 'main_menu')],
		[(0, 148, 660, 65), Show('save')],
		[(0, 213, 660, 65), Show('load')],
		[(0, 278, 660, 65), Show('preferences')],
		[(0, 343, 660, 65), exit_from_game],
	)
	
	def show_pause():
		if pause_screen.disable:
			return
		if renpy.has_screen('pause'):
			return
		
		pause_screen.show_time = get_game_time()
		pause_screen.hide_time = None
		show_screen('pause')
	pause_screen.show = show_pause
	
	
	pause_screen.appearance_time    = 0.5
	pause_screen.disappearance_time = 0.5
	
	def get_pause_alpha():
		if pause_screen.hide_time is not None:
			dtime = get_game_time() - pause_screen.hide_time
			alpha = 1 - dtime / pause_screen.disappearance_time
			if alpha < 0:
				hide_screen('pause')
		else:
			dtime = get_game_time() - pause_screen.show_time
			alpha = dtime / pause_screen.appearance_time
		return in_bounds(alpha, 0, 1)
	
	def hide_pause():
		if get_pause_alpha() >= 1:
			pause_screen.hide_time = get_game_time()


screen pause:
	zorder 10000
	modal  True
	save   False
	
	alpha get_pause_alpha()
	
	
	key 'ESCAPE' action hide_pause
	
	button:
		ground im.rect('#000')
		hover  im.rect('#000')
		
		size 1.0
		alpha 0.01
		corner_sizes 0
		mouse False
		
		action    hide_pause
		alternate hide_pause
	
	
	image gui.pause_bg:
		skip_mouse True
		align 0.5
		xsize 660 / 1920
		ysize 463 / 1080
	
	imagemap:
		ground gui.pause_ground
		hover  gui.pause_hover
		
		align 0.5
		xsize 660 / 1920
		ysize 463 / 1080
		
		for rect, action in pause_screen.hotspots:
			hotspot rect:
				action action
				alternate hide_pause
