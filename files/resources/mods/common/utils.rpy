init python:

	def volume(vol, chnl):
		renpy.music.set_volume(vol, channel=chnl)
	
	def pause(sec = None, hard = False):
		global pause_end
		pause_end = get_game_time() + (1e9 if sec is None else sec)
	renpy.pause = pause
	
	
	
	def show_achievement(name):
		if persistent.endings[name]:
			return
		
		persistent.endings[name] = True
		persistent.endings = dict(persistent.endings) # upd ref
		
		renpy.music.play(sfx_achievement, 'sound')
		
		global ach_path
		ach_path = 'images/misc/ach/' + name + '.webp'
		renpy.call('show_achievement')

init:
	image ach = ach_path

label show_achievement:
	show ach:
		size (443, 95)
        align (1.1, 0.97)
        ease 1.0 align (0.85, 0.97)
        ease 0.5 align (0.95, 0.97)
        pause 1.5
        ease 0.5 align (1.5, 0.97)
	pause 3.5
	hide ach
