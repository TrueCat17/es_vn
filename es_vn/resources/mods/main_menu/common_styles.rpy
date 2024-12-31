init:
	style title is text:
		yalign 0.5
		color '#FFF'
		
		font 'CenturyGothic'
		text_size 60 / 1080
	
	style title_star is image:
		yalign 0.5
		xsize 47 / 1920
		ysize 45 / 1080
	
	style title_btn is textbutton:
		ground im.rect('#0000')
		hover  im.rect('#0000')
		
		text_align 'center'
		text_size 60 / 1080
		
		font 'CenturyGothic'
		color '#909CA3'
		hover_color '#FFF'
		
		xsize 500 / 1920
		ysize 65 / 1080
	
	
	style back_btn is title_btn:
		xsize 270 / 1920
		xpos 50 / 1920
		yalign 0.9
	
	
	style gallery_page is text:
		font 'CenturyGothic'
		color '#909CA3'
		text_size 60 / 1080
		
		ysize 65 / 1080
		xpos 1870 / 1920
		xanchor 1.0
		yalign 0.9
	
	style gallery_next_btn is button:
		ground 'images/gui/dialogue/day/forward_idle.webp'
		hover  'images/gui/dialogue/day/forward_hover.webp'
		xpos 1890 / 1920
		xanchor 1.0
		yalign 0.5
		
		xsize 116 / 1920
		ysize 84 / 1080
		corner_sizes 0
	
	style gallery_prev_btn is gallery_next_btn:
		ground 'images/gui/dialogue/day/backward_idle.webp'
		hover  'images/gui/dialogue/day/backward_hover.webp'
		xpos 30 / 1920
		xanchor 0.0
