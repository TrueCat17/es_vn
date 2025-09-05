init python:
	map_zones_rects = {
		"me_mt_house":   [ 825,  47, 180, 183],
		"estrade":       [1039,  47, 249, 183],
		"music_club":    [ 541, 231, 170, 125],
		"square":        [ 825, 357, 180, 308],
		"dining_hall":   [1006, 457, 153, 208],
		"sport_area":    [1160, 457, 418, 208],
		"beach":         [1160, 666, 418, 205],
		"boat_station":  [ 825, 666, 180, 205],
		"clubs":         [ 418, 357, 293, 308],
		"library":       [1160, 231, 128, 225],
		"medic_house":   [1039, 231, 120, 225],
		"camp_entrance": [ 278, 357, 139, 308],
		"forest":        [ 541,  47, 170, 183],
	}
	
	
	map_zones_labels = {}
	def disable_all_zones():
		global map_zones_labels
		map_zones_labels = {}
	
	
	def set_zone(zone, label):
		map_zones_labels[zone] = label
		rect = map_zones_rects[zone]
	
	def reset_zone(zone):
		if zone in map_zones_labels:
			del map_zones_labels[zone]
	
	
	last_zone = ''
	def goto_zone(zone):
		global last_zone
		last_zone = zone
		
		label = map_zones_labels[zone]
		renpy.jump(label)
		
		hide_screen('map')
	
	def disable_current_zone():
		if last_zone:
			del map_zones_labels[last_zone]
	
	
	def show_map():
		available_bg = 'images/maps/available.jpg'
		args = [get_image_size(available_bg)]
		
		# workaround for correct render of texture with scaling
		args.append((0, 0))
		args.append(im.recolor(available_bg, 255, 255, 255, 0))
		
		for zone in map_zones_labels:
			rect = map_zones_rects[zone]
			part = im.crop(available_bg, *rect)
			
			args.append((rect[0], rect[1]))
			args.append(part)
		
		global available_zones
		available_zones = im.composite(*args)
		
		renpy.scene()
		show_screen('map')
	
	
	def wait_map():
		return not has_screen('map')
	can_exec_next_check_funcs.append(wait_map)


screen map:
	image 'images/maps/bg.jpg':
		size 1.0
	
	imagemap:
		size 1.0
		
		ground available_zones
		hover  'images/maps/selected.jpg'
		
		for zone in map_zones_labels:
			hotspot map_zones_rects[zone] action goto_zone(zone)
