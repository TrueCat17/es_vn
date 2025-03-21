init:
	transform backdrop_trans:
		align (-0.2, 1.0)
		linear 2.0 xalign 0.1

init python:
	def new_chapter(day_number, chapter_name, backdrop):
		global chapter_day_number, save_name, chapter_backdrop
		chapter_day_number = str(day_number) if backdrop != 'epilogue' else '...'
		save_name = _(chapter_name)
		chapter_backdrop = backdrop
		
		set_mode_adv()
		
		if backdrop != 'prologue':
			renpy.call('show_chapter')


label show_chapter:
	pause 1
	
	$ chapter_monitor_index = 0
	$ chapter_monitor_nums = [1, 2, 3, 2]
	
	$ chapter_show_time = get_game_time()
	$ chapter_hide_time = None
	$ show_screen('chapter')
	scene with fade
	$ chapter_show_time = get_game_time() - 1
	
	if chapter_backdrop == 'dv':
		show dv normal pioneer at backdrop_trans with dissolve
	if chapter_backdrop == 'sl':
		show sl normal pioneer at backdrop_trans with dissolve
	if chapter_backdrop == 'un':
		show un normal pioneer at backdrop_trans with dissolve
	if chapter_backdrop == 'us':
		show us normal pioneer at backdrop_trans with dissolve
	
	pause 5
	
	$ chapter_hide_time = get_game_time()
	scene bg black with dissolve
	
	$ chapter_hide_time = get_game_time() - 1
	$ hide_screen('chapter')


screen chapter:
	zorder -10
	
	image 'images/anim/backdrop/back.jpg':
		size 1.0
	
	text ('День ' + chapter_day_number):
		pos 0.32
		font 'DejavuSerif'
		color        '#FFF'
		outlinecolor '#000'
		text_size 140 / 1080
	
	python:
		dtime = int(get_game_time() * 10) % 10
		prev_dtime = int((get_game_time() - get_last_tick()) * 10) % 10
		if dtime != prev_dtime:
			chapter_monitor_index += 1
			if chapter_monitor_index == len(chapter_monitor_nums):
				chapter_monitor_index = 0
	
	image ('images/anim/backdrop/%s.webp' % chapter_monitor_nums[chapter_monitor_index]):
		size 1.0
	
	python:
		if chapter_hide_time is None:
			dtime = in_bounds(get_game_time() - chapter_show_time, 0, 1)
		else:
			dtime = 1 - in_bounds(get_game_time() - chapter_hide_time, 0, 1)
	
	image im.rect('#000'):
		size 1.0
		alpha 1 - dtime
