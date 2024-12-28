init -990 python:
	# characters with <static> color names
	
	sm = Character('Семён', color = (225, 221, 125))
	my = Character('Я'    , color = (225, 221, 125))
	
	voice = Character('Голос', color = (225, 221, 125))
	
	pi = Character('Пионер', color = (230, 0, 0))
	
	all = Character('Пионеры', color = (227, 58, 58))
	
	dreamgirl   = Character('...',          color = (192, 192, 192))
	bush        = Character('Голос',        color = (192, 192, 192))
	FIXME_voice = Character('Голос',        color = (192, 192, 192))
	odn         = Character('Одногруппник', color = (192, 192, 192))
	message     = Character('Сообщение',    color = (192, 192, 192))
	
	me = sm
	
	
	
	# characters with <dynamic> colors
	
	character_colors = {
		'dv': { 'day': (255, 170,   0), 'night': (210, 139,  16) },
		'un': { 'day': (185,  86, 255), 'night': (170, 100, 217) },
		'sl': { 'day': (255, 210,   0), 'night': (214, 176,   0) },
		'mi': { 'day': (  0, 222, 255), 'night': (  0, 180, 207), 'sunset': (  0, 252, 255) },
		'us': { 'day': (255,  50,   0), 'night': (234,  55,   0) },
		
		'cs': { 'day': (165, 165, 255), 'night': (134, 134, 230) },
		'mz': { 'day': ( 74, 134, 255), 'night': ( 84, 129, 219), 'sunset': (114, 160, 255) },
		'mt': { 'day': (  0, 234,  50), 'night': (  0, 182,  39) },
		'el': { 'day': (255, 255,   0), 'night': (205, 205,   0) },
		'sh': { 'day': (255, 242,  38), 'night': (205, 194,  18) },
		'uv': { 'day': ( 78, 255,   0), 'night': ( 64, 208,   0) },
	}
	
	# python_name: (color_name, name)
	character_names = {
		'dv':  ('dv', 'Алиса'),
		'dvp': ('dv', 'Пионерка'),
		'dvg': ('dv', 'Девушка'),
		
		'un':  ('un', 'Лена'),
		'unp': ('un', 'Пионерка'),
		
		'sl':  ('sl', 'Славя'),
		'slp': ('sl', 'Пионерка'),
		'slg': ('sl', 'Девушка'),
		'sa':  ('sl', 'Саша'),
		
		'mi':  ('mi', 'Мику'),
		'mip': ('mi', 'Пионерка'),
		'ma':  ('mi', 'Маша'),
		
		'us':  ('us', 'Ульяна'),
		'usp': ('us', 'Пионерка'),
		'usg': ('us', 'Девушка'),
		
		'cs':  ('cs', 'Виола'),
		'csp': ('cs', 'Медсестра'),
		
		'mz':  ('mz', 'Женя'),
		'mzp': ('mz', 'Пионерка'),
		
		'mt':       ('mt', 'Ольга Дмитриевна'),
		'mtp':      ('mt', 'Вожатая'),
		'mt_voice': ('mt', 'Голос'),
		
		'el':  ('el', 'Электроник'),
		'elp': ('el', 'Пионер'),
		'ro':  ('el', 'Роутер'),
		
		'sh':  ('sh', 'Шурик'),
		'shp': ('sh', 'Пионер'),
		
		'uv':  ('uv', 'Юля'),
		'uvp': ('uv', 'Странная девочка'),
	}
	
	
	def update_character_colors(time_name):
		g = globals()
		
		for python_name, (color_name, name) in character_names.items():
			colors = character_colors[color_name]
			color = colors[time_name if time_name in colors else 'day']
			
			if python_name not in g:
				g[python_name] = Character(name, color = color)
			else:
				g[python_name].name_text_color = color
	
	
	lp_dv = lp_un = lp_sl = lp_mi = lp_us = 0
