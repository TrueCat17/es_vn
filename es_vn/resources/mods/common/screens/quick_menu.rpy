init:
	style quick_buttons_bg:
		ysize 1
		ysize_min 1

screen quick_menu:
	ysize 1
	
	hbox:
		align (1.0, 1.0)
		
		image im.rect('F000'):
			alpha 1 if db.visible and db.mode == 'adv' else 0
			
			xsize 240 / 1920
			ysize gui.get_int('dialogue_box_height')
			
			hbox:
				ypos int(35 / 1080 * get_stage_height())
				yanchor 1.0
				spacing 35 / 1920
				
				for name, action, ground, hover in gui.quick_buttons:
					button:
						xsize 27 / 1920
						ysize 20 / 1080
						
						ground ground
						hover  hover
						
						action action
						alternate pause_screen.show
		
		null:
			xsize gui.get_int('dialogue_button_spacing', obj = db) * 2 + gui.get_int('dialogue_button_width', obj = db)
