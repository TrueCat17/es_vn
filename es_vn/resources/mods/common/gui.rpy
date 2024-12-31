init:
	$ preferences.tabs.remove('Language')
	
	style menu_text:
		color '#FFF'
	
	style bool_text:
		color '#FFF'
	
	style page_button:
		ground im.rect('#0000')
		hover  im.rect('#0000')
		
		color '#909CA3'
		hover_color '#FFF'


init python:
	def calc_gui_min(prop):
		value = gui[prop]
		min_size = 1006 if 'width' in prop or 'xpos' in prop else 566
		gui[prop + '_min'] = round(value * min_size)
	
	
	gui.dialogue_menu_button_width = 0
	
	gui.dialogue_box_height = 151 / 1080
	calc_gui_min('dialogue_box_height')
	
	gui.dialogue_text_ypos = 42 / 1080
	calc_gui_min('dialogue_text_ypos')
	gui.dialogue_text_height = 0.09
	gui.dialogue_text_size = 0.028
	gui.dialogue_text_color = '#FFDD7D'
	
	gui.name_box_bg = im.rect('#F000')
	gui.name_box_xpos = 15
	gui.name_box_xpos_min = 0
	gui.name_box_ypos = 10 / 1080
	gui.name_box_xanchor = 0
	gui.name_box_yanchor = 0
	gui.name_box_width  = 210 / 1920
	gui.name_box_width_min = 0
	gui.name_box_height = 0.03
	calc_gui_min('name_box_height')
	
	gui.name_text_size = 0.028
	calc_gui_min('name_text_size')
	gui.name_text_xalign = 0
	gui.name_text_yalign = 0.5
	
	gui.dialogue_button_width = 116 / 1920
	gui.dialogue_button_height = 84 / 1080
	gui.dialogue_button_spacing = 32 / 1920
	
	gui.nvl_top_indent = 0.14
	gui.nvl_spacing = 2
	gui.nvl_thought_xpos = 0.09
	gui.nvl_name_xpos = 0.17
	gui.nvl_name_width = 0.15
	gui.nvl_text_xpos = 0.175
	
	gui.history_name_xpos  = 170 / 1920
	gui.history_name_width = 170 / 1920
	
	gui.history_text_xpos  = 190 / 1920
	
	
	gui.slot_pages = 9
	slots.pages = ['auto', 'quick'] + [str(i + 1) for i in range(gui.slot_pages)]
	
	
	gui.quick_buttons_top_indent = 0
	
	gui.quick_buttons = [
		['hide', Exec('db.hide_interface = True'), '', ''],
		['save', Show('save'),                     '', ''],
		['menu', pause_screen.show,                '', ''],
		['load', Show('load'),                     '', ''],
	]
	
	
	make_time('prologue')
	prolog_time = prologue_time
	
	def set_interface_time(time_name):
		gui.dialogue_box_bg = 'images/gui/dialogue/' + time_name + '/dialogue_box.png'
		
		gui.dialogue_prev_ground = 'images/gui/dialogue/' + time_name + '/backward_idle.png'
		gui.dialogue_prev_hover  = 'images/gui/dialogue/' + time_name + '/backward_hover.png'
		
		gui.dialogue_next_ground = 'images/gui/dialogue/' + time_name + '/forward_idle.png'
		gui.dialogue_next_hover  = 'images/gui/dialogue/' + time_name + '/forward_hover.png'
		
		for props in gui.quick_buttons:
			btn_name = props[0]
			props[2] = get_back_with_color('images/gui/dialogue/' + time_name + '/' + btn_name + '_idle.webp')
			props[3] = get_back_with_color('images/gui/dialogue/' + time_name + '/' + btn_name + '_hover.webp')
		
		gui.choice_box = 'images/gui/choice/' + time_name + '/choice_box.webp'
		gui.nvl_bg = im.scale_without_borders(gui.choice_box, 1920, 1080, 50)
		
		gui.pause_bg     = 'images/gui/pause_menu/' + time_name + '/ingame_menu.webp'
		gui.pause_ground = 'images/gui/pause_menu/' + time_name + '/ingame_menu_ground.webp'
		gui.pause_hover  = 'images/gui/pause_menu/' + time_name + '/ingame_menu_hover.webp'
		
		update_character_colors(time_name)
		
		db.update_styles()
	
	signals.add('time', set_interface_time)
	day_time(need = True)
	
	
	gui.load_bg = 'images/gui/save_load/load_bg.jpg'
	gui.save_bg = 'images/gui/save_load/save_bg.jpg'
	gui.prefs_bg = gui.load_bg
