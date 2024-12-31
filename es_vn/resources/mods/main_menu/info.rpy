init python:
	info_btns = [
		('Группа Бесконечного Лета в VK', 'https://vk.com/everlasting.summer.official'),
		('Группа движка Ren-Engine в VK', 'https://vk.com/ren_engine'),
	]
	
	def copy_link(link):
		set_clipboard_text(link)
		notification.out('Ссылка скопирована')

init:
	style info_btn is textbutton:
		ground im.rect('#0000')
		hover  im.rect('#0000')
		
		font 'CenturyGothic'
		color '#EEE'
		hover_color '#08F'
		text_size 35 / 1080
		
		xsize 600 / 1920
		ysize 50 / 1080

screen info:
	image 'images/misc/ach/bg.jpg':
		size 1.0
	
	
	hbox:
		spacing 40 / 1920
		xalign 0.5
		yalign 0.083
		
		image 'images/misc/star.webp':
			style 'title_star'
		
		text 'Информация':
			style 'title'
		
		image 'images/misc/star.webp':
			style 'title_star'
	
	
	vbox:
		align (0.5, 0.25)
		spacing 30
		
		for text, link in info_btns:
			textbutton text:
				style 'info_btn'
				action copy_link(link)
	
	
	textbutton '← Назад':
		style 'back_btn'
		action Hide('info')
	
	key 'ESCAPE' action Hide('info')

