init:
	image un night = im.Recolor(im.Composite((386, 975),
		(  0,   0), "images/sprites/normal/un/un_1_body.png",
		(  4, 328), "images/sprites/normal/un/un_1_pioneer.png",
		(149, 196), "images/sprites/normal/un/un_1_shy.png",
	), 160, 200, 210)
	
	image un normal pioneer red = im.Recolor(im.Composite((386, 975),
		(  0,   0), "images/sprites/normal/un/un_1_body.png",
		(  4, 328), "images/sprites/normal/un/un_1_pioneer.png",
		(170, 193), "images/sprites/normal/un/un_1_normal.png",
	), 255, 25, 25)
	
	image un surprise pioneer red = im.Recolor(im.Composite((471, 950),
		(  0,   0), "images/sprites/normal/un/un_2_body.png",
		( 43, 313), "images/sprites/normal/un/un_2_pioneer.png",
		(146, 162), "images/sprites/normal/un/un_2_surprise.png",
	), 255, 25, 25)