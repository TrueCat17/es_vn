init python:
	choice_colors = {
		'day':      '#466123',
		'night':    '#145644',
		'sunset':   '#69652f',
		'prologue': '#496463',
	}
	
	choice_colors_hover = {
		'day':      '#9dcd55',
		'night':    '#3ccfa2',
		'sunset':   '#dcd168',
		'prologue': '#98d8da',
	}

init:
	style choice_button:
		ground im.rect('0000')
		hover  im.rect('0000')
		xsize 0.8
		ysize     37 / 1080
		text_size 37 / 1080
		text_align 'center'
		font 'Corbel'
	
	style choice_buttons_vbox:
		spacing 3

screen choice_menu:
	modal True
	zorder 100
	
	image gui.choice_box:
		align 0.5
		corner_sizes 50
		
		xsize 1.0
		
		$ spacing = style.choice_buttons_vbox.spacing
		ysize (style.choice_button.get_current('ysize') + spacing) * len(choice_menu_variants) - spacing + 105
	
	vbox:
		style 'choice_buttons_vbox'
		
		for i, text in enumerate(choice_menu_variants):
			if text:
				textbutton _(text):
					style 'choice_button'
					
					color       choice_colors[      times['current_name']]
					hover_color choice_colors_hover[times['current_name']]
					
					action Return(i)
			elif text is not None:
				null style 'choice_button'
	
	use dialogue_box_buttons(disable_next_btn = True)