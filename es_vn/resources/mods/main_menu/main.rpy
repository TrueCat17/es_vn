init python:
#	start_mod('std')
	set_can_mouse_hide(False)
	config.has_autosave = False
	
	pause_screen.disable = True
	
	main_menu_bgm = 'sound/music/blow_with_the_fires.ogg'
#	show_screen('gallery')


screen main_menu:
	zorder -100
	
	imagemap:
		ground 'images/gui/main_menu/ground.jpg'
		hover  'images/gui/main_menu/hover.jpg'
		
		hotspot ( 439, 265, 318, 621) action start_mod('std')
		hotspot ( 787, 261, 270, 537) action Show('load')
		hotspot ( 494, 125, 768,  86) action Show('info')
		hotspot (1083, 258, 229, 538) action Show('gallery')
		hotspot (1067, 748, 252, 312) action Show('preferences')
		hotspot (1459, 532, 149, 295) action exit_from_game hover_sound 'sound/sfx/menu_gate.ogg'
	
	button:
		ground 'images/gui/main_menu/owl_ground.webp'
		hover  'images/gui/main_menu/owl_hover.webp'
		
		action Show('achievements')
		hover_sound 'sound/test.ogg'
		
		xpos 135 / 1920
		ypos 606 / 1080
		xsize 144 / 1920
		ysize 144 / 1080


init:
	$ default_decl_at = []
	
	image bg soviet_games = 'images/misc/soviet_games.jpg'
	image bg disclaimer   = 'images/misc/disclaimer.jpg'
	
	python:
		hour = int(time.strftime('%H'))
		day_time = 'day'
		if hour >= 22 or hour <= 6:
			day_time = 'night'
		elif hour in (7, 8, 20, 21):
			day_time = 'sunset'
	
	image bg splashscreen = 'images/misc/splashscreen_' + day_time + '.webp'
	image logo            = 'images/misc/logo_'         + day_time + '.webp'


label start:
#	$ db.skip_tab = True
	show bg soviet_games with dissolve
	pause 3
	show bg disclaimer with dissolve
	pause
	
	show bg splashscreen with dissolve:
		yalign 0.0
		linear 3 yalign 1.0
	pause 3
	show logo with dissolve:
		align 0.5
	pause 3
	
	$ show_screen('main_menu')
	$ my_play(main_menu_bgm, fadein = 3)
	
	hide bg
	hide logo
	with fade
	
	$ db.skip_tab = False
	$ hide_screen('dialogue_box')
	
	while True:
		pause 0.1
