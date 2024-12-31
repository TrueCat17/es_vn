init python:
	gallery_types = (
		'ИЛЛЮСТРАЦИИ',
		'ФОНЫ',
		'СПРАЙТЫ',
		'МУЗЫКА',
	)
	gallery_type = gallery_types[0]
	gallery_type_prev = ''
	
	def get_gallery_types():
		index = gallery_types.index(gallery_type)
		count = len(gallery_types)
		return (
			# text                                 xpos     xanchor
			(gallery_types[(index - 1) % count], 50 / 1920,   0.0),
			(gallery_type,                       0.5,         0.5),
			(gallery_types[(index + 1) % count], 1870 / 1920, 1.0),
		)


screen gallery:
	zorder -50
	
	image 'images/misc/ach/bg.jpg':
		size 1.0
	
	
	$ gallery_type_prev = gallery_type
	
	for text, xpos, xanchor in get_gallery_types():
		hbox:
			spacing 40 / 1920
			xpos xpos
			xanchor xanchor
			yalign 0.083
			
			if text == gallery_type:
				image 'images/misc/star.webp':
					style 'title_star'
				
				text text:
					style 'title'
				
				image 'images/misc/star.webp':
					style 'title_star'
			
			else:
				textbutton text:
					style 'title_btn'
					text_align xanchor
					action 'gallery_type = text'
	
	
	if gallery_type in ('ИЛЛЮСТРАЦИИ', 'ФОНЫ'):
		$ bg_or_cg = 'bg' if gallery_type == 'ФОНЫ' else 'cg'
		use gallery_bg_cg
	if gallery_type == 'СПРАЙТЫ':
		use gallery_sprites
	if gallery_type == 'МУЗЫКА':
		use gallery_music
	
	
	textbutton '← Назад':
		style 'back_btn'
		action Hide('gallery')
	
	if not has_screen('dialogue_box'):
		key 'ESCAPE' action Hide('gallery')

