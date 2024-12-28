init python:
	objs = []
	def set_count(count):
		global objs
		d = count - len(objs)
		
		if d < 0:
			objs = objs[0:count]
		else:
			width, height = get_stage_size()
			
			for i in range(d):
				size = random.randint(2, 10)
				
				x = random.uniform(0, 1)
				y = random.uniform(0, 1)
				dx = random.uniform(-100, 100) * size / width
				dy = random.uniform(100, 150) * size / height
				
				obj = [x, y, dx, dy, size]
				objs.append(obj)
	
	def show_snow(appearance_time, count = 50):
		global snow_show_time, snow_hide_time, snow_appearance_time
		snow_show_time = get_game_time()
		snow_hide_time = None
		snow_appearance_time = max(appearance_time, 0.01)
		set_count(count)
		show_screen('snow')
	
	def hide_snow(disappearance_time):
		global snow_hide_time, snow_disappearance_time
		snow_hide_time = get_game_time()
		snow_disappearance_time = max(disappearance_time, 0.01)
		hide_screen('snow')
	
	
	def update_snow():
		k = get_last_tick()
		
		x, y, dx, dy, size = 0, 1, 2, 3, 4
		for obj in objs:
			obj[x] = (obj[x] + obj[dx] * k) % 1.0
			obj[y] = (obj[y] + obj[dy] * k) % 1.0
		
		if snow_hide_time is None:
			alpha = (get_game_time() - snow_show_time) / snow_appearance_time
		else:
			alpha = 1 - (get_game_time() - snow_hide_time) / snow_disappearance_time
		return in_bounds(alpha, 0, 1)


screen snow:
	zorder -2.5
	
	$ alpha = update_snow()
	alpha alpha
	
	# x, y, dx, dy, size = 0, 1, 2, 3, 4
	for obj in objs:
		image 'images/anim/snow.webp':
			xpos obj[0]
			ypos obj[1]
			size obj[4]