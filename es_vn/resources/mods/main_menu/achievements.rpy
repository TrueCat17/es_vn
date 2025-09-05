init python:
	endings = (
		('Семён, хорошая',  'main_good', 'epilogue_main'),
		('Семён, плохая',   'main_bad',  'main_bad_ending'),
		('Славя, хорошая',  'sl_good',   'epilogue_sl'),
		('Славя, плохая',   'sl_bad',    'epilogue_sl'),
		('Алиса, хорошая',  'dv_good',   'epilogue_dv'),
		('Алиса, плохая',   'dv_bad',    'epilogue_dv'),
		('Лена, хорошая',   'un_good',   'epilogue_un_good'),
		('Лена, плохая',    'un_bad',    'epilogue_un_bad'),
		('Ульяна, хорошая', 'us_good',   'epilogue_us'),
		('Ульяна, плохая',  'us_bad',    'epilogue_us'),
		('Мику',            'mi',        'epilogue_mi'),
		('Юля',             'uv_good',   'epilogue_uv_ulya'),
		('Все вместе',      'uv_harem',  'epilogue_uv_city'),
	)
	
	ach_first_page = True
	
	def ach_start(ach_name, label_name):
		persistent.jump_to = label_name
		persistent.replay = ach_name
		start_mod('std')


init:
	style ach_btn is textbutton:
		yalign 0.5
		xsize 0.232
		ysize 50 / 1080
		
		text_size 40 / 1080
		text_align 'left'
		
		font 'CenturyGothic'
		color '#909CA3'
		hover_color '#FFF'
		
		ground im.rect('#0000')
		hover  im.rect('#0000')
	
	style ach_btn_blocked is ach_btn:
		mouse False
		hover_color '#909CA3'


screen achievements:
	image 'images/misc/ach/bg.jpg':
		size 1.0
	
	
	hbox:
		spacing 40 / 1920
		xalign 0.5
		yalign 0.083
		
		image 'images/misc/star.webp':
			style 'title_star'
		
		text 'Концовки':
			style 'title'
		
		image 'images/misc/star.webp':
			style 'title_star'
	
	
	vbox:
		pos  (0.23, 0.154)
		size (0.61, 0.75)
		
		for text, ach_name, label_name in (endings[:7] if ach_first_page else endings[7:]):
			python:
				ach_enabled = persistent.endings[ach_name]
				if not ach_enabled:
					text = '?' * 10
					ach_name = 'void'
			
			hbox:
				textbutton text:
					style 'ach_btn' if ach_enabled else 'ach_btn_blocked'
					action ach_start(ach_name, label_name) if ach_enabled else None
				
				image ('images/misc/ach/' + ach_name + '.webp'):
					xsize 443 / 1920
					ysize  95 / 1080
	
	
	textbutton ('→' if ach_first_page else '←'):
		style 'ach_btn'
		text_align 'center'
		text_size 60 / 1080
		ysize 65 / 1080
		xalign 0.5
		yalign 0.82
		action 'ach_first_page = not ach_first_page'
	
	
	textbutton '← Назад':
		style 'back_btn'
		action Hide('achievements')
	
	key 'ESCAPE' action Hide('achievements')

