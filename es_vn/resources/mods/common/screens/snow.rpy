init python:
	snowflakes = []
	def set_snowflake_count(count):
		d = count - len(snowflakes)
		
		if d < 0:
			snowflakes[count:] = []
		else:
			width, height = get_stage_size()
			
			for i in range(d):
				size = random.randint(2, 10)
				
				x = random.uniform(0, 1)
				y = random.uniform(0, 1)
				dx = random.uniform(-100, 100) * size / width
				dy = random.uniform( 100, 150) * size / height
				
				snowflake = [x, y, dx, dy, size]
				snowflakes.append(snowflake)
	
	def show_snow(appearance_time, count = 50):
		global snow_show_time, snow_hide_time, snow_appearance_time
		snow_show_time = get_game_time()
		snow_hide_time = None
		snow_appearance_time = max(appearance_time, 0.01)
		set_snowflake_count(count)
		show_screen('snow')
	
	def hide_snow(disappearance_time):
		global snow_hide_time, snow_disappearance_time
		snow_hide_time = get_game_time()
		snow_disappearance_time = max(disappearance_time, 0.01)
	
	
	def update_snow():
		k = get_last_tick()
		
		for snowflake in snowflakes:
			snowflake[0] = (snowflake[0] + snowflake[2] * k) % 1.0
			snowflake[1] = (snowflake[1] + snowflake[3] * k) % 1.0
		
		if snow_hide_time is None:
			alpha = (get_game_time() - snow_show_time) / snow_appearance_time
		else:
			alpha = 1 - (get_game_time() - snow_hide_time) / snow_disappearance_time
			if alpha <= 0:
				hide_screen('snow')
		return in_bounds(alpha, 0, 1)


screen snow:
	zorder -2.5
	
	$ alpha = update_snow()
	alpha alpha
	
	# snowflake = [x, y, dx, dy, size]
	for snowflake in snowflakes:
		image 'images/anim/snow.webp':
			xpos snowflake[0]
			ypos snowflake[1]
			size snowflake[4]
