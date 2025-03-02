init python:

	# only for scaling sprites!
	config.width, config.height = 1920, 1080
	
	# Sprite Recolor
	def _sr(path):
		return im.recolor(path, *sprite_time_rgb)


init:

	image cs normal close = _sr(im.Composite((579, 1080),
		(  0,   0), "images/sprites/close/cs/cs_1_body.png",
		(144, 128), "images/sprites/close/cs/cs_1_normal.png",
	))
	image cs normal glasses close = _sr(im.Composite((579, 1080),
		(  0,   0), "images/sprites/close/cs/cs_1_body.png",
		(170, 318), "images/sprites/close/cs/cs_1_glasses.png",
		(144, 128), "images/sprites/close/cs/cs_1_normal.png",
	))
	image cs normal stethoscope close = _sr(im.Composite((579, 1080),
		(  0,   0), "images/sprites/close/cs/cs_1_body.png",
		( 65, 347), "images/sprites/close/cs/cs_1_stethoscope.png",
		(144, 128), "images/sprites/close/cs/cs_1_normal.png",
	))
	image cs shy close = _sr(im.Composite((579, 1080),
		(  0,   0), "images/sprites/close/cs/cs_1_body.png",
		(157, 143), "images/sprites/close/cs/cs_1_shy.png",
	))
	image cs shy glasses close = _sr(im.Composite((579, 1080),
		(  0,   0), "images/sprites/close/cs/cs_1_body.png",
		(170, 318), "images/sprites/close/cs/cs_1_glasses.png",
		(157, 143), "images/sprites/close/cs/cs_1_shy.png",
	))
	image cs shy stethoscope close = _sr(im.Composite((579, 1080),
		(  0,   0), "images/sprites/close/cs/cs_1_body.png",
		( 65, 347), "images/sprites/close/cs/cs_1_stethoscope.png",
		(157, 143), "images/sprites/close/cs/cs_1_shy.png",
	))
	image cs smile close = _sr(im.Composite((579, 1080),
		(  0,   0), "images/sprites/close/cs/cs_1_body.png",
		(177, 119), "images/sprites/close/cs/cs_1_smile.png",
	))
	image cs smile glasses close = _sr(im.Composite((579, 1080),
		(  0,   0), "images/sprites/close/cs/cs_1_body.png",
		(170, 318), "images/sprites/close/cs/cs_1_glasses.png",
		(177, 119), "images/sprites/close/cs/cs_1_smile.png",
	))
	image cs smile stethoscope close = _sr(im.Composite((579, 1080),
		(  0,   0), "images/sprites/close/cs/cs_1_body.png",
		( 65, 347), "images/sprites/close/cs/cs_1_stethoscope.png",
		(177, 119), "images/sprites/close/cs/cs_1_smile.png",
	))
	
	image cs normal = _sr(im.Composite((464, 1063),
		(  0,   0), "images/sprites/normal/cs/cs_1_body.png",
		(115, 112), "images/sprites/normal/cs/cs_1_normal.png",
	))
	image cs normal glasses = _sr(im.Composite((464, 1063),
		(  0,   0), "images/sprites/normal/cs/cs_1_body.png",
		(136, 263), "images/sprites/normal/cs/cs_1_glasses.png",
		(115, 112), "images/sprites/normal/cs/cs_1_normal.png",
	))
	image cs normal stethoscope = _sr(im.Composite((464, 1063),
		(  0,   0), "images/sprites/normal/cs/cs_1_body.png",
		( 53, 287), "images/sprites/normal/cs/cs_1_stethoscope.png",
		(115, 112), "images/sprites/normal/cs/cs_1_normal.png",
	))
	image cs shy = _sr(im.Composite((464, 1063),
		(  0,   0), "images/sprites/normal/cs/cs_1_body.png",
		(126, 124), "images/sprites/normal/cs/cs_1_shy.png",
	))
	image cs shy glasses = _sr(im.Composite((464, 1063),
		(  0,   0), "images/sprites/normal/cs/cs_1_body.png",
		(136, 263), "images/sprites/normal/cs/cs_1_glasses.png",
		(126, 124), "images/sprites/normal/cs/cs_1_shy.png",
	))
	image cs shy stethoscope = _sr(im.Composite((464, 1063),
		(  0,   0), "images/sprites/normal/cs/cs_1_body.png",
		( 53, 287), "images/sprites/normal/cs/cs_1_stethoscope.png",
		(126, 124), "images/sprites/normal/cs/cs_1_shy.png",
	))
	image cs smile = _sr(im.Composite((464, 1063),
		(  0,   0), "images/sprites/normal/cs/cs_1_body.png",
		(142, 104), "images/sprites/normal/cs/cs_1_smile.png",
	))
	image cs smile glasses = _sr(im.Composite((464, 1063),
		(  0,   0), "images/sprites/normal/cs/cs_1_body.png",
		(136, 263), "images/sprites/normal/cs/cs_1_glasses.png",
		(142, 104), "images/sprites/normal/cs/cs_1_smile.png",
	))
	image cs smile stethoscope = _sr(im.Composite((464, 1063),
		(  0,   0), "images/sprites/normal/cs/cs_1_body.png",
		( 53, 287), "images/sprites/normal/cs/cs_1_stethoscope.png",
		(142, 104), "images/sprites/normal/cs/cs_1_smile.png",
	))
	
	image cs normal far = _sr(im.Composite((348, 955),
		(  0,   0), "images/sprites/far/cs/cs_1_body.png",
		( 86,  84), "images/sprites/far/cs/cs_1_normal.png",
	))
	image cs normal glasses far = _sr(im.Composite((348, 955),
		(  0,   0), "images/sprites/far/cs/cs_1_body.png",
		(102, 198), "images/sprites/far/cs/cs_1_glasses.png",
		( 86,  84), "images/sprites/far/cs/cs_1_normal.png",
	))
	image cs normal stethoscope far = _sr(im.Composite((348, 955),
		(  0,   0), "images/sprites/far/cs/cs_1_body.png",
		( 39, 215), "images/sprites/far/cs/cs_1_stethoscope.png",
		( 86,  84), "images/sprites/far/cs/cs_1_normal.png",
	))
	image cs shy far = _sr(im.Composite((348, 955),
		(  0,   0), "images/sprites/far/cs/cs_1_body.png",
		( 95,  93), "images/sprites/far/cs/cs_1_shy.png",
	))
	image cs shy glasses far = _sr(im.Composite((348, 955),
		(  0,   0), "images/sprites/far/cs/cs_1_body.png",
		(102, 198), "images/sprites/far/cs/cs_1_glasses.png",
		( 95,  93), "images/sprites/far/cs/cs_1_shy.png",
	))
	image cs shy stethoscope far = _sr(im.Composite((348, 955),
		(  0,   0), "images/sprites/far/cs/cs_1_body.png",
		( 39, 215), "images/sprites/far/cs/cs_1_stethoscope.png",
		( 95,  93), "images/sprites/far/cs/cs_1_shy.png",
	))
	image cs smile far = _sr(im.Composite((348, 955),
		(  0,   0), "images/sprites/far/cs/cs_1_body.png",
		(106,  78), "images/sprites/far/cs/cs_1_smile.png",
	))
	image cs smile glasses far = _sr(im.Composite((348, 955),
		(  0,   0), "images/sprites/far/cs/cs_1_body.png",
		(102, 198), "images/sprites/far/cs/cs_1_glasses.png",
		(106,  78), "images/sprites/far/cs/cs_1_smile.png",
	))
	image cs smile stethoscope far = _sr(im.Composite((348, 955),
		(  0,   0), "images/sprites/far/cs/cs_1_body.png",
		( 39, 215), "images/sprites/far/cs/cs_1_stethoscope.png",
		(106,  78), "images/sprites/far/cs/cs_1_smile.png",
	))
	
	image dv angry pioneer close = _sr(im.Composite((488, 888),
		(  0,   0), "images/sprites/close/dv/dv_5_body.png",
		( 24, 316), "images/sprites/close/dv/dv_5_pioneer.png",
		(232, 190), "images/sprites/close/dv/dv_5_angry.png",
	))
	image dv angry pioneer2 close = _sr(im.Composite((515, 888),
		( 27,   0), "images/sprites/close/dv/dv_5_body.png",
		(  0, 325), "images/sprites/close/dv/dv_5_pioneer2.png",
		(259, 190), "images/sprites/close/dv/dv_5_angry.png",
	))
	image dv cry pioneer close = _sr(im.Composite((480, 879),
		(  0,   0), "images/sprites/close/dv/dv_1_body.png",
		(  2, 315), "images/sprites/close/dv/dv_1_pioneer.png",
		( 92, 130), "images/sprites/close/dv/dv_1_cry.png",
	))
	image dv cry pioneer2 close = _sr(im.Composite((501, 879),
		( 21,   0), "images/sprites/close/dv/dv_1_body.png",
		(  0, 311), "images/sprites/close/dv/dv_1_pioneer2.png",
		(113, 130), "images/sprites/close/dv/dv_1_cry.png",
	))
	image dv cry swim close = _sr(im.Composite((480, 879),
		(  0,   0), "images/sprites/close/dv/dv_1_body.png",
		(107, 305), "images/sprites/close/dv/dv_1_swim.png",
		( 92, 130), "images/sprites/close/dv/dv_1_cry.png",
	))
	image dv grin pioneer close = _sr(im.Composite((717, 918),
		(  0,   0), "images/sprites/close/dv/dv_2_body.png",
		(106, 341), "images/sprites/close/dv/dv_2_pioneer.png",
		(227, 147), "images/sprites/close/dv/dv_2_grin.png",
	))
	image dv grin pioneer2 close = _sr(im.Composite((717, 918),
		(  0,   0), "images/sprites/close/dv/dv_2_body.png",
		( 13, 257), "images/sprites/close/dv/dv_2_pioneer2.png",
		(227, 147), "images/sprites/close/dv/dv_2_grin.png",
	))
	image dv grin swim close = _sr(im.Composite((717, 918),
		(  0,   0), "images/sprites/close/dv/dv_2_body.png",
		(184, 341), "images/sprites/close/dv/dv_2_swim.png",
		(227, 147), "images/sprites/close/dv/dv_2_grin.png",
	))
	image dv guilty pioneer close = _sr(im.Composite((463, 878),
		(  0,   0), "images/sprites/close/dv/dv_3_body.png",
		( 25, 297), "images/sprites/close/dv/dv_3_pioneer.png",
		(124, 161), "images/sprites/close/dv/dv_3_guilty.png",
	))
	image dv guilty pioneer2 close = _sr(im.Composite((463, 878),
		(  0,   0), "images/sprites/close/dv/dv_3_body.png",
		( 25, 305), "images/sprites/close/dv/dv_3_pioneer2.png",
		(124, 161), "images/sprites/close/dv/dv_3_guilty.png",
	))
	image dv laugh coat close = _sr(im.Composite((529, 922),
		(  9,   0), "images/sprites/close/dv/dv_4_body.png",
		(  0, 307), "images/sprites/close/dv/dv_4_coat.png",
		(294, 170), "images/sprites/close/dv/dv_4_laugh.png",
	))
	image dv laugh pioneer close = _sr(im.Composite((520, 922),
		(  0,   0), "images/sprites/close/dv/dv_4_body.png",
		( 49, 335), "images/sprites/close/dv/dv_4_pioneer.png",
		(285, 170), "images/sprites/close/dv/dv_4_laugh.png",
	))
	image dv laugh pioneer2 close = _sr(im.Composite((520, 922),
		(  0,   0), "images/sprites/close/dv/dv_4_body.png",
		( 49, 346), "images/sprites/close/dv/dv_4_pioneer2.png",
		(285, 170), "images/sprites/close/dv/dv_4_laugh.png",
	))
	image dv laugh swim close = _sr(im.Composite((518, 922),
		(  0,   0), "images/sprites/close/dv/dv_4_body.png",
		(149, 346), "images/sprites/close/dv/dv_4_swim.png",
		(285, 170), "images/sprites/close/dv/dv_4_laugh.png",
	))
	image dv normal pioneer close = _sr(im.Composite((520, 922),
		(  0,   0), "images/sprites/close/dv/dv_4_body.png",
		( 49, 335), "images/sprites/close/dv/dv_4_pioneer.png",
		(291, 168), "images/sprites/close/dv/dv_4_normal.png",
	))
	image dv normal pioneer2 close = _sr(im.Composite((520, 922),
		(  0,   0), "images/sprites/close/dv/dv_4_body.png",
		( 49, 346), "images/sprites/close/dv/dv_4_pioneer2.png",
		(291, 168), "images/sprites/close/dv/dv_4_normal.png",
	))
	image dv normal swim close = _sr(im.Composite((518, 922),
		(  0,   0), "images/sprites/close/dv/dv_4_body.png",
		(149, 346), "images/sprites/close/dv/dv_4_swim.png",
		(291, 168), "images/sprites/close/dv/dv_4_normal.png",
	))
	image dv rage pioneer close = _sr(im.Composite((488, 888),
		(  0,   0), "images/sprites/close/dv/dv_5_body.png",
		( 24, 316), "images/sprites/close/dv/dv_5_pioneer.png",
		(210, 174), "images/sprites/close/dv/dv_5_rage.png",
	))
	image dv rage pioneer2 close = _sr(im.Composite((515, 888),
		( 27,   0), "images/sprites/close/dv/dv_5_body.png",
		(  0, 325), "images/sprites/close/dv/dv_5_pioneer2.png",
		(237, 174), "images/sprites/close/dv/dv_5_rage.png",
	))
	image dv sad pioneer close = _sr(im.Composite((463, 878),
		(  0,   0), "images/sprites/close/dv/dv_3_body.png",
		( 25, 297), "images/sprites/close/dv/dv_3_pioneer.png",
		(122, 118), "images/sprites/close/dv/dv_3_sad.png",
	))
	image dv sad pioneer2 close = _sr(im.Composite((463, 878),
		(  0,   0), "images/sprites/close/dv/dv_3_body.png",
		( 25, 305), "images/sprites/close/dv/dv_3_pioneer2.png",
		(122, 118), "images/sprites/close/dv/dv_3_sad.png",
	))
	image dv scared pioneer close = _sr(im.Composite((480, 879),
		(  0,   0), "images/sprites/close/dv/dv_1_body.png",
		(  2, 315), "images/sprites/close/dv/dv_1_pioneer.png",
		( 93, 122), "images/sprites/close/dv/dv_1_scared.png",
	))
	image dv scared pioneer2 close = _sr(im.Composite((501, 879),
		( 21,   0), "images/sprites/close/dv/dv_1_body.png",
		(  0, 311), "images/sprites/close/dv/dv_1_pioneer2.png",
		(114, 122), "images/sprites/close/dv/dv_1_scared.png",
	))
	image dv scared swim close = _sr(im.Composite((480, 879),
		(  0,   0), "images/sprites/close/dv/dv_1_body.png",
		(107, 305), "images/sprites/close/dv/dv_1_swim.png",
		( 93, 122), "images/sprites/close/dv/dv_1_scared.png",
	))
	image dv shocked pioneer close = _sr(im.Composite((480, 879),
		(  0,   0), "images/sprites/close/dv/dv_1_body.png",
		(  2, 315), "images/sprites/close/dv/dv_1_pioneer.png",
		( 91, 131), "images/sprites/close/dv/dv_1_shocked.png",
	))
	image dv shocked pioneer2 close = _sr(im.Composite((501, 879),
		( 21,   0), "images/sprites/close/dv/dv_1_body.png",
		(  0, 311), "images/sprites/close/dv/dv_1_pioneer2.png",
		(112, 131), "images/sprites/close/dv/dv_1_shocked.png",
	))
	image dv shocked swim close = _sr(im.Composite((480, 879),
		(  0,   0), "images/sprites/close/dv/dv_1_body.png",
		(107, 305), "images/sprites/close/dv/dv_1_swim.png",
		( 91, 131), "images/sprites/close/dv/dv_1_shocked.png",
	))
	image dv shy pioneer close = _sr(im.Composite((463, 878),
		(  0,   0), "images/sprites/close/dv/dv_3_body.png",
		( 25, 297), "images/sprites/close/dv/dv_3_pioneer.png",
		(103, 155), "images/sprites/close/dv/dv_3_shy.png",
	))
	image dv shy pioneer2 close = _sr(im.Composite((463, 878),
		(  0,   0), "images/sprites/close/dv/dv_3_body.png",
		( 25, 305), "images/sprites/close/dv/dv_3_pioneer2.png",
		(103, 155), "images/sprites/close/dv/dv_3_shy.png",
	))
	image dv smile coat close = _sr(im.Composite((529, 922),
		(  9,   0), "images/sprites/close/dv/dv_4_body.png",
		(  0, 307), "images/sprites/close/dv/dv_4_coat.png",
		(298, 172), "images/sprites/close/dv/dv_4_smile.png",
	))
	image dv smile pioneer close = _sr(im.Composite((520, 922),
		(  0,   0), "images/sprites/close/dv/dv_4_body.png",
		( 49, 335), "images/sprites/close/dv/dv_4_pioneer.png",
		(289, 172), "images/sprites/close/dv/dv_4_smile.png",
	))
	image dv smile pioneer2 close = _sr(im.Composite((520, 922),
		(  0,   0), "images/sprites/close/dv/dv_4_body.png",
		( 49, 346), "images/sprites/close/dv/dv_4_pioneer2.png",
		(289, 172), "images/sprites/close/dv/dv_4_smile.png",
	))
	image dv smile swim close = _sr(im.Composite((518, 922),
		(  0,   0), "images/sprites/close/dv/dv_4_body.png",
		(149, 346), "images/sprites/close/dv/dv_4_swim.png",
		(289, 172), "images/sprites/close/dv/dv_4_smile.png",
	))
	image dv surprise coat close = _sr(im.Composite((481, 879),
		(  0,   0), "images/sprites/close/dv/dv_1_body.png",
		( 10, 268), "images/sprites/close/dv/dv_1_coat.png",
		( 90, 127), "images/sprites/close/dv/dv_1_surprise.png",
	))
	image dv surprise pioneer close = _sr(im.Composite((480, 879),
		(  0,   0), "images/sprites/close/dv/dv_1_body.png",
		(  2, 315), "images/sprites/close/dv/dv_1_pioneer.png",
		( 90, 127), "images/sprites/close/dv/dv_1_surprise.png",
	))
	image dv surprise pioneer2 close = _sr(im.Composite((501, 879),
		( 21,   0), "images/sprites/close/dv/dv_1_body.png",
		(  0, 311), "images/sprites/close/dv/dv_1_pioneer2.png",
		(111, 127), "images/sprites/close/dv/dv_1_surprise.png",
	))
	image dv surprise swim close = _sr(im.Composite((480, 879),
		(  0,   0), "images/sprites/close/dv/dv_1_body.png",
		(107, 305), "images/sprites/close/dv/dv_1_swim.png",
		( 90, 127), "images/sprites/close/dv/dv_1_surprise.png",
	))
	
	image dv angry coat = _sr(im.Composite((392, 900),
		(  0,   0), "images/sprites/normal/dv/dv_5_body.png",
		( 21, 213), "images/sprites/normal/dv/dv_5_coat.png",
		(185, 151), "images/sprites/normal/dv/dv_5_angry.png",
	))
	image dv angry pioneer = _sr(im.Composite((392, 900),
		(  0,   0), "images/sprites/normal/dv/dv_5_body.png",
		( 14, 252), "images/sprites/normal/dv/dv_5_pioneer.png",
		(185, 151), "images/sprites/normal/dv/dv_5_angry.png",
	))
	image dv angry pioneer2 = _sr(im.Composite((414, 900),
		( 22,   0), "images/sprites/normal/dv/dv_5_body.png",
		(  0, 259), "images/sprites/normal/dv/dv_5_pioneer2.png",
		(207, 151), "images/sprites/normal/dv/dv_5_angry.png",
	))
	image dv cry coat = _sr(im.Composite((388, 893),
		(  0,   0), "images/sprites/normal/dv/dv_1_body.png",
		(  6, 213), "images/sprites/normal/dv/dv_1_coat.png",
		( 74, 104), "images/sprites/normal/dv/dv_1_cry.png",
	))
	image dv cry pioneer = _sr(im.Composite((397, 893),
		( 12,   0), "images/sprites/normal/dv/dv_1_body.png",
		(  0, 252), "images/sprites/normal/dv/dv_1_pioneer.png",
		( 86, 104), "images/sprites/normal/dv/dv_1_cry.png",
	))
	image dv cry pioneer2 = _sr(im.Composite((401, 893),
		( 16,   0), "images/sprites/normal/dv/dv_1_body.png",
		(  0, 249), "images/sprites/normal/dv/dv_1_pioneer2.png",
		( 90, 104), "images/sprites/normal/dv/dv_1_cry.png",
	))
	image dv cry swim = _sr(im.Composite((385, 893),
		(  0,   0), "images/sprites/normal/dv/dv_1_body.png",
		( 26, 244), "images/sprites/normal/dv/dv_1_swim.png",
		( 74, 104), "images/sprites/normal/dv/dv_1_cry.png",
	))
	image dv grin pioneer = _sr(im.Composite((574, 925),
		(  0,   0), "images/sprites/normal/dv/dv_2_body.png",
		( 80, 273), "images/sprites/normal/dv/dv_2_pioneer.png",
		(182, 118), "images/sprites/normal/dv/dv_2_grin.png",
	))
	image dv grin pioneer2 = _sr(im.Composite((574, 925),
		(  0,   0), "images/sprites/normal/dv/dv_2_body.png",
		( 10, 206), "images/sprites/normal/dv/dv_2_pioneer2.png",
		(182, 118), "images/sprites/normal/dv/dv_2_grin.png",
	))
	image dv grin swim = _sr(im.Composite((574, 925),
		(  0,   0), "images/sprites/normal/dv/dv_2_body.png",
		(124, 274), "images/sprites/normal/dv/dv_2_swim.png",
		(182, 118), "images/sprites/normal/dv/dv_2_grin.png",
	))
	image dv guilty pioneer = _sr(im.Composite((376, 893),
		(  5,   0), "images/sprites/normal/dv/dv_3_body.png",
		(  0, 238), "images/sprites/normal/dv/dv_3_pioneer.png",
		(104, 129), "images/sprites/normal/dv/dv_3_guilty.png",
	))
	image dv guilty pioneer2 = _sr(im.Composite((376, 893),
		(  5,   0), "images/sprites/normal/dv/dv_3_body.png",
		(  0, 245), "images/sprites/normal/dv/dv_3_pioneer2.png",
		(104, 129), "images/sprites/normal/dv/dv_3_guilty.png",
	))
	image dv laugh coat = _sr(im.Composite((447, 928),
		(  8,   0), "images/sprites/normal/dv/dv_4_body.png",
		(  0, 245), "images/sprites/normal/dv/dv_4_coat.png",
		(236, 136), "images/sprites/normal/dv/dv_4_laugh.png",
	))
	image dv laugh pioneer = _sr(im.Composite((439, 928),
		(  0,   0), "images/sprites/normal/dv/dv_4_body.png",
		( 39, 268), "images/sprites/normal/dv/dv_4_pioneer.png",
		(228, 136), "images/sprites/normal/dv/dv_4_laugh.png",
	))
	image dv laugh pioneer2 = _sr(im.Composite((439, 928),
		(  0,   0), "images/sprites/normal/dv/dv_4_body.png",
		( 26, 277), "images/sprites/normal/dv/dv_4_pioneer2.png",
		(228, 136), "images/sprites/normal/dv/dv_4_laugh.png",
	))
	image dv laugh swim = _sr(im.Composite((439, 928),
		(  0,   0), "images/sprites/normal/dv/dv_4_body.png",
		(117, 277), "images/sprites/normal/dv/dv_4_swim.png",
		(228, 136), "images/sprites/normal/dv/dv_4_laugh.png",
	))
	image dv normal coat = _sr(im.Composite((447, 928),
		(  8,   0), "images/sprites/normal/dv/dv_4_body.png",
		(  0, 245), "images/sprites/normal/dv/dv_4_coat.png",
		(241, 134), "images/sprites/normal/dv/dv_4_normal.png",
	))
	image dv normal pioneer = _sr(im.Composite((439, 928),
		(  0,   0), "images/sprites/normal/dv/dv_4_body.png",
		( 39, 268), "images/sprites/normal/dv/dv_4_pioneer.png",
		(233, 134), "images/sprites/normal/dv/dv_4_normal.png",
	))
	image dv normal pioneer2 = _sr(im.Composite((439, 928),
		(  0,   0), "images/sprites/normal/dv/dv_4_body.png",
		( 26, 277), "images/sprites/normal/dv/dv_4_pioneer2.png",
		(233, 134), "images/sprites/normal/dv/dv_4_normal.png",
	))
	image dv normal swim = _sr(im.Composite((439, 928),
		(  0,   0), "images/sprites/normal/dv/dv_4_body.png",
		(117, 277), "images/sprites/normal/dv/dv_4_swim.png",
		(233, 134), "images/sprites/normal/dv/dv_4_normal.png",
	))
	image dv rage pioneer = _sr(im.Composite((392, 900),
		(  0,   0), "images/sprites/normal/dv/dv_5_body.png",
		( 14, 252), "images/sprites/normal/dv/dv_5_pioneer.png",
		(167, 139), "images/sprites/normal/dv/dv_5_rage.png",
	))
	image dv rage pioneer2 = _sr(im.Composite((414, 900),
		( 22,   0), "images/sprites/normal/dv/dv_5_body.png",
		(  0, 259), "images/sprites/normal/dv/dv_5_pioneer2.png",
		(189, 139), "images/sprites/normal/dv/dv_5_rage.png",
	))
	image dv sad pioneer = _sr(im.Composite((376, 893),
		(  5,   0), "images/sprites/normal/dv/dv_3_body.png",
		(  0, 238), "images/sprites/normal/dv/dv_3_pioneer.png",
		(102,  95), "images/sprites/normal/dv/dv_3_sad.png",
	))
	image dv sad pioneer2 = _sr(im.Composite((376, 893),
		(  5,   0), "images/sprites/normal/dv/dv_3_body.png",
		(  0, 245), "images/sprites/normal/dv/dv_3_pioneer2.png",
		(102,  95), "images/sprites/normal/dv/dv_3_sad.png",
	))
	image dv scared pioneer = _sr(im.Composite((397, 893),
		( 12,   0), "images/sprites/normal/dv/dv_1_body.png",
		(  0, 252), "images/sprites/normal/dv/dv_1_pioneer.png",
		( 87,  97), "images/sprites/normal/dv/dv_1_scared.png",
	))
	image dv scared pioneer2 = _sr(im.Composite((401, 893),
		( 16,   0), "images/sprites/normal/dv/dv_1_body.png",
		(  0, 249), "images/sprites/normal/dv/dv_1_pioneer2.png",
		( 91,  97), "images/sprites/normal/dv/dv_1_scared.png",
	))
	image dv scared swim = _sr(im.Composite((385, 893),
		(  0,   0), "images/sprites/normal/dv/dv_1_body.png",
		( 26, 244), "images/sprites/normal/dv/dv_1_swim.png",
		( 75,  97), "images/sprites/normal/dv/dv_1_scared.png",
	))
	image dv shocked pioneer = _sr(im.Composite((397, 893),
		( 12,   0), "images/sprites/normal/dv/dv_1_body.png",
		(  0, 252), "images/sprites/normal/dv/dv_1_pioneer.png",
		( 85, 105), "images/sprites/normal/dv/dv_1_shocked.png",
	))
	image dv shocked pioneer2 = _sr(im.Composite((401, 893),
		( 16,   0), "images/sprites/normal/dv/dv_1_body.png",
		(  0, 249), "images/sprites/normal/dv/dv_1_pioneer2.png",
		( 89, 105), "images/sprites/normal/dv/dv_1_shocked.png",
	))
	image dv shocked swim = _sr(im.Composite((385, 893),
		(  0,   0), "images/sprites/normal/dv/dv_1_body.png",
		( 26, 244), "images/sprites/normal/dv/dv_1_swim.png",
		( 73, 105), "images/sprites/normal/dv/dv_1_shocked.png",
	))
	image dv shy coat = _sr(im.Composite((371, 893),
		(  0,   0), "images/sprites/normal/dv/dv_3_body.png",
		( 21, 223), "images/sprites/normal/dv/dv_3_coat.png",
		( 82, 124), "images/sprites/normal/dv/dv_3_shy.png",
	))
	image dv shy pioneer = _sr(im.Composite((376, 893),
		(  5,   0), "images/sprites/normal/dv/dv_3_body.png",
		(  0, 238), "images/sprites/normal/dv/dv_3_pioneer.png",
		( 87, 124), "images/sprites/normal/dv/dv_3_shy.png",
	))
	image dv shy pioneer2 = _sr(im.Composite((376, 893),
		(  5,   0), "images/sprites/normal/dv/dv_3_body.png",
		(  0, 245), "images/sprites/normal/dv/dv_3_pioneer2.png",
		( 87, 124), "images/sprites/normal/dv/dv_3_shy.png",
	))
	image dv smile coat = _sr(im.Composite((447, 928),
		(  8,   0), "images/sprites/normal/dv/dv_4_body.png",
		(  0, 245), "images/sprites/normal/dv/dv_4_coat.png",
		(240, 138), "images/sprites/normal/dv/dv_4_smile.png",
	))
	image dv smile pioneer = _sr(im.Composite((439, 928),
		(  0,   0), "images/sprites/normal/dv/dv_4_body.png",
		( 39, 268), "images/sprites/normal/dv/dv_4_pioneer.png",
		(232, 138), "images/sprites/normal/dv/dv_4_smile.png",
	))
	image dv smile pioneer2 = _sr(im.Composite((439, 928),
		(  0,   0), "images/sprites/normal/dv/dv_4_body.png",
		( 26, 277), "images/sprites/normal/dv/dv_4_pioneer2.png",
		(232, 138), "images/sprites/normal/dv/dv_4_smile.png",
	))
	image dv smile swim = _sr(im.Composite((439, 928),
		(  0,   0), "images/sprites/normal/dv/dv_4_body.png",
		(117, 277), "images/sprites/normal/dv/dv_4_swim.png",
		(232, 138), "images/sprites/normal/dv/dv_4_smile.png",
	))
	image dv surprise coat = _sr(im.Composite((388, 893),
		(  0,   0), "images/sprites/normal/dv/dv_1_body.png",
		(  6, 213), "images/sprites/normal/dv/dv_1_coat.png",
		( 72, 102), "images/sprites/normal/dv/dv_1_surprise.png",
	))
	image dv surprise pioneer = _sr(im.Composite((397, 893),
		( 12,   0), "images/sprites/normal/dv/dv_1_body.png",
		(  0, 252), "images/sprites/normal/dv/dv_1_pioneer.png",
		( 84, 102), "images/sprites/normal/dv/dv_1_surprise.png",
	))
	image dv surprise pioneer2 = _sr(im.Composite((401, 893),
		( 16,   0), "images/sprites/normal/dv/dv_1_body.png",
		(  0, 249), "images/sprites/normal/dv/dv_1_pioneer2.png",
		( 88, 102), "images/sprites/normal/dv/dv_1_surprise.png",
	))
	image dv surprise swim = _sr(im.Composite((385, 893),
		(  0,   0), "images/sprites/normal/dv/dv_1_body.png",
		( 26, 244), "images/sprites/normal/dv/dv_1_swim.png",
		( 72, 102), "images/sprites/normal/dv/dv_1_surprise.png",
	))
	
	image dv angry pioneer far = _sr(im.Composite((297, 833),
		(  0,   0), "images/sprites/far/dv/dv_5_body.png",
		(  3, 190), "images/sprites/far/dv/dv_5_pioneer.png",
		(139, 114), "images/sprites/far/dv/dv_5_angry.png",
	))
	image dv angry pioneer2 far = _sr(im.Composite((313, 833),
		( 16,   0), "images/sprites/far/dv/dv_5_body.png",
		(  0, 195), "images/sprites/far/dv/dv_5_pioneer2.png",
		(155, 114), "images/sprites/far/dv/dv_5_angry.png",
	))
	image dv cry pioneer far = _sr(im.Composite((308, 828),
		( 19,   0), "images/sprites/far/dv/dv_1_body.png",
		(  0, 189), "images/sprites/far/dv/dv_1_pioneer.png",
		( 74,  79), "images/sprites/far/dv/dv_1_cry.png",
	))
	image dv cry pioneer2 far = _sr(im.Composite((308, 828),
		( 19,   0), "images/sprites/far/dv/dv_1_body.png",
		(  0, 187), "images/sprites/far/dv/dv_1_pioneer2.png",
		( 74,  79), "images/sprites/far/dv/dv_1_cry.png",
	))
	image dv cry swim far = _sr(im.Composite((289, 828),
		(  0,   0), "images/sprites/far/dv/dv_1_body.png",
		( 19, 184), "images/sprites/far/dv/dv_1_swim.png",
		( 55,  79), "images/sprites/far/dv/dv_1_cry.png",
	))
	image dv grin pioneer far = _sr(im.Composite((431, 851),
		(  0,   0), "images/sprites/far/dv/dv_2_body.png",
		( 52, 205), "images/sprites/far/dv/dv_2_pioneer.png",
		(137,  88), "images/sprites/far/dv/dv_2_grin.png",
	))
	image dv grin pioneer2 far = _sr(im.Composite((431, 851),
		(  0,   0), "images/sprites/far/dv/dv_2_body.png",
		(  8, 154), "images/sprites/far/dv/dv_2_pioneer2.png",
		(137,  88), "images/sprites/far/dv/dv_2_grin.png",
	))
	image dv grin swim far = _sr(im.Composite((431, 851),
		(  0,   0), "images/sprites/far/dv/dv_2_body.png",
		( 93, 205), "images/sprites/far/dv/dv_2_swim.png",
		(137,  88), "images/sprites/far/dv/dv_2_grin.png",
	))
	image dv guilty pioneer far = _sr(im.Composite((291, 827),
		( 10,   0), "images/sprites/far/dv/dv_3_body.png",
		(  0, 178), "images/sprites/far/dv/dv_3_pioneer.png",
		( 84,  97), "images/sprites/far/dv/dv_3_guilty.png",
	))
	image dv guilty pioneer2 far = _sr(im.Composite((291, 827),
		( 10,   0), "images/sprites/far/dv/dv_3_body.png",
		(  0, 183), "images/sprites/far/dv/dv_3_pioneer2.png",
		( 84,  97), "images/sprites/far/dv/dv_3_guilty.png",
	))
	image dv laugh pioneer far = _sr(im.Composite((379, 854),
		(  0,   0), "images/sprites/far/dv/dv_4_body.png",
		( 29, 202), "images/sprites/far/dv/dv_4_pioneer.png",
		(170, 103), "images/sprites/far/dv/dv_4_laugh.png",
	))
	image dv laugh pioneer2 far = _sr(im.Composite((379, 854),
		(  0,   0), "images/sprites/far/dv/dv_4_body.png",
		( 19, 208), "images/sprites/far/dv/dv_4_pioneer2.png",
		(170, 103), "images/sprites/far/dv/dv_4_laugh.png",
	))
	image dv laugh swim far = _sr(im.Composite((379, 854),
		(  0,   0), "images/sprites/far/dv/dv_4_body.png",
		( 87, 208), "images/sprites/far/dv/dv_4_swim.png",
		(170, 103), "images/sprites/far/dv/dv_4_laugh.png",
	))
	image dv normal pioneer far = _sr(im.Composite((379, 854),
		(  0,   0), "images/sprites/far/dv/dv_4_body.png",
		( 29, 202), "images/sprites/far/dv/dv_4_pioneer.png",
		(174, 101), "images/sprites/far/dv/dv_4_normal.png",
	))
	image dv normal pioneer2 far = _sr(im.Composite((379, 854),
		(  0,   0), "images/sprites/far/dv/dv_4_body.png",
		( 19, 208), "images/sprites/far/dv/dv_4_pioneer2.png",
		(174, 101), "images/sprites/far/dv/dv_4_normal.png",
	))
	image dv normal swim far = _sr(im.Composite((379, 854),
		(  0,   0), "images/sprites/far/dv/dv_4_body.png",
		( 87, 208), "images/sprites/far/dv/dv_4_swim.png",
		(174, 101), "images/sprites/far/dv/dv_4_normal.png",
	))
	image dv rage pioneer far = _sr(im.Composite((297, 833),
		(  0,   0), "images/sprites/far/dv/dv_5_body.png",
		(  3, 190), "images/sprites/far/dv/dv_5_pioneer.png",
		(126, 104), "images/sprites/far/dv/dv_5_rage.png",
	))
	image dv rage pioneer2 far = _sr(im.Composite((313, 833),
		( 16,   0), "images/sprites/far/dv/dv_5_body.png",
		(  0, 195), "images/sprites/far/dv/dv_5_pioneer2.png",
		(142, 104), "images/sprites/far/dv/dv_5_rage.png",
	))
	image dv sad pioneer far = _sr(im.Composite((291, 827),
		( 10,   0), "images/sprites/far/dv/dv_3_body.png",
		(  0, 178), "images/sprites/far/dv/dv_3_pioneer.png",
		( 83,  71), "images/sprites/far/dv/dv_3_sad.png",
	))
	image dv sad pioneer2 far = _sr(im.Composite((291, 827),
		( 10,   0), "images/sprites/far/dv/dv_3_body.png",
		(  0, 183), "images/sprites/far/dv/dv_3_pioneer2.png",
		( 83,  71), "images/sprites/far/dv/dv_3_sad.png",
	))
	image dv scared pioneer far = _sr(im.Composite((308, 828),
		( 19,   0), "images/sprites/far/dv/dv_1_body.png",
		(  0, 189), "images/sprites/far/dv/dv_1_pioneer.png",
		( 75,  73), "images/sprites/far/dv/dv_1_scared.png",
	))
	image dv scared pioneer2 far = _sr(im.Composite((308, 828),
		( 19,   0), "images/sprites/far/dv/dv_1_body.png",
		(  0, 187), "images/sprites/far/dv/dv_1_pioneer2.png",
		( 75,  73), "images/sprites/far/dv/dv_1_scared.png",
	))
	image dv scared swim far = _sr(im.Composite((289, 828),
		(  0,   0), "images/sprites/far/dv/dv_1_body.png",
		( 19, 184), "images/sprites/far/dv/dv_1_swim.png",
		( 56,  73), "images/sprites/far/dv/dv_1_scared.png",
	))
	image dv shocked pioneer far = _sr(im.Composite((308, 828),
		( 19,   0), "images/sprites/far/dv/dv_1_body.png",
		(  0, 189), "images/sprites/far/dv/dv_1_pioneer.png",
		( 74,  79), "images/sprites/far/dv/dv_1_shocked.png",
	))
	image dv shocked pioneer2 far = _sr(im.Composite((308, 828),
		( 19,   0), "images/sprites/far/dv/dv_1_body.png",
		(  0, 187), "images/sprites/far/dv/dv_1_pioneer2.png",
		( 74,  79), "images/sprites/far/dv/dv_1_shocked.png",
	))
	image dv shocked swim far = _sr(im.Composite((289, 828),
		(  0,   0), "images/sprites/far/dv/dv_1_body.png",
		( 19, 184), "images/sprites/far/dv/dv_1_swim.png",
		( 55,  79), "images/sprites/far/dv/dv_1_shocked.png",
	))
	image dv shy pioneer far = _sr(im.Composite((291, 827),
		( 10,   0), "images/sprites/far/dv/dv_3_body.png",
		(  0, 178), "images/sprites/far/dv/dv_3_pioneer.png",
		( 71,  93), "images/sprites/far/dv/dv_3_shy.png",
	))
	image dv shy pioneer2 far = _sr(im.Composite((291, 827),
		( 10,   0), "images/sprites/far/dv/dv_3_body.png",
		(  0, 183), "images/sprites/far/dv/dv_3_pioneer2.png",
		( 71,  93), "images/sprites/far/dv/dv_3_shy.png",
	))
	image dv smile pioneer far = _sr(im.Composite((379, 854),
		(  0,   0), "images/sprites/far/dv/dv_4_body.png",
		( 29, 202), "images/sprites/far/dv/dv_4_pioneer.png",
		(173, 104), "images/sprites/far/dv/dv_4_smile.png",
	))
	image dv smile pioneer2 far = _sr(im.Composite((379, 854),
		(  0,   0), "images/sprites/far/dv/dv_4_body.png",
		( 19, 208), "images/sprites/far/dv/dv_4_pioneer2.png",
		(173, 104), "images/sprites/far/dv/dv_4_smile.png",
	))
	image dv smile swim far = _sr(im.Composite((379, 854),
		(  0,   0), "images/sprites/far/dv/dv_4_body.png",
		( 87, 208), "images/sprites/far/dv/dv_4_swim.png",
		(173, 104), "images/sprites/far/dv/dv_4_smile.png",
	))
	image dv surprise pioneer far = _sr(im.Composite((308, 828),
		( 19,   0), "images/sprites/far/dv/dv_1_body.png",
		(  0, 189), "images/sprites/far/dv/dv_1_pioneer.png",
		( 73,  77), "images/sprites/far/dv/dv_1_surprise.png",
	))
	image dv surprise pioneer2 far = _sr(im.Composite((308, 828),
		( 19,   0), "images/sprites/far/dv/dv_1_body.png",
		(  0, 187), "images/sprites/far/dv/dv_1_pioneer2.png",
		( 73,  77), "images/sprites/far/dv/dv_1_surprise.png",
	))
	image dv surprise swim far = _sr(im.Composite((289, 828),
		(  0,   0), "images/sprites/far/dv/dv_1_body.png",
		( 19, 184), "images/sprites/far/dv/dv_1_swim.png",
		( 54,  77), "images/sprites/far/dv/dv_1_surprise.png",
	))
	
	image el angry pioneer close = _sr(im.Composite((619, 1042),
		(  0,   0), "images/sprites/close/el/el_3_body.png",
		( 88, 347), "images/sprites/close/el/el_3_pioneer.png",
		(195, 135), "images/sprites/close/el/el_3_angry.png",
	))
	image el fingal pioneer close = _sr(im.Composite((562, 1045),
		(  0,   0), "images/sprites/close/el/el_2_body.png",
		( 12, 347), "images/sprites/close/el/el_2_pioneer.png",
		(231, 135), "images/sprites/close/el/el_2_fingal.png",
	))
	image el grin pioneer close = _sr(im.Composite((721, 1035),
		(  0,   0), "images/sprites/close/el/el_1_body.png",
		(  0, 283), "images/sprites/close/el/el_1_pioneer.png",
		(248, 135), "images/sprites/close/el/el_1_grin.png",
	))
	image el laugh pioneer close = _sr(im.Composite((619, 1042),
		(  0,   0), "images/sprites/close/el/el_3_body.png",
		( 88, 347), "images/sprites/close/el/el_3_pioneer.png",
		(195, 135), "images/sprites/close/el/el_3_laugh.png",
	))
	image el normal pioneer close = _sr(im.Composite((721, 1035),
		(  0,   0), "images/sprites/close/el/el_1_body.png",
		(  0, 283), "images/sprites/close/el/el_1_pioneer.png",
		(248, 149), "images/sprites/close/el/el_1_normal.png",
	))
	image el sad pioneer close = _sr(im.Composite((562, 1045),
		(  0,   0), "images/sprites/close/el/el_2_body.png",
		( 12, 347), "images/sprites/close/el/el_2_pioneer.png",
		(228, 135), "images/sprites/close/el/el_2_sad.png",
	))
	image el scared pioneer close = _sr(im.Composite((562, 1045),
		(  0,   0), "images/sprites/close/el/el_2_body.png",
		( 12, 347), "images/sprites/close/el/el_2_pioneer.png",
		(235, 118), "images/sprites/close/el/el_2_scared.png",
	))
	image el serious pioneer close = _sr(im.Composite((619, 1042),
		(  0,   0), "images/sprites/close/el/el_3_body.png",
		( 88, 347), "images/sprites/close/el/el_3_pioneer.png",
		(195, 135), "images/sprites/close/el/el_3_serious.png",
	))
	image el shocked pioneer close = _sr(im.Composite((562, 1045),
		(  0,   0), "images/sprites/close/el/el_2_body.png",
		( 12, 347), "images/sprites/close/el/el_2_pioneer.png",
		(233, 112), "images/sprites/close/el/el_2_shocked.png",
	))
	image el smile pioneer close = _sr(im.Composite((721, 1035),
		(  0,   0), "images/sprites/close/el/el_1_body.png",
		(  0, 283), "images/sprites/close/el/el_1_pioneer.png",
		(248, 135), "images/sprites/close/el/el_1_smile.png",
	))
	image el surprise pioneer close = _sr(im.Composite((562, 1045),
		(  0,   0), "images/sprites/close/el/el_2_body.png",
		( 12, 347), "images/sprites/close/el/el_2_pioneer.png",
		(223, 112), "images/sprites/close/el/el_2_surprise.png",
	))
	image el upset pioneer close = _sr(im.Composite((562, 1045),
		(  0,   0), "images/sprites/close/el/el_2_body.png",
		( 12, 347), "images/sprites/close/el/el_2_pioneer.png",
		(231, 135), "images/sprites/close/el/el_2_upset.png",
	))
	
	image el angry pioneer = _sr(im.Composite((495, 1024),
		(  0,   0), "images/sprites/normal/el/el_3_body.png",
		( 70, 278), "images/sprites/normal/el/el_3_pioneer.png",
		(155, 108), "images/sprites/normal/el/el_3_angry.png",
	))
	image el fingal pioneer = _sr(im.Composite((450, 1026),
		(  0,   0), "images/sprites/normal/el/el_2_body.png",
		(  9, 277), "images/sprites/normal/el/el_2_pioneer.png",
		(184, 108), "images/sprites/normal/el/el_2_fingal.png",
	))
	image el grin pioneer = _sr(im.Composite((577, 1018),
		(  1,   0), "images/sprites/normal/el/el_1_body.png",
		(  0, 226), "images/sprites/normal/el/el_1_pioneer.png",
		(198, 108), "images/sprites/normal/el/el_1_grin.png",
	))
	image el laugh pioneer = _sr(im.Composite((495, 1024),
		(  0,   0), "images/sprites/normal/el/el_3_body.png",
		( 70, 278), "images/sprites/normal/el/el_3_pioneer.png",
		(156, 108), "images/sprites/normal/el/el_3_laugh.png",
	))
	image el normal pioneer = _sr(im.Composite((577, 1018),
		(  1,   0), "images/sprites/normal/el/el_1_body.png",
		(  0, 226), "images/sprites/normal/el/el_1_pioneer.png",
		(198, 119), "images/sprites/normal/el/el_1_normal.png",
	))
	image el sad pioneer = _sr(im.Composite((450, 1026),
		(  0,   0), "images/sprites/normal/el/el_2_body.png",
		(  9, 277), "images/sprites/normal/el/el_2_pioneer.png",
		(183, 107), "images/sprites/normal/el/el_2_sad.png",
	))
	image el scared pioneer = _sr(im.Composite((450, 1026),
		(  0,   0), "images/sprites/normal/el/el_2_body.png",
		(  9, 277), "images/sprites/normal/el/el_2_pioneer.png",
		(188,  94), "images/sprites/normal/el/el_2_scared.png",
	))
	image el serious pioneer = _sr(im.Composite((495, 1024),
		(  0,   0), "images/sprites/normal/el/el_3_body.png",
		( 70, 278), "images/sprites/normal/el/el_3_pioneer.png",
		(156, 108), "images/sprites/normal/el/el_3_serious.png",
	))
	image el shocked pioneer = _sr(im.Composite((450, 1026),
		(  0,   0), "images/sprites/normal/el/el_2_body.png",
		(  9, 277), "images/sprites/normal/el/el_2_pioneer.png",
		(186,  89), "images/sprites/normal/el/el_2_shocked.png",
	))
	image el smile pioneer = _sr(im.Composite((577, 1018),
		(  1,   0), "images/sprites/normal/el/el_1_body.png",
		(  0, 226), "images/sprites/normal/el/el_1_pioneer.png",
		(198, 108), "images/sprites/normal/el/el_1_smile.png",
	))
	image el surprise pioneer = _sr(im.Composite((450, 1026),
		(  0,   0), "images/sprites/normal/el/el_2_body.png",
		(  9, 277), "images/sprites/normal/el/el_2_pioneer.png",
		(178,  89), "images/sprites/normal/el/el_2_surprise.png",
	))
	image el upset pioneer = _sr(im.Composite((450, 1026),
		(  0,   0), "images/sprites/normal/el/el_2_body.png",
		(  9, 277), "images/sprites/normal/el/el_2_pioneer.png",
		(184, 108), "images/sprites/normal/el/el_2_upset.png",
	))
	
	image el angry pioneer far = _sr(im.Composite((372, 925),
		(  0,   0), "images/sprites/far/el/el_3_body.png",
		( 53, 208), "images/sprites/far/el/el_3_pioneer.png",
		(117,  80), "images/sprites/far/el/el_3_angry.png",
	))
	image el fingal pioneer far = _sr(im.Composite((337, 927),
		(  0,   0), "images/sprites/far/el/el_2_body.png",
		(  7, 208), "images/sprites/far/el/el_2_pioneer.png",
		(138,  81), "images/sprites/far/el/el_2_fingal.png",
	))
	image el grin pioneer far = _sr(im.Composite((432, 921),
		(  0,   0), "images/sprites/far/el/el_1_body.png",
		(  0, 169), "images/sprites/far/el/el_1_pioneer.png",
		(148,  81), "images/sprites/far/el/el_1_grin.png",
	))
	image el laugh pioneer far = _sr(im.Composite((372, 925),
		(  0,   0), "images/sprites/far/el/el_3_body.png",
		( 53, 208), "images/sprites/far/el/el_3_pioneer.png",
		(117,  81), "images/sprites/far/el/el_3_laugh.png",
	))
	image el normal pioneer far = _sr(im.Composite((432, 921),
		(  0,   0), "images/sprites/far/el/el_1_body.png",
		(  0, 169), "images/sprites/far/el/el_1_pioneer.png",
		(148,  89), "images/sprites/far/el/el_1_normal.png",
	))
	image el sad pioneer far = _sr(im.Composite((337, 927),
		(  0,   0), "images/sprites/far/el/el_2_body.png",
		(  7, 208), "images/sprites/far/el/el_2_pioneer.png",
		(137,  81), "images/sprites/far/el/el_2_sad.png",
	))
	image el scared pioneer far = _sr(im.Composite((337, 927),
		(  0,   0), "images/sprites/far/el/el_2_body.png",
		(  7, 208), "images/sprites/far/el/el_2_pioneer.png",
		(140,  70), "images/sprites/far/el/el_2_scared.png",
	))
	image el serious pioneer far = _sr(im.Composite((372, 925),
		(  0,   0), "images/sprites/far/el/el_3_body.png",
		( 53, 208), "images/sprites/far/el/el_3_pioneer.png",
		(117,  81), "images/sprites/far/el/el_3_serious.png",
	))
	image el shocked pioneer far = _sr(im.Composite((337, 927),
		(  0,   0), "images/sprites/far/el/el_2_body.png",
		(  7, 208), "images/sprites/far/el/el_2_pioneer.png",
		(139,  67), "images/sprites/far/el/el_2_shocked.png",
	))
	image el smile pioneer far = _sr(im.Composite((432, 921),
		(  0,   0), "images/sprites/far/el/el_1_body.png",
		(  0, 169), "images/sprites/far/el/el_1_pioneer.png",
		(148,  81), "images/sprites/far/el/el_1_smile.png",
	))
	image el surprise pioneer far = _sr(im.Composite((337, 927),
		(  0,   0), "images/sprites/far/el/el_2_body.png",
		(  7, 208), "images/sprites/far/el/el_2_pioneer.png",
		(133,  67), "images/sprites/far/el/el_2_surprise.png",
	))
	image el upset pioneer far = _sr(im.Composite((337, 927),
		(  0,   0), "images/sprites/far/el/el_2_body.png",
		(  7, 208), "images/sprites/far/el/el_2_pioneer.png",
		(138,  81), "images/sprites/far/el/el_2_upset.png",
	))
	
	image mi angry pioneer close = _sr(im.Composite((726, 855),
		(  0,   0), "images/sprites/close/mi/mi_3_body.png",
		(107, 326), "images/sprites/close/mi/mi_3_pioneer.png",
		(330, 179), "images/sprites/close/mi/mi_3_angry.png",
	))
	image mi angry swim close = _sr(im.Composite((726, 855),
		(  0,   0), "images/sprites/close/mi/mi_3_body.png",
		(205, 336), "images/sprites/close/mi/mi_3_swim.png",
		(330, 179), "images/sprites/close/mi/mi_3_angry.png",
	))
	image mi cry pioneer close = _sr(im.Composite((666, 854),
		(  0,   0), "images/sprites/close/mi/mi_1_body.png",
		( 76, 306), "images/sprites/close/mi/mi_1_pioneer.png",
		(268, 150), "images/sprites/close/mi/mi_1_cry.png",
	))
	image mi cry swim close = _sr(im.Composite((666, 854),
		(  0,   0), "images/sprites/close/mi/mi_1_body.png",
		(170, 330), "images/sprites/close/mi/mi_1_swim.png",
		(268, 150), "images/sprites/close/mi/mi_1_cry.png",
	))
	image mi cry_smile pioneer close = _sr(im.Composite((715, 839),
		(  0,   0), "images/sprites/close/mi/mi_2_body.png",
		(191, 287), "images/sprites/close/mi/mi_2_pioneer.png",
		(219, 170), "images/sprites/close/mi/mi_2_cry_smile.png",
	))
	image mi cry_smile swim close = _sr(im.Composite((715, 839),
		(  0,   0), "images/sprites/close/mi/mi_2_body.png",
		(268, 312), "images/sprites/close/mi/mi_2_swim.png",
		(219, 170), "images/sprites/close/mi/mi_2_cry_smile.png",
	))
	image mi dontlike pioneer close = _sr(im.Composite((666, 854),
		(  0,   0), "images/sprites/close/mi/mi_1_body.png",
		( 76, 306), "images/sprites/close/mi/mi_1_pioneer.png",
		(268, 146), "images/sprites/close/mi/mi_1_dontlike.png",
	))
	image mi dontlike swim close = _sr(im.Composite((666, 854),
		(  0,   0), "images/sprites/close/mi/mi_1_body.png",
		(170, 330), "images/sprites/close/mi/mi_1_swim.png",
		(268, 146), "images/sprites/close/mi/mi_1_dontlike.png",
	))
	image mi grin pioneer close = _sr(im.Composite((715, 839),
		(  0,   0), "images/sprites/close/mi/mi_2_body.png",
		(191, 287), "images/sprites/close/mi/mi_2_pioneer.png",
		(216, 163), "images/sprites/close/mi/mi_2_grin.png",
	))
	image mi grin swim close = _sr(im.Composite((715, 839),
		(  0,   0), "images/sprites/close/mi/mi_2_body.png",
		(268, 312), "images/sprites/close/mi/mi_2_swim.png",
		(216, 163), "images/sprites/close/mi/mi_2_grin.png",
	))
	image mi happy pioneer close = _sr(im.Composite((715, 839),
		(  0,   0), "images/sprites/close/mi/mi_2_body.png",
		(191, 287), "images/sprites/close/mi/mi_2_pioneer.png",
		(216, 170), "images/sprites/close/mi/mi_2_happy.png",
	))
	image mi happy swim close = _sr(im.Composite((715, 839),
		(  0,   0), "images/sprites/close/mi/mi_2_body.png",
		(268, 312), "images/sprites/close/mi/mi_2_swim.png",
		(216, 170), "images/sprites/close/mi/mi_2_happy.png",
	))
	image mi laugh pioneer close = _sr(im.Composite((666, 854),
		(  0,   0), "images/sprites/close/mi/mi_1_body.png",
		( 76, 306), "images/sprites/close/mi/mi_1_pioneer.png",
		(283, 142), "images/sprites/close/mi/mi_1_laugh.png",
	))
	image mi laugh swim close = _sr(im.Composite((666, 854),
		(  0,   0), "images/sprites/close/mi/mi_1_body.png",
		(170, 330), "images/sprites/close/mi/mi_1_swim.png",
		(283, 142), "images/sprites/close/mi/mi_1_laugh.png",
	))
	image mi normal pioneer close = _sr(im.Composite((726, 855),
		(  0,   0), "images/sprites/close/mi/mi_3_body.png",
		(107, 326), "images/sprites/close/mi/mi_3_pioneer.png",
		(331, 166), "images/sprites/close/mi/mi_3_normal.png",
	))
	image mi normal swim close = _sr(im.Composite((726, 855),
		(  0,   0), "images/sprites/close/mi/mi_3_body.png",
		(205, 336), "images/sprites/close/mi/mi_3_swim.png",
		(331, 166), "images/sprites/close/mi/mi_3_normal.png",
	))
	image mi rage pioneer close = _sr(im.Composite((726, 855),
		(  0,   0), "images/sprites/close/mi/mi_3_body.png",
		(107, 326), "images/sprites/close/mi/mi_3_pioneer.png",
		(303, 171), "images/sprites/close/mi/mi_3_rage.png",
	))
	image mi rage swim close = _sr(im.Composite((726, 855),
		(  0,   0), "images/sprites/close/mi/mi_3_body.png",
		(205, 336), "images/sprites/close/mi/mi_3_swim.png",
		(303, 171), "images/sprites/close/mi/mi_3_rage.png",
	))
	image mi sad pioneer close = _sr(im.Composite((715, 839),
		(  0,   0), "images/sprites/close/mi/mi_2_body.png",
		(191, 287), "images/sprites/close/mi/mi_2_pioneer.png",
		(222, 173), "images/sprites/close/mi/mi_2_sad.png",
	))
	image mi sad swim close = _sr(im.Composite((715, 839),
		(  0,   0), "images/sprites/close/mi/mi_2_body.png",
		(268, 312), "images/sprites/close/mi/mi_2_swim.png",
		(222, 173), "images/sprites/close/mi/mi_2_sad.png",
	))
	image mi scared pioneer close = _sr(im.Composite((666, 854),
		(  0,   0), "images/sprites/close/mi/mi_1_body.png",
		( 76, 306), "images/sprites/close/mi/mi_1_pioneer.png",
		(285, 133), "images/sprites/close/mi/mi_1_scared.png",
	))
	image mi scared swim close = _sr(im.Composite((666, 854),
		(  0,   0), "images/sprites/close/mi/mi_1_body.png",
		(170, 330), "images/sprites/close/mi/mi_1_swim.png",
		(285, 133), "images/sprites/close/mi/mi_1_scared.png",
	))
	image mi serious pioneer close = _sr(im.Composite((726, 855),
		(  0,   0), "images/sprites/close/mi/mi_3_body.png",
		(107, 326), "images/sprites/close/mi/mi_3_pioneer.png",
		(325, 176), "images/sprites/close/mi/mi_3_serious.png",
	))
	image mi serious swim close = _sr(im.Composite((726, 855),
		(  0,   0), "images/sprites/close/mi/mi_3_body.png",
		(205, 336), "images/sprites/close/mi/mi_3_swim.png",
		(325, 176), "images/sprites/close/mi/mi_3_serious.png",
	))
	image mi shocked pioneer close = _sr(im.Composite((666, 854),
		(  0,   0), "images/sprites/close/mi/mi_1_body.png",
		( 76, 306), "images/sprites/close/mi/mi_1_pioneer.png",
		(290, 124), "images/sprites/close/mi/mi_1_shocked.png",
	))
	image mi shocked swim close = _sr(im.Composite((666, 854),
		(  0,   0), "images/sprites/close/mi/mi_1_body.png",
		(170, 330), "images/sprites/close/mi/mi_1_swim.png",
		(290, 124), "images/sprites/close/mi/mi_1_shocked.png",
	))
	image mi shy pioneer close = _sr(im.Composite((666, 854),
		(  0,   0), "images/sprites/close/mi/mi_1_body.png",
		( 76, 306), "images/sprites/close/mi/mi_1_pioneer.png",
		(259, 136), "images/sprites/close/mi/mi_1_shy.png",
	))
	image mi shy swim close = _sr(im.Composite((666, 854),
		(  0,   0), "images/sprites/close/mi/mi_1_body.png",
		(170, 330), "images/sprites/close/mi/mi_1_swim.png",
		(259, 136), "images/sprites/close/mi/mi_1_shy.png",
	))
	image mi smile pioneer close = _sr(im.Composite((715, 839),
		(  0,   0), "images/sprites/close/mi/mi_2_body.png",
		(191, 287), "images/sprites/close/mi/mi_2_pioneer.png",
		(212, 165), "images/sprites/close/mi/mi_2_smile.png",
	))
	image mi smile swim close = _sr(im.Composite((715, 839),
		(  0,   0), "images/sprites/close/mi/mi_2_body.png",
		(268, 312), "images/sprites/close/mi/mi_2_swim.png",
		(212, 165), "images/sprites/close/mi/mi_2_smile.png",
	))
	image mi surprise pioneer close = _sr(im.Composite((666, 854),
		(  0,   0), "images/sprites/close/mi/mi_1_body.png",
		( 76, 306), "images/sprites/close/mi/mi_1_pioneer.png",
		(282, 113), "images/sprites/close/mi/mi_1_surprise.png",
	))
	image mi surprise swim close = _sr(im.Composite((666, 854),
		(  0,   0), "images/sprites/close/mi/mi_1_body.png",
		(170, 330), "images/sprites/close/mi/mi_1_swim.png",
		(282, 113), "images/sprites/close/mi/mi_1_surprise.png",
	))
	image mi upset pioneer close = _sr(im.Composite((726, 855),
		(  0,   0), "images/sprites/close/mi/mi_3_body.png",
		(107, 326), "images/sprites/close/mi/mi_3_pioneer.png",
		(322, 179), "images/sprites/close/mi/mi_3_upset.png",
	))
	image mi upset swim close = _sr(im.Composite((726, 855),
		(  0,   0), "images/sprites/close/mi/mi_3_body.png",
		(205, 336), "images/sprites/close/mi/mi_3_swim.png",
		(322, 179), "images/sprites/close/mi/mi_3_upset.png",
	))
	
	image mi angry pioneer = _sr(im.Composite((709, 874),
		(  0,   0), "images/sprites/normal/mi/mi_3_body.png",
		(153, 261), "images/sprites/normal/mi/mi_3_pioneer.png",
		(331, 143), "images/sprites/normal/mi/mi_3_angry.png",
	))
	image mi angry swim = _sr(im.Composite((709, 874),
		(  0,   0), "images/sprites/normal/mi/mi_3_body.png",
		(231, 269), "images/sprites/normal/mi/mi_3_swim.png",
		(331, 143), "images/sprites/normal/mi/mi_3_angry.png",
	))
	image mi cry pioneer = _sr(im.Composite((621, 873),
		(  0,   0), "images/sprites/normal/mi/mi_1_body.png",
		( 90, 245), "images/sprites/normal/mi/mi_1_pioneer.png",
		(302, 119), "images/sprites/normal/mi/mi_1_cry.png",
	))
	image mi cry swim = _sr(im.Composite((621, 873),
		(  0,   0), "images/sprites/normal/mi/mi_1_body.png",
		(146, 263), "images/sprites/normal/mi/mi_1_swim.png",
		(302, 119), "images/sprites/normal/mi/mi_1_cry.png",
	))
	image mi cry_smile pioneer = _sr(im.Composite((602, 862),
		(  0,   0), "images/sprites/normal/mi/mi_2_body.png",
		(129, 230), "images/sprites/normal/mi/mi_2_pioneer.png",
		(205, 137), "images/sprites/normal/mi/mi_2_cry_smile.png",
	))
	image mi cry_smile swim = _sr(im.Composite((602, 862),
		(  0,   0), "images/sprites/normal/mi/mi_2_body.png",
		(174, 251), "images/sprites/normal/mi/mi_2_swim.png",
		(205, 137), "images/sprites/normal/mi/mi_2_cry_smile.png",
	))
	image mi dontlike pioneer = _sr(im.Composite((621, 873),
		(  0,   0), "images/sprites/normal/mi/mi_1_body.png",
		( 90, 245), "images/sprites/normal/mi/mi_1_pioneer.png",
		(302, 116), "images/sprites/normal/mi/mi_1_dontlike.png",
	))
	image mi dontlike swim = _sr(im.Composite((621, 873),
		(  0,   0), "images/sprites/normal/mi/mi_1_body.png",
		(146, 263), "images/sprites/normal/mi/mi_1_swim.png",
		(302, 116), "images/sprites/normal/mi/mi_1_dontlike.png",
	))
	image mi grin pioneer = _sr(im.Composite((602, 862),
		(  0,   0), "images/sprites/normal/mi/mi_2_body.png",
		(129, 230), "images/sprites/normal/mi/mi_2_pioneer.png",
		(202, 131), "images/sprites/normal/mi/mi_2_grin.png",
	))
	image mi grin swim = _sr(im.Composite((602, 862),
		(  0,   0), "images/sprites/normal/mi/mi_2_body.png",
		(174, 251), "images/sprites/normal/mi/mi_2_swim.png",
		(202, 131), "images/sprites/normal/mi/mi_2_grin.png",
	))
	image mi happy pioneer = _sr(im.Composite((602, 862),
		(  0,   0), "images/sprites/normal/mi/mi_2_body.png",
		(129, 230), "images/sprites/normal/mi/mi_2_pioneer.png",
		(203, 137), "images/sprites/normal/mi/mi_2_happy.png",
	))
	image mi happy swim = _sr(im.Composite((602, 862),
		(  0,   0), "images/sprites/normal/mi/mi_2_body.png",
		(174, 251), "images/sprites/normal/mi/mi_2_swim.png",
		(203, 137), "images/sprites/normal/mi/mi_2_happy.png",
	))
	image mi laugh pioneer = _sr(im.Composite((621, 873),
		(  0,   0), "images/sprites/normal/mi/mi_1_body.png",
		( 90, 245), "images/sprites/normal/mi/mi_1_pioneer.png",
		(314, 113), "images/sprites/normal/mi/mi_1_laugh.png",
	))
	image mi laugh swim = _sr(im.Composite((621, 873),
		(  0,   0), "images/sprites/normal/mi/mi_1_body.png",
		(146, 263), "images/sprites/normal/mi/mi_1_swim.png",
		(314, 113), "images/sprites/normal/mi/mi_1_laugh.png",
	))
	image mi normal pioneer = _sr(im.Composite((709, 874),
		(  0,   0), "images/sprites/normal/mi/mi_3_body.png",
		(153, 261), "images/sprites/normal/mi/mi_3_pioneer.png",
		(332, 132), "images/sprites/normal/mi/mi_3_normal.png",
	))
	image mi normal swim = _sr(im.Composite((709, 874),
		(  0,   0), "images/sprites/normal/mi/mi_3_body.png",
		(231, 269), "images/sprites/normal/mi/mi_3_swim.png",
		(332, 132), "images/sprites/normal/mi/mi_3_normal.png",
	))
	image mi rage pioneer = _sr(im.Composite((709, 874),
		(  0,   0), "images/sprites/normal/mi/mi_3_body.png",
		(153, 261), "images/sprites/normal/mi/mi_3_pioneer.png",
		(310, 137), "images/sprites/normal/mi/mi_3_rage.png",
	))
	image mi rage swim = _sr(im.Composite((709, 874),
		(  0,   0), "images/sprites/normal/mi/mi_3_body.png",
		(231, 269), "images/sprites/normal/mi/mi_3_swim.png",
		(310, 137), "images/sprites/normal/mi/mi_3_rage.png",
	))
	image mi sad pioneer = _sr(im.Composite((602, 862),
		(  0,   0), "images/sprites/normal/mi/mi_2_body.png",
		(129, 230), "images/sprites/normal/mi/mi_2_pioneer.png",
		(207, 139), "images/sprites/normal/mi/mi_2_sad.png",
	))
	image mi sad swim = _sr(im.Composite((602, 862),
		(  0,   0), "images/sprites/normal/mi/mi_2_body.png",
		(174, 251), "images/sprites/normal/mi/mi_2_swim.png",
		(207, 139), "images/sprites/normal/mi/mi_2_sad.png",
	))
	image mi scared pioneer = _sr(im.Composite((621, 873),
		(  0,   0), "images/sprites/normal/mi/mi_1_body.png",
		( 90, 245), "images/sprites/normal/mi/mi_1_pioneer.png",
		(316, 106), "images/sprites/normal/mi/mi_1_scared.png",
	))
	image mi scared swim = _sr(im.Composite((621, 873),
		(  0,   0), "images/sprites/normal/mi/mi_1_body.png",
		(146, 263), "images/sprites/normal/mi/mi_1_swim.png",
		(316, 106), "images/sprites/normal/mi/mi_1_scared.png",
	))
	image mi serious pioneer = _sr(im.Composite((709, 874),
		(  0,   0), "images/sprites/normal/mi/mi_3_body.png",
		(153, 261), "images/sprites/normal/mi/mi_3_pioneer.png",
		(328, 141), "images/sprites/normal/mi/mi_3_serious.png",
	))
	image mi serious swim = _sr(im.Composite((709, 874),
		(  0,   0), "images/sprites/normal/mi/mi_3_body.png",
		(231, 269), "images/sprites/normal/mi/mi_3_swim.png",
		(328, 141), "images/sprites/normal/mi/mi_3_serious.png",
	))
	image mi shocked pioneer = _sr(im.Composite((621, 873),
		(  0,   0), "images/sprites/normal/mi/mi_1_body.png",
		( 90, 245), "images/sprites/normal/mi/mi_1_pioneer.png",
		(320,  99), "images/sprites/normal/mi/mi_1_shocked.png",
	))
	image mi shocked swim = _sr(im.Composite((621, 873),
		(  0,   0), "images/sprites/normal/mi/mi_1_body.png",
		(146, 263), "images/sprites/normal/mi/mi_1_swim.png",
		(320,  99), "images/sprites/normal/mi/mi_1_shocked.png",
	))
	image mi shy pioneer = _sr(im.Composite((621, 873),
		(  0,   0), "images/sprites/normal/mi/mi_1_body.png",
		( 90, 245), "images/sprites/normal/mi/mi_1_pioneer.png",
		(295, 108), "images/sprites/normal/mi/mi_1_shy.png",
	))
	image mi shy swim = _sr(im.Composite((621, 873),
		(  0,   0), "images/sprites/normal/mi/mi_1_body.png",
		(146, 263), "images/sprites/normal/mi/mi_1_swim.png",
		(295, 108), "images/sprites/normal/mi/mi_1_shy.png",
	))
	image mi smile pioneer = _sr(im.Composite((602, 862),
		(  0,   0), "images/sprites/normal/mi/mi_2_body.png",
		(129, 230), "images/sprites/normal/mi/mi_2_pioneer.png",
		(200, 133), "images/sprites/normal/mi/mi_2_smile.png",
	))
	image mi smile swim = _sr(im.Composite((602, 862),
		(  0,   0), "images/sprites/normal/mi/mi_2_body.png",
		(174, 251), "images/sprites/normal/mi/mi_2_swim.png",
		(200, 133), "images/sprites/normal/mi/mi_2_smile.png",
	))
	image mi surprise pioneer = _sr(im.Composite((621, 873),
		(  0,   0), "images/sprites/normal/mi/mi_1_body.png",
		( 90, 245), "images/sprites/normal/mi/mi_1_pioneer.png",
		(313,  90), "images/sprites/normal/mi/mi_1_surprise.png",
	))
	image mi surprise swim = _sr(im.Composite((621, 873),
		(  0,   0), "images/sprites/normal/mi/mi_1_body.png",
		(146, 263), "images/sprites/normal/mi/mi_1_swim.png",
		(313,  90), "images/sprites/normal/mi/mi_1_surprise.png",
	))
	image mi upset pioneer = _sr(im.Composite((709, 874),
		(  0,   0), "images/sprites/normal/mi/mi_3_body.png",
		(153, 261), "images/sprites/normal/mi/mi_3_pioneer.png",
		(325, 143), "images/sprites/normal/mi/mi_3_upset.png",
	))
	image mi upset swim = _sr(im.Composite((709, 874),
		(  0,   0), "images/sprites/normal/mi/mi_3_body.png",
		(231, 269), "images/sprites/normal/mi/mi_3_swim.png",
		(325, 143), "images/sprites/normal/mi/mi_3_upset.png",
	))
	
	image mi angry pioneer far = _sr(im.Composite((531, 813),
		(  0,   0), "images/sprites/far/mi/mi_3_body.png",
		(114, 196), "images/sprites/far/mi/mi_3_pioneer.png",
		(248, 107), "images/sprites/far/mi/mi_3_angry.png",
	))
	image mi angry swim far = _sr(im.Composite((531, 813),
		(  0,   0), "images/sprites/far/mi/mi_3_body.png",
		(173, 201), "images/sprites/far/mi/mi_3_swim.png",
		(248, 107), "images/sprites/far/mi/mi_3_angry.png",
	))
	image mi cry pioneer far = _sr(im.Composite((482, 812),
		(  0,   0), "images/sprites/far/mi/mi_1_body.png",
		( 79, 183), "images/sprites/far/mi/mi_1_pioneer.png",
		(243,  89), "images/sprites/far/mi/mi_1_cry.png",
	))
	image mi cry swim far = _sr(im.Composite((482, 812),
		(  0,   0), "images/sprites/far/mi/mi_1_body.png",
		(125, 197), "images/sprites/far/mi/mi_1_swim.png",
		(243,  89), "images/sprites/far/mi/mi_1_cry.png",
	))
	image mi cry_smile pioneer far = _sr(im.Composite((452, 804),
		(  0,   0), "images/sprites/far/mi/mi_2_body.png",
		( 87, 172), "images/sprites/far/mi/mi_2_pioneer.png",
		(154, 102), "images/sprites/far/mi/mi_2_cry_smile.png",
	))
	image mi cry_smile swim far = _sr(im.Composite((452, 804),
		(  0,   0), "images/sprites/far/mi/mi_2_body.png",
		(131, 188), "images/sprites/far/mi/mi_2_swim.png",
		(154, 102), "images/sprites/far/mi/mi_2_cry_smile.png",
	))
	image mi dontlike pioneer far = _sr(im.Composite((482, 812),
		(  0,   0), "images/sprites/far/mi/mi_1_body.png",
		( 79, 183), "images/sprites/far/mi/mi_1_pioneer.png",
		(242,  87), "images/sprites/far/mi/mi_1_dontlike.png",
	))
	image mi dontlike swim far = _sr(im.Composite((482, 812),
		(  0,   0), "images/sprites/far/mi/mi_1_body.png",
		(125, 197), "images/sprites/far/mi/mi_1_swim.png",
		(242,  87), "images/sprites/far/mi/mi_1_dontlike.png",
	))
	image mi grin pioneer far = _sr(im.Composite((452, 804),
		(  0,   0), "images/sprites/far/mi/mi_2_body.png",
		( 87, 172), "images/sprites/far/mi/mi_2_pioneer.png",
		(152,  98), "images/sprites/far/mi/mi_2_grin.png",
	))
	image mi grin swim far = _sr(im.Composite((452, 804),
		(  0,   0), "images/sprites/far/mi/mi_2_body.png",
		(131, 188), "images/sprites/far/mi/mi_2_swim.png",
		(152,  98), "images/sprites/far/mi/mi_2_grin.png",
	))
	image mi happy pioneer far = _sr(im.Composite((452, 804),
		(  0,   0), "images/sprites/far/mi/mi_2_body.png",
		( 87, 172), "images/sprites/far/mi/mi_2_pioneer.png",
		(153, 102), "images/sprites/far/mi/mi_2_happy.png",
	))
	image mi happy swim far = _sr(im.Composite((452, 804),
		(  0,   0), "images/sprites/far/mi/mi_2_body.png",
		(131, 188), "images/sprites/far/mi/mi_2_swim.png",
		(153, 102), "images/sprites/far/mi/mi_2_happy.png",
	))
	image mi laugh pioneer far = _sr(im.Composite((482, 812),
		(  0,   0), "images/sprites/far/mi/mi_1_body.png",
		( 79, 183), "images/sprites/far/mi/mi_1_pioneer.png",
		(252,  84), "images/sprites/far/mi/mi_1_laugh.png",
	))
	image mi laugh swim far = _sr(im.Composite((482, 812),
		(  0,   0), "images/sprites/far/mi/mi_1_body.png",
		(125, 197), "images/sprites/far/mi/mi_1_swim.png",
		(252,  84), "images/sprites/far/mi/mi_1_laugh.png",
	))
	image mi normal pioneer far = _sr(im.Composite((531, 813),
		(  0,   0), "images/sprites/far/mi/mi_3_body.png",
		(114, 196), "images/sprites/far/mi/mi_3_pioneer.png",
		(249,  99), "images/sprites/far/mi/mi_3_normal.png",
	))
	image mi normal swim far = _sr(im.Composite((531, 813),
		(  0,   0), "images/sprites/far/mi/mi_3_body.png",
		(173, 201), "images/sprites/far/mi/mi_3_swim.png",
		(249,  99), "images/sprites/far/mi/mi_3_normal.png",
	))
	image mi rage pioneer far = _sr(im.Composite((531, 813),
		(  0,   0), "images/sprites/far/mi/mi_3_body.png",
		(114, 196), "images/sprites/far/mi/mi_3_pioneer.png",
		(232, 102), "images/sprites/far/mi/mi_3_rage.png",
	))
	image mi rage swim far = _sr(im.Composite((531, 813),
		(  0,   0), "images/sprites/far/mi/mi_3_body.png",
		(173, 201), "images/sprites/far/mi/mi_3_swim.png",
		(232, 102), "images/sprites/far/mi/mi_3_rage.png",
	))
	image mi sad pioneer far = _sr(im.Composite((452, 804),
		(  0,   0), "images/sprites/far/mi/mi_2_body.png",
		( 87, 172), "images/sprites/far/mi/mi_2_pioneer.png",
		(156, 104), "images/sprites/far/mi/mi_2_sad.png",
	))
	image mi sad swim far = _sr(im.Composite((452, 804),
		(  0,   0), "images/sprites/far/mi/mi_2_body.png",
		(131, 188), "images/sprites/far/mi/mi_2_swim.png",
		(156, 104), "images/sprites/far/mi/mi_2_sad.png",
	))
	image mi scared pioneer far = _sr(im.Composite((482, 812),
		(  0,   0), "images/sprites/far/mi/mi_1_body.png",
		( 79, 183), "images/sprites/far/mi/mi_1_pioneer.png",
		(252,  79), "images/sprites/far/mi/mi_1_scared.png",
	))
	image mi scared swim far = _sr(im.Composite((482, 812),
		(  0,   0), "images/sprites/far/mi/mi_1_body.png",
		(125, 197), "images/sprites/far/mi/mi_1_swim.png",
		(252,  79), "images/sprites/far/mi/mi_1_scared.png",
	))
	image mi serious pioneer far = _sr(im.Composite((531, 813),
		(  0,   0), "images/sprites/far/mi/mi_3_body.png",
		(114, 196), "images/sprites/far/mi/mi_3_pioneer.png",
		(245, 105), "images/sprites/far/mi/mi_3_serious.png",
	))
	image mi serious swim far = _sr(im.Composite((531, 813),
		(  0,   0), "images/sprites/far/mi/mi_3_body.png",
		(173, 201), "images/sprites/far/mi/mi_3_swim.png",
		(245, 105), "images/sprites/far/mi/mi_3_serious.png",
	))
	image mi shocked pioneer far = _sr(im.Composite((482, 812),
		(  0,   0), "images/sprites/far/mi/mi_1_body.png",
		( 79, 183), "images/sprites/far/mi/mi_1_pioneer.png",
		(255,  74), "images/sprites/far/mi/mi_1_shocked.png",
	))
	image mi shocked swim far = _sr(im.Composite((482, 812),
		(  0,   0), "images/sprites/far/mi/mi_1_body.png",
		(125, 197), "images/sprites/far/mi/mi_1_swim.png",
		(255,  74), "images/sprites/far/mi/mi_1_shocked.png",
	))
	image mi shy pioneer far = _sr(im.Composite((482, 812),
		(  0,   0), "images/sprites/far/mi/mi_1_body.png",
		( 79, 183), "images/sprites/far/mi/mi_1_pioneer.png",
		(237,  81), "images/sprites/far/mi/mi_1_shy.png",
	))
	image mi shy swim far = _sr(im.Composite((482, 812),
		(  0,   0), "images/sprites/far/mi/mi_1_body.png",
		(125, 197), "images/sprites/far/mi/mi_1_swim.png",
		(237,  81), "images/sprites/far/mi/mi_1_shy.png",
	))
	image mi smile pioneer far = _sr(im.Composite((452, 804),
		(  0,   0), "images/sprites/far/mi/mi_2_body.png",
		( 87, 172), "images/sprites/far/mi/mi_2_pioneer.png",
		(150,  99), "images/sprites/far/mi/mi_2_smile.png",
	))
	image mi smile swim far = _sr(im.Composite((452, 804),
		(  0,   0), "images/sprites/far/mi/mi_2_body.png",
		(131, 188), "images/sprites/far/mi/mi_2_swim.png",
		(150,  99), "images/sprites/far/mi/mi_2_smile.png",
	))
	image mi surprise pioneer far = _sr(im.Composite((482, 812),
		(  0,   0), "images/sprites/far/mi/mi_1_body.png",
		( 79, 183), "images/sprites/far/mi/mi_1_pioneer.png",
		(251,  67), "images/sprites/far/mi/mi_1_surprise.png",
	))
	image mi surprise swim far = _sr(im.Composite((482, 812),
		(  0,   0), "images/sprites/far/mi/mi_1_body.png",
		(125, 197), "images/sprites/far/mi/mi_1_swim.png",
		(251,  67), "images/sprites/far/mi/mi_1_surprise.png",
	))
	image mi upset pioneer far = _sr(im.Composite((531, 813),
		(  0,   0), "images/sprites/far/mi/mi_3_body.png",
		(114, 196), "images/sprites/far/mi/mi_3_pioneer.png",
		(243, 107), "images/sprites/far/mi/mi_3_upset.png",
	))
	image mi upset swim far = _sr(im.Composite((531, 813),
		(  0,   0), "images/sprites/far/mi/mi_3_body.png",
		(173, 201), "images/sprites/far/mi/mi_3_swim.png",
		(243, 107), "images/sprites/far/mi/mi_3_upset.png",
	))
	
	image mt angry dress close = _sr(im.Composite((840, 955),
		(  0,   0), "images/sprites/close/mt/mt_2_body.png",
		(211, 327), "images/sprites/close/mt/mt_2_dress.png",
		(287, 147), "images/sprites/close/mt/mt_2_angry.png",
	))
	image mt angry panama dress close = _sr(im.Composite((840, 988),
		(  0,  33), "images/sprites/close/mt/mt_2_body.png",
		(197,   0), "images/sprites/close/mt/mt_2_panama.png",
		(287, 180), "images/sprites/close/mt/mt_2_angry.png",
		(211, 360), "images/sprites/close/mt/mt_2_dress.png",
	))
	image mt angry panama pioneer close = _sr(im.Composite((840, 988),
		(  0,  33), "images/sprites/close/mt/mt_2_body.png",
		(197,   0), "images/sprites/close/mt/mt_2_panama.png",
		(287, 180), "images/sprites/close/mt/mt_2_angry.png",
		( 73, 344), "images/sprites/close/mt/mt_2_pioneer.png",
	))
	image mt angry panama swim close = _sr(im.Composite((840, 988),
		(  0,  33), "images/sprites/close/mt/mt_2_body.png",
		(197,   0), "images/sprites/close/mt/mt_2_panama.png",
		(287, 180), "images/sprites/close/mt/mt_2_angry.png",
		(223, 360), "images/sprites/close/mt/mt_2_swim.png",
	))
	image mt angry pioneer close = _sr(im.Composite((840, 955),
		(  0,   0), "images/sprites/close/mt/mt_2_body.png",
		( 73, 311), "images/sprites/close/mt/mt_2_pioneer.png",
		(287, 147), "images/sprites/close/mt/mt_2_angry.png",
	))
	image mt angry swim close = _sr(im.Composite((840, 955),
		(  0,   0), "images/sprites/close/mt/mt_2_body.png",
		(223, 327), "images/sprites/close/mt/mt_2_swim.png",
		(287, 147), "images/sprites/close/mt/mt_2_angry.png",
	))
	image mt grin panama pioneer close = _sr(im.Composite((551, 1080),
		( 32,  31), "images/sprites/close/mt/mt_3_body.png",
		( 53,   0), "images/sprites/close/mt/mt_3_panama.png",
		(154, 203), "images/sprites/close/mt/mt_3_grin.png",
		(  0, 372), "images/sprites/close/mt/mt_3_pioneer.png",
	))
	image mt grin pioneer close = _sr(im.Composite((551, 1049),
		( 32,   0), "images/sprites/close/mt/mt_3_body.png",
		(  0, 341), "images/sprites/close/mt/mt_3_pioneer.png",
		(154, 172), "images/sprites/close/mt/mt_3_grin.png",
	))
	image mt laugh panama pioneer close = _sr(im.Composite((551, 1080),
		( 32,  31), "images/sprites/close/mt/mt_3_body.png",
		( 53,   0), "images/sprites/close/mt/mt_3_panama.png",
		(156, 205), "images/sprites/close/mt/mt_3_laugh.png",
		(  0, 372), "images/sprites/close/mt/mt_3_pioneer.png",
	))
	image mt laugh pioneer close = _sr(im.Composite((551, 1049),
		( 32,   0), "images/sprites/close/mt/mt_3_body.png",
		(  0, 341), "images/sprites/close/mt/mt_3_pioneer.png",
		(156, 174), "images/sprites/close/mt/mt_3_laugh.png",
	))
	image mt normal dress close = _sr(im.Composite((531, 1043),
		(  0,   0), "images/sprites/close/mt/mt_1_body.png",
		( 45, 364), "images/sprites/close/mt/mt_1_dress.png",
		(161, 142), "images/sprites/close/mt/mt_1_normal.png",
	))
	image mt normal panama dress close = _sr(im.Composite((531, 1070),
		(  0,  27), "images/sprites/close/mt/mt_1_body.png",
		( 60,   0), "images/sprites/close/mt/mt_1_panama.png",
		(161, 169), "images/sprites/close/mt/mt_1_normal.png",
		( 45, 391), "images/sprites/close/mt/mt_1_dress.png",
	))
	image mt normal panama pioneer close = _sr(im.Composite((541, 1070),
		(  0,  27), "images/sprites/close/mt/mt_1_body.png",
		( 60,   0), "images/sprites/close/mt/mt_1_panama.png",
		(161, 169), "images/sprites/close/mt/mt_1_normal.png",
		( 42, 343), "images/sprites/close/mt/mt_1_pioneer.png",
	))
	image mt normal panama swim close = _sr(im.Composite((531, 1070),
		(  0,  27), "images/sprites/close/mt/mt_1_body.png",
		( 60,   0), "images/sprites/close/mt/mt_1_panama.png",
		(161, 169), "images/sprites/close/mt/mt_1_normal.png",
		( 75, 382), "images/sprites/close/mt/mt_1_swim.png",
	))
	image mt normal pioneer close = _sr(im.Composite((541, 1043),
		(  0,   0), "images/sprites/close/mt/mt_1_body.png",
		( 42, 316), "images/sprites/close/mt/mt_1_pioneer.png",
		(161, 142), "images/sprites/close/mt/mt_1_normal.png",
	))
	image mt normal swim close = _sr(im.Composite((531, 1043),
		(  0,   0), "images/sprites/close/mt/mt_1_body.png",
		( 75, 355), "images/sprites/close/mt/mt_1_swim.png",
		(161, 142), "images/sprites/close/mt/mt_1_normal.png",
	))
	image mt rage dress close = _sr(im.Composite((840, 955),
		(  0,   0), "images/sprites/close/mt/mt_2_body.png",
		(211, 327), "images/sprites/close/mt/mt_2_dress.png",
		(309, 161), "images/sprites/close/mt/mt_2_rage.png",
	))
	image mt rage panama dress close = _sr(im.Composite((840, 988),
		(  0,  33), "images/sprites/close/mt/mt_2_body.png",
		(197,   0), "images/sprites/close/mt/mt_2_panama.png",
		(309, 194), "images/sprites/close/mt/mt_2_rage.png",
		(211, 360), "images/sprites/close/mt/mt_2_dress.png",
	))
	image mt rage panama pioneer close = _sr(im.Composite((840, 988),
		(  0,  33), "images/sprites/close/mt/mt_2_body.png",
		(197,   0), "images/sprites/close/mt/mt_2_panama.png",
		(309, 194), "images/sprites/close/mt/mt_2_rage.png",
		( 73, 344), "images/sprites/close/mt/mt_2_pioneer.png",
	))
	image mt rage panama swim close = _sr(im.Composite((840, 988),
		(  0,  33), "images/sprites/close/mt/mt_2_body.png",
		(197,   0), "images/sprites/close/mt/mt_2_panama.png",
		(309, 194), "images/sprites/close/mt/mt_2_rage.png",
		(223, 360), "images/sprites/close/mt/mt_2_swim.png",
	))
	image mt rage pioneer close = _sr(im.Composite((840, 955),
		(  0,   0), "images/sprites/close/mt/mt_2_body.png",
		( 73, 311), "images/sprites/close/mt/mt_2_pioneer.png",
		(309, 161), "images/sprites/close/mt/mt_2_rage.png",
	))
	image mt rage swim close = _sr(im.Composite((840, 955),
		(  0,   0), "images/sprites/close/mt/mt_2_body.png",
		(223, 327), "images/sprites/close/mt/mt_2_swim.png",
		(309, 161), "images/sprites/close/mt/mt_2_rage.png",
	))
	image mt sad dress close = _sr(im.Composite((531, 1043),
		(  0,   0), "images/sprites/close/mt/mt_1_body.png",
		( 45, 364), "images/sprites/close/mt/mt_1_dress.png",
		(161, 142), "images/sprites/close/mt/mt_1_sad.png",
	))
	image mt sad panama dress close = _sr(im.Composite((531, 1070),
		(  0,  27), "images/sprites/close/mt/mt_1_body.png",
		( 60,   0), "images/sprites/close/mt/mt_1_panama.png",
		(161, 169), "images/sprites/close/mt/mt_1_sad.png",
		( 45, 391), "images/sprites/close/mt/mt_1_dress.png",
	))
	image mt sad panama pioneer close = _sr(im.Composite((541, 1070),
		(  0,  27), "images/sprites/close/mt/mt_1_body.png",
		( 60,   0), "images/sprites/close/mt/mt_1_panama.png",
		(161, 169), "images/sprites/close/mt/mt_1_sad.png",
		( 42, 343), "images/sprites/close/mt/mt_1_pioneer.png",
	))
	image mt sad panama swim close = _sr(im.Composite((531, 1070),
		(  0,  27), "images/sprites/close/mt/mt_1_body.png",
		( 60,   0), "images/sprites/close/mt/mt_1_panama.png",
		(161, 169), "images/sprites/close/mt/mt_1_sad.png",
		( 75, 382), "images/sprites/close/mt/mt_1_swim.png",
	))
	image mt sad pioneer close = _sr(im.Composite((541, 1043),
		(  0,   0), "images/sprites/close/mt/mt_1_body.png",
		( 42, 316), "images/sprites/close/mt/mt_1_pioneer.png",
		(161, 142), "images/sprites/close/mt/mt_1_sad.png",
	))
	image mt sad swim close = _sr(im.Composite((531, 1043),
		(  0,   0), "images/sprites/close/mt/mt_1_body.png",
		( 75, 355), "images/sprites/close/mt/mt_1_swim.png",
		(161, 142), "images/sprites/close/mt/mt_1_sad.png",
	))
	image mt smile dress close = _sr(im.Composite((531, 1043),
		(  0,   0), "images/sprites/close/mt/mt_1_body.png",
		( 45, 364), "images/sprites/close/mt/mt_1_dress.png",
		(161, 142), "images/sprites/close/mt/mt_1_smile.png",
	))
	image mt smile panama dress close = _sr(im.Composite((531, 1070),
		(  0,  27), "images/sprites/close/mt/mt_1_body.png",
		( 60,   0), "images/sprites/close/mt/mt_1_panama.png",
		(161, 169), "images/sprites/close/mt/mt_1_smile.png",
		( 45, 391), "images/sprites/close/mt/mt_1_dress.png",
	))
	image mt smile panama pioneer close = _sr(im.Composite((541, 1070),
		(  0,  27), "images/sprites/close/mt/mt_1_body.png",
		( 60,   0), "images/sprites/close/mt/mt_1_panama.png",
		(161, 169), "images/sprites/close/mt/mt_1_smile.png",
		( 42, 343), "images/sprites/close/mt/mt_1_pioneer.png",
	))
	image mt smile panama swim close = _sr(im.Composite((531, 1070),
		(  0,  27), "images/sprites/close/mt/mt_1_body.png",
		( 60,   0), "images/sprites/close/mt/mt_1_panama.png",
		(161, 169), "images/sprites/close/mt/mt_1_smile.png",
		( 75, 382), "images/sprites/close/mt/mt_1_swim.png",
	))
	image mt smile pioneer close = _sr(im.Composite((541, 1043),
		(  0,   0), "images/sprites/close/mt/mt_1_body.png",
		( 42, 316), "images/sprites/close/mt/mt_1_pioneer.png",
		(161, 142), "images/sprites/close/mt/mt_1_smile.png",
	))
	image mt smile swim close = _sr(im.Composite((531, 1043),
		(  0,   0), "images/sprites/close/mt/mt_1_body.png",
		( 75, 355), "images/sprites/close/mt/mt_1_swim.png",
		(161, 142), "images/sprites/close/mt/mt_1_smile.png",
	))
	image mt surprise dress close = _sr(im.Composite((531, 1043),
		(  0,   0), "images/sprites/close/mt/mt_1_body.png",
		( 45, 364), "images/sprites/close/mt/mt_1_dress.png",
		(161, 145), "images/sprites/close/mt/mt_1_surprise.png",
	))
	image mt surprise panama dress close = _sr(im.Composite((531, 1070),
		(  0,  27), "images/sprites/close/mt/mt_1_body.png",
		( 60,   0), "images/sprites/close/mt/mt_1_panama.png",
		(161, 172), "images/sprites/close/mt/mt_1_surprise.png",
		( 45, 391), "images/sprites/close/mt/mt_1_dress.png",
	))
	image mt surprise panama pioneer close = _sr(im.Composite((541, 1070),
		(  0,  27), "images/sprites/close/mt/mt_1_body.png",
		( 60,   0), "images/sprites/close/mt/mt_1_panama.png",
		(161, 172), "images/sprites/close/mt/mt_1_surprise.png",
		( 42, 343), "images/sprites/close/mt/mt_1_pioneer.png",
	))
	image mt surprise panama swim close = _sr(im.Composite((531, 1070),
		(  0,  27), "images/sprites/close/mt/mt_1_body.png",
		( 60,   0), "images/sprites/close/mt/mt_1_panama.png",
		(161, 172), "images/sprites/close/mt/mt_1_surprise.png",
		( 75, 382), "images/sprites/close/mt/mt_1_swim.png",
	))
	image mt surprise pioneer close = _sr(im.Composite((541, 1043),
		(  0,   0), "images/sprites/close/mt/mt_1_body.png",
		( 42, 316), "images/sprites/close/mt/mt_1_pioneer.png",
		(161, 145), "images/sprites/close/mt/mt_1_surprise.png",
	))
	image mt surprise swim close = _sr(im.Composite((531, 1043),
		(  0,   0), "images/sprites/close/mt/mt_1_body.png",
		( 75, 355), "images/sprites/close/mt/mt_1_swim.png",
		(161, 145), "images/sprites/close/mt/mt_1_surprise.png",
	))
	
	image mt angry dress = _sr(im.Composite((673, 954),
		(  0,   0), "images/sprites/normal/mt/mt_2_body.png",
		(140, 261), "images/sprites/normal/mt/mt_2_dress.png",
		(231, 118), "images/sprites/normal/mt/mt_2_angry.png",
	))
	image mt angry panama dress = _sr(im.Composite((673, 981),
		(  0,  27), "images/sprites/normal/mt/mt_2_body.png",
		(159,   0), "images/sprites/normal/mt/mt_2_panama.png",
		(231, 145), "images/sprites/normal/mt/mt_2_angry.png",
		(140, 288), "images/sprites/normal/mt/mt_2_dress.png",
	))
	image mt angry panama pioneer = _sr(im.Composite((673, 981),
		(  0,  27), "images/sprites/normal/mt/mt_2_body.png",
		(159,   0), "images/sprites/normal/mt/mt_2_panama.png",
		(231, 145), "images/sprites/normal/mt/mt_2_angry.png",
		( 59, 275), "images/sprites/normal/mt/mt_2_pioneer.png",
	))
	image mt angry panama swim = _sr(im.Composite((673, 981),
		(  0,  27), "images/sprites/normal/mt/mt_2_body.png",
		(159,   0), "images/sprites/normal/mt/mt_2_panama.png",
		(231, 145), "images/sprites/normal/mt/mt_2_angry.png",
		(179, 289), "images/sprites/normal/mt/mt_2_swim.png",
	))
	image mt angry pioneer = _sr(im.Composite((673, 954),
		(  0,   0), "images/sprites/normal/mt/mt_2_body.png",
		( 59, 248), "images/sprites/normal/mt/mt_2_pioneer.png",
		(231, 118), "images/sprites/normal/mt/mt_2_angry.png",
	))
	image mt angry swim = _sr(im.Composite((673, 954),
		(  0,   0), "images/sprites/normal/mt/mt_2_body.png",
		(179, 262), "images/sprites/normal/mt/mt_2_swim.png",
		(231, 118), "images/sprites/normal/mt/mt_2_angry.png",
	))
	image mt grin panama pioneer = _sr(im.Composite((455, 1054),
		( 34,  24), "images/sprites/normal/mt/mt_3_body.png",
		( 55,   0), "images/sprites/normal/mt/mt_3_panama.png",
		(137, 162), "images/sprites/normal/mt/mt_3_grin.png",
		(  0, 298), "images/sprites/normal/mt/mt_3_pioneer.png",
	))
	image mt grin pioneer = _sr(im.Composite((455, 1030),
		( 34,   0), "images/sprites/normal/mt/mt_3_body.png",
		(  0, 274), "images/sprites/normal/mt/mt_3_pioneer.png",
		(137, 138), "images/sprites/normal/mt/mt_3_grin.png",
	))
	image mt laugh panama pioneer = _sr(im.Composite((455, 1054),
		( 34,  24), "images/sprites/normal/mt/mt_3_body.png",
		( 55,   0), "images/sprites/normal/mt/mt_3_panama.png",
		(138, 164), "images/sprites/normal/mt/mt_3_laugh.png",
		(  0, 298), "images/sprites/normal/mt/mt_3_pioneer.png",
	))
	image mt laugh pioneer = _sr(im.Composite((455, 1030),
		( 34,   0), "images/sprites/normal/mt/mt_3_body.png",
		(  0, 274), "images/sprites/normal/mt/mt_3_pioneer.png",
		(138, 140), "images/sprites/normal/mt/mt_3_laugh.png",
	))
	image mt normal dress = _sr(im.Composite((485, 1025),
		(  0,   0), "images/sprites/normal/mt/mt_1_body.png",
		( 78, 292), "images/sprites/normal/mt/mt_1_dress.png",
		(180, 114), "images/sprites/normal/mt/mt_1_normal.png",
	))
	image mt normal panama dress = _sr(im.Composite((485, 1046),
		(  0,  21), "images/sprites/normal/mt/mt_1_body.png",
		( 99,   0), "images/sprites/normal/mt/mt_1_panama.png",
		(180, 135), "images/sprites/normal/mt/mt_1_normal.png",
		( 78, 313), "images/sprites/normal/mt/mt_1_dress.png",
	))
	image mt normal panama pioneer = _sr(im.Composite((485, 1046),
		(  0,  21), "images/sprites/normal/mt/mt_1_body.png",
		( 99,   0), "images/sprites/normal/mt/mt_1_panama.png",
		(180, 135), "images/sprites/normal/mt/mt_1_normal.png",
		( 54, 275), "images/sprites/normal/mt/mt_1_pioneer.png",
	))
	image mt normal panama swim = _sr(im.Composite((485, 1046),
		(  0,  21), "images/sprites/normal/mt/mt_1_body.png",
		( 99,   0), "images/sprites/normal/mt/mt_1_panama.png",
		(180, 135), "images/sprites/normal/mt/mt_1_normal.png",
		(111, 306), "images/sprites/normal/mt/mt_1_swim.png",
	))
	image mt normal pioneer = _sr(im.Composite((485, 1025),
		(  0,   0), "images/sprites/normal/mt/mt_1_body.png",
		( 54, 254), "images/sprites/normal/mt/mt_1_pioneer.png",
		(180, 114), "images/sprites/normal/mt/mt_1_normal.png",
	))
	image mt normal swim = _sr(im.Composite((485, 1025),
		(  0,   0), "images/sprites/normal/mt/mt_1_body.png",
		(111, 285), "images/sprites/normal/mt/mt_1_swim.png",
		(180, 114), "images/sprites/normal/mt/mt_1_normal.png",
	))
	image mt rage dress = _sr(im.Composite((673, 954),
		(  0,   0), "images/sprites/normal/mt/mt_2_body.png",
		(140, 261), "images/sprites/normal/mt/mt_2_dress.png",
		(248, 128), "images/sprites/normal/mt/mt_2_rage.png",
	))
	image mt rage panama dress = _sr(im.Composite((673, 981),
		(  0,  27), "images/sprites/normal/mt/mt_2_body.png",
		(159,   0), "images/sprites/normal/mt/mt_2_panama.png",
		(248, 155), "images/sprites/normal/mt/mt_2_rage.png",
		(140, 288), "images/sprites/normal/mt/mt_2_dress.png",
	))
	image mt rage panama pioneer = _sr(im.Composite((673, 981),
		(  0,  27), "images/sprites/normal/mt/mt_2_body.png",
		(159,   0), "images/sprites/normal/mt/mt_2_panama.png",
		(248, 155), "images/sprites/normal/mt/mt_2_rage.png",
		( 59, 275), "images/sprites/normal/mt/mt_2_pioneer.png",
	))
	image mt rage panama swim = _sr(im.Composite((673, 981),
		(  0,  27), "images/sprites/normal/mt/mt_2_body.png",
		(159,   0), "images/sprites/normal/mt/mt_2_panama.png",
		(248, 155), "images/sprites/normal/mt/mt_2_rage.png",
		(179, 289), "images/sprites/normal/mt/mt_2_swim.png",
	))
	image mt rage pioneer = _sr(im.Composite((673, 954),
		(  0,   0), "images/sprites/normal/mt/mt_2_body.png",
		( 59, 248), "images/sprites/normal/mt/mt_2_pioneer.png",
		(248, 128), "images/sprites/normal/mt/mt_2_rage.png",
	))
	image mt rage swim = _sr(im.Composite((673, 954),
		(  0,   0), "images/sprites/normal/mt/mt_2_body.png",
		(179, 262), "images/sprites/normal/mt/mt_2_swim.png",
		(248, 128), "images/sprites/normal/mt/mt_2_rage.png",
	))
	image mt sad dress = _sr(im.Composite((485, 1025),
		(  0,   0), "images/sprites/normal/mt/mt_1_body.png",
		( 78, 292), "images/sprites/normal/mt/mt_1_dress.png",
		(180, 114), "images/sprites/normal/mt/mt_1_sad.png",
	))
	image mt sad panama dress = _sr(im.Composite((485, 1046),
		(  0,  21), "images/sprites/normal/mt/mt_1_body.png",
		( 99,   0), "images/sprites/normal/mt/mt_1_panama.png",
		(180, 135), "images/sprites/normal/mt/mt_1_sad.png",
		( 78, 313), "images/sprites/normal/mt/mt_1_dress.png",
	))
	image mt sad panama pioneer = _sr(im.Composite((485, 1046),
		(  0,  21), "images/sprites/normal/mt/mt_1_body.png",
		( 99,   0), "images/sprites/normal/mt/mt_1_panama.png",
		(180, 135), "images/sprites/normal/mt/mt_1_sad.png",
		( 54, 275), "images/sprites/normal/mt/mt_1_pioneer.png",
	))
	image mt sad panama swim = _sr(im.Composite((485, 1046),
		(  0,  21), "images/sprites/normal/mt/mt_1_body.png",
		( 99,   0), "images/sprites/normal/mt/mt_1_panama.png",
		(180, 135), "images/sprites/normal/mt/mt_1_sad.png",
		(111, 306), "images/sprites/normal/mt/mt_1_swim.png",
	))
	image mt sad pioneer = _sr(im.Composite((485, 1025),
		(  0,   0), "images/sprites/normal/mt/mt_1_body.png",
		( 54, 254), "images/sprites/normal/mt/mt_1_pioneer.png",
		(180, 114), "images/sprites/normal/mt/mt_1_sad.png",
	))
	image mt sad swim = _sr(im.Composite((485, 1025),
		(  0,   0), "images/sprites/normal/mt/mt_1_body.png",
		(111, 285), "images/sprites/normal/mt/mt_1_swim.png",
		(180, 114), "images/sprites/normal/mt/mt_1_sad.png",
	))
	image mt scared pioneer = _sr(im.Composite((455, 1030),
		( 34,   0), "images/sprites/normal/mt/mt_3_body.png",
		(  0, 274), "images/sprites/normal/mt/mt_3_pioneer.png",
		(141, 134), "images/sprites/normal/mt/mt_3_scared.png",
	))
	image mt shocked pioneer = _sr(im.Composite((673, 954),
		(  0,   0), "images/sprites/normal/mt/mt_2_body.png",
		( 59, 248), "images/sprites/normal/mt/mt_2_pioneer.png",
		(228, 119), "images/sprites/normal/mt/mt_2_shocked.png",
	))
	image mt smile dress = _sr(im.Composite((485, 1025),
		(  0,   0), "images/sprites/normal/mt/mt_1_body.png",
		( 78, 292), "images/sprites/normal/mt/mt_1_dress.png",
		(180, 114), "images/sprites/normal/mt/mt_1_smile.png",
	))
	image mt smile panama dress = _sr(im.Composite((485, 1046),
		(  0,  21), "images/sprites/normal/mt/mt_1_body.png",
		( 99,   0), "images/sprites/normal/mt/mt_1_panama.png",
		(180, 135), "images/sprites/normal/mt/mt_1_smile.png",
		( 78, 313), "images/sprites/normal/mt/mt_1_dress.png",
	))
	image mt smile panama pioneer = _sr(im.Composite((485, 1046),
		(  0,  21), "images/sprites/normal/mt/mt_1_body.png",
		( 99,   0), "images/sprites/normal/mt/mt_1_panama.png",
		(180, 135), "images/sprites/normal/mt/mt_1_smile.png",
		( 54, 275), "images/sprites/normal/mt/mt_1_pioneer.png",
	))
	image mt smile panama swim = _sr(im.Composite((485, 1046),
		(  0,  21), "images/sprites/normal/mt/mt_1_body.png",
		( 99,   0), "images/sprites/normal/mt/mt_1_panama.png",
		(180, 135), "images/sprites/normal/mt/mt_1_smile.png",
		(111, 306), "images/sprites/normal/mt/mt_1_swim.png",
	))
	image mt smile pioneer = _sr(im.Composite((485, 1025),
		(  0,   0), "images/sprites/normal/mt/mt_1_body.png",
		( 54, 254), "images/sprites/normal/mt/mt_1_pioneer.png",
		(180, 114), "images/sprites/normal/mt/mt_1_smile.png",
	))
	image mt smile swim = _sr(im.Composite((485, 1025),
		(  0,   0), "images/sprites/normal/mt/mt_1_body.png",
		(111, 285), "images/sprites/normal/mt/mt_1_swim.png",
		(180, 114), "images/sprites/normal/mt/mt_1_smile.png",
	))
	image mt surprise dress = _sr(im.Composite((485, 1025),
		(  0,   0), "images/sprites/normal/mt/mt_1_body.png",
		( 78, 292), "images/sprites/normal/mt/mt_1_dress.png",
		(180, 117), "images/sprites/normal/mt/mt_1_surprise.png",
	))
	image mt surprise panama dress = _sr(im.Composite((485, 1046),
		(  0,  21), "images/sprites/normal/mt/mt_1_body.png",
		( 99,   0), "images/sprites/normal/mt/mt_1_panama.png",
		(180, 138), "images/sprites/normal/mt/mt_1_surprise.png",
		( 78, 313), "images/sprites/normal/mt/mt_1_dress.png",
	))
	image mt surprise panama pioneer = _sr(im.Composite((485, 1046),
		(  0,  21), "images/sprites/normal/mt/mt_1_body.png",
		( 99,   0), "images/sprites/normal/mt/mt_1_panama.png",
		(180, 138), "images/sprites/normal/mt/mt_1_surprise.png",
		( 54, 275), "images/sprites/normal/mt/mt_1_pioneer.png",
	))
	image mt surprise panama swim = _sr(im.Composite((485, 1046),
		(  0,  21), "images/sprites/normal/mt/mt_1_body.png",
		( 99,   0), "images/sprites/normal/mt/mt_1_panama.png",
		(180, 138), "images/sprites/normal/mt/mt_1_surprise.png",
		(111, 306), "images/sprites/normal/mt/mt_1_swim.png",
	))
	image mt surprise pioneer = _sr(im.Composite((485, 1025),
		(  0,   0), "images/sprites/normal/mt/mt_1_body.png",
		( 54, 254), "images/sprites/normal/mt/mt_1_pioneer.png",
		(180, 117), "images/sprites/normal/mt/mt_1_surprise.png",
	))
	image mt surprise swim = _sr(im.Composite((485, 1025),
		(  0,   0), "images/sprites/normal/mt/mt_1_body.png",
		(111, 285), "images/sprites/normal/mt/mt_1_swim.png",
		(180, 117), "images/sprites/normal/mt/mt_1_surprise.png",
	))
	
	image mt angry dress far = _sr(im.Composite((505, 873),
		(  0,   0), "images/sprites/far/mt/mt_2_body.png",
		(105, 196), "images/sprites/far/mt/mt_2_dress.png",
		(173,  88), "images/sprites/far/mt/mt_2_angry.png",
	))
	image mt angry panama dress far = _sr(im.Composite((505, 893),
		(  0,  20), "images/sprites/far/mt/mt_2_body.png",
		(119,   0), "images/sprites/far/mt/mt_2_panama.png",
		(173, 108), "images/sprites/far/mt/mt_2_angry.png",
		(105, 216), "images/sprites/far/mt/mt_2_dress.png",
	))
	image mt angry panama pioneer far = _sr(im.Composite((505, 893),
		(  0,  20), "images/sprites/far/mt/mt_2_body.png",
		(119,   0), "images/sprites/far/mt/mt_2_panama.png",
		(173, 108), "images/sprites/far/mt/mt_2_angry.png",
		( 44, 206), "images/sprites/far/mt/mt_2_pioneer.png",
	))
	image mt angry panama swim far = _sr(im.Composite((505, 893),
		(  0,  20), "images/sprites/far/mt/mt_2_body.png",
		(119,   0), "images/sprites/far/mt/mt_2_panama.png",
		(173, 108), "images/sprites/far/mt/mt_2_angry.png",
		(134, 216), "images/sprites/far/mt/mt_2_swim.png",
	))
	image mt angry pioneer far = _sr(im.Composite((505, 873),
		(  0,   0), "images/sprites/far/mt/mt_2_body.png",
		( 44, 186), "images/sprites/far/mt/mt_2_pioneer.png",
		(173,  88), "images/sprites/far/mt/mt_2_angry.png",
	))
	image mt angry swim far = _sr(im.Composite((505, 873),
		(  0,   0), "images/sprites/far/mt/mt_2_body.png",
		(134, 196), "images/sprites/far/mt/mt_2_swim.png",
		(173,  88), "images/sprites/far/mt/mt_2_angry.png",
	))
	image mt grin panama pioneer far = _sr(im.Composite((346, 948),
		( 29,  18), "images/sprites/far/mt/mt_3_body.png",
		( 46,   0), "images/sprites/far/mt/mt_3_panama.png",
		(107, 122), "images/sprites/far/mt/mt_3_grin.png",
		(  0, 223), "images/sprites/far/mt/mt_3_pioneer.png",
	))
	image mt grin pioneer far = _sr(im.Composite((346, 930),
		( 29,   0), "images/sprites/far/mt/mt_3_body.png",
		(  0, 205), "images/sprites/far/mt/mt_3_pioneer.png",
		(107, 104), "images/sprites/far/mt/mt_3_grin.png",
	))
	image mt laugh panama pioneer far = _sr(im.Composite((346, 948),
		( 29,  18), "images/sprites/far/mt/mt_3_body.png",
		( 46,   0), "images/sprites/far/mt/mt_3_panama.png",
		(108, 123), "images/sprites/far/mt/mt_3_laugh.png",
		(  0, 223), "images/sprites/far/mt/mt_3_pioneer.png",
	))
	image mt laugh pioneer far = _sr(im.Composite((346, 930),
		( 29,   0), "images/sprites/far/mt/mt_3_body.png",
		(  0, 205), "images/sprites/far/mt/mt_3_pioneer.png",
		(108, 105), "images/sprites/far/mt/mt_3_laugh.png",
	))
	image mt normal dress far = _sr(im.Composite((364, 926),
		(  0,   0), "images/sprites/far/mt/mt_1_body.png",
		( 58, 218), "images/sprites/far/mt/mt_1_dress.png",
		(135,  85), "images/sprites/far/mt/mt_1_normal.png",
	))
	image mt normal panama dress far = _sr(im.Composite((364, 942),
		(  0,  16), "images/sprites/far/mt/mt_1_body.png",
		( 74,   0), "images/sprites/far/mt/mt_1_panama.png",
		(135, 101), "images/sprites/far/mt/mt_1_normal.png",
		( 58, 234), "images/sprites/far/mt/mt_1_dress.png",
	))
	image mt normal panama pioneer far = _sr(im.Composite((364, 942),
		(  0,  16), "images/sprites/far/mt/mt_1_body.png",
		( 74,   0), "images/sprites/far/mt/mt_1_panama.png",
		(135, 101), "images/sprites/far/mt/mt_1_normal.png",
		( 32, 206), "images/sprites/far/mt/mt_1_pioneer.png",
	))
	image mt normal panama swim far = _sr(im.Composite((364, 942),
		(  0,  16), "images/sprites/far/mt/mt_1_body.png",
		( 74,   0), "images/sprites/far/mt/mt_1_panama.png",
		(135, 101), "images/sprites/far/mt/mt_1_normal.png",
		( 83, 229), "images/sprites/far/mt/mt_1_swim.png",
	))
	image mt normal pioneer far = _sr(im.Composite((364, 926),
		(  0,   0), "images/sprites/far/mt/mt_1_body.png",
		( 32, 190), "images/sprites/far/mt/mt_1_pioneer.png",
		(135,  85), "images/sprites/far/mt/mt_1_normal.png",
	))
	image mt normal swim far = _sr(im.Composite((364, 926),
		(  0,   0), "images/sprites/far/mt/mt_1_body.png",
		( 83, 213), "images/sprites/far/mt/mt_1_swim.png",
		(135,  85), "images/sprites/far/mt/mt_1_normal.png",
	))
	image mt rage dress far = _sr(im.Composite((505, 873),
		(  0,   0), "images/sprites/far/mt/mt_2_body.png",
		(105, 196), "images/sprites/far/mt/mt_2_dress.png",
		(186,  96), "images/sprites/far/mt/mt_2_rage.png",
	))
	image mt rage panama dress far = _sr(im.Composite((505, 893),
		(  0,  20), "images/sprites/far/mt/mt_2_body.png",
		(119,   0), "images/sprites/far/mt/mt_2_panama.png",
		(186, 116), "images/sprites/far/mt/mt_2_rage.png",
		(105, 216), "images/sprites/far/mt/mt_2_dress.png",
	))
	image mt rage panama pioneer far = _sr(im.Composite((505, 893),
		(  0,  20), "images/sprites/far/mt/mt_2_body.png",
		(119,   0), "images/sprites/far/mt/mt_2_panama.png",
		(186, 116), "images/sprites/far/mt/mt_2_rage.png",
		( 44, 206), "images/sprites/far/mt/mt_2_pioneer.png",
	))
	image mt rage panama swim far = _sr(im.Composite((505, 893),
		(  0,  20), "images/sprites/far/mt/mt_2_body.png",
		(119,   0), "images/sprites/far/mt/mt_2_panama.png",
		(186, 116), "images/sprites/far/mt/mt_2_rage.png",
		(134, 216), "images/sprites/far/mt/mt_2_swim.png",
	))
	image mt rage pioneer far = _sr(im.Composite((505, 873),
		(  0,   0), "images/sprites/far/mt/mt_2_body.png",
		( 44, 186), "images/sprites/far/mt/mt_2_pioneer.png",
		(186,  96), "images/sprites/far/mt/mt_2_rage.png",
	))
	image mt rage swim far = _sr(im.Composite((505, 873),
		(  0,   0), "images/sprites/far/mt/mt_2_body.png",
		(134, 196), "images/sprites/far/mt/mt_2_swim.png",
		(186,  96), "images/sprites/far/mt/mt_2_rage.png",
	))
	image mt sad dress far = _sr(im.Composite((364, 926),
		(  0,   0), "images/sprites/far/mt/mt_1_body.png",
		( 58, 218), "images/sprites/far/mt/mt_1_dress.png",
		(135,  85), "images/sprites/far/mt/mt_1_sad.png",
	))
	image mt sad panama dress far = _sr(im.Composite((364, 942),
		(  0,  16), "images/sprites/far/mt/mt_1_body.png",
		( 74,   0), "images/sprites/far/mt/mt_1_panama.png",
		(135, 101), "images/sprites/far/mt/mt_1_sad.png",
		( 58, 234), "images/sprites/far/mt/mt_1_dress.png",
	))
	image mt sad panama pioneer far = _sr(im.Composite((364, 942),
		(  0,  16), "images/sprites/far/mt/mt_1_body.png",
		( 74,   0), "images/sprites/far/mt/mt_1_panama.png",
		(135, 101), "images/sprites/far/mt/mt_1_sad.png",
		( 32, 206), "images/sprites/far/mt/mt_1_pioneer.png",
	))
	image mt sad panama swim far = _sr(im.Composite((364, 942),
		(  0,  16), "images/sprites/far/mt/mt_1_body.png",
		( 74,   0), "images/sprites/far/mt/mt_1_panama.png",
		(135, 101), "images/sprites/far/mt/mt_1_sad.png",
		( 83, 229), "images/sprites/far/mt/mt_1_swim.png",
	))
	image mt sad pioneer far = _sr(im.Composite((364, 926),
		(  0,   0), "images/sprites/far/mt/mt_1_body.png",
		( 32, 190), "images/sprites/far/mt/mt_1_pioneer.png",
		(135,  85), "images/sprites/far/mt/mt_1_sad.png",
	))
	image mt sad swim far = _sr(im.Composite((364, 926),
		(  0,   0), "images/sprites/far/mt/mt_1_body.png",
		( 83, 213), "images/sprites/far/mt/mt_1_swim.png",
		(135,  85), "images/sprites/far/mt/mt_1_sad.png",
	))
	image mt smile dress far = _sr(im.Composite((364, 926),
		(  0,   0), "images/sprites/far/mt/mt_1_body.png",
		( 58, 218), "images/sprites/far/mt/mt_1_dress.png",
		(135,  85), "images/sprites/far/mt/mt_1_smile.png",
	))
	image mt smile panama dress far = _sr(im.Composite((364, 942),
		(  0,  16), "images/sprites/far/mt/mt_1_body.png",
		( 74,   0), "images/sprites/far/mt/mt_1_panama.png",
		(135, 101), "images/sprites/far/mt/mt_1_smile.png",
		( 58, 234), "images/sprites/far/mt/mt_1_dress.png",
	))
	image mt smile panama pioneer far = _sr(im.Composite((364, 942),
		(  0,  16), "images/sprites/far/mt/mt_1_body.png",
		( 74,   0), "images/sprites/far/mt/mt_1_panama.png",
		(135, 101), "images/sprites/far/mt/mt_1_smile.png",
		( 32, 206), "images/sprites/far/mt/mt_1_pioneer.png",
	))
	image mt smile panama swim far = _sr(im.Composite((364, 942),
		(  0,  16), "images/sprites/far/mt/mt_1_body.png",
		( 74,   0), "images/sprites/far/mt/mt_1_panama.png",
		(135, 101), "images/sprites/far/mt/mt_1_smile.png",
		( 83, 229), "images/sprites/far/mt/mt_1_swim.png",
	))
	image mt smile pioneer far = _sr(im.Composite((364, 926),
		(  0,   0), "images/sprites/far/mt/mt_1_body.png",
		( 32, 190), "images/sprites/far/mt/mt_1_pioneer.png",
		(135,  85), "images/sprites/far/mt/mt_1_smile.png",
	))
	image mt smile swim far = _sr(im.Composite((364, 926),
		(  0,   0), "images/sprites/far/mt/mt_1_body.png",
		( 83, 213), "images/sprites/far/mt/mt_1_swim.png",
		(135,  85), "images/sprites/far/mt/mt_1_smile.png",
	))
	image mt surprise dress far = _sr(im.Composite((364, 926),
		(  0,   0), "images/sprites/far/mt/mt_1_body.png",
		( 58, 218), "images/sprites/far/mt/mt_1_dress.png",
		(135,  87), "images/sprites/far/mt/mt_1_surprise.png",
	))
	image mt surprise panama dress far = _sr(im.Composite((364, 942),
		(  0,  16), "images/sprites/far/mt/mt_1_body.png",
		( 74,   0), "images/sprites/far/mt/mt_1_panama.png",
		(135, 103), "images/sprites/far/mt/mt_1_surprise.png",
		( 58, 234), "images/sprites/far/mt/mt_1_dress.png",
	))
	image mt surprise panama pioneer far = _sr(im.Composite((364, 942),
		(  0,  16), "images/sprites/far/mt/mt_1_body.png",
		( 74,   0), "images/sprites/far/mt/mt_1_panama.png",
		(135, 103), "images/sprites/far/mt/mt_1_surprise.png",
		( 32, 206), "images/sprites/far/mt/mt_1_pioneer.png",
	))
	image mt surprise panama swim far = _sr(im.Composite((364, 942),
		(  0,  16), "images/sprites/far/mt/mt_1_body.png",
		( 74,   0), "images/sprites/far/mt/mt_1_panama.png",
		(135, 103), "images/sprites/far/mt/mt_1_surprise.png",
		( 83, 229), "images/sprites/far/mt/mt_1_swim.png",
	))
	image mt surprise pioneer far = _sr(im.Composite((364, 926),
		(  0,   0), "images/sprites/far/mt/mt_1_body.png",
		( 32, 190), "images/sprites/far/mt/mt_1_pioneer.png",
		(135,  87), "images/sprites/far/mt/mt_1_surprise.png",
	))
	image mt surprise swim far = _sr(im.Composite((364, 926),
		(  0,   0), "images/sprites/far/mt/mt_1_body.png",
		( 83, 213), "images/sprites/far/mt/mt_1_swim.png",
		(135,  87), "images/sprites/far/mt/mt_1_surprise.png",
	))
	
	image mz angry glasses pioneer close = _sr(im.Composite((471, 838),
		(  0,   0), "images/sprites/close/mz/mz_2_body.png",
		(157, 287), "images/sprites/close/mz/mz_2_glasses.png",
		(151, 249), "images/sprites/close/mz/mz_2_angry.png",
		( 21, 378), "images/sprites/close/mz/mz_2_pioneer.png",
	))
	image mz angry pioneer close = _sr(im.Composite((471, 838),
		(  0,   0), "images/sprites/close/mz/mz_2_body.png",
		( 21, 378), "images/sprites/close/mz/mz_2_pioneer.png",
		(151, 249), "images/sprites/close/mz/mz_2_angry.png",
	))
	image mz bukal glasses pioneer close = _sr(im.Composite((494, 864),
		(  0,   0), "images/sprites/close/mz/mz_1_body.png",
		(193, 238), "images/sprites/close/mz/mz_1_glasses.png",
		(194, 221), "images/sprites/close/mz/mz_1_bukal.png",
		(104, 370), "images/sprites/close/mz/mz_1_pioneer.png",
	))
	image mz bukal pioneer close = _sr(im.Composite((494, 864),
		(  0,   0), "images/sprites/close/mz/mz_1_body.png",
		(104, 370), "images/sprites/close/mz/mz_1_pioneer.png",
		(194, 221), "images/sprites/close/mz/mz_1_bukal.png",
	))
	image mz laugh glasses pioneer close = _sr(im.Composite((494, 864),
		(  0,   0), "images/sprites/close/mz/mz_1_body.png",
		(193, 238), "images/sprites/close/mz/mz_1_glasses.png",
		(197, 209), "images/sprites/close/mz/mz_1_laugh.png",
		(104, 370), "images/sprites/close/mz/mz_1_pioneer.png",
	))
	image mz laugh pioneer close = _sr(im.Composite((494, 864),
		(  0,   0), "images/sprites/close/mz/mz_1_body.png",
		(104, 370), "images/sprites/close/mz/mz_1_pioneer.png",
		(197, 209), "images/sprites/close/mz/mz_1_laugh.png",
	))
	image mz normal glasses pioneer close = _sr(im.Composite((494, 864),
		(  0,   0), "images/sprites/close/mz/mz_1_body.png",
		(193, 238), "images/sprites/close/mz/mz_1_glasses.png",
		(189, 222), "images/sprites/close/mz/mz_1_normal.png",
		(104, 370), "images/sprites/close/mz/mz_1_pioneer.png",
	))
	image mz normal pioneer close = _sr(im.Composite((494, 864),
		(  0,   0), "images/sprites/close/mz/mz_1_body.png",
		(104, 370), "images/sprites/close/mz/mz_1_pioneer.png",
		(189, 222), "images/sprites/close/mz/mz_1_normal.png",
	))
	image mz rage glasses pioneer close = _sr(im.Composite((471, 838),
		(  0,   0), "images/sprites/close/mz/mz_2_body.png",
		(157, 287), "images/sprites/close/mz/mz_2_glasses.png",
		(155, 260), "images/sprites/close/mz/mz_2_rage.png",
		( 21, 378), "images/sprites/close/mz/mz_2_pioneer.png",
	))
	image mz rage pioneer close = _sr(im.Composite((471, 838),
		(  0,   0), "images/sprites/close/mz/mz_2_body.png",
		( 21, 378), "images/sprites/close/mz/mz_2_pioneer.png",
		(155, 260), "images/sprites/close/mz/mz_2_rage.png",
	))
	image mz shy glasses pioneer close = _sr(im.Composite((425, 880),
		(  0,   0), "images/sprites/close/mz/mz_3_body.png",
		(215, 228), "images/sprites/close/mz/mz_3_glasses.png",
		(199, 209), "images/sprites/close/mz/mz_3_shy.png",
		(  3, 376), "images/sprites/close/mz/mz_3_pioneer.png",
	))
	image mz shy pioneer close = _sr(im.Composite((425, 880),
		(  0,   0), "images/sprites/close/mz/mz_3_body.png",
		(  3, 376), "images/sprites/close/mz/mz_3_pioneer.png",
		(199, 209), "images/sprites/close/mz/mz_3_shy.png",
	))
	image mz smile glasses pioneer close = _sr(im.Composite((425, 880),
		(  0,   0), "images/sprites/close/mz/mz_3_body.png",
		(215, 228), "images/sprites/close/mz/mz_3_glasses.png",
		(220, 197), "images/sprites/close/mz/mz_3_smile.png",
		(  3, 376), "images/sprites/close/mz/mz_3_pioneer.png",
	))
	image mz smile pioneer close = _sr(im.Composite((425, 880),
		(  0,   0), "images/sprites/close/mz/mz_3_body.png",
		(  3, 376), "images/sprites/close/mz/mz_3_pioneer.png",
		(220, 197), "images/sprites/close/mz/mz_3_smile.png",
	))
	
	image mz angry glasses pioneer = _sr(im.Composite((379, 860),
		(  0,   0), "images/sprites/normal/mz/mz_2_body.png",
		(125, 229), "images/sprites/normal/mz/mz_2_glasses.png",
		(120, 198), "images/sprites/normal/mz/mz_2_angry.png",
		( 17, 301), "images/sprites/normal/mz/mz_2_pioneer.png",
	))
	image mz angry pioneer = _sr(im.Composite((379, 860),
		(  0,   0), "images/sprites/normal/mz/mz_2_body.png",
		( 17, 301), "images/sprites/normal/mz/mz_2_pioneer.png",
		(120, 198), "images/sprites/normal/mz/mz_2_angry.png",
	))
	image mz bukal glasses pioneer = _sr(im.Composite((416, 881),
		(  0,   0), "images/sprites/normal/mz/mz_1_body.png",
		(154, 190), "images/sprites/normal/mz/mz_1_glasses.png",
		(155, 177), "images/sprites/normal/mz/mz_1_bukal.png",
		( 39, 296), "images/sprites/normal/mz/mz_1_pioneer.png",
	))
	image mz bukal pioneer = _sr(im.Composite((416, 881),
		(  0,   0), "images/sprites/normal/mz/mz_1_body.png",
		( 39, 296), "images/sprites/normal/mz/mz_1_pioneer.png",
		(155, 177), "images/sprites/normal/mz/mz_1_bukal.png",
	))
	image mz laugh glasses pioneer = _sr(im.Composite((416, 881),
		(  0,   0), "images/sprites/normal/mz/mz_1_body.png",
		(154, 190), "images/sprites/normal/mz/mz_1_glasses.png",
		(157, 167), "images/sprites/normal/mz/mz_1_laugh.png",
		( 39, 296), "images/sprites/normal/mz/mz_1_pioneer.png",
	))
	image mz laugh pioneer = _sr(im.Composite((416, 881),
		(  0,   0), "images/sprites/normal/mz/mz_1_body.png",
		( 39, 296), "images/sprites/normal/mz/mz_1_pioneer.png",
		(157, 167), "images/sprites/normal/mz/mz_1_laugh.png",
	))
	image mz normal glasses pioneer = _sr(im.Composite((416, 881),
		(  0,   0), "images/sprites/normal/mz/mz_1_body.png",
		(154, 190), "images/sprites/normal/mz/mz_1_glasses.png",
		(151, 177), "images/sprites/normal/mz/mz_1_normal.png",
		( 39, 296), "images/sprites/normal/mz/mz_1_pioneer.png",
	))
	image mz normal pioneer = _sr(im.Composite((416, 881),
		(  0,   0), "images/sprites/normal/mz/mz_1_body.png",
		( 39, 296), "images/sprites/normal/mz/mz_1_pioneer.png",
		(151, 177), "images/sprites/normal/mz/mz_1_normal.png",
	))
	image mz rage glasses pioneer = _sr(im.Composite((379, 860),
		(  0,   0), "images/sprites/normal/mz/mz_2_body.png",
		(125, 229), "images/sprites/normal/mz/mz_2_glasses.png",
		(124, 207), "images/sprites/normal/mz/mz_2_rage.png",
		( 17, 301), "images/sprites/normal/mz/mz_2_pioneer.png",
	))
	image mz rage pioneer = _sr(im.Composite((379, 860),
		(  0,   0), "images/sprites/normal/mz/mz_2_body.png",
		( 17, 301), "images/sprites/normal/mz/mz_2_pioneer.png",
		(124, 207), "images/sprites/normal/mz/mz_2_rage.png",
	))
	image mz shy glasses pioneer = _sr(im.Composite((344, 894),
		(  0,   0), "images/sprites/normal/mz/mz_3_body.png",
		(172, 182), "images/sprites/normal/mz/mz_3_glasses.png",
		(159, 167), "images/sprites/normal/mz/mz_3_shy.png",
		(  2, 301), "images/sprites/normal/mz/mz_3_pioneer.png",
	))
	image mz shy pioneer = _sr(im.Composite((344, 894),
		(  0,   0), "images/sprites/normal/mz/mz_3_body.png",
		(  2, 301), "images/sprites/normal/mz/mz_3_pioneer.png",
		(159, 167), "images/sprites/normal/mz/mz_3_shy.png",
	))
	image mz smile glasses pioneer = _sr(im.Composite((344, 894),
		(  0,   0), "images/sprites/normal/mz/mz_3_body.png",
		(172, 182), "images/sprites/normal/mz/mz_3_glasses.png",
		(176, 158), "images/sprites/normal/mz/mz_3_smile.png",
		(  2, 301), "images/sprites/normal/mz/mz_3_pioneer.png",
	))
	image mz smile pioneer = _sr(im.Composite((344, 894),
		(  0,   0), "images/sprites/normal/mz/mz_3_body.png",
		(  2, 301), "images/sprites/normal/mz/mz_3_pioneer.png",
		(176, 158), "images/sprites/normal/mz/mz_3_smile.png",
	))
	
	image mz angry glasses pioneer far = _sr(im.Composite((286, 803),
		(  0,   0), "images/sprites/far/mz/mz_2_body.png",
		( 94, 172), "images/sprites/far/mz/mz_2_glasses.png",
		( 90, 149), "images/sprites/far/mz/mz_2_angry.png",
		( 13, 226), "images/sprites/far/mz/mz_2_pioneer.png",
	))
	image mz angry pioneer far = _sr(im.Composite((286, 803),
		(  0,   0), "images/sprites/far/mz/mz_2_body.png",
		( 13, 226), "images/sprites/far/mz/mz_2_pioneer.png",
		( 90, 149), "images/sprites/far/mz/mz_2_angry.png",
	))
	image mz bukal glasses pioneer far = _sr(im.Composite((316, 819),
		(  0,   0), "images/sprites/far/mz/mz_1_body.png",
		(115, 143), "images/sprites/far/mz/mz_1_glasses.png",
		(116, 133), "images/sprites/far/mz/mz_1_bukal.png",
		( 29, 222), "images/sprites/far/mz/mz_1_pioneer.png",
	))
	image mz bukal pioneer far = _sr(im.Composite((316, 819),
		(  0,   0), "images/sprites/far/mz/mz_1_body.png",
		( 29, 222), "images/sprites/far/mz/mz_1_pioneer.png",
		(116, 133), "images/sprites/far/mz/mz_1_bukal.png",
	))
	image mz laugh glasses pioneer far = _sr(im.Composite((316, 819),
		(  0,   0), "images/sprites/far/mz/mz_1_body.png",
		(115, 143), "images/sprites/far/mz/mz_1_glasses.png",
		(118, 126), "images/sprites/far/mz/mz_1_laugh.png",
		( 29, 222), "images/sprites/far/mz/mz_1_pioneer.png",
	))
	image mz laugh pioneer far = _sr(im.Composite((316, 819),
		(  0,   0), "images/sprites/far/mz/mz_1_body.png",
		( 29, 222), "images/sprites/far/mz/mz_1_pioneer.png",
		(118, 126), "images/sprites/far/mz/mz_1_laugh.png",
	))
	image mz normal glasses pioneer far = _sr(im.Composite((316, 819),
		(  0,   0), "images/sprites/far/mz/mz_1_body.png",
		(115, 143), "images/sprites/far/mz/mz_1_glasses.png",
		(113, 134), "images/sprites/far/mz/mz_1_normal.png",
		( 29, 222), "images/sprites/far/mz/mz_1_pioneer.png",
	))
	image mz normal pioneer far = _sr(im.Composite((316, 819),
		(  0,   0), "images/sprites/far/mz/mz_1_body.png",
		( 29, 222), "images/sprites/far/mz/mz_1_pioneer.png",
		(113, 134), "images/sprites/far/mz/mz_1_normal.png",
	))
	image mz rage glasses pioneer far = _sr(im.Composite((286, 803),
		(  0,   0), "images/sprites/far/mz/mz_2_body.png",
		( 94, 172), "images/sprites/far/mz/mz_2_glasses.png",
		( 93, 156), "images/sprites/far/mz/mz_2_rage.png",
		( 13, 226), "images/sprites/far/mz/mz_2_pioneer.png",
	))
	image mz rage pioneer far = _sr(im.Composite((286, 803),
		(  0,   0), "images/sprites/far/mz/mz_2_body.png",
		( 13, 226), "images/sprites/far/mz/mz_2_pioneer.png",
		( 93, 156), "images/sprites/far/mz/mz_2_rage.png",
	))
	image mz shy glasses pioneer far = _sr(im.Composite((262, 828),
		(  0,   0), "images/sprites/far/mz/mz_3_body.png",
		(129, 137), "images/sprites/far/mz/mz_3_glasses.png",
		(119, 125), "images/sprites/far/mz/mz_3_shy.png",
		(  0, 225), "images/sprites/far/mz/mz_3_pioneer.png",
	))
	image mz shy pioneer far = _sr(im.Composite((262, 828),
		(  0,   0), "images/sprites/far/mz/mz_3_body.png",
		(  0, 225), "images/sprites/far/mz/mz_3_pioneer.png",
		(119, 125), "images/sprites/far/mz/mz_3_shy.png",
	))
	image mz smile glasses pioneer far = _sr(im.Composite((262, 828),
		(  0,   0), "images/sprites/far/mz/mz_3_body.png",
		(129, 137), "images/sprites/far/mz/mz_3_glasses.png",
		(132, 118), "images/sprites/far/mz/mz_3_smile.png",
		(  0, 225), "images/sprites/far/mz/mz_3_pioneer.png",
	))
	image mz smile pioneer far = _sr(im.Composite((262, 828),
		(  0,   0), "images/sprites/far/mz/mz_3_body.png",
		(  0, 225), "images/sprites/far/mz/mz_3_pioneer.png",
		(132, 118), "images/sprites/far/mz/mz_3_smile.png",
	))
	
	image pi close = _sr(im.Composite((558, 1068),
		(  0,   0), "images/sprites/close/pi/pi_1_pioneer.png",
	))
	
	image pi normal = _sr(im.Composite((447, 1045),
		(  0,   0), "images/sprites/normal/pi/pi_1_pioneer.png",
	))
	image pi smile = _sr(im.Composite((447, 1045),
		(  0,   0), "images/sprites/normal/pi/pi_1_pioneer_smile.png",
	))
	
	image pi far = _sr(im.Composite((335, 941),
		(  0,   0), "images/sprites/far/pi/pi_1_pioneer.png",
	))
	
	image sh cry close = _sr(im.Composite((661, 1037),
		(  0,   0), "images/sprites/close/sh/sh_2_body.png",
		(186, 105), "images/sprites/close/sh/sh_2_rage.png",
		(184, 146), "images/sprites/close/sh/sh_2_cry.png",
	))
	image sh cry pioneer close = _sr(im.Composite((661, 1037),
		(  0,   0), "images/sprites/close/sh/sh_2_body.png",
		(184, 146), "images/sprites/close/sh/sh_2_cry.png",
	))
	image sh laugh close = _sr(im.Composite((619, 1033),
		(  0,   0), "images/sprites/close/sh/sh_1_body.png",
		(216, 141), "images/sprites/close/sh/sh_1_laugh.png",
		(216, 141), "images/sprites/close/sh/sh_1_laugh.png",
	))
	image sh laugh pioneer close = _sr(im.Composite((619, 1033),
		(  0,   0), "images/sprites/close/sh/sh_1_body.png",
		(216, 141), "images/sprites/close/sh/sh_1_laugh.png",
	))
	image sh normal close = _sr(im.Composite((705, 1035),
		(  0,   0), "images/sprites/close/sh/sh_3_body.png",
		(200, 128), "images/sprites/close/sh/sh_3_normal.png",
		(200, 128), "images/sprites/close/sh/sh_3_normal.png",
	))
	image sh normal pioneer close = _sr(im.Composite((705, 1035),
		(  0,   0), "images/sprites/close/sh/sh_3_body.png",
		(200, 128), "images/sprites/close/sh/sh_3_normal.png",
	))
	image sh normal_smile close = _sr(im.Composite((661, 1037),
		(  0,   0), "images/sprites/close/sh/sh_2_body.png",
		(186, 105), "images/sprites/close/sh/sh_2_rage.png",
		(184, 142), "images/sprites/close/sh/sh_2_normal_smile.png",
	))
	image sh normal_smile pioneer close = _sr(im.Composite((661, 1037),
		(  0,   0), "images/sprites/close/sh/sh_2_body.png",
		(184, 142), "images/sprites/close/sh/sh_2_normal_smile.png",
	))
	image sh rage close = _sr(im.Composite((661, 1037),
		(  0,   0), "images/sprites/close/sh/sh_2_body.png",
		(186, 105), "images/sprites/close/sh/sh_2_rage.png",
		(186, 105), "images/sprites/close/sh/sh_2_rage.png",
	))
	image sh rage pioneer close = _sr(im.Composite((661, 1037),
		(  0,   0), "images/sprites/close/sh/sh_2_body.png",
		(186, 105), "images/sprites/close/sh/sh_2_rage.png",
	))
	image sh scared close = _sr(im.Composite((619, 1033),
		(  0,   0), "images/sprites/close/sh/sh_1_body.png",
		(216, 141), "images/sprites/close/sh/sh_1_laugh.png",
		(204, 112), "images/sprites/close/sh/sh_1_scared.png",
	))
	image sh scared pioneer close = _sr(im.Composite((619, 1033),
		(  0,   0), "images/sprites/close/sh/sh_1_body.png",
		(204, 112), "images/sprites/close/sh/sh_1_scared.png",
	))
	image sh serious close = _sr(im.Composite((705, 1035),
		(  0,   0), "images/sprites/close/sh/sh_3_body.png",
		(200, 128), "images/sprites/close/sh/sh_3_normal.png",
		(200, 137), "images/sprites/close/sh/sh_3_serious.png",
	))
	image sh serious pioneer close = _sr(im.Composite((705, 1035),
		(  0,   0), "images/sprites/close/sh/sh_3_body.png",
		(200, 137), "images/sprites/close/sh/sh_3_serious.png",
	))
	image sh smile close = _sr(im.Composite((619, 1033),
		(  0,   0), "images/sprites/close/sh/sh_1_body.png",
		(216, 141), "images/sprites/close/sh/sh_1_laugh.png",
		(216, 141), "images/sprites/close/sh/sh_1_smile.png",
	))
	image sh smile pioneer close = _sr(im.Composite((619, 1033),
		(  0,   0), "images/sprites/close/sh/sh_1_body.png",
		(216, 141), "images/sprites/close/sh/sh_1_smile.png",
	))
	image sh surprise close = _sr(im.Composite((705, 1035),
		(  0,   0), "images/sprites/close/sh/sh_3_body.png",
		(200, 128), "images/sprites/close/sh/sh_3_normal.png",
		(200, 107), "images/sprites/close/sh/sh_3_surprise.png",
	))
	image sh surprise pioneer close = _sr(im.Composite((705, 1035),
		(  0,   0), "images/sprites/close/sh/sh_3_body.png",
		(200, 107), "images/sprites/close/sh/sh_3_surprise.png",
	))
	image sh upset close = _sr(im.Composite((619, 1033),
		(  0,   0), "images/sprites/close/sh/sh_1_body.png",
		(216, 141), "images/sprites/close/sh/sh_1_laugh.png",
		(216, 131), "images/sprites/close/sh/sh_1_upset.png",
	))
	image sh upset pioneer close = _sr(im.Composite((619, 1033),
		(  0,   0), "images/sprites/close/sh/sh_1_body.png",
		(216, 131), "images/sprites/close/sh/sh_1_upset.png",
	))
	
	image sh cry = _sr(im.Composite((529, 1019),
		(  0,   0), "images/sprites/normal/sh/sh_2_body.png",
		(149,  83), "images/sprites/normal/sh/sh_2_rage.png",
		(147, 116), "images/sprites/normal/sh/sh_2_cry.png",
	))
	image sh cry pioneer = _sr(im.Composite((529, 1019),
		(  0,   0), "images/sprites/normal/sh/sh_2_body.png",
		(147, 116), "images/sprites/normal/sh/sh_2_cry.png",
	))
	image sh laugh = _sr(im.Composite((496, 1017),
		(  0,   0), "images/sprites/normal/sh/sh_1_body.png",
		(173, 113), "images/sprites/normal/sh/sh_1_laugh.png",
		(173, 113), "images/sprites/normal/sh/sh_1_laugh.png",
	))
	image sh laugh pioneer = _sr(im.Composite((496, 1017),
		(  0,   0), "images/sprites/normal/sh/sh_1_body.png",
		(173, 113), "images/sprites/normal/sh/sh_1_laugh.png",
	))
	image sh normal = _sr(im.Composite((563, 1018),
		(  0,   0), "images/sprites/normal/sh/sh_3_body.png",
		(159, 103), "images/sprites/normal/sh/sh_3_normal.png",
		(159, 103), "images/sprites/normal/sh/sh_3_normal.png",
	))
	image sh normal pioneer = _sr(im.Composite((563, 1018),
		(  0,   0), "images/sprites/normal/sh/sh_3_body.png",
		(159, 103), "images/sprites/normal/sh/sh_3_normal.png",
	))
	image sh normal_smile = _sr(im.Composite((529, 1019),
		(  0,   0), "images/sprites/normal/sh/sh_2_body.png",
		(149,  83), "images/sprites/normal/sh/sh_2_rage.png",
		(147, 113), "images/sprites/normal/sh/sh_2_normal_smile.png",
	))
	image sh normal_smile pioneer = _sr(im.Composite((529, 1019),
		(  0,   0), "images/sprites/normal/sh/sh_2_body.png",
		(147, 113), "images/sprites/normal/sh/sh_2_normal_smile.png",
	))
	image sh rage = _sr(im.Composite((529, 1019),
		(  0,   0), "images/sprites/normal/sh/sh_2_body.png",
		(149,  83), "images/sprites/normal/sh/sh_2_rage.png",
		(149,  83), "images/sprites/normal/sh/sh_2_rage.png",
	))
	image sh rage pioneer = _sr(im.Composite((529, 1019),
		(  0,   0), "images/sprites/normal/sh/sh_2_body.png",
		(149,  83), "images/sprites/normal/sh/sh_2_rage.png",
	))
	image sh scared = _sr(im.Composite((496, 1017),
		(  0,   0), "images/sprites/normal/sh/sh_1_body.png",
		(173, 113), "images/sprites/normal/sh/sh_1_laugh.png",
		(163,  90), "images/sprites/normal/sh/sh_1_scared.png",
	))
	image sh scared pioneer = _sr(im.Composite((496, 1017),
		(  0,   0), "images/sprites/normal/sh/sh_1_body.png",
		(163,  90), "images/sprites/normal/sh/sh_1_scared.png",
	))
	image sh serious = _sr(im.Composite((563, 1018),
		(  0,   0), "images/sprites/normal/sh/sh_3_body.png",
		(159, 103), "images/sprites/normal/sh/sh_3_normal.png",
		(159, 110), "images/sprites/normal/sh/sh_3_serious.png",
	))
	image sh serious pioneer = _sr(im.Composite((563, 1018),
		(  0,   0), "images/sprites/normal/sh/sh_3_body.png",
		(159, 110), "images/sprites/normal/sh/sh_3_serious.png",
	))
	image sh smile = _sr(im.Composite((496, 1017),
		(  0,   0), "images/sprites/normal/sh/sh_1_body.png",
		(173, 113), "images/sprites/normal/sh/sh_1_laugh.png",
		(173, 113), "images/sprites/normal/sh/sh_1_smile.png",
	))
	image sh smile pioneer = _sr(im.Composite((496, 1017),
		(  0,   0), "images/sprites/normal/sh/sh_1_body.png",
		(173, 113), "images/sprites/normal/sh/sh_1_smile.png",
	))
	image sh surprise = _sr(im.Composite((563, 1018),
		(  0,   0), "images/sprites/normal/sh/sh_3_body.png",
		(159, 103), "images/sprites/normal/sh/sh_3_normal.png",
		(159,  86), "images/sprites/normal/sh/sh_3_surprise.png",
	))
	image sh surprise pioneer = _sr(im.Composite((563, 1018),
		(  0,   0), "images/sprites/normal/sh/sh_3_body.png",
		(159,  86), "images/sprites/normal/sh/sh_3_surprise.png",
	))
	image sh upset = _sr(im.Composite((496, 1017),
		(  0,   0), "images/sprites/normal/sh/sh_1_body.png",
		(173, 113), "images/sprites/normal/sh/sh_1_laugh.png",
		(173, 105), "images/sprites/normal/sh/sh_1_upset.png",
	))
	image sh upset pioneer = _sr(im.Composite((496, 1017),
		(  0,   0), "images/sprites/normal/sh/sh_1_body.png",
		(173, 105), "images/sprites/normal/sh/sh_1_upset.png",
	))
	
	image sh cry far = _sr(im.Composite((397, 922),
		(  0,   0), "images/sprites/far/sh/sh_2_body.png",
		(111,  62), "images/sprites/far/sh/sh_2_rage.png",
		(110,  87), "images/sprites/far/sh/sh_2_cry.png",
	))
	image sh cry pioneer far = _sr(im.Composite((397, 922),
		(  0,   0), "images/sprites/far/sh/sh_2_body.png",
		(110,  87), "images/sprites/far/sh/sh_2_cry.png",
	))
	image sh laugh far = _sr(im.Composite((372, 920),
		(  0,   0), "images/sprites/far/sh/sh_1_body.png",
		(130,  85), "images/sprites/far/sh/sh_1_laugh.png",
		(130,  85), "images/sprites/far/sh/sh_1_laugh.png",
	))
	image sh laugh pioneer far = _sr(im.Composite((372, 920),
		(  0,   0), "images/sprites/far/sh/sh_1_body.png",
		(130,  85), "images/sprites/far/sh/sh_1_laugh.png",
	))
	image sh normal far = _sr(im.Composite((423, 921),
		(  0,   0), "images/sprites/far/sh/sh_3_body.png",
		(120,  77), "images/sprites/far/sh/sh_3_normal.png",
		(120,  77), "images/sprites/far/sh/sh_3_normal.png",
	))
	image sh normal pioneer far = _sr(im.Composite((423, 921),
		(  0,   0), "images/sprites/far/sh/sh_3_body.png",
		(120,  77), "images/sprites/far/sh/sh_3_normal.png",
	))
	image sh normal_smile far = _sr(im.Composite((397, 922),
		(  0,   0), "images/sprites/far/sh/sh_2_body.png",
		(111,  62), "images/sprites/far/sh/sh_2_rage.png",
		(110,  85), "images/sprites/far/sh/sh_2_normal_smile.png",
	))
	image sh normal_smile pioneer far = _sr(im.Composite((397, 922),
		(  0,   0), "images/sprites/far/sh/sh_2_body.png",
		(110,  85), "images/sprites/far/sh/sh_2_normal_smile.png",
	))
	image sh rage far = _sr(im.Composite((397, 922),
		(  0,   0), "images/sprites/far/sh/sh_2_body.png",
		(111,  62), "images/sprites/far/sh/sh_2_rage.png",
		(111,  62), "images/sprites/far/sh/sh_2_rage.png",
	))
	image sh rage pioneer far = _sr(im.Composite((397, 922),
		(  0,   0), "images/sprites/far/sh/sh_2_body.png",
		(111,  62), "images/sprites/far/sh/sh_2_rage.png",
	))
	image sh scared far = _sr(im.Composite((372, 920),
		(  0,   0), "images/sprites/far/sh/sh_1_body.png",
		(130,  85), "images/sprites/far/sh/sh_1_laugh.png",
		(123,  67), "images/sprites/far/sh/sh_1_scared.png",
	))
	image sh scared pioneer far = _sr(im.Composite((372, 920),
		(  0,   0), "images/sprites/far/sh/sh_1_body.png",
		(123,  67), "images/sprites/far/sh/sh_1_scared.png",
	))
	image sh serious far = _sr(im.Composite((423, 921),
		(  0,   0), "images/sprites/far/sh/sh_3_body.png",
		(120,  77), "images/sprites/far/sh/sh_3_normal.png",
		(120,  82), "images/sprites/far/sh/sh_3_serious.png",
	))
	image sh serious pioneer far = _sr(im.Composite((423, 921),
		(  0,   0), "images/sprites/far/sh/sh_3_body.png",
		(120,  82), "images/sprites/far/sh/sh_3_serious.png",
	))
	image sh smile far = _sr(im.Composite((372, 920),
		(  0,   0), "images/sprites/far/sh/sh_1_body.png",
		(130,  85), "images/sprites/far/sh/sh_1_laugh.png",
		(130,  85), "images/sprites/far/sh/sh_1_smile.png",
	))
	image sh smile pioneer far = _sr(im.Composite((372, 920),
		(  0,   0), "images/sprites/far/sh/sh_1_body.png",
		(130,  85), "images/sprites/far/sh/sh_1_smile.png",
	))
	image sh surprise far = _sr(im.Composite((423, 921),
		(  0,   0), "images/sprites/far/sh/sh_3_body.png",
		(120,  77), "images/sprites/far/sh/sh_3_normal.png",
		(120,  64), "images/sprites/far/sh/sh_3_surprise.png",
	))
	image sh surprise pioneer far = _sr(im.Composite((423, 921),
		(  0,   0), "images/sprites/far/sh/sh_3_body.png",
		(120,  64), "images/sprites/far/sh/sh_3_surprise.png",
	))
	image sh upset far = _sr(im.Composite((372, 920),
		(  0,   0), "images/sprites/far/sh/sh_1_body.png",
		(130,  85), "images/sprites/far/sh/sh_1_laugh.png",
		(130,  78), "images/sprites/far/sh/sh_1_upset.png",
	))
	image sh upset pioneer far = _sr(im.Composite((372, 920),
		(  0,   0), "images/sprites/far/sh/sh_1_body.png",
		(130,  78), "images/sprites/far/sh/sh_1_upset.png",
	))
	
	image sl angry dress close = _sr(im.Composite((733, 925),
		(  0,   0), "images/sprites/close/sl/sl_3_body.png",
		(361, 340), "images/sprites/close/sl/sl_3_dress.png",
		(496, 140), "images/sprites/close/sl/sl_3_angry.png",
	))
	image sl angry pioneer close = _sr(im.Composite((753, 925),
		(  0,   0), "images/sprites/close/sl/sl_3_body.png",
		(318, 308), "images/sprites/close/sl/sl_3_pioneer.png",
		(496, 140), "images/sprites/close/sl/sl_3_angry.png",
	))
	image sl angry sport close = _sr(im.Composite((733, 925),
		(  0,   0), "images/sprites/close/sl/sl_3_body.png",
		(358, 362), "images/sprites/close/sl/sl_3_sport.png",
		(496, 140), "images/sprites/close/sl/sl_3_angry.png",
	))
	image sl angry swim close = _sr(im.Composite((733, 925),
		(  0,   0), "images/sprites/close/sl/sl_3_body.png",
		(406, 350), "images/sprites/close/sl/sl_3_swim.png",
		(496, 140), "images/sprites/close/sl/sl_3_angry.png",
	))
	image sl happy dress close = _sr(im.Composite((516, 929),
		(  0,   0), "images/sprites/close/sl/sl_2_body.png",
		(104, 348), "images/sprites/close/sl/sl_2_dress.png",
		(254, 139), "images/sprites/close/sl/sl_2_happy.png",
	))
	image sl happy pioneer close = _sr(im.Composite((533, 929),
		(  0,   0), "images/sprites/close/sl/sl_2_body.png",
		( 99, 328), "images/sprites/close/sl/sl_2_pioneer.png",
		(254, 139), "images/sprites/close/sl/sl_2_happy.png",
	))
	image sl happy sport close = _sr(im.Composite((516, 929),
		(  0,   0), "images/sprites/close/sl/sl_2_body.png",
		(105, 367), "images/sprites/close/sl/sl_2_sport.png",
		(254, 139), "images/sprites/close/sl/sl_2_happy.png",
	))
	image sl happy swim close = _sr(im.Composite((516, 929),
		(  0,   0), "images/sprites/close/sl/sl_2_body.png",
		(109, 365), "images/sprites/close/sl/sl_2_swim.png",
		(254, 139), "images/sprites/close/sl/sl_2_happy.png",
	))
	image sl laugh dress close = _sr(im.Composite((516, 929),
		(  0,   0), "images/sprites/close/sl/sl_2_body.png",
		(104, 348), "images/sprites/close/sl/sl_2_dress.png",
		(243, 138), "images/sprites/close/sl/sl_2_laugh.png",
	))
	image sl laugh pioneer close = _sr(im.Composite((533, 929),
		(  0,   0), "images/sprites/close/sl/sl_2_body.png",
		( 99, 328), "images/sprites/close/sl/sl_2_pioneer.png",
		(243, 138), "images/sprites/close/sl/sl_2_laugh.png",
	))
	image sl laugh sport close = _sr(im.Composite((516, 929),
		(  0,   0), "images/sprites/close/sl/sl_2_body.png",
		(105, 367), "images/sprites/close/sl/sl_2_sport.png",
		(243, 138), "images/sprites/close/sl/sl_2_laugh.png",
	))
	image sl laugh swim close = _sr(im.Composite((516, 929),
		(  0,   0), "images/sprites/close/sl/sl_2_body.png",
		(109, 365), "images/sprites/close/sl/sl_2_swim.png",
		(243, 138), "images/sprites/close/sl/sl_2_laugh.png",
	))
	image sl normal dress close = _sr(im.Composite((517, 921),
		(  0,   0), "images/sprites/close/sl/sl_1_body.png",
		( 25, 323), "images/sprites/close/sl/sl_1_dress.png",
		(108, 148), "images/sprites/close/sl/sl_1_normal.png",
	))
	image sl normal pioneer close = _sr(im.Composite((517, 921),
		(  0,   0), "images/sprites/close/sl/sl_1_body.png",
		(  5, 300), "images/sprites/close/sl/sl_1_pioneer.png",
		(108, 148), "images/sprites/close/sl/sl_1_normal.png",
	))
	image sl normal sport close = _sr(im.Composite((517, 921),
		(  0,   0), "images/sprites/close/sl/sl_1_body.png",
		( 25, 343), "images/sprites/close/sl/sl_1_sport.png",
		(108, 148), "images/sprites/close/sl/sl_1_normal.png",
	))
	image sl normal swim close = _sr(im.Composite((517, 921),
		(  0,   0), "images/sprites/close/sl/sl_1_body.png",
		( 26, 341), "images/sprites/close/sl/sl_1_swim.png",
		(108, 148), "images/sprites/close/sl/sl_1_normal.png",
	))
	image sl sad dress close = _sr(im.Composite((733, 925),
		(  0,   0), "images/sprites/close/sl/sl_3_body.png",
		(361, 340), "images/sprites/close/sl/sl_3_dress.png",
		(503, 143), "images/sprites/close/sl/sl_3_sad.png",
	))
	image sl sad pioneer close = _sr(im.Composite((753, 925),
		(  0,   0), "images/sprites/close/sl/sl_3_body.png",
		(318, 308), "images/sprites/close/sl/sl_3_pioneer.png",
		(503, 143), "images/sprites/close/sl/sl_3_sad.png",
	))
	image sl sad sport close = _sr(im.Composite((733, 925),
		(  0,   0), "images/sprites/close/sl/sl_3_body.png",
		(358, 362), "images/sprites/close/sl/sl_3_sport.png",
		(503, 143), "images/sprites/close/sl/sl_3_sad.png",
	))
	image sl sad swim close = _sr(im.Composite((733, 925),
		(  0,   0), "images/sprites/close/sl/sl_3_body.png",
		(406, 350), "images/sprites/close/sl/sl_3_swim.png",
		(503, 143), "images/sprites/close/sl/sl_3_sad.png",
	))
	image sl scared dress close = _sr(im.Composite((420, 876),
		(  0,   0), "images/sprites/close/sl/sl_4_body.png",
		( 39, 323), "images/sprites/close/sl/sl_4_dress.png",
		(116, 101), "images/sprites/close/sl/sl_4_scared.png",
	))
	image sl scared pioneer close = _sr(im.Composite((442, 876),
		( 19,   0), "images/sprites/close/sl/sl_4_body.png",
		(  0, 301), "images/sprites/close/sl/sl_4_pioneer.png",
		(135, 101), "images/sprites/close/sl/sl_4_scared.png",
	))
	image sl scared sport close = _sr(im.Composite((420, 876),
		(  0,   0), "images/sprites/close/sl/sl_4_body.png",
		( 37, 341), "images/sprites/close/sl/sl_4_sport.png",
		(116, 101), "images/sprites/close/sl/sl_4_scared.png",
	))
	image sl scared swim close = _sr(im.Composite((420, 876),
		(  0,   0), "images/sprites/close/sl/sl_4_body.png",
		(104, 334), "images/sprites/close/sl/sl_4_swim.png",
		(116, 101), "images/sprites/close/sl/sl_4_scared.png",
	))
	image sl serious dress close = _sr(im.Composite((517, 921),
		(  0,   0), "images/sprites/close/sl/sl_1_body.png",
		( 25, 323), "images/sprites/close/sl/sl_1_dress.png",
		(101, 149), "images/sprites/close/sl/sl_1_serious.png",
	))
	image sl serious pioneer close = _sr(im.Composite((517, 921),
		(  0,   0), "images/sprites/close/sl/sl_1_body.png",
		(  5, 300), "images/sprites/close/sl/sl_1_pioneer.png",
		(101, 149), "images/sprites/close/sl/sl_1_serious.png",
	))
	image sl serious sport close = _sr(im.Composite((517, 921),
		(  0,   0), "images/sprites/close/sl/sl_1_body.png",
		( 25, 343), "images/sprites/close/sl/sl_1_sport.png",
		(101, 149), "images/sprites/close/sl/sl_1_serious.png",
	))
	image sl serious swim close = _sr(im.Composite((517, 921),
		(  0,   0), "images/sprites/close/sl/sl_1_body.png",
		( 26, 341), "images/sprites/close/sl/sl_1_swim.png",
		(101, 149), "images/sprites/close/sl/sl_1_serious.png",
	))
	image sl shy dress close = _sr(im.Composite((516, 929),
		(  0,   0), "images/sprites/close/sl/sl_2_body.png",
		(104, 348), "images/sprites/close/sl/sl_2_dress.png",
		(180, 135), "images/sprites/close/sl/sl_2_shy.png",
	))
	image sl shy pioneer close = _sr(im.Composite((533, 929),
		(  0,   0), "images/sprites/close/sl/sl_2_body.png",
		( 99, 328), "images/sprites/close/sl/sl_2_pioneer.png",
		(180, 135), "images/sprites/close/sl/sl_2_shy.png",
	))
	image sl shy sport close = _sr(im.Composite((516, 929),
		(  0,   0), "images/sprites/close/sl/sl_2_body.png",
		(105, 367), "images/sprites/close/sl/sl_2_sport.png",
		(180, 135), "images/sprites/close/sl/sl_2_shy.png",
	))
	image sl shy swim close = _sr(im.Composite((516, 929),
		(  0,   0), "images/sprites/close/sl/sl_2_body.png",
		(109, 365), "images/sprites/close/sl/sl_2_swim.png",
		(180, 135), "images/sprites/close/sl/sl_2_shy.png",
	))
	image sl smile dress close = _sr(im.Composite((517, 921),
		(  0,   0), "images/sprites/close/sl/sl_1_body.png",
		( 25, 323), "images/sprites/close/sl/sl_1_dress.png",
		(108, 147), "images/sprites/close/sl/sl_1_smile.png",
	))
	image sl smile pioneer close = _sr(im.Composite((517, 921),
		(  0,   0), "images/sprites/close/sl/sl_1_body.png",
		(  5, 300), "images/sprites/close/sl/sl_1_pioneer.png",
		(108, 147), "images/sprites/close/sl/sl_1_smile.png",
	))
	image sl smile sport close = _sr(im.Composite((517, 921),
		(  0,   0), "images/sprites/close/sl/sl_1_body.png",
		( 25, 343), "images/sprites/close/sl/sl_1_sport.png",
		(108, 147), "images/sprites/close/sl/sl_1_smile.png",
	))
	image sl smile swim close = _sr(im.Composite((517, 921),
		(  0,   0), "images/sprites/close/sl/sl_1_body.png",
		( 26, 341), "images/sprites/close/sl/sl_1_swim.png",
		(108, 147), "images/sprites/close/sl/sl_1_smile.png",
	))
	image sl smile2 dress close = _sr(im.Composite((516, 929),
		(  0,   0), "images/sprites/close/sl/sl_2_body.png",
		(104, 348), "images/sprites/close/sl/sl_2_dress.png",
		(264, 137), "images/sprites/close/sl/sl_2_smile2.png",
	))
	image sl smile2 pioneer close = _sr(im.Composite((533, 929),
		(  0,   0), "images/sprites/close/sl/sl_2_body.png",
		( 99, 328), "images/sprites/close/sl/sl_2_pioneer.png",
		(264, 137), "images/sprites/close/sl/sl_2_smile2.png",
	))
	image sl smile2 sport close = _sr(im.Composite((516, 929),
		(  0,   0), "images/sprites/close/sl/sl_2_body.png",
		(105, 367), "images/sprites/close/sl/sl_2_sport.png",
		(264, 137), "images/sprites/close/sl/sl_2_smile2.png",
	))
	image sl smile2 swim close = _sr(im.Composite((516, 929),
		(  0,   0), "images/sprites/close/sl/sl_2_body.png",
		(109, 365), "images/sprites/close/sl/sl_2_swim.png",
		(264, 137), "images/sprites/close/sl/sl_2_smile2.png",
	))
	image sl surprise dress close = _sr(im.Composite((733, 925),
		(  0,   0), "images/sprites/close/sl/sl_3_body.png",
		(361, 340), "images/sprites/close/sl/sl_3_dress.png",
		(472, 134), "images/sprites/close/sl/sl_3_surprise.png",
	))
	image sl surprise pioneer close = _sr(im.Composite((753, 925),
		(  0,   0), "images/sprites/close/sl/sl_3_body.png",
		(318, 308), "images/sprites/close/sl/sl_3_pioneer.png",
		(472, 134), "images/sprites/close/sl/sl_3_surprise.png",
	))
	image sl surprise sport close = _sr(im.Composite((733, 925),
		(  0,   0), "images/sprites/close/sl/sl_3_body.png",
		(358, 362), "images/sprites/close/sl/sl_3_sport.png",
		(472, 134), "images/sprites/close/sl/sl_3_surprise.png",
	))
	image sl surprise swim close = _sr(im.Composite((733, 925),
		(  0,   0), "images/sprites/close/sl/sl_3_body.png",
		(406, 350), "images/sprites/close/sl/sl_3_swim.png",
		(472, 134), "images/sprites/close/sl/sl_3_surprise.png",
	))
	image sl tender dress close = _sr(im.Composite((420, 876),
		(  0,   0), "images/sprites/close/sl/sl_4_body.png",
		( 39, 323), "images/sprites/close/sl/sl_4_dress.png",
		(105, 170), "images/sprites/close/sl/sl_4_tender.png",
	))
	image sl tender pioneer close = _sr(im.Composite((442, 876),
		( 19,   0), "images/sprites/close/sl/sl_4_body.png",
		(  0, 301), "images/sprites/close/sl/sl_4_pioneer.png",
		(124, 170), "images/sprites/close/sl/sl_4_tender.png",
	))
	image sl tender sport close = _sr(im.Composite((420, 876),
		(  0,   0), "images/sprites/close/sl/sl_4_body.png",
		( 37, 341), "images/sprites/close/sl/sl_4_sport.png",
		(105, 170), "images/sprites/close/sl/sl_4_tender.png",
	))
	image sl tender swim close = _sr(im.Composite((420, 876),
		(  0,   0), "images/sprites/close/sl/sl_4_body.png",
		(104, 334), "images/sprites/close/sl/sl_4_swim.png",
		(105, 170), "images/sprites/close/sl/sl_4_tender.png",
	))
	
	image sl angry dress = _sr(im.Composite((637, 930),
		(  0,   0), "images/sprites/normal/sl/sl_3_body.png",
		(230, 272), "images/sprites/normal/sl/sl_3_dress.png",
		(397, 112), "images/sprites/normal/sl/sl_3_angry.png",
	))
	image sl angry pioneer = _sr(im.Composite((637, 930),
		(  0,   0), "images/sprites/normal/sl/sl_3_body.png",
		(212, 247), "images/sprites/normal/sl/sl_3_pioneer.png",
		(397, 112), "images/sprites/normal/sl/sl_3_angry.png",
	))
	image sl angry sport = _sr(im.Composite((637, 930),
		(  0,   0), "images/sprites/normal/sl/sl_3_body.png",
		(257, 290), "images/sprites/normal/sl/sl_3_sport.png",
		(397, 112), "images/sprites/normal/sl/sl_3_angry.png",
	))
	image sl angry swim = _sr(im.Composite((637, 930),
		(  0,   0), "images/sprites/normal/sl/sl_3_body.png",
		(276, 280), "images/sprites/normal/sl/sl_3_swim.png",
		(397, 112), "images/sprites/normal/sl/sl_3_angry.png",
	))
	image sl happy dress = _sr(im.Composite((417, 933),
		(  0,   0), "images/sprites/normal/sl/sl_2_body.png",
		( 41, 278), "images/sprites/normal/sl/sl_2_dress.png",
		(204, 111), "images/sprites/normal/sl/sl_2_happy.png",
	))
	image sl happy pioneer = _sr(im.Composite((427, 933),
		(  0,   0), "images/sprites/normal/sl/sl_2_body.png",
		( 30, 262), "images/sprites/normal/sl/sl_2_pioneer.png",
		(204, 111), "images/sprites/normal/sl/sl_2_happy.png",
	))
	image sl happy sport = _sr(im.Composite((413, 933),
		(  0,   0), "images/sprites/normal/sl/sl_2_body.png",
		( 65, 293), "images/sprites/normal/sl/sl_2_sport.png",
		(204, 111), "images/sprites/normal/sl/sl_2_happy.png",
	))
	image sl happy swim = _sr(im.Composite((413, 933),
		(  0,   0), "images/sprites/normal/sl/sl_2_body.png",
		( 73, 292), "images/sprites/normal/sl/sl_2_swim.png",
		(204, 111), "images/sprites/normal/sl/sl_2_happy.png",
	))
	image sl laugh dress = _sr(im.Composite((417, 933),
		(  0,   0), "images/sprites/normal/sl/sl_2_body.png",
		( 41, 278), "images/sprites/normal/sl/sl_2_dress.png",
		(195, 110), "images/sprites/normal/sl/sl_2_laugh.png",
	))
	image sl laugh pioneer = _sr(im.Composite((427, 933),
		(  0,   0), "images/sprites/normal/sl/sl_2_body.png",
		( 30, 262), "images/sprites/normal/sl/sl_2_pioneer.png",
		(195, 110), "images/sprites/normal/sl/sl_2_laugh.png",
	))
	image sl laugh sport = _sr(im.Composite((413, 933),
		(  0,   0), "images/sprites/normal/sl/sl_2_body.png",
		( 65, 293), "images/sprites/normal/sl/sl_2_sport.png",
		(195, 110), "images/sprites/normal/sl/sl_2_laugh.png",
	))
	image sl laugh swim = _sr(im.Composite((413, 933),
		(  0,   0), "images/sprites/normal/sl/sl_2_body.png",
		( 73, 292), "images/sprites/normal/sl/sl_2_swim.png",
		(195, 110), "images/sprites/normal/sl/sl_2_laugh.png",
	))
	image sl normal dress = _sr(im.Composite((527, 927),
		(  0,   0), "images/sprites/normal/sl/sl_1_body.png",
		( 74, 258), "images/sprites/normal/sl/sl_1_dress.png",
		(159, 118), "images/sprites/normal/sl/sl_1_normal.png",
	))
	image sl normal pioneer = _sr(im.Composite((527, 927),
		(  0,   0), "images/sprites/normal/sl/sl_1_body.png",
		( 51, 240), "images/sprites/normal/sl/sl_1_pioneer.png",
		(159, 118), "images/sprites/normal/sl/sl_1_normal.png",
	))
	image sl normal sport = _sr(im.Composite((527, 927),
		(  0,   0), "images/sprites/normal/sl/sl_1_body.png",
		( 85, 275), "images/sprites/normal/sl/sl_1_sport.png",
		(159, 118), "images/sprites/normal/sl/sl_1_normal.png",
	))
	image sl normal swim = _sr(im.Composite((527, 927),
		(  0,   0), "images/sprites/normal/sl/sl_1_body.png",
		( 93, 273), "images/sprites/normal/sl/sl_1_swim.png",
		(159, 118), "images/sprites/normal/sl/sl_1_normal.png",
	))
	image sl sad dress = _sr(im.Composite((637, 930),
		(  0,   0), "images/sprites/normal/sl/sl_3_body.png",
		(230, 272), "images/sprites/normal/sl/sl_3_dress.png",
		(402, 115), "images/sprites/normal/sl/sl_3_sad.png",
	))
	image sl sad pioneer = _sr(im.Composite((637, 930),
		(  0,   0), "images/sprites/normal/sl/sl_3_body.png",
		(212, 247), "images/sprites/normal/sl/sl_3_pioneer.png",
		(402, 115), "images/sprites/normal/sl/sl_3_sad.png",
	))
	image sl sad sport = _sr(im.Composite((637, 930),
		(  0,   0), "images/sprites/normal/sl/sl_3_body.png",
		(257, 290), "images/sprites/normal/sl/sl_3_sport.png",
		(402, 115), "images/sprites/normal/sl/sl_3_sad.png",
	))
	image sl sad swim = _sr(im.Composite((637, 930),
		(  0,   0), "images/sprites/normal/sl/sl_3_body.png",
		(276, 280), "images/sprites/normal/sl/sl_3_swim.png",
		(402, 115), "images/sprites/normal/sl/sl_3_sad.png",
	))
	image sl scared dress = _sr(im.Composite((451, 891),
		(  0,   0), "images/sprites/normal/sl/sl_4_body.png",
		( 45, 258), "images/sprites/normal/sl/sl_4_dress.png",
		(150,  81), "images/sprites/normal/sl/sl_4_scared.png",
	))
	image sl scared pioneer = _sr(im.Composite((451, 891),
		(  0,   0), "images/sprites/normal/sl/sl_4_body.png",
		( 30, 241), "images/sprites/normal/sl/sl_4_pioneer.png",
		(150,  81), "images/sprites/normal/sl/sl_4_scared.png",
	))
	image sl scared sport = _sr(im.Composite((451, 891),
		(  0,   0), "images/sprites/normal/sl/sl_4_body.png",
		( 58, 273), "images/sprites/normal/sl/sl_4_sport.png",
		(150,  81), "images/sprites/normal/sl/sl_4_scared.png",
	))
	image sl scared swim = _sr(im.Composite((451, 891),
		(  0,   0), "images/sprites/normal/sl/sl_4_body.png",
		( 75, 268), "images/sprites/normal/sl/sl_4_swim.png",
		(150,  81), "images/sprites/normal/sl/sl_4_scared.png",
	))
	image sl serious dress = _sr(im.Composite((527, 927),
		(  0,   0), "images/sprites/normal/sl/sl_1_body.png",
		( 74, 258), "images/sprites/normal/sl/sl_1_dress.png",
		(154, 119), "images/sprites/normal/sl/sl_1_serious.png",
	))
	image sl serious pioneer = _sr(im.Composite((527, 927),
		(  0,   0), "images/sprites/normal/sl/sl_1_body.png",
		( 51, 240), "images/sprites/normal/sl/sl_1_pioneer.png",
		(154, 119), "images/sprites/normal/sl/sl_1_serious.png",
	))
	image sl serious sport = _sr(im.Composite((527, 927),
		(  0,   0), "images/sprites/normal/sl/sl_1_body.png",
		( 85, 275), "images/sprites/normal/sl/sl_1_sport.png",
		(154, 119), "images/sprites/normal/sl/sl_1_serious.png",
	))
	image sl serious swim = _sr(im.Composite((527, 927),
		(  0,   0), "images/sprites/normal/sl/sl_1_body.png",
		( 93, 273), "images/sprites/normal/sl/sl_1_swim.png",
		(154, 119), "images/sprites/normal/sl/sl_1_serious.png",
	))
	image sl shy dress = _sr(im.Composite((417, 933),
		(  0,   0), "images/sprites/normal/sl/sl_2_body.png",
		( 41, 278), "images/sprites/normal/sl/sl_2_dress.png",
		(144, 108), "images/sprites/normal/sl/sl_2_shy.png",
	))
	image sl shy pioneer = _sr(im.Composite((427, 933),
		(  0,   0), "images/sprites/normal/sl/sl_2_body.png",
		( 30, 262), "images/sprites/normal/sl/sl_2_pioneer.png",
		(144, 108), "images/sprites/normal/sl/sl_2_shy.png",
	))
	image sl shy sport = _sr(im.Composite((413, 933),
		(  0,   0), "images/sprites/normal/sl/sl_2_body.png",
		( 65, 293), "images/sprites/normal/sl/sl_2_sport.png",
		(144, 108), "images/sprites/normal/sl/sl_2_shy.png",
	))
	image sl shy swim = _sr(im.Composite((413, 933),
		(  0,   0), "images/sprites/normal/sl/sl_2_body.png",
		( 73, 292), "images/sprites/normal/sl/sl_2_swim.png",
		(144, 108), "images/sprites/normal/sl/sl_2_shy.png",
	))
	image sl smile dress = _sr(im.Composite((527, 927),
		(  0,   0), "images/sprites/normal/sl/sl_1_body.png",
		( 74, 258), "images/sprites/normal/sl/sl_1_dress.png",
		(159, 118), "images/sprites/normal/sl/sl_1_smile.png",
	))
	image sl smile pioneer = _sr(im.Composite((527, 927),
		(  0,   0), "images/sprites/normal/sl/sl_1_body.png",
		( 51, 240), "images/sprites/normal/sl/sl_1_pioneer.png",
		(159, 118), "images/sprites/normal/sl/sl_1_smile.png",
	))
	image sl smile sport = _sr(im.Composite((527, 927),
		(  0,   0), "images/sprites/normal/sl/sl_1_body.png",
		( 85, 275), "images/sprites/normal/sl/sl_1_sport.png",
		(159, 118), "images/sprites/normal/sl/sl_1_smile.png",
	))
	image sl smile swim = _sr(im.Composite((527, 927),
		(  0,   0), "images/sprites/normal/sl/sl_1_body.png",
		( 93, 273), "images/sprites/normal/sl/sl_1_swim.png",
		(159, 118), "images/sprites/normal/sl/sl_1_smile.png",
	))
	image sl smile2 dress = _sr(im.Composite((417, 933),
		(  0,   0), "images/sprites/normal/sl/sl_2_body.png",
		( 41, 278), "images/sprites/normal/sl/sl_2_dress.png",
		(211, 109), "images/sprites/normal/sl/sl_2_smile2.png",
	))
	image sl smile2 pioneer = _sr(im.Composite((427, 933),
		(  0,   0), "images/sprites/normal/sl/sl_2_body.png",
		( 30, 262), "images/sprites/normal/sl/sl_2_pioneer.png",
		(211, 109), "images/sprites/normal/sl/sl_2_smile2.png",
	))
	image sl smile2 sport = _sr(im.Composite((413, 933),
		(  0,   0), "images/sprites/normal/sl/sl_2_body.png",
		( 65, 293), "images/sprites/normal/sl/sl_2_sport.png",
		(211, 109), "images/sprites/normal/sl/sl_2_smile2.png",
	))
	image sl smile2 swim = _sr(im.Composite((413, 933),
		(  0,   0), "images/sprites/normal/sl/sl_2_body.png",
		( 73, 292), "images/sprites/normal/sl/sl_2_swim.png",
		(211, 109), "images/sprites/normal/sl/sl_2_smile2.png",
	))
	image sl surprise dress = _sr(im.Composite((637, 930),
		(  0,   0), "images/sprites/normal/sl/sl_3_body.png",
		(230, 272), "images/sprites/normal/sl/sl_3_dress.png",
		(378, 107), "images/sprites/normal/sl/sl_3_surprise.png",
	))
	image sl surprise pioneer = _sr(im.Composite((637, 930),
		(  0,   0), "images/sprites/normal/sl/sl_3_body.png",
		(212, 247), "images/sprites/normal/sl/sl_3_pioneer.png",
		(378, 107), "images/sprites/normal/sl/sl_3_surprise.png",
	))
	image sl surprise sport = _sr(im.Composite((637, 930),
		(  0,   0), "images/sprites/normal/sl/sl_3_body.png",
		(257, 290), "images/sprites/normal/sl/sl_3_sport.png",
		(378, 107), "images/sprites/normal/sl/sl_3_surprise.png",
	))
	image sl surprise swim = _sr(im.Composite((637, 930),
		(  0,   0), "images/sprites/normal/sl/sl_3_body.png",
		(276, 280), "images/sprites/normal/sl/sl_3_swim.png",
		(378, 107), "images/sprites/normal/sl/sl_3_surprise.png",
	))
	image sl tender dress = _sr(im.Composite((451, 891),
		(  0,   0), "images/sprites/normal/sl/sl_4_body.png",
		( 45, 258), "images/sprites/normal/sl/sl_4_dress.png",
		(141, 136), "images/sprites/normal/sl/sl_4_tender.png",
	))
	image sl tender pioneer = _sr(im.Composite((451, 891),
		(  0,   0), "images/sprites/normal/sl/sl_4_body.png",
		( 30, 241), "images/sprites/normal/sl/sl_4_pioneer.png",
		(141, 136), "images/sprites/normal/sl/sl_4_tender.png",
	))
	image sl tender sport = _sr(im.Composite((451, 891),
		(  0,   0), "images/sprites/normal/sl/sl_4_body.png",
		( 58, 273), "images/sprites/normal/sl/sl_4_sport.png",
		(141, 136), "images/sprites/normal/sl/sl_4_tender.png",
	))
	image sl tender swim = _sr(im.Composite((451, 891),
		(  0,   0), "images/sprites/normal/sl/sl_4_body.png",
		( 75, 268), "images/sprites/normal/sl/sl_4_swim.png",
		(141, 136), "images/sprites/normal/sl/sl_4_tender.png",
	))
	
	image sl angry dress far = _sr(im.Composite((478, 855),
		(  0,   0), "images/sprites/far/sl/sl_3_body.png",
		(156, 204), "images/sprites/far/sl/sl_3_dress.png",
		(298,  84), "images/sprites/far/sl/sl_3_angry.png",
	))
	image sl angry pioneer far = _sr(im.Composite((478, 855),
		(  0,   0), "images/sprites/far/sl/sl_3_body.png",
		(159, 185), "images/sprites/far/sl/sl_3_pioneer.png",
		(298,  84), "images/sprites/far/sl/sl_3_angry.png",
	))
	image sl angry sport far = _sr(im.Composite((478, 855),
		(  0,   0), "images/sprites/far/sl/sl_3_body.png",
		(193, 217), "images/sprites/far/sl/sl_3_sport.png",
		(298,  84), "images/sprites/far/sl/sl_3_angry.png",
	))
	image sl angry swim far = _sr(im.Composite((478, 855),
		(  0,   0), "images/sprites/far/sl/sl_3_body.png",
		(207, 210), "images/sprites/far/sl/sl_3_swim.png",
		(298,  84), "images/sprites/far/sl/sl_3_angry.png",
	))
	image sl happy dress far = _sr(im.Composite((326, 857),
		(  0,   0), "images/sprites/far/sl/sl_2_body.png",
		( 15, 208), "images/sprites/far/sl/sl_2_dress.png",
		(153,  83), "images/sprites/far/sl/sl_2_happy.png",
	))
	image sl happy pioneer far = _sr(im.Composite((321, 857),
		(  0,   0), "images/sprites/far/sl/sl_2_body.png",
		( 23, 196), "images/sprites/far/sl/sl_2_pioneer.png",
		(153,  83), "images/sprites/far/sl/sl_2_happy.png",
	))
	image sl happy sport far = _sr(im.Composite((310, 857),
		(  0,   0), "images/sprites/far/sl/sl_2_body.png",
		( 49, 219), "images/sprites/far/sl/sl_2_sport.png",
		(153,  83), "images/sprites/far/sl/sl_2_happy.png",
	))
	image sl happy swim far = _sr(im.Composite((310, 857),
		(  0,   0), "images/sprites/far/sl/sl_2_body.png",
		( 55, 218), "images/sprites/far/sl/sl_2_swim.png",
		(153,  83), "images/sprites/far/sl/sl_2_happy.png",
	))
	image sl laugh dress far = _sr(im.Composite((326, 857),
		(  0,   0), "images/sprites/far/sl/sl_2_body.png",
		( 15, 208), "images/sprites/far/sl/sl_2_dress.png",
		(146,  82), "images/sprites/far/sl/sl_2_laugh.png",
	))
	image sl laugh pioneer far = _sr(im.Composite((321, 857),
		(  0,   0), "images/sprites/far/sl/sl_2_body.png",
		( 23, 196), "images/sprites/far/sl/sl_2_pioneer.png",
		(146,  82), "images/sprites/far/sl/sl_2_laugh.png",
	))
	image sl laugh sport far = _sr(im.Composite((310, 857),
		(  0,   0), "images/sprites/far/sl/sl_2_body.png",
		( 49, 219), "images/sprites/far/sl/sl_2_sport.png",
		(146,  82), "images/sprites/far/sl/sl_2_laugh.png",
	))
	image sl laugh swim far = _sr(im.Composite((310, 857),
		(  0,   0), "images/sprites/far/sl/sl_2_body.png",
		( 55, 218), "images/sprites/far/sl/sl_2_swim.png",
		(146,  82), "images/sprites/far/sl/sl_2_laugh.png",
	))
	image sl normal dress far = _sr(im.Composite((396, 853),
		(  0,   0), "images/sprites/far/sl/sl_1_body.png",
		( 40, 194), "images/sprites/far/sl/sl_1_dress.png",
		(119,  89), "images/sprites/far/sl/sl_1_normal.png",
	))
	image sl normal pioneer far = _sr(im.Composite((425, 853),
		(  0,   0), "images/sprites/far/sl/sl_1_body.png",
		( 39, 180), "images/sprites/far/sl/sl_1_pioneer.png",
		(119,  89), "images/sprites/far/sl/sl_1_normal.png",
	))
	image sl normal sport far = _sr(im.Composite((396, 853),
		(  0,   0), "images/sprites/far/sl/sl_1_body.png",
		( 64, 206), "images/sprites/far/sl/sl_1_sport.png",
		(119,  89), "images/sprites/far/sl/sl_1_normal.png",
	))
	image sl normal swim far = _sr(im.Composite((396, 853),
		(  0,   0), "images/sprites/far/sl/sl_1_body.png",
		( 70, 205), "images/sprites/far/sl/sl_1_swim.png",
		(119,  89), "images/sprites/far/sl/sl_1_normal.png",
	))
	image sl sad dress far = _sr(im.Composite((478, 855),
		(  0,   0), "images/sprites/far/sl/sl_3_body.png",
		(156, 204), "images/sprites/far/sl/sl_3_dress.png",
		(302,  86), "images/sprites/far/sl/sl_3_sad.png",
	))
	image sl sad pioneer far = _sr(im.Composite((478, 855),
		(  0,   0), "images/sprites/far/sl/sl_3_body.png",
		(159, 185), "images/sprites/far/sl/sl_3_pioneer.png",
		(302,  86), "images/sprites/far/sl/sl_3_sad.png",
	))
	image sl sad sport far = _sr(im.Composite((478, 855),
		(  0,   0), "images/sprites/far/sl/sl_3_body.png",
		(193, 217), "images/sprites/far/sl/sl_3_sport.png",
		(302,  86), "images/sprites/far/sl/sl_3_sad.png",
	))
	image sl sad swim far = _sr(im.Composite((478, 855),
		(  0,   0), "images/sprites/far/sl/sl_3_body.png",
		(207, 210), "images/sprites/far/sl/sl_3_swim.png",
		(302,  86), "images/sprites/far/sl/sl_3_sad.png",
	))
	image sl scared dress far = _sr(im.Composite((338, 826),
		(  0,   0), "images/sprites/far/sl/sl_4_body.png",
		( 18, 194), "images/sprites/far/sl/sl_4_dress.png",
		(112,  61), "images/sprites/far/sl/sl_4_scared.png",
	))
	image sl scared pioneer far = _sr(im.Composite((338, 826),
		(  0,   0), "images/sprites/far/sl/sl_4_body.png",
		( 23, 181), "images/sprites/far/sl/sl_4_pioneer.png",
		(112,  61), "images/sprites/far/sl/sl_4_scared.png",
	))
	image sl scared sport far = _sr(im.Composite((338, 826),
		(  0,   0), "images/sprites/far/sl/sl_4_body.png",
		( 43, 205), "images/sprites/far/sl/sl_4_sport.png",
		(112,  61), "images/sprites/far/sl/sl_4_scared.png",
	))
	image sl scared swim far = _sr(im.Composite((338, 826),
		(  0,   0), "images/sprites/far/sl/sl_4_body.png",
		( 56, 201), "images/sprites/far/sl/sl_4_swim.png",
		(112,  61), "images/sprites/far/sl/sl_4_scared.png",
	))
	image sl serious dress far = _sr(im.Composite((396, 853),
		(  0,   0), "images/sprites/far/sl/sl_1_body.png",
		( 40, 194), "images/sprites/far/sl/sl_1_dress.png",
		(116,  90), "images/sprites/far/sl/sl_1_serious.png",
	))
	image sl serious pioneer far = _sr(im.Composite((425, 853),
		(  0,   0), "images/sprites/far/sl/sl_1_body.png",
		( 39, 180), "images/sprites/far/sl/sl_1_pioneer.png",
		(116,  90), "images/sprites/far/sl/sl_1_serious.png",
	))
	image sl serious sport far = _sr(im.Composite((396, 853),
		(  0,   0), "images/sprites/far/sl/sl_1_body.png",
		( 64, 206), "images/sprites/far/sl/sl_1_sport.png",
		(116,  90), "images/sprites/far/sl/sl_1_serious.png",
	))
	image sl serious swim far = _sr(im.Composite((396, 853),
		(  0,   0), "images/sprites/far/sl/sl_1_body.png",
		( 70, 205), "images/sprites/far/sl/sl_1_swim.png",
		(116,  90), "images/sprites/far/sl/sl_1_serious.png",
	))
	image sl shy dress far = _sr(im.Composite((326, 857),
		(  0,   0), "images/sprites/far/sl/sl_2_body.png",
		( 15, 208), "images/sprites/far/sl/sl_2_dress.png",
		(109,  81), "images/sprites/far/sl/sl_2_shy.png",
	))
	image sl shy pioneer far = _sr(im.Composite((321, 857),
		(  0,   0), "images/sprites/far/sl/sl_2_body.png",
		( 23, 196), "images/sprites/far/sl/sl_2_pioneer.png",
		(109,  81), "images/sprites/far/sl/sl_2_shy.png",
	))
	image sl shy sport far = _sr(im.Composite((310, 857),
		(  0,   0), "images/sprites/far/sl/sl_2_body.png",
		( 49, 219), "images/sprites/far/sl/sl_2_sport.png",
		(109,  81), "images/sprites/far/sl/sl_2_shy.png",
	))
	image sl shy swim far = _sr(im.Composite((310, 857),
		(  0,   0), "images/sprites/far/sl/sl_2_body.png",
		( 55, 218), "images/sprites/far/sl/sl_2_swim.png",
		(109,  81), "images/sprites/far/sl/sl_2_shy.png",
	))
	image sl smile dress far = _sr(im.Composite((396, 853),
		(  0,   0), "images/sprites/far/sl/sl_1_body.png",
		( 40, 194), "images/sprites/far/sl/sl_1_dress.png",
		(119,  88), "images/sprites/far/sl/sl_1_smile.png",
	))
	image sl smile pioneer far = _sr(im.Composite((425, 853),
		(  0,   0), "images/sprites/far/sl/sl_1_body.png",
		( 39, 180), "images/sprites/far/sl/sl_1_pioneer.png",
		(119,  88), "images/sprites/far/sl/sl_1_smile.png",
	))
	image sl smile sport far = _sr(im.Composite((396, 853),
		(  0,   0), "images/sprites/far/sl/sl_1_body.png",
		( 64, 206), "images/sprites/far/sl/sl_1_sport.png",
		(119,  88), "images/sprites/far/sl/sl_1_smile.png",
	))
	image sl smile swim far = _sr(im.Composite((396, 853),
		(  0,   0), "images/sprites/far/sl/sl_1_body.png",
		( 70, 205), "images/sprites/far/sl/sl_1_swim.png",
		(119,  88), "images/sprites/far/sl/sl_1_smile.png",
	))
	image sl smile2 dress far = _sr(im.Composite((326, 857),
		(  0,   0), "images/sprites/far/sl/sl_2_body.png",
		( 15, 208), "images/sprites/far/sl/sl_2_dress.png",
		(159,  82), "images/sprites/far/sl/sl_2_smile2.png",
	))
	image sl smile2 pioneer far = _sr(im.Composite((321, 857),
		(  0,   0), "images/sprites/far/sl/sl_2_body.png",
		( 23, 196), "images/sprites/far/sl/sl_2_pioneer.png",
		(159,  82), "images/sprites/far/sl/sl_2_smile2.png",
	))
	image sl smile2 sport far = _sr(im.Composite((310, 857),
		(  0,   0), "images/sprites/far/sl/sl_2_body.png",
		( 49, 219), "images/sprites/far/sl/sl_2_sport.png",
		(159,  82), "images/sprites/far/sl/sl_2_smile2.png",
	))
	image sl smile2 swim far = _sr(im.Composite((310, 857),
		(  0,   0), "images/sprites/far/sl/sl_2_body.png",
		( 55, 218), "images/sprites/far/sl/sl_2_swim.png",
		(159,  82), "images/sprites/far/sl/sl_2_smile2.png",
	))
	image sl surprise dress far = _sr(im.Composite((478, 855),
		(  0,   0), "images/sprites/far/sl/sl_3_body.png",
		(156, 204), "images/sprites/far/sl/sl_3_dress.png",
		(284,  80), "images/sprites/far/sl/sl_3_surprise.png",
	))
	image sl surprise pioneer far = _sr(im.Composite((478, 855),
		(  0,   0), "images/sprites/far/sl/sl_3_body.png",
		(159, 185), "images/sprites/far/sl/sl_3_pioneer.png",
		(284,  80), "images/sprites/far/sl/sl_3_surprise.png",
	))
	image sl surprise sport far = _sr(im.Composite((478, 855),
		(  0,   0), "images/sprites/far/sl/sl_3_body.png",
		(193, 217), "images/sprites/far/sl/sl_3_sport.png",
		(284,  80), "images/sprites/far/sl/sl_3_surprise.png",
	))
	image sl surprise swim far = _sr(im.Composite((478, 855),
		(  0,   0), "images/sprites/far/sl/sl_3_body.png",
		(207, 210), "images/sprites/far/sl/sl_3_swim.png",
		(284,  80), "images/sprites/far/sl/sl_3_surprise.png",
	))
	image sl tender dress far = _sr(im.Composite((338, 826),
		(  0,   0), "images/sprites/far/sl/sl_4_body.png",
		( 18, 194), "images/sprites/far/sl/sl_4_dress.png",
		(105, 102), "images/sprites/far/sl/sl_4_tender.png",
	))
	image sl tender pioneer far = _sr(im.Composite((338, 826),
		(  0,   0), "images/sprites/far/sl/sl_4_body.png",
		( 23, 181), "images/sprites/far/sl/sl_4_pioneer.png",
		(105, 102), "images/sprites/far/sl/sl_4_tender.png",
	))
	image sl tender sport far = _sr(im.Composite((338, 826),
		(  0,   0), "images/sprites/far/sl/sl_4_body.png",
		( 43, 205), "images/sprites/far/sl/sl_4_sport.png",
		(105, 102), "images/sprites/far/sl/sl_4_tender.png",
	))
	image sl tender swim far = _sr(im.Composite((338, 826),
		(  0,   0), "images/sprites/far/sl/sl_4_body.png",
		( 56, 201), "images/sprites/far/sl/sl_4_swim.png",
		(105, 102), "images/sprites/far/sl/sl_4_tender.png",
	))
	
	image un angry dress close = _sr(im.Composite((483, 981),
		(  0,   0), "images/sprites/close/un/un_1_body.png",
		(113, 432), "images/sprites/close/un/un_1_dress.png",
		(210, 238), "images/sprites/close/un/un_1_angry.png",
	))
	image un angry pioneer close = _sr(im.Composite((483, 981),
		(  0,   0), "images/sprites/close/un/un_1_body.png",
		( 39, 409), "images/sprites/close/un/un_1_pioneer.png",
		(210, 238), "images/sprites/close/un/un_1_angry.png",
	))
	image un angry sport close = _sr(im.Composite((483, 981),
		(  0,   0), "images/sprites/close/un/un_1_body.png",
		( 43, 454), "images/sprites/close/un/un_1_sport.png",
		(210, 238), "images/sprites/close/un/un_1_angry.png",
	))
	image un angry swim close = _sr(im.Composite((483, 981),
		(  0,   0), "images/sprites/close/un/un_1_body.png",
		( 82, 444), "images/sprites/close/un/un_1_swim.png",
		(210, 238), "images/sprites/close/un/un_1_angry.png",
	))
	image un angry2 dress close = _sr(im.Composite((571, 979),
		(  0,   0), "images/sprites/close/un/un_3_body.png",
		( 86, 442), "images/sprites/close/un/un_3_dress.png",
		(167, 239), "images/sprites/close/un/un_3_angry2.png",
	))
	image un angry2 pioneer close = _sr(im.Composite((571, 979),
		(  0,   0), "images/sprites/close/un/un_3_body.png",
		( 35, 416), "images/sprites/close/un/un_3_pioneer.png",
		(167, 239), "images/sprites/close/un/un_3_angry2.png",
	))
	image un angry2 sport close = _sr(im.Composite((705, 1018),
		(134,  39), "images/sprites/close/un/un_3_body.png",
		(  0,   0), "images/sprites/close/un/un_3_sport.png",
		(301, 278), "images/sprites/close/un/un_3_angry2.png",
	))
	image un cry dress close = _sr(im.Composite((588, 950),
		(  0,   0), "images/sprites/close/un/un_2_body.png",
		(128, 405), "images/sprites/close/un/un_2_dress.png",
		(183, 206), "images/sprites/close/un/un_2_cry.png",
	))
	image un cry pioneer close = _sr(im.Composite((588, 950),
		(  0,   0), "images/sprites/close/un/un_2_body.png",
		( 85, 391), "images/sprites/close/un/un_2_pioneer.png",
		(183, 206), "images/sprites/close/un/un_2_cry.png",
	))
	image un cry sport close = _sr(im.Composite((588, 950),
		(  0,   0), "images/sprites/close/un/un_2_body.png",
		( 97, 442), "images/sprites/close/un/un_2_sport.png",
		(183, 206), "images/sprites/close/un/un_2_cry.png",
	))
	image un cry swim close = _sr(im.Composite((588, 950),
		(  0,   0), "images/sprites/close/un/un_2_body.png",
		(112, 421), "images/sprites/close/un/un_2_swim.png",
		(183, 206), "images/sprites/close/un/un_2_cry.png",
	))
	image un cry_smile dress close = _sr(im.Composite((588, 950),
		(  0,   0), "images/sprites/close/un/un_2_body.png",
		(128, 405), "images/sprites/close/un/un_2_dress.png",
		(199, 206), "images/sprites/close/un/un_2_cry_smile.png",
	))
	image un cry_smile pioneer close = _sr(im.Composite((588, 950),
		(  0,   0), "images/sprites/close/un/un_2_body.png",
		( 85, 391), "images/sprites/close/un/un_2_pioneer.png",
		(199, 206), "images/sprites/close/un/un_2_cry_smile.png",
	))
	image un cry_smile sport close = _sr(im.Composite((588, 950),
		(  0,   0), "images/sprites/close/un/un_2_body.png",
		( 97, 442), "images/sprites/close/un/un_2_sport.png",
		(199, 206), "images/sprites/close/un/un_2_cry_smile.png",
	))
	image un cry_smile swim close = _sr(im.Composite((588, 950),
		(  0,   0), "images/sprites/close/un/un_2_body.png",
		(112, 421), "images/sprites/close/un/un_2_swim.png",
		(199, 206), "images/sprites/close/un/un_2_cry_smile.png",
	))
	image un evil_smile dress close = _sr(im.Composite((483, 981),
		(  0,   0), "images/sprites/close/un/un_1_body.png",
		(113, 432), "images/sprites/close/un/un_1_dress.png",
		(210, 238), "images/sprites/close/un/un_1_evil_smile.png",
	))
	image un evil_smile pioneer close = _sr(im.Composite((483, 981),
		(  0,   0), "images/sprites/close/un/un_1_body.png",
		( 39, 409), "images/sprites/close/un/un_1_pioneer.png",
		(210, 238), "images/sprites/close/un/un_1_evil_smile.png",
	))
	image un evil_smile sport close = _sr(im.Composite((483, 981),
		(  0,   0), "images/sprites/close/un/un_1_body.png",
		( 43, 454), "images/sprites/close/un/un_1_sport.png",
		(210, 238), "images/sprites/close/un/un_1_evil_smile.png",
	))
	image un evil_smile swim close = _sr(im.Composite((483, 981),
		(  0,   0), "images/sprites/close/un/un_1_body.png",
		( 82, 444), "images/sprites/close/un/un_1_swim.png",
		(210, 238), "images/sprites/close/un/un_1_evil_smile.png",
	))
	image un grin dress close = _sr(im.Composite((571, 979),
		(  0,   0), "images/sprites/close/un/un_3_body.png",
		( 86, 442), "images/sprites/close/un/un_3_dress.png",
		(172, 247), "images/sprites/close/un/un_3_grin.png",
	))
	image un grin pioneer close = _sr(im.Composite((571, 979),
		(  0,   0), "images/sprites/close/un/un_3_body.png",
		( 35, 416), "images/sprites/close/un/un_3_pioneer.png",
		(172, 247), "images/sprites/close/un/un_3_grin.png",
	))
	image un grin sport close = _sr(im.Composite((705, 1018),
		(134,  39), "images/sprites/close/un/un_3_body.png",
		(  0,   0), "images/sprites/close/un/un_3_sport.png",
		(306, 286), "images/sprites/close/un/un_3_grin.png",
	))
	image un laugh dress close = _sr(im.Composite((571, 979),
		(  0,   0), "images/sprites/close/un/un_3_body.png",
		( 86, 442), "images/sprites/close/un/un_3_dress.png",
		(153, 245), "images/sprites/close/un/un_3_laugh.png",
	))
	image un laugh pioneer close = _sr(im.Composite((571, 979),
		(  0,   0), "images/sprites/close/un/un_3_body.png",
		( 35, 416), "images/sprites/close/un/un_3_pioneer.png",
		(153, 245), "images/sprites/close/un/un_3_laugh.png",
	))
	image un laugh sport close = _sr(im.Composite((705, 1018),
		(134,  39), "images/sprites/close/un/un_3_body.png",
		(  0,   0), "images/sprites/close/un/un_3_sport.png",
		(287, 284), "images/sprites/close/un/un_3_laugh.png",
	))
	image un normal dress close = _sr(im.Composite((483, 981),
		(  0,   0), "images/sprites/close/un/un_1_body.png",
		(113, 432), "images/sprites/close/un/un_1_dress.png",
		(213, 242), "images/sprites/close/un/un_1_normal.png",
	))
	image un normal pioneer close = _sr(im.Composite((483, 981),
		(  0,   0), "images/sprites/close/un/un_1_body.png",
		( 39, 409), "images/sprites/close/un/un_1_pioneer.png",
		(213, 242), "images/sprites/close/un/un_1_normal.png",
	))
	image un normal sport close = _sr(im.Composite((483, 981),
		(  0,   0), "images/sprites/close/un/un_1_body.png",
		( 43, 454), "images/sprites/close/un/un_1_sport.png",
		(213, 242), "images/sprites/close/un/un_1_normal.png",
	))
	image un normal swim close = _sr(im.Composite((483, 981),
		(  0,   0), "images/sprites/close/un/un_1_body.png",
		( 82, 444), "images/sprites/close/un/un_1_swim.png",
		(213, 242), "images/sprites/close/un/un_1_normal.png",
	))
	image un rage dress close = _sr(im.Composite((571, 979),
		(  0,   0), "images/sprites/close/un/un_3_body.png",
		( 86, 442), "images/sprites/close/un/un_3_dress.png",
		(170, 242), "images/sprites/close/un/un_3_rage.png",
	))
	image un rage pioneer close = _sr(im.Composite((571, 979),
		(  0,   0), "images/sprites/close/un/un_3_body.png",
		( 35, 416), "images/sprites/close/un/un_3_pioneer.png",
		(170, 242), "images/sprites/close/un/un_3_rage.png",
	))
	image un rage sport close = _sr(im.Composite((705, 1018),
		(134,  39), "images/sprites/close/un/un_3_body.png",
		(  0,   0), "images/sprites/close/un/un_3_sport.png",
		(304, 281), "images/sprites/close/un/un_3_rage.png",
	))
	image un sad dress close = _sr(im.Composite((588, 950),
		(  0,   0), "images/sprites/close/un/un_2_body.png",
		(128, 405), "images/sprites/close/un/un_2_dress.png",
		(199, 205), "images/sprites/close/un/un_2_sad.png",
	))
	image un sad pioneer close = _sr(im.Composite((588, 950),
		(  0,   0), "images/sprites/close/un/un_2_body.png",
		( 85, 391), "images/sprites/close/un/un_2_pioneer.png",
		(199, 205), "images/sprites/close/un/un_2_sad.png",
	))
	image un sad sport close = _sr(im.Composite((588, 950),
		(  0,   0), "images/sprites/close/un/un_2_body.png",
		( 97, 442), "images/sprites/close/un/un_2_sport.png",
		(199, 205), "images/sprites/close/un/un_2_sad.png",
	))
	image un sad swim close = _sr(im.Composite((588, 950),
		(  0,   0), "images/sprites/close/un/un_2_body.png",
		(112, 421), "images/sprites/close/un/un_2_swim.png",
		(199, 205), "images/sprites/close/un/un_2_sad.png",
	))
	image un scared dress close = _sr(im.Composite((588, 950),
		(  0,   0), "images/sprites/close/un/un_2_body.png",
		(128, 405), "images/sprites/close/un/un_2_dress.png",
		(197, 196), "images/sprites/close/un/un_2_scared.png",
	))
	image un scared pioneer close = _sr(im.Composite((588, 950),
		(  0,   0), "images/sprites/close/un/un_2_body.png",
		( 85, 391), "images/sprites/close/un/un_2_pioneer.png",
		(197, 196), "images/sprites/close/un/un_2_scared.png",
	))
	image un scared sport close = _sr(im.Composite((588, 950),
		(  0,   0), "images/sprites/close/un/un_2_body.png",
		( 97, 442), "images/sprites/close/un/un_2_sport.png",
		(197, 196), "images/sprites/close/un/un_2_scared.png",
	))
	image un scared swim close = _sr(im.Composite((588, 950),
		(  0,   0), "images/sprites/close/un/un_2_body.png",
		(112, 421), "images/sprites/close/un/un_2_swim.png",
		(197, 196), "images/sprites/close/un/un_2_scared.png",
	))
	image un serious dress close = _sr(im.Composite((571, 979),
		(  0,   0), "images/sprites/close/un/un_3_body.png",
		( 86, 442), "images/sprites/close/un/un_3_dress.png",
		(175, 237), "images/sprites/close/un/un_3_serious.png",
	))
	image un serious pioneer close = _sr(im.Composite((571, 979),
		(  0,   0), "images/sprites/close/un/un_3_body.png",
		( 35, 416), "images/sprites/close/un/un_3_pioneer.png",
		(175, 237), "images/sprites/close/un/un_3_serious.png",
	))
	image un serious sport close = _sr(im.Composite((705, 1018),
		(134,  39), "images/sprites/close/un/un_3_body.png",
		(  0,   0), "images/sprites/close/un/un_3_sport.png",
		(309, 276), "images/sprites/close/un/un_3_serious.png",
	))
	image un shocked dress close = _sr(im.Composite((588, 950),
		(  0,   0), "images/sprites/close/un/un_2_body.png",
		(128, 405), "images/sprites/close/un/un_2_dress.png",
		(198, 197), "images/sprites/close/un/un_2_shocked.png",
	))
	image un shocked pioneer close = _sr(im.Composite((588, 950),
		(  0,   0), "images/sprites/close/un/un_2_body.png",
		( 85, 391), "images/sprites/close/un/un_2_pioneer.png",
		(198, 197), "images/sprites/close/un/un_2_shocked.png",
	))
	image un shocked sport close = _sr(im.Composite((588, 950),
		(  0,   0), "images/sprites/close/un/un_2_body.png",
		( 97, 442), "images/sprites/close/un/un_2_sport.png",
		(198, 197), "images/sprites/close/un/un_2_shocked.png",
	))
	image un shocked swim close = _sr(im.Composite((588, 950),
		(  0,   0), "images/sprites/close/un/un_2_body.png",
		(112, 421), "images/sprites/close/un/un_2_swim.png",
		(198, 197), "images/sprites/close/un/un_2_shocked.png",
	))
	image un shy dress close = _sr(im.Composite((483, 981),
		(  0,   0), "images/sprites/close/un/un_1_body.png",
		(113, 432), "images/sprites/close/un/un_1_dress.png",
		(186, 245), "images/sprites/close/un/un_1_shy.png",
	))
	image un shy pioneer close = _sr(im.Composite((483, 981),
		(  0,   0), "images/sprites/close/un/un_1_body.png",
		( 39, 409), "images/sprites/close/un/un_1_pioneer.png",
		(186, 245), "images/sprites/close/un/un_1_shy.png",
	))
	image un shy sport close = _sr(im.Composite((483, 981),
		(  0,   0), "images/sprites/close/un/un_1_body.png",
		( 43, 454), "images/sprites/close/un/un_1_sport.png",
		(186, 245), "images/sprites/close/un/un_1_shy.png",
	))
	image un shy swim close = _sr(im.Composite((483, 981),
		(  0,   0), "images/sprites/close/un/un_1_body.png",
		( 82, 444), "images/sprites/close/un/un_1_swim.png",
		(186, 245), "images/sprites/close/un/un_1_shy.png",
	))
	image un smile dress close = _sr(im.Composite((483, 981),
		(  0,   0), "images/sprites/close/un/un_1_body.png",
		(113, 432), "images/sprites/close/un/un_1_dress.png",
		(209, 247), "images/sprites/close/un/un_1_smile.png",
	))
	image un smile pioneer close = _sr(im.Composite((483, 981),
		(  0,   0), "images/sprites/close/un/un_1_body.png",
		( 39, 409), "images/sprites/close/un/un_1_pioneer.png",
		(209, 247), "images/sprites/close/un/un_1_smile.png",
	))
	image un smile sport close = _sr(im.Composite((483, 981),
		(  0,   0), "images/sprites/close/un/un_1_body.png",
		( 43, 454), "images/sprites/close/un/un_1_sport.png",
		(209, 247), "images/sprites/close/un/un_1_smile.png",
	))
	image un smile swim close = _sr(im.Composite((483, 981),
		(  0,   0), "images/sprites/close/un/un_1_body.png",
		( 82, 444), "images/sprites/close/un/un_1_swim.png",
		(209, 247), "images/sprites/close/un/un_1_smile.png",
	))
	image un smile2 dress close = _sr(im.Composite((483, 981),
		(  0,   0), "images/sprites/close/un/un_1_body.png",
		(113, 432), "images/sprites/close/un/un_1_dress.png",
		(209, 247), "images/sprites/close/un/un_1_smile2.png",
	))
	image un smile2 pioneer close = _sr(im.Composite((483, 981),
		(  0,   0), "images/sprites/close/un/un_1_body.png",
		( 39, 409), "images/sprites/close/un/un_1_pioneer.png",
		(209, 247), "images/sprites/close/un/un_1_smile2.png",
	))
	image un smile2 sport close = _sr(im.Composite((483, 981),
		(  0,   0), "images/sprites/close/un/un_1_body.png",
		( 43, 454), "images/sprites/close/un/un_1_sport.png",
		(209, 247), "images/sprites/close/un/un_1_smile2.png",
	))
	image un smile2 swim close = _sr(im.Composite((483, 981),
		(  0,   0), "images/sprites/close/un/un_1_body.png",
		( 82, 444), "images/sprites/close/un/un_1_swim.png",
		(209, 247), "images/sprites/close/un/un_1_smile2.png",
	))
	image un smile3 dress close = _sr(im.Composite((571, 979),
		(  0,   0), "images/sprites/close/un/un_3_body.png",
		( 86, 442), "images/sprites/close/un/un_3_dress.png",
		(174, 240), "images/sprites/close/un/un_3_smile3.png",
	))
	image un smile3 pioneer close = _sr(im.Composite((571, 979),
		(  0,   0), "images/sprites/close/un/un_3_body.png",
		( 35, 416), "images/sprites/close/un/un_3_pioneer.png",
		(174, 240), "images/sprites/close/un/un_3_smile3.png",
	))
	image un smile3 sport close = _sr(im.Composite((705, 1018),
		(134,  39), "images/sprites/close/un/un_3_body.png",
		(  0,   0), "images/sprites/close/un/un_3_sport.png",
		(308, 279), "images/sprites/close/un/un_3_smile3.png",
	))
	image un surprise dress close = _sr(im.Composite((588, 950),
		(  0,   0), "images/sprites/close/un/un_2_body.png",
		(128, 405), "images/sprites/close/un/un_2_dress.png",
		(182, 202), "images/sprites/close/un/un_2_surprise.png",
	))
	image un surprise pioneer close = _sr(im.Composite((588, 950),
		(  0,   0), "images/sprites/close/un/un_2_body.png",
		( 85, 391), "images/sprites/close/un/un_2_pioneer.png",
		(182, 202), "images/sprites/close/un/un_2_surprise.png",
	))
	image un surprise sport close = _sr(im.Composite((588, 950),
		(  0,   0), "images/sprites/close/un/un_2_body.png",
		( 97, 442), "images/sprites/close/un/un_2_sport.png",
		(182, 202), "images/sprites/close/un/un_2_surprise.png",
	))
	image un surprise swim close = _sr(im.Composite((588, 950),
		(  0,   0), "images/sprites/close/un/un_2_body.png",
		(112, 421), "images/sprites/close/un/un_2_swim.png",
		(182, 202), "images/sprites/close/un/un_2_surprise.png",
	))
	
	image un angry dress = _sr(im.Composite((386, 975),
		(  0,   0), "images/sprites/normal/un/un_1_body.png",
		( 23, 346), "images/sprites/normal/un/un_1_dress.png",
		(168, 191), "images/sprites/normal/un/un_1_angry.png",
	))
	image un angry pioneer = _sr(im.Composite((386, 975),
		(  0,   0), "images/sprites/normal/un/un_1_body.png",
		(  4, 328), "images/sprites/normal/un/un_1_pioneer.png",
		(168, 191), "images/sprites/normal/un/un_1_angry.png",
	))
	image un angry sport = _sr(im.Composite((386, 975),
		(  0,   0), "images/sprites/normal/un/un_1_body.png",
		( 34, 363), "images/sprites/normal/un/un_1_sport.png",
		(168, 191), "images/sprites/normal/un/un_1_angry.png",
	))
	image un angry swim = _sr(im.Composite((386, 975),
		(  0,   0), "images/sprites/normal/un/un_1_body.png",
		( 35, 355), "images/sprites/normal/un/un_1_swim.png",
		(168, 191), "images/sprites/normal/un/un_1_angry.png",
	))
	image un angry2 dress = _sr(im.Composite((457, 973),
		(  0,   0), "images/sprites/normal/un/un_3_body.png",
		( 27, 353), "images/sprites/normal/un/un_3_dress.png",
		(134, 191), "images/sprites/normal/un/un_3_angry2.png",
	))
	image un angry2 pioneer = _sr(im.Composite((457, 973),
		(  0,   0), "images/sprites/normal/un/un_3_body.png",
		(  0, 333), "images/sprites/normal/un/un_3_pioneer.png",
		(134, 191), "images/sprites/normal/un/un_3_angry2.png",
	))
	image un angry2 sport = _sr(im.Composite((564, 1005),
		(107,  32), "images/sprites/normal/un/un_3_body.png",
		(  0,   0), "images/sprites/normal/un/un_3_sport.png",
		(241, 223), "images/sprites/normal/un/un_3_angry2.png",
	))
	image un cry dress = _sr(im.Composite((471, 950),
		(  0,   0), "images/sprites/normal/un/un_2_body.png",
		( 60, 324), "images/sprites/normal/un/un_2_dress.png",
		(147, 165), "images/sprites/normal/un/un_2_cry.png",
	))
	image un cry pioneer = _sr(im.Composite((471, 950),
		(  0,   0), "images/sprites/normal/un/un_2_body.png",
		( 43, 313), "images/sprites/normal/un/un_2_pioneer.png",
		(147, 165), "images/sprites/normal/un/un_2_cry.png",
	))
	image un cry sport = _sr(im.Composite((471, 950),
		(  0,   0), "images/sprites/normal/un/un_2_body.png",
		( 78, 353), "images/sprites/normal/un/un_2_sport.png",
		(147, 165), "images/sprites/normal/un/un_2_cry.png",
	))
	image un cry swim = _sr(im.Composite((471, 950),
		(  0,   0), "images/sprites/normal/un/un_2_body.png",
		( 73, 337), "images/sprites/normal/un/un_2_swim.png",
		(147, 165), "images/sprites/normal/un/un_2_cry.png",
	))
	image un cry_smile dress = _sr(im.Composite((471, 950),
		(  0,   0), "images/sprites/normal/un/un_2_body.png",
		( 60, 324), "images/sprites/normal/un/un_2_dress.png",
		(159, 165), "images/sprites/normal/un/un_2_cry_smile.png",
	))
	image un cry_smile pioneer = _sr(im.Composite((471, 950),
		(  0,   0), "images/sprites/normal/un/un_2_body.png",
		( 43, 313), "images/sprites/normal/un/un_2_pioneer.png",
		(159, 165), "images/sprites/normal/un/un_2_cry_smile.png",
	))
	image un cry_smile sport = _sr(im.Composite((471, 950),
		(  0,   0), "images/sprites/normal/un/un_2_body.png",
		( 78, 353), "images/sprites/normal/un/un_2_sport.png",
		(159, 165), "images/sprites/normal/un/un_2_cry_smile.png",
	))
	image un cry_smile swim = _sr(im.Composite((471, 950),
		(  0,   0), "images/sprites/normal/un/un_2_body.png",
		( 73, 337), "images/sprites/normal/un/un_2_swim.png",
		(159, 165), "images/sprites/normal/un/un_2_cry_smile.png",
	))
	image un evil_smile dress = _sr(im.Composite((386, 975),
		(  0,   0), "images/sprites/normal/un/un_1_body.png",
		( 23, 346), "images/sprites/normal/un/un_1_dress.png",
		(168, 191), "images/sprites/normal/un/un_1_evil_smile.png",
	))
	image un evil_smile pioneer = _sr(im.Composite((386, 975),
		(  0,   0), "images/sprites/normal/un/un_1_body.png",
		(  4, 328), "images/sprites/normal/un/un_1_pioneer.png",
		(168, 191), "images/sprites/normal/un/un_1_evil_smile.png",
	))
	image un evil_smile sport = _sr(im.Composite((386, 975),
		(  0,   0), "images/sprites/normal/un/un_1_body.png",
		( 34, 363), "images/sprites/normal/un/un_1_sport.png",
		(168, 191), "images/sprites/normal/un/un_1_evil_smile.png",
	))
	image un evil_smile swim = _sr(im.Composite((386, 975),
		(  0,   0), "images/sprites/normal/un/un_1_body.png",
		( 35, 355), "images/sprites/normal/un/un_1_swim.png",
		(168, 191), "images/sprites/normal/un/un_1_evil_smile.png",
	))
	image un grin dress = _sr(im.Composite((457, 973),
		(  0,   0), "images/sprites/normal/un/un_3_body.png",
		( 27, 353), "images/sprites/normal/un/un_3_dress.png",
		(138, 197), "images/sprites/normal/un/un_3_grin.png",
	))
	image un grin pioneer = _sr(im.Composite((457, 973),
		(  0,   0), "images/sprites/normal/un/un_3_body.png",
		(  0, 333), "images/sprites/normal/un/un_3_pioneer.png",
		(138, 197), "images/sprites/normal/un/un_3_grin.png",
	))
	image un grin sport = _sr(im.Composite((564, 1005),
		(107,  32), "images/sprites/normal/un/un_3_body.png",
		(  0,   0), "images/sprites/normal/un/un_3_sport.png",
		(245, 229), "images/sprites/normal/un/un_3_grin.png",
	))
	image un laugh dress = _sr(im.Composite((457, 973),
		(  0,   0), "images/sprites/normal/un/un_3_body.png",
		( 27, 353), "images/sprites/normal/un/un_3_dress.png",
		(122, 196), "images/sprites/normal/un/un_3_laugh.png",
	))
	image un laugh pioneer = _sr(im.Composite((457, 973),
		(  0,   0), "images/sprites/normal/un/un_3_body.png",
		(  0, 333), "images/sprites/normal/un/un_3_pioneer.png",
		(122, 196), "images/sprites/normal/un/un_3_laugh.png",
	))
	image un laugh sport = _sr(im.Composite((564, 1005),
		(107,  32), "images/sprites/normal/un/un_3_body.png",
		(  0,   0), "images/sprites/normal/un/un_3_sport.png",
		(229, 228), "images/sprites/normal/un/un_3_laugh.png",
	))
	image un normal dress = _sr(im.Composite((386, 975),
		(  0,   0), "images/sprites/normal/un/un_1_body.png",
		( 23, 346), "images/sprites/normal/un/un_1_dress.png",
		(170, 193), "images/sprites/normal/un/un_1_normal.png",
	))
	image un normal pioneer = _sr(im.Composite((386, 975),
		(  0,   0), "images/sprites/normal/un/un_1_body.png",
		(  4, 328), "images/sprites/normal/un/un_1_pioneer.png",
		(170, 193), "images/sprites/normal/un/un_1_normal.png",
	))
	image un normal sport = _sr(im.Composite((386, 975),
		(  0,   0), "images/sprites/normal/un/un_1_body.png",
		( 34, 363), "images/sprites/normal/un/un_1_sport.png",
		(170, 193), "images/sprites/normal/un/un_1_normal.png",
	))
	image un normal swim = _sr(im.Composite((386, 975),
		(  0,   0), "images/sprites/normal/un/un_1_body.png",
		( 35, 355), "images/sprites/normal/un/un_1_swim.png",
		(170, 193), "images/sprites/normal/un/un_1_normal.png",
	))
	image un rage dress = _sr(im.Composite((457, 973),
		(  0,   0), "images/sprites/normal/un/un_3_body.png",
		( 27, 353), "images/sprites/normal/un/un_3_dress.png",
		(136, 193), "images/sprites/normal/un/un_3_rage.png",
	))
	image un rage pioneer = _sr(im.Composite((457, 973),
		(  0,   0), "images/sprites/normal/un/un_3_body.png",
		(  0, 333), "images/sprites/normal/un/un_3_pioneer.png",
		(136, 193), "images/sprites/normal/un/un_3_rage.png",
	))
	image un rage sport = _sr(im.Composite((564, 1005),
		(107,  32), "images/sprites/normal/un/un_3_body.png",
		(  0,   0), "images/sprites/normal/un/un_3_sport.png",
		(243, 225), "images/sprites/normal/un/un_3_rage.png",
	))
	image un sad dress = _sr(im.Composite((471, 950),
		(  0,   0), "images/sprites/normal/un/un_2_body.png",
		( 60, 324), "images/sprites/normal/un/un_2_dress.png",
		(159, 163), "images/sprites/normal/un/un_2_sad.png",
	))
	image un sad pioneer = _sr(im.Composite((471, 950),
		(  0,   0), "images/sprites/normal/un/un_2_body.png",
		( 43, 313), "images/sprites/normal/un/un_2_pioneer.png",
		(159, 163), "images/sprites/normal/un/un_2_sad.png",
	))
	image un sad sport = _sr(im.Composite((471, 950),
		(  0,   0), "images/sprites/normal/un/un_2_body.png",
		( 78, 353), "images/sprites/normal/un/un_2_sport.png",
		(159, 163), "images/sprites/normal/un/un_2_sad.png",
	))
	image un sad swim = _sr(im.Composite((471, 950),
		(  0,   0), "images/sprites/normal/un/un_2_body.png",
		( 73, 337), "images/sprites/normal/un/un_2_swim.png",
		(159, 163), "images/sprites/normal/un/un_2_sad.png",
	))
	image un scared dress = _sr(im.Composite((471, 950),
		(  0,   0), "images/sprites/normal/un/un_2_body.png",
		( 60, 324), "images/sprites/normal/un/un_2_dress.png",
		(158, 157), "images/sprites/normal/un/un_2_scared.png",
	))
	image un scared pioneer = _sr(im.Composite((471, 950),
		(  0,   0), "images/sprites/normal/un/un_2_body.png",
		( 43, 313), "images/sprites/normal/un/un_2_pioneer.png",
		(158, 157), "images/sprites/normal/un/un_2_scared.png",
	))
	image un scared sport = _sr(im.Composite((471, 950),
		(  0,   0), "images/sprites/normal/un/un_2_body.png",
		( 78, 353), "images/sprites/normal/un/un_2_sport.png",
		(158, 157), "images/sprites/normal/un/un_2_scared.png",
	))
	image un scared swim = _sr(im.Composite((471, 950),
		(  0,   0), "images/sprites/normal/un/un_2_body.png",
		( 73, 337), "images/sprites/normal/un/un_2_swim.png",
		(158, 157), "images/sprites/normal/un/un_2_scared.png",
	))
	image un serious dress = _sr(im.Composite((457, 973),
		(  0,   0), "images/sprites/normal/un/un_3_body.png",
		( 27, 353), "images/sprites/normal/un/un_3_dress.png",
		(140, 189), "images/sprites/normal/un/un_3_serious.png",
	))
	image un serious pioneer = _sr(im.Composite((457, 973),
		(  0,   0), "images/sprites/normal/un/un_3_body.png",
		(  0, 333), "images/sprites/normal/un/un_3_pioneer.png",
		(140, 189), "images/sprites/normal/un/un_3_serious.png",
	))
	image un serious sport = _sr(im.Composite((564, 1005),
		(107,  32), "images/sprites/normal/un/un_3_body.png",
		(  0,   0), "images/sprites/normal/un/un_3_sport.png",
		(247, 221), "images/sprites/normal/un/un_3_serious.png",
	))
	image un shocked dress = _sr(im.Composite((471, 950),
		(  0,   0), "images/sprites/normal/un/un_2_body.png",
		( 60, 324), "images/sprites/normal/un/un_2_dress.png",
		(159, 157), "images/sprites/normal/un/un_2_shocked.png",
	))
	image un shocked pioneer = _sr(im.Composite((471, 950),
		(  0,   0), "images/sprites/normal/un/un_2_body.png",
		( 43, 313), "images/sprites/normal/un/un_2_pioneer.png",
		(159, 157), "images/sprites/normal/un/un_2_shocked.png",
	))
	image un shocked sport = _sr(im.Composite((471, 950),
		(  0,   0), "images/sprites/normal/un/un_2_body.png",
		( 78, 353), "images/sprites/normal/un/un_2_sport.png",
		(159, 157), "images/sprites/normal/un/un_2_shocked.png",
	))
	image un shocked swim = _sr(im.Composite((471, 950),
		(  0,   0), "images/sprites/normal/un/un_2_body.png",
		( 73, 337), "images/sprites/normal/un/un_2_swim.png",
		(159, 157), "images/sprites/normal/un/un_2_shocked.png",
	))
	image un shy dress = _sr(im.Composite((386, 975),
		(  0,   0), "images/sprites/normal/un/un_1_body.png",
		( 23, 346), "images/sprites/normal/un/un_1_dress.png",
		(149, 196), "images/sprites/normal/un/un_1_shy.png",
	))
	image un shy pioneer = _sr(im.Composite((386, 975),
		(  0,   0), "images/sprites/normal/un/un_1_body.png",
		(  4, 328), "images/sprites/normal/un/un_1_pioneer.png",
		(149, 196), "images/sprites/normal/un/un_1_shy.png",
	))
	image un shy sport = _sr(im.Composite((386, 975),
		(  0,   0), "images/sprites/normal/un/un_1_body.png",
		( 34, 363), "images/sprites/normal/un/un_1_sport.png",
		(149, 196), "images/sprites/normal/un/un_1_shy.png",
	))
	image un shy swim = _sr(im.Composite((386, 975),
		(  0,   0), "images/sprites/normal/un/un_1_body.png",
		( 35, 355), "images/sprites/normal/un/un_1_swim.png",
		(149, 196), "images/sprites/normal/un/un_1_shy.png",
	))
	image un smile dress = _sr(im.Composite((386, 975),
		(  0,   0), "images/sprites/normal/un/un_1_body.png",
		( 23, 346), "images/sprites/normal/un/un_1_dress.png",
		(167, 198), "images/sprites/normal/un/un_1_smile.png",
	))
	image un smile pioneer = _sr(im.Composite((386, 975),
		(  0,   0), "images/sprites/normal/un/un_1_body.png",
		(  4, 328), "images/sprites/normal/un/un_1_pioneer.png",
		(167, 198), "images/sprites/normal/un/un_1_smile.png",
	))
	image un smile sport = _sr(im.Composite((386, 975),
		(  0,   0), "images/sprites/normal/un/un_1_body.png",
		( 34, 363), "images/sprites/normal/un/un_1_sport.png",
		(167, 198), "images/sprites/normal/un/un_1_smile.png",
	))
	image un smile swim = _sr(im.Composite((386, 975),
		(  0,   0), "images/sprites/normal/un/un_1_body.png",
		( 35, 355), "images/sprites/normal/un/un_1_swim.png",
		(167, 198), "images/sprites/normal/un/un_1_smile.png",
	))
	image un smile2 dress = _sr(im.Composite((386, 975),
		(  0,   0), "images/sprites/normal/un/un_1_body.png",
		( 23, 346), "images/sprites/normal/un/un_1_dress.png",
		(167, 198), "images/sprites/normal/un/un_1_smile2.png",
	))
	image un smile2 pioneer = _sr(im.Composite((386, 975),
		(  0,   0), "images/sprites/normal/un/un_1_body.png",
		(  4, 328), "images/sprites/normal/un/un_1_pioneer.png",
		(167, 198), "images/sprites/normal/un/un_1_smile2.png",
	))
	image un smile2 sport = _sr(im.Composite((386, 975),
		(  0,   0), "images/sprites/normal/un/un_1_body.png",
		( 34, 363), "images/sprites/normal/un/un_1_sport.png",
		(167, 198), "images/sprites/normal/un/un_1_smile2.png",
	))
	image un smile2 swim = _sr(im.Composite((386, 975),
		(  0,   0), "images/sprites/normal/un/un_1_body.png",
		( 35, 355), "images/sprites/normal/un/un_1_swim.png",
		(167, 198), "images/sprites/normal/un/un_1_smile2.png",
	))
	image un smile3 dress = _sr(im.Composite((457, 973),
		(  0,   0), "images/sprites/normal/un/un_3_body.png",
		( 27, 353), "images/sprites/normal/un/un_3_dress.png",
		(139, 192), "images/sprites/normal/un/un_3_smile3.png",
	))
	image un smile3 pioneer = _sr(im.Composite((457, 973),
		(  0,   0), "images/sprites/normal/un/un_3_body.png",
		(  0, 333), "images/sprites/normal/un/un_3_pioneer.png",
		(139, 192), "images/sprites/normal/un/un_3_smile3.png",
	))
	image un smile3 sport = _sr(im.Composite((564, 1005),
		(107,  32), "images/sprites/normal/un/un_3_body.png",
		(  0,   0), "images/sprites/normal/un/un_3_sport.png",
		(246, 224), "images/sprites/normal/un/un_3_smile3.png",
	))
	image un surprise dress = _sr(im.Composite((471, 950),
		(  0,   0), "images/sprites/normal/un/un_2_body.png",
		( 60, 324), "images/sprites/normal/un/un_2_dress.png",
		(146, 162), "images/sprites/normal/un/un_2_surprise.png",
	))
	image un surprise pioneer = _sr(im.Composite((471, 950),
		(  0,   0), "images/sprites/normal/un/un_2_body.png",
		( 43, 313), "images/sprites/normal/un/un_2_pioneer.png",
		(146, 162), "images/sprites/normal/un/un_2_surprise.png",
	))
	image un surprise sport = _sr(im.Composite((471, 950),
		(  0,   0), "images/sprites/normal/un/un_2_body.png",
		( 78, 353), "images/sprites/normal/un/un_2_sport.png",
		(146, 162), "images/sprites/normal/un/un_2_surprise.png",
	))
	image un surprise swim = _sr(im.Composite((471, 950),
		(  0,   0), "images/sprites/normal/un/un_2_body.png",
		( 73, 337), "images/sprites/normal/un/un_2_swim.png",
		(146, 162), "images/sprites/normal/un/un_2_surprise.png",
	))
	
	image un angry dress far = _sr(im.Composite((319, 889),
		( 29,   0), "images/sprites/far/un/un_1_body.png",
		(  0, 259), "images/sprites/far/un/un_1_dress.png",
		(155, 143), "images/sprites/far/un/un_1_angry.png",
	))
	image un angry pioneer far = _sr(im.Composite((290, 889),
		(  0,   0), "images/sprites/far/un/un_1_body.png",
		(  3, 246), "images/sprites/far/un/un_1_pioneer.png",
		(126, 143), "images/sprites/far/un/un_1_angry.png",
	))
	image un angry sport far = _sr(im.Composite((290, 889),
		(  0,   0), "images/sprites/far/un/un_1_body.png",
		( 26, 272), "images/sprites/far/un/un_1_sport.png",
		(126, 143), "images/sprites/far/un/un_1_angry.png",
	))
	image un angry swim far = _sr(im.Composite((290, 889),
		(  0,   0), "images/sprites/far/un/un_1_body.png",
		( 26, 267), "images/sprites/far/un/un_1_swim.png",
		(126, 143), "images/sprites/far/un/un_1_angry.png",
	))
	image un angry2 dress far = _sr(im.Composite((368, 887),
		( 25,   0), "images/sprites/far/un/un_3_body.png",
		(  0, 265), "images/sprites/far/un/un_3_dress.png",
		(125, 143), "images/sprites/far/un/un_3_angry2.png",
	))
	image un angry2 pioneer far = _sr(im.Composite((343, 887),
		(  0,   0), "images/sprites/far/un/un_3_body.png",
		(  0, 249), "images/sprites/far/un/un_3_pioneer.png",
		(100, 143), "images/sprites/far/un/un_3_angry2.png",
	))
	image un angry2 sport far = _sr(im.Composite((423, 911),
		( 80,  24), "images/sprites/far/un/un_3_body.png",
		(  0,   0), "images/sprites/far/un/un_3_sport.png",
		(180, 167), "images/sprites/far/un/un_3_angry2.png",
	))
	image un cry dress far = _sr(im.Composite((353, 870),
		(  0,   0), "images/sprites/far/un/un_2_body.png",
		(  0, 243), "images/sprites/far/un/un_2_dress.png",
		(109, 124), "images/sprites/far/un/un_2_cry.png",
	))
	image un cry pioneer far = _sr(im.Composite((353, 870),
		(  0,   0), "images/sprites/far/un/un_2_body.png",
		( 32, 234), "images/sprites/far/un/un_2_pioneer.png",
		(109, 124), "images/sprites/far/un/un_2_cry.png",
	))
	image un cry sport far = _sr(im.Composite((353, 870),
		(  0,   0), "images/sprites/far/un/un_2_body.png",
		( 58, 265), "images/sprites/far/un/un_2_sport.png",
		(109, 124), "images/sprites/far/un/un_2_cry.png",
	))
	image un cry swim far = _sr(im.Composite((353, 870),
		(  0,   0), "images/sprites/far/un/un_2_body.png",
		( 54, 253), "images/sprites/far/un/un_2_swim.png",
		(109, 124), "images/sprites/far/un/un_2_cry.png",
	))
	image un cry_smile dress far = _sr(im.Composite((353, 870),
		(  0,   0), "images/sprites/far/un/un_2_body.png",
		(  0, 243), "images/sprites/far/un/un_2_dress.png",
		(119, 124), "images/sprites/far/un/un_2_cry_smile.png",
	))
	image un cry_smile pioneer far = _sr(im.Composite((353, 870),
		(  0,   0), "images/sprites/far/un/un_2_body.png",
		( 32, 234), "images/sprites/far/un/un_2_pioneer.png",
		(119, 124), "images/sprites/far/un/un_2_cry_smile.png",
	))
	image un cry_smile sport far = _sr(im.Composite((353, 870),
		(  0,   0), "images/sprites/far/un/un_2_body.png",
		( 58, 265), "images/sprites/far/un/un_2_sport.png",
		(119, 124), "images/sprites/far/un/un_2_cry_smile.png",
	))
	image un cry_smile swim far = _sr(im.Composite((353, 870),
		(  0,   0), "images/sprites/far/un/un_2_body.png",
		( 54, 253), "images/sprites/far/un/un_2_swim.png",
		(119, 124), "images/sprites/far/un/un_2_cry_smile.png",
	))
	image un evil_smile dress far = _sr(im.Composite((319, 889),
		( 29,   0), "images/sprites/far/un/un_1_body.png",
		(  0, 259), "images/sprites/far/un/un_1_dress.png",
		(155, 143), "images/sprites/far/un/un_1_evil_smile.png",
	))
	image un evil_smile pioneer far = _sr(im.Composite((290, 889),
		(  0,   0), "images/sprites/far/un/un_1_body.png",
		(  3, 246), "images/sprites/far/un/un_1_pioneer.png",
		(126, 143), "images/sprites/far/un/un_1_evil_smile.png",
	))
	image un evil_smile sport far = _sr(im.Composite((290, 889),
		(  0,   0), "images/sprites/far/un/un_1_body.png",
		( 26, 272), "images/sprites/far/un/un_1_sport.png",
		(126, 143), "images/sprites/far/un/un_1_evil_smile.png",
	))
	image un evil_smile swim far = _sr(im.Composite((290, 889),
		(  0,   0), "images/sprites/far/un/un_1_body.png",
		( 26, 267), "images/sprites/far/un/un_1_swim.png",
		(126, 143), "images/sprites/far/un/un_1_evil_smile.png",
	))
	image un grin dress far = _sr(im.Composite((368, 887),
		( 25,   0), "images/sprites/far/un/un_3_body.png",
		(  0, 265), "images/sprites/far/un/un_3_dress.png",
		(128, 147), "images/sprites/far/un/un_3_grin.png",
	))
	image un grin pioneer far = _sr(im.Composite((343, 887),
		(  0,   0), "images/sprites/far/un/un_3_body.png",
		(  0, 249), "images/sprites/far/un/un_3_pioneer.png",
		(103, 147), "images/sprites/far/un/un_3_grin.png",
	))
	image un grin sport far = _sr(im.Composite((423, 911),
		( 80,  24), "images/sprites/far/un/un_3_body.png",
		(  0,   0), "images/sprites/far/un/un_3_sport.png",
		(183, 171), "images/sprites/far/un/un_3_grin.png",
	))
	image un laugh dress far = _sr(im.Composite((368, 887),
		( 25,   0), "images/sprites/far/un/un_3_body.png",
		(  0, 265), "images/sprites/far/un/un_3_dress.png",
		(117, 147), "images/sprites/far/un/un_3_laugh.png",
	))
	image un laugh pioneer far = _sr(im.Composite((343, 887),
		(  0,   0), "images/sprites/far/un/un_3_body.png",
		(  0, 249), "images/sprites/far/un/un_3_pioneer.png",
		( 92, 147), "images/sprites/far/un/un_3_laugh.png",
	))
	image un laugh sport far = _sr(im.Composite((423, 911),
		( 80,  24), "images/sprites/far/un/un_3_body.png",
		(  0,   0), "images/sprites/far/un/un_3_sport.png",
		(172, 171), "images/sprites/far/un/un_3_laugh.png",
	))
	image un normal dress far = _sr(im.Composite((319, 889),
		( 29,   0), "images/sprites/far/un/un_1_body.png",
		(  0, 259), "images/sprites/far/un/un_1_dress.png",
		(157, 145), "images/sprites/far/un/un_1_normal.png",
	))
	image un normal pioneer far = _sr(im.Composite((290, 889),
		(  0,   0), "images/sprites/far/un/un_1_body.png",
		(  3, 246), "images/sprites/far/un/un_1_pioneer.png",
		(128, 145), "images/sprites/far/un/un_1_normal.png",
	))
	image un normal sport far = _sr(im.Composite((290, 889),
		(  0,   0), "images/sprites/far/un/un_1_body.png",
		( 26, 272), "images/sprites/far/un/un_1_sport.png",
		(128, 145), "images/sprites/far/un/un_1_normal.png",
	))
	image un normal swim far = _sr(im.Composite((290, 889),
		(  0,   0), "images/sprites/far/un/un_1_body.png",
		( 26, 267), "images/sprites/far/un/un_1_swim.png",
		(128, 145), "images/sprites/far/un/un_1_normal.png",
	))
	image un rage dress far = _sr(im.Composite((368, 887),
		( 25,   0), "images/sprites/far/un/un_3_body.png",
		(  0, 265), "images/sprites/far/un/un_3_dress.png",
		(127, 144), "images/sprites/far/un/un_3_rage.png",
	))
	image un rage pioneer far = _sr(im.Composite((343, 887),
		(  0,   0), "images/sprites/far/un/un_3_body.png",
		(  0, 249), "images/sprites/far/un/un_3_pioneer.png",
		(102, 144), "images/sprites/far/un/un_3_rage.png",
	))
	image un rage sport far = _sr(im.Composite((423, 911),
		( 80,  24), "images/sprites/far/un/un_3_body.png",
		(  0,   0), "images/sprites/far/un/un_3_sport.png",
		(182, 168), "images/sprites/far/un/un_3_rage.png",
	))
	image un sad dress far = _sr(im.Composite((353, 870),
		(  0,   0), "images/sprites/far/un/un_2_body.png",
		(  0, 243), "images/sprites/far/un/un_2_dress.png",
		(119, 123), "images/sprites/far/un/un_2_sad.png",
	))
	image un sad pioneer far = _sr(im.Composite((353, 870),
		(  0,   0), "images/sprites/far/un/un_2_body.png",
		( 32, 234), "images/sprites/far/un/un_2_pioneer.png",
		(119, 123), "images/sprites/far/un/un_2_sad.png",
	))
	image un sad sport far = _sr(im.Composite((353, 870),
		(  0,   0), "images/sprites/far/un/un_2_body.png",
		( 58, 265), "images/sprites/far/un/un_2_sport.png",
		(119, 123), "images/sprites/far/un/un_2_sad.png",
	))
	image un sad swim far = _sr(im.Composite((353, 870),
		(  0,   0), "images/sprites/far/un/un_2_body.png",
		( 54, 253), "images/sprites/far/un/un_2_swim.png",
		(119, 123), "images/sprites/far/un/un_2_sad.png",
	))
	image un scared dress far = _sr(im.Composite((353, 870),
		(  0,   0), "images/sprites/far/un/un_2_body.png",
		(  0, 243), "images/sprites/far/un/un_2_dress.png",
		(118, 117), "images/sprites/far/un/un_2_scared.png",
	))
	image un scared pioneer far = _sr(im.Composite((353, 870),
		(  0,   0), "images/sprites/far/un/un_2_body.png",
		( 32, 234), "images/sprites/far/un/un_2_pioneer.png",
		(118, 117), "images/sprites/far/un/un_2_scared.png",
	))
	image un scared sport far = _sr(im.Composite((353, 870),
		(  0,   0), "images/sprites/far/un/un_2_body.png",
		( 58, 265), "images/sprites/far/un/un_2_sport.png",
		(118, 117), "images/sprites/far/un/un_2_scared.png",
	))
	image un scared swim far = _sr(im.Composite((353, 870),
		(  0,   0), "images/sprites/far/un/un_2_body.png",
		( 54, 253), "images/sprites/far/un/un_2_swim.png",
		(118, 117), "images/sprites/far/un/un_2_scared.png",
	))
	image un serious dress far = _sr(im.Composite((368, 887),
		( 25,   0), "images/sprites/far/un/un_3_body.png",
		(  0, 265), "images/sprites/far/un/un_3_dress.png",
		(130, 142), "images/sprites/far/un/un_3_serious.png",
	))
	image un serious pioneer far = _sr(im.Composite((343, 887),
		(  0,   0), "images/sprites/far/un/un_3_body.png",
		(  0, 249), "images/sprites/far/un/un_3_pioneer.png",
		(105, 142), "images/sprites/far/un/un_3_serious.png",
	))
	image un serious sport far = _sr(im.Composite((423, 911),
		( 80,  24), "images/sprites/far/un/un_3_body.png",
		(  0,   0), "images/sprites/far/un/un_3_sport.png",
		(185, 166), "images/sprites/far/un/un_3_serious.png",
	))
	image un shocked dress far = _sr(im.Composite((353, 870),
		(  0,   0), "images/sprites/far/un/un_2_body.png",
		(  0, 243), "images/sprites/far/un/un_2_dress.png",
		(118, 118), "images/sprites/far/un/un_2_shocked.png",
	))
	image un shocked pioneer far = _sr(im.Composite((353, 870),
		(  0,   0), "images/sprites/far/un/un_2_body.png",
		( 32, 234), "images/sprites/far/un/un_2_pioneer.png",
		(118, 118), "images/sprites/far/un/un_2_shocked.png",
	))
	image un shocked sport far = _sr(im.Composite((353, 870),
		(  0,   0), "images/sprites/far/un/un_2_body.png",
		( 58, 265), "images/sprites/far/un/un_2_sport.png",
		(118, 118), "images/sprites/far/un/un_2_shocked.png",
	))
	image un shocked swim far = _sr(im.Composite((353, 870),
		(  0,   0), "images/sprites/far/un/un_2_body.png",
		( 54, 253), "images/sprites/far/un/un_2_swim.png",
		(118, 118), "images/sprites/far/un/un_2_shocked.png",
	))
	image un shy dress far = _sr(im.Composite((319, 889),
		( 29,   0), "images/sprites/far/un/un_1_body.png",
		(  0, 259), "images/sprites/far/un/un_1_dress.png",
		(141, 147), "images/sprites/far/un/un_1_shy.png",
	))
	image un shy pioneer far = _sr(im.Composite((290, 889),
		(  0,   0), "images/sprites/far/un/un_1_body.png",
		(  3, 246), "images/sprites/far/un/un_1_pioneer.png",
		(112, 147), "images/sprites/far/un/un_1_shy.png",
	))
	image un shy sport far = _sr(im.Composite((290, 889),
		(  0,   0), "images/sprites/far/un/un_1_body.png",
		( 26, 272), "images/sprites/far/un/un_1_sport.png",
		(112, 147), "images/sprites/far/un/un_1_shy.png",
	))
	image un shy swim far = _sr(im.Composite((290, 889),
		(  0,   0), "images/sprites/far/un/un_1_body.png",
		( 26, 267), "images/sprites/far/un/un_1_swim.png",
		(112, 147), "images/sprites/far/un/un_1_shy.png",
	))
	image un smile dress far = _sr(im.Composite((319, 889),
		( 29,   0), "images/sprites/far/un/un_1_body.png",
		(  0, 259), "images/sprites/far/un/un_1_dress.png",
		(154, 148), "images/sprites/far/un/un_1_smile.png",
	))
	image un smile pioneer far = _sr(im.Composite((290, 889),
		(  0,   0), "images/sprites/far/un/un_1_body.png",
		(  3, 246), "images/sprites/far/un/un_1_pioneer.png",
		(125, 148), "images/sprites/far/un/un_1_smile.png",
	))
	image un smile sport far = _sr(im.Composite((290, 889),
		(  0,   0), "images/sprites/far/un/un_1_body.png",
		( 26, 272), "images/sprites/far/un/un_1_sport.png",
		(125, 148), "images/sprites/far/un/un_1_smile.png",
	))
	image un smile swim far = _sr(im.Composite((290, 889),
		(  0,   0), "images/sprites/far/un/un_1_body.png",
		( 26, 267), "images/sprites/far/un/un_1_swim.png",
		(125, 148), "images/sprites/far/un/un_1_smile.png",
	))
	image un smile2 dress far = _sr(im.Composite((319, 889),
		( 29,   0), "images/sprites/far/un/un_1_body.png",
		(  0, 259), "images/sprites/far/un/un_1_dress.png",
		(154, 148), "images/sprites/far/un/un_1_smile2.png",
	))
	image un smile2 pioneer far = _sr(im.Composite((290, 889),
		(  0,   0), "images/sprites/far/un/un_1_body.png",
		(  3, 246), "images/sprites/far/un/un_1_pioneer.png",
		(125, 148), "images/sprites/far/un/un_1_smile2.png",
	))
	image un smile2 sport far = _sr(im.Composite((290, 889),
		(  0,   0), "images/sprites/far/un/un_1_body.png",
		( 26, 272), "images/sprites/far/un/un_1_sport.png",
		(125, 148), "images/sprites/far/un/un_1_smile2.png",
	))
	image un smile2 swim far = _sr(im.Composite((290, 889),
		(  0,   0), "images/sprites/far/un/un_1_body.png",
		( 26, 267), "images/sprites/far/un/un_1_swim.png",
		(125, 148), "images/sprites/far/un/un_1_smile2.png",
	))
	image un smile3 dress far = _sr(im.Composite((368, 887),
		( 25,   0), "images/sprites/far/un/un_3_body.png",
		(  0, 265), "images/sprites/far/un/un_3_dress.png",
		(129, 143), "images/sprites/far/un/un_3_smile3.png",
	))
	image un smile3 pioneer far = _sr(im.Composite((343, 887),
		(  0,   0), "images/sprites/far/un/un_3_body.png",
		(  0, 249), "images/sprites/far/un/un_3_pioneer.png",
		(104, 143), "images/sprites/far/un/un_3_smile3.png",
	))
	image un smile3 sport far = _sr(im.Composite((423, 911),
		( 80,  24), "images/sprites/far/un/un_3_body.png",
		(  0,   0), "images/sprites/far/un/un_3_sport.png",
		(184, 167), "images/sprites/far/un/un_3_smile3.png",
	))
	image un surprise dress far = _sr(im.Composite((353, 870),
		(  0,   0), "images/sprites/far/un/un_2_body.png",
		(  0, 243), "images/sprites/far/un/un_2_dress.png",
		(109, 121), "images/sprites/far/un/un_2_surprise.png",
	))
	image un surprise pioneer far = _sr(im.Composite((353, 870),
		(  0,   0), "images/sprites/far/un/un_2_body.png",
		( 32, 234), "images/sprites/far/un/un_2_pioneer.png",
		(109, 121), "images/sprites/far/un/un_2_surprise.png",
	))
	image un surprise sport far = _sr(im.Composite((353, 870),
		(  0,   0), "images/sprites/far/un/un_2_body.png",
		( 58, 265), "images/sprites/far/un/un_2_sport.png",
		(109, 121), "images/sprites/far/un/un_2_surprise.png",
	))
	image un surprise swim far = _sr(im.Composite((353, 870),
		(  0,   0), "images/sprites/far/un/un_2_body.png",
		( 54, 253), "images/sprites/far/un/un_2_swim.png",
		(109, 121), "images/sprites/far/un/un_2_surprise.png",
	))
	
	image us angry dress close = _sr(im.Composite((738, 591),
		(  0,   0), "images/sprites/close/us/us_2_body.png",
		(219, 262), "images/sprites/close/us/us_2_dress.png",
		(277, 125), "images/sprites/close/us/us_2_angry.png",
	))
	image us angry pioneer close = _sr(im.Composite((738, 591),
		(  0,   0), "images/sprites/close/us/us_2_body.png",
		(145, 307), "images/sprites/close/us/us_2_pioneer.png",
		(277, 125), "images/sprites/close/us/us_2_angry.png",
	))
	image us angry sport close = _sr(im.Composite((738, 591),
		(  0,   0), "images/sprites/close/us/us_2_body.png",
		(154, 330), "images/sprites/close/us/us_2_sport.png",
		(277, 125), "images/sprites/close/us/us_2_angry.png",
	))
	image us angry swim close = _sr(im.Composite((738, 591),
		(  0,   0), "images/sprites/close/us/us_2_body.png",
		(217, 344), "images/sprites/close/us/us_2_swim.png",
		(277, 125), "images/sprites/close/us/us_2_angry.png",
	))
	image us calml dress close = _sr(im.Composite((738, 591),
		(  0,   0), "images/sprites/close/us/us_2_body.png",
		(219, 262), "images/sprites/close/us/us_2_dress.png",
		(280, 132), "images/sprites/close/us/us_2_calml.png",
	))
	image us calml pioneer close = _sr(im.Composite((738, 591),
		(  0,   0), "images/sprites/close/us/us_2_body.png",
		(145, 307), "images/sprites/close/us/us_2_pioneer.png",
		(280, 132), "images/sprites/close/us/us_2_calml.png",
	))
	image us calml sport close = _sr(im.Composite((738, 591),
		(  0,   0), "images/sprites/close/us/us_2_body.png",
		(154, 330), "images/sprites/close/us/us_2_sport.png",
		(280, 132), "images/sprites/close/us/us_2_calml.png",
	))
	image us calml swim close = _sr(im.Composite((738, 591),
		(  0,   0), "images/sprites/close/us/us_2_body.png",
		(217, 344), "images/sprites/close/us/us_2_swim.png",
		(280, 132), "images/sprites/close/us/us_2_calml.png",
	))
	image us cry dress close = _sr(im.Composite((706, 588),
		(  0,   0), "images/sprites/close/us/us_3_body.png",
		(235, 234), "images/sprites/close/us/us_3_dress.png",
		(270, 140), "images/sprites/close/us/us_3_cry.png",
	))
	image us cry pioneer close = _sr(im.Composite((706, 588),
		(  0,   0), "images/sprites/close/us/us_3_body.png",
		(155, 327), "images/sprites/close/us/us_3_pioneer.png",
		(270, 140), "images/sprites/close/us/us_3_cry.png",
	))
	image us cry sport close = _sr(im.Composite((706, 588),
		(  0,   0), "images/sprites/close/us/us_3_body.png",
		(162, 336), "images/sprites/close/us/us_3_sport.png",
		(270, 140), "images/sprites/close/us/us_3_cry.png",
	))
	image us cry swim close = _sr(im.Composite((706, 588),
		(  0,   0), "images/sprites/close/us/us_3_body.png",
		(236, 360), "images/sprites/close/us/us_3_swim.png",
		(270, 140), "images/sprites/close/us/us_3_cry.png",
	))
	image us cry2 dress close = _sr(im.Composite((706, 588),
		(  0,   0), "images/sprites/close/us/us_3_body.png",
		(235, 234), "images/sprites/close/us/us_3_dress.png",
		(272, 140), "images/sprites/close/us/us_3_cry2.png",
	))
	image us cry2 pioneer close = _sr(im.Composite((706, 588),
		(  0,   0), "images/sprites/close/us/us_3_body.png",
		(155, 327), "images/sprites/close/us/us_3_pioneer.png",
		(272, 140), "images/sprites/close/us/us_3_cry2.png",
	))
	image us cry2 sport close = _sr(im.Composite((706, 588),
		(  0,   0), "images/sprites/close/us/us_3_body.png",
		(162, 336), "images/sprites/close/us/us_3_sport.png",
		(272, 140), "images/sprites/close/us/us_3_cry2.png",
	))
	image us cry2 swim close = _sr(im.Composite((706, 588),
		(  0,   0), "images/sprites/close/us/us_3_body.png",
		(236, 360), "images/sprites/close/us/us_3_swim.png",
		(272, 140), "images/sprites/close/us/us_3_cry2.png",
	))
	image us dontlike dress close = _sr(im.Composite((738, 591),
		(  0,   0), "images/sprites/close/us/us_2_body.png",
		(219, 262), "images/sprites/close/us/us_2_dress.png",
		(283, 125), "images/sprites/close/us/us_2_dontlike.png",
	))
	image us dontlike pioneer close = _sr(im.Composite((738, 591),
		(  0,   0), "images/sprites/close/us/us_2_body.png",
		(145, 307), "images/sprites/close/us/us_2_pioneer.png",
		(283, 125), "images/sprites/close/us/us_2_dontlike.png",
	))
	image us dontlike sport close = _sr(im.Composite((738, 591),
		(  0,   0), "images/sprites/close/us/us_2_body.png",
		(154, 330), "images/sprites/close/us/us_2_sport.png",
		(283, 125), "images/sprites/close/us/us_2_dontlike.png",
	))
	image us dontlike swim close = _sr(im.Composite((738, 591),
		(  0,   0), "images/sprites/close/us/us_2_body.png",
		(217, 344), "images/sprites/close/us/us_2_swim.png",
		(283, 125), "images/sprites/close/us/us_2_dontlike.png",
	))
	image us fear dress close = _sr(im.Composite((738, 591),
		(  0,   0), "images/sprites/close/us/us_2_body.png",
		(219, 262), "images/sprites/close/us/us_2_dress.png",
		(280, 112), "images/sprites/close/us/us_2_fear.png",
	))
	image us fear pioneer close = _sr(im.Composite((738, 591),
		(  0,   0), "images/sprites/close/us/us_2_body.png",
		(145, 307), "images/sprites/close/us/us_2_pioneer.png",
		(280, 112), "images/sprites/close/us/us_2_fear.png",
	))
	image us fear sport close = _sr(im.Composite((738, 591),
		(  0,   0), "images/sprites/close/us/us_2_body.png",
		(154, 330), "images/sprites/close/us/us_2_sport.png",
		(280, 112), "images/sprites/close/us/us_2_fear.png",
	))
	image us fear swim close = _sr(im.Composite((738, 591),
		(  0,   0), "images/sprites/close/us/us_2_body.png",
		(217, 344), "images/sprites/close/us/us_2_swim.png",
		(280, 112), "images/sprites/close/us/us_2_fear.png",
	))
	image us grin dress close = _sr(im.Composite((703, 587),
		(  0,   0), "images/sprites/close/us/us_1_body.png",
		(237, 343), "images/sprites/close/us/us_1_dress.png",
		(256, 140), "images/sprites/close/us/us_1_grin.png",
	))
	image us grin pioneer close = _sr(im.Composite((703, 587),
		(  0,   0), "images/sprites/close/us/us_1_body.png",
		(149, 322), "images/sprites/close/us/us_1_pioneer.png",
		(256, 140), "images/sprites/close/us/us_1_grin.png",
	))
	image us grin sport close = _sr(im.Composite((703, 587),
		(  0,   0), "images/sprites/close/us/us_1_body.png",
		(126, 354), "images/sprites/close/us/us_1_sport.png",
		(256, 140), "images/sprites/close/us/us_1_grin.png",
	))
	image us grin swim close = _sr(im.Composite((703, 587),
		(  0,   0), "images/sprites/close/us/us_1_body.png",
		(236, 361), "images/sprites/close/us/us_1_swim.png",
		(256, 140), "images/sprites/close/us/us_1_grin.png",
	))
	image us laugh dress close = _sr(im.Composite((703, 587),
		(  0,   0), "images/sprites/close/us/us_1_body.png",
		(237, 343), "images/sprites/close/us/us_1_dress.png",
		(262, 160), "images/sprites/close/us/us_1_laugh.png",
	))
	image us laugh pioneer close = _sr(im.Composite((703, 587),
		(  0,   0), "images/sprites/close/us/us_1_body.png",
		(149, 322), "images/sprites/close/us/us_1_pioneer.png",
		(262, 160), "images/sprites/close/us/us_1_laugh.png",
	))
	image us laugh sport close = _sr(im.Composite((703, 587),
		(  0,   0), "images/sprites/close/us/us_1_body.png",
		(126, 354), "images/sprites/close/us/us_1_sport.png",
		(262, 160), "images/sprites/close/us/us_1_laugh.png",
	))
	image us laugh swim close = _sr(im.Composite((703, 587),
		(  0,   0), "images/sprites/close/us/us_1_body.png",
		(236, 361), "images/sprites/close/us/us_1_swim.png",
		(262, 160), "images/sprites/close/us/us_1_laugh.png",
	))
	image us laugh2 dress close = _sr(im.Composite((703, 587),
		(  0,   0), "images/sprites/close/us/us_1_body.png",
		(237, 343), "images/sprites/close/us/us_1_dress.png",
		(262, 160), "images/sprites/close/us/us_1_laugh2.png",
	))
	image us laugh2 pioneer close = _sr(im.Composite((703, 587),
		(  0,   0), "images/sprites/close/us/us_1_body.png",
		(149, 322), "images/sprites/close/us/us_1_pioneer.png",
		(262, 160), "images/sprites/close/us/us_1_laugh2.png",
	))
	image us laugh2 sport close = _sr(im.Composite((703, 587),
		(  0,   0), "images/sprites/close/us/us_1_body.png",
		(126, 354), "images/sprites/close/us/us_1_sport.png",
		(262, 160), "images/sprites/close/us/us_1_laugh2.png",
	))
	image us laugh2 swim close = _sr(im.Composite((703, 587),
		(  0,   0), "images/sprites/close/us/us_1_body.png",
		(236, 361), "images/sprites/close/us/us_1_swim.png",
		(262, 160), "images/sprites/close/us/us_1_laugh2.png",
	))
	image us normal dress close = _sr(im.Composite((703, 587),
		(  0,   0), "images/sprites/close/us/us_1_body.png",
		(237, 343), "images/sprites/close/us/us_1_dress.png",
		(263, 150), "images/sprites/close/us/us_1_normal.png",
	))
	image us normal pioneer close = _sr(im.Composite((703, 587),
		(  0,   0), "images/sprites/close/us/us_1_body.png",
		(149, 322), "images/sprites/close/us/us_1_pioneer.png",
		(263, 150), "images/sprites/close/us/us_1_normal.png",
	))
	image us normal sport close = _sr(im.Composite((703, 587),
		(  0,   0), "images/sprites/close/us/us_1_body.png",
		(126, 354), "images/sprites/close/us/us_1_sport.png",
		(263, 150), "images/sprites/close/us/us_1_normal.png",
	))
	image us normal swim close = _sr(im.Composite((703, 587),
		(  0,   0), "images/sprites/close/us/us_1_body.png",
		(236, 361), "images/sprites/close/us/us_1_swim.png",
		(263, 150), "images/sprites/close/us/us_1_normal.png",
	))
	image us sad dress close = _sr(im.Composite((703, 587),
		(  0,   0), "images/sprites/close/us/us_1_body.png",
		(237, 343), "images/sprites/close/us/us_1_dress.png",
		(263, 154), "images/sprites/close/us/us_1_sad.png",
	))
	image us sad pioneer close = _sr(im.Composite((703, 587),
		(  0,   0), "images/sprites/close/us/us_1_body.png",
		(149, 322), "images/sprites/close/us/us_1_pioneer.png",
		(263, 154), "images/sprites/close/us/us_1_sad.png",
	))
	image us sad sport close = _sr(im.Composite((703, 587),
		(  0,   0), "images/sprites/close/us/us_1_body.png",
		(126, 354), "images/sprites/close/us/us_1_sport.png",
		(263, 154), "images/sprites/close/us/us_1_sad.png",
	))
	image us sad swim close = _sr(im.Composite((703, 587),
		(  0,   0), "images/sprites/close/us/us_1_body.png",
		(236, 361), "images/sprites/close/us/us_1_swim.png",
		(263, 154), "images/sprites/close/us/us_1_sad.png",
	))
	image us shy dress close = _sr(im.Composite((706, 588),
		(  0,   0), "images/sprites/close/us/us_3_body.png",
		(235, 234), "images/sprites/close/us/us_3_dress.png",
		(260, 134), "images/sprites/close/us/us_3_shy.png",
	))
	image us shy pioneer close = _sr(im.Composite((706, 588),
		(  0,   0), "images/sprites/close/us/us_3_body.png",
		(155, 327), "images/sprites/close/us/us_3_pioneer.png",
		(260, 134), "images/sprites/close/us/us_3_shy.png",
	))
	image us shy sport close = _sr(im.Composite((706, 588),
		(  0,   0), "images/sprites/close/us/us_3_body.png",
		(162, 336), "images/sprites/close/us/us_3_sport.png",
		(260, 134), "images/sprites/close/us/us_3_shy.png",
	))
	image us shy swim close = _sr(im.Composite((706, 588),
		(  0,   0), "images/sprites/close/us/us_3_body.png",
		(236, 360), "images/sprites/close/us/us_3_swim.png",
		(260, 134), "images/sprites/close/us/us_3_shy.png",
	))
	image us shy2 dress close = _sr(im.Composite((706, 588),
		(  0,   0), "images/sprites/close/us/us_3_body.png",
		(235, 234), "images/sprites/close/us/us_3_dress.png",
		(259, 141), "images/sprites/close/us/us_3_shy2.png",
	))
	image us shy2 pioneer close = _sr(im.Composite((706, 588),
		(  0,   0), "images/sprites/close/us/us_3_body.png",
		(155, 327), "images/sprites/close/us/us_3_pioneer.png",
		(259, 141), "images/sprites/close/us/us_3_shy2.png",
	))
	image us shy2 sport close = _sr(im.Composite((706, 588),
		(  0,   0), "images/sprites/close/us/us_3_body.png",
		(162, 336), "images/sprites/close/us/us_3_sport.png",
		(259, 141), "images/sprites/close/us/us_3_shy2.png",
	))
	image us shy2 swim close = _sr(im.Composite((706, 588),
		(  0,   0), "images/sprites/close/us/us_3_body.png",
		(236, 360), "images/sprites/close/us/us_3_swim.png",
		(259, 141), "images/sprites/close/us/us_3_shy2.png",
	))
	image us smile dress close = _sr(im.Composite((703, 587),
		(  0,   0), "images/sprites/close/us/us_1_body.png",
		(237, 343), "images/sprites/close/us/us_1_dress.png",
		(254, 166), "images/sprites/close/us/us_1_smile.png",
	))
	image us smile pioneer close = _sr(im.Composite((703, 587),
		(  0,   0), "images/sprites/close/us/us_1_body.png",
		(149, 322), "images/sprites/close/us/us_1_pioneer.png",
		(254, 166), "images/sprites/close/us/us_1_smile.png",
	))
	image us smile sport close = _sr(im.Composite((703, 587),
		(  0,   0), "images/sprites/close/us/us_1_body.png",
		(126, 354), "images/sprites/close/us/us_1_sport.png",
		(254, 166), "images/sprites/close/us/us_1_smile.png",
	))
	image us smile swim close = _sr(im.Composite((703, 587),
		(  0,   0), "images/sprites/close/us/us_1_body.png",
		(236, 361), "images/sprites/close/us/us_1_swim.png",
		(254, 166), "images/sprites/close/us/us_1_smile.png",
	))
	image us surp1 dress close = _sr(im.Composite((706, 588),
		(  0,   0), "images/sprites/close/us/us_3_body.png",
		(235, 234), "images/sprites/close/us/us_3_dress.png",
		(252, 136), "images/sprites/close/us/us_3_surp1.png",
	))
	image us surp1 pioneer close = _sr(im.Composite((706, 588),
		(  0,   0), "images/sprites/close/us/us_3_body.png",
		(155, 327), "images/sprites/close/us/us_3_pioneer.png",
		(252, 136), "images/sprites/close/us/us_3_surp1.png",
	))
	image us surp1 sport close = _sr(im.Composite((706, 588),
		(  0,   0), "images/sprites/close/us/us_3_body.png",
		(162, 336), "images/sprites/close/us/us_3_sport.png",
		(252, 136), "images/sprites/close/us/us_3_surp1.png",
	))
	image us surp1 swim close = _sr(im.Composite((706, 588),
		(  0,   0), "images/sprites/close/us/us_3_body.png",
		(236, 360), "images/sprites/close/us/us_3_swim.png",
		(252, 136), "images/sprites/close/us/us_3_surp1.png",
	))
	image us surp2 dress close = _sr(im.Composite((706, 588),
		(  0,   0), "images/sprites/close/us/us_3_body.png",
		(235, 234), "images/sprites/close/us/us_3_dress.png",
		(252, 136), "images/sprites/close/us/us_3_surp2.png",
	))
	image us surp2 pioneer close = _sr(im.Composite((706, 588),
		(  0,   0), "images/sprites/close/us/us_3_body.png",
		(155, 327), "images/sprites/close/us/us_3_pioneer.png",
		(252, 136), "images/sprites/close/us/us_3_surp2.png",
	))
	image us surp2 sport close = _sr(im.Composite((706, 588),
		(  0,   0), "images/sprites/close/us/us_3_body.png",
		(162, 336), "images/sprites/close/us/us_3_sport.png",
		(252, 136), "images/sprites/close/us/us_3_surp2.png",
	))
	image us surp2 swim close = _sr(im.Composite((706, 588),
		(  0,   0), "images/sprites/close/us/us_3_body.png",
		(236, 360), "images/sprites/close/us/us_3_swim.png",
		(252, 136), "images/sprites/close/us/us_3_surp2.png",
	))
	image us surp3 dress close = _sr(im.Composite((706, 588),
		(  0,   0), "images/sprites/close/us/us_3_body.png",
		(235, 234), "images/sprites/close/us/us_3_dress.png",
		(252, 136), "images/sprites/close/us/us_3_surp3.png",
	))
	image us surp3 pioneer close = _sr(im.Composite((706, 588),
		(  0,   0), "images/sprites/close/us/us_3_body.png",
		(155, 327), "images/sprites/close/us/us_3_pioneer.png",
		(252, 136), "images/sprites/close/us/us_3_surp3.png",
	))
	image us surp3 sport close = _sr(im.Composite((706, 588),
		(  0,   0), "images/sprites/close/us/us_3_body.png",
		(162, 336), "images/sprites/close/us/us_3_sport.png",
		(252, 136), "images/sprites/close/us/us_3_surp3.png",
	))
	image us surp3 swim close = _sr(im.Composite((706, 588),
		(  0,   0), "images/sprites/close/us/us_3_body.png",
		(236, 360), "images/sprites/close/us/us_3_swim.png",
		(252, 136), "images/sprites/close/us/us_3_surp3.png",
	))
	image us upset dress close = _sr(im.Composite((738, 591),
		(  0,   0), "images/sprites/close/us/us_2_body.png",
		(219, 262), "images/sprites/close/us/us_2_dress.png",
		(284, 136), "images/sprites/close/us/us_2_upset.png",
	))
	image us upset pioneer close = _sr(im.Composite((738, 591),
		(  0,   0), "images/sprites/close/us/us_2_body.png",
		(145, 307), "images/sprites/close/us/us_2_pioneer.png",
		(284, 136), "images/sprites/close/us/us_2_upset.png",
	))
	image us upset sport close = _sr(im.Composite((738, 591),
		(  0,   0), "images/sprites/close/us/us_2_body.png",
		(154, 330), "images/sprites/close/us/us_2_sport.png",
		(284, 136), "images/sprites/close/us/us_2_upset.png",
	))
	image us upset swim close = _sr(im.Composite((738, 591),
		(  0,   0), "images/sprites/close/us/us_2_body.png",
		(217, 344), "images/sprites/close/us/us_2_swim.png",
		(284, 136), "images/sprites/close/us/us_2_upset.png",
	))
	
	image us angry dress = _sr(im.Composite((591, 663),
		(  0,   0), "images/sprites/normal/us/us_2_body.png",
		(158, 209), "images/sprites/normal/us/us_2_dress.png",
		(221, 100), "images/sprites/normal/us/us_2_angry.png",
	))
	image us angry pioneer = _sr(im.Composite((591, 663),
		(  0,   0), "images/sprites/normal/us/us_2_body.png",
		(116, 246), "images/sprites/normal/us/us_2_pioneer.png",
		(221, 100), "images/sprites/normal/us/us_2_angry.png",
	))
	image us angry sport = _sr(im.Composite((591, 663),
		(  0,   0), "images/sprites/normal/us/us_2_body.png",
		(123, 264), "images/sprites/normal/us/us_2_sport.png",
		(221, 100), "images/sprites/normal/us/us_2_angry.png",
	))
	image us angry swim = _sr(im.Composite((591, 663),
		(  0,   0), "images/sprites/normal/us/us_2_body.png",
		(167, 275), "images/sprites/normal/us/us_2_swim.png",
		(221, 100), "images/sprites/normal/us/us_2_angry.png",
	))
	image us calml dress = _sr(im.Composite((591, 663),
		(  0,   0), "images/sprites/normal/us/us_2_body.png",
		(158, 209), "images/sprites/normal/us/us_2_dress.png",
		(224, 106), "images/sprites/normal/us/us_2_calml.png",
	))
	image us calml pioneer = _sr(im.Composite((591, 663),
		(  0,   0), "images/sprites/normal/us/us_2_body.png",
		(116, 246), "images/sprites/normal/us/us_2_pioneer.png",
		(224, 106), "images/sprites/normal/us/us_2_calml.png",
	))
	image us calml sport = _sr(im.Composite((591, 663),
		(  0,   0), "images/sprites/normal/us/us_2_body.png",
		(123, 264), "images/sprites/normal/us/us_2_sport.png",
		(224, 106), "images/sprites/normal/us/us_2_calml.png",
	))
	image us calml swim = _sr(im.Composite((591, 663),
		(  0,   0), "images/sprites/normal/us/us_2_body.png",
		(167, 275), "images/sprites/normal/us/us_2_swim.png",
		(224, 106), "images/sprites/normal/us/us_2_calml.png",
	))
	image us cry dress = _sr(im.Composite((565, 660),
		(  0,   0), "images/sprites/normal/us/us_3_body.png",
		(158, 187), "images/sprites/normal/us/us_3_dress.png",
		(216, 111), "images/sprites/normal/us/us_3_cry.png",
	))
	image us cry pioneer = _sr(im.Composite((565, 660),
		(  0,   0), "images/sprites/normal/us/us_3_body.png",
		(124, 261), "images/sprites/normal/us/us_3_pioneer.png",
		(216, 111), "images/sprites/normal/us/us_3_cry.png",
	))
	image us cry sport = _sr(im.Composite((565, 660),
		(  0,   0), "images/sprites/normal/us/us_3_body.png",
		(129, 268), "images/sprites/normal/us/us_3_sport.png",
		(216, 111), "images/sprites/normal/us/us_3_cry.png",
	))
	image us cry swim = _sr(im.Composite((565, 660),
		(  0,   0), "images/sprites/normal/us/us_3_body.png",
		(161, 287), "images/sprites/normal/us/us_3_swim.png",
		(216, 111), "images/sprites/normal/us/us_3_cry.png",
	))
	image us cry2 dress = _sr(im.Composite((565, 660),
		(  0,   0), "images/sprites/normal/us/us_3_body.png",
		(158, 187), "images/sprites/normal/us/us_3_dress.png",
		(218, 112), "images/sprites/normal/us/us_3_cry2.png",
	))
	image us cry2 pioneer = _sr(im.Composite((565, 660),
		(  0,   0), "images/sprites/normal/us/us_3_body.png",
		(124, 261), "images/sprites/normal/us/us_3_pioneer.png",
		(218, 112), "images/sprites/normal/us/us_3_cry2.png",
	))
	image us cry2 sport = _sr(im.Composite((565, 660),
		(  0,   0), "images/sprites/normal/us/us_3_body.png",
		(129, 268), "images/sprites/normal/us/us_3_sport.png",
		(218, 112), "images/sprites/normal/us/us_3_cry2.png",
	))
	image us cry2 swim = _sr(im.Composite((565, 660),
		(  0,   0), "images/sprites/normal/us/us_3_body.png",
		(161, 287), "images/sprites/normal/us/us_3_swim.png",
		(218, 112), "images/sprites/normal/us/us_3_cry2.png",
	))
	image us dontlike dress = _sr(im.Composite((591, 663),
		(  0,   0), "images/sprites/normal/us/us_2_body.png",
		(158, 209), "images/sprites/normal/us/us_2_dress.png",
		(226, 100), "images/sprites/normal/us/us_2_dontlike.png",
	))
	image us dontlike pioneer = _sr(im.Composite((591, 663),
		(  0,   0), "images/sprites/normal/us/us_2_body.png",
		(116, 246), "images/sprites/normal/us/us_2_pioneer.png",
		(226, 100), "images/sprites/normal/us/us_2_dontlike.png",
	))
	image us dontlike sport = _sr(im.Composite((591, 663),
		(  0,   0), "images/sprites/normal/us/us_2_body.png",
		(123, 264), "images/sprites/normal/us/us_2_sport.png",
		(226, 100), "images/sprites/normal/us/us_2_dontlike.png",
	))
	image us dontlike swim = _sr(im.Composite((591, 663),
		(  0,   0), "images/sprites/normal/us/us_2_body.png",
		(167, 275), "images/sprites/normal/us/us_2_swim.png",
		(226, 100), "images/sprites/normal/us/us_2_dontlike.png",
	))
	image us fear dress = _sr(im.Composite((591, 663),
		(  0,   0), "images/sprites/normal/us/us_2_body.png",
		(158, 209), "images/sprites/normal/us/us_2_dress.png",
		(224,  90), "images/sprites/normal/us/us_2_fear.png",
	))
	image us fear pioneer = _sr(im.Composite((591, 663),
		(  0,   0), "images/sprites/normal/us/us_2_body.png",
		(116, 246), "images/sprites/normal/us/us_2_pioneer.png",
		(224,  90), "images/sprites/normal/us/us_2_fear.png",
	))
	image us fear sport = _sr(im.Composite((591, 663),
		(  0,   0), "images/sprites/normal/us/us_2_body.png",
		(123, 264), "images/sprites/normal/us/us_2_sport.png",
		(224,  90), "images/sprites/normal/us/us_2_fear.png",
	))
	image us fear swim = _sr(im.Composite((591, 663),
		(  0,   0), "images/sprites/normal/us/us_2_body.png",
		(167, 275), "images/sprites/normal/us/us_2_swim.png",
		(224,  90), "images/sprites/normal/us/us_2_fear.png",
	))
	image us grin dress = _sr(im.Composite((562, 660),
		(  0,   0), "images/sprites/normal/us/us_1_body.png",
		(156, 275), "images/sprites/normal/us/us_1_dress.png",
		(204, 112), "images/sprites/normal/us/us_1_grin.png",
	))
	image us grin pioneer = _sr(im.Composite((562, 660),
		(  0,   0), "images/sprites/normal/us/us_1_body.png",
		(119, 258), "images/sprites/normal/us/us_1_pioneer.png",
		(204, 112), "images/sprites/normal/us/us_1_grin.png",
	))
	image us grin sport = _sr(im.Composite((562, 660),
		(  0,   0), "images/sprites/normal/us/us_1_body.png",
		(101, 284), "images/sprites/normal/us/us_1_sport.png",
		(204, 112), "images/sprites/normal/us/us_1_grin.png",
	))
	image us grin swim = _sr(im.Composite((562, 660),
		(  0,   0), "images/sprites/normal/us/us_1_body.png",
		(159, 289), "images/sprites/normal/us/us_1_swim.png",
		(204, 112), "images/sprites/normal/us/us_1_grin.png",
	))
	image us laugh dress = _sr(im.Composite((562, 660),
		(  0,   0), "images/sprites/normal/us/us_1_body.png",
		(156, 275), "images/sprites/normal/us/us_1_dress.png",
		(209, 129), "images/sprites/normal/us/us_1_laugh.png",
	))
	image us laugh pioneer = _sr(im.Composite((562, 660),
		(  0,   0), "images/sprites/normal/us/us_1_body.png",
		(119, 258), "images/sprites/normal/us/us_1_pioneer.png",
		(209, 129), "images/sprites/normal/us/us_1_laugh.png",
	))
	image us laugh sport = _sr(im.Composite((562, 660),
		(  0,   0), "images/sprites/normal/us/us_1_body.png",
		(101, 284), "images/sprites/normal/us/us_1_sport.png",
		(209, 129), "images/sprites/normal/us/us_1_laugh.png",
	))
	image us laugh swim = _sr(im.Composite((562, 660),
		(  0,   0), "images/sprites/normal/us/us_1_body.png",
		(159, 289), "images/sprites/normal/us/us_1_swim.png",
		(209, 129), "images/sprites/normal/us/us_1_laugh.png",
	))
	image us laugh2 dress = _sr(im.Composite((562, 660),
		(  0,   0), "images/sprites/normal/us/us_1_body.png",
		(156, 275), "images/sprites/normal/us/us_1_dress.png",
		(209, 129), "images/sprites/normal/us/us_1_laugh2.png",
	))
	image us laugh2 pioneer = _sr(im.Composite((562, 660),
		(  0,   0), "images/sprites/normal/us/us_1_body.png",
		(119, 258), "images/sprites/normal/us/us_1_pioneer.png",
		(209, 129), "images/sprites/normal/us/us_1_laugh2.png",
	))
	image us laugh2 sport = _sr(im.Composite((562, 660),
		(  0,   0), "images/sprites/normal/us/us_1_body.png",
		(101, 284), "images/sprites/normal/us/us_1_sport.png",
		(209, 129), "images/sprites/normal/us/us_1_laugh2.png",
	))
	image us laugh2 swim = _sr(im.Composite((562, 660),
		(  0,   0), "images/sprites/normal/us/us_1_body.png",
		(159, 289), "images/sprites/normal/us/us_1_swim.png",
		(209, 129), "images/sprites/normal/us/us_1_laugh2.png",
	))
	image us normal dress = _sr(im.Composite((562, 660),
		(  0,   0), "images/sprites/normal/us/us_1_body.png",
		(156, 275), "images/sprites/normal/us/us_1_dress.png",
		(210, 121), "images/sprites/normal/us/us_1_normal.png",
	))
	image us normal pioneer = _sr(im.Composite((562, 660),
		(  0,   0), "images/sprites/normal/us/us_1_body.png",
		(119, 258), "images/sprites/normal/us/us_1_pioneer.png",
		(210, 121), "images/sprites/normal/us/us_1_normal.png",
	))
	image us normal sport = _sr(im.Composite((562, 660),
		(  0,   0), "images/sprites/normal/us/us_1_body.png",
		(101, 284), "images/sprites/normal/us/us_1_sport.png",
		(210, 121), "images/sprites/normal/us/us_1_normal.png",
	))
	image us normal swim = _sr(im.Composite((562, 660),
		(  0,   0), "images/sprites/normal/us/us_1_body.png",
		(159, 289), "images/sprites/normal/us/us_1_swim.png",
		(210, 121), "images/sprites/normal/us/us_1_normal.png",
	))
	image us sad dress = _sr(im.Composite((562, 660),
		(  0,   0), "images/sprites/normal/us/us_1_body.png",
		(156, 275), "images/sprites/normal/us/us_1_dress.png",
		(210, 124), "images/sprites/normal/us/us_1_sad.png",
	))
	image us sad pioneer = _sr(im.Composite((562, 660),
		(  0,   0), "images/sprites/normal/us/us_1_body.png",
		(119, 258), "images/sprites/normal/us/us_1_pioneer.png",
		(210, 124), "images/sprites/normal/us/us_1_sad.png",
	))
	image us sad sport = _sr(im.Composite((562, 660),
		(  0,   0), "images/sprites/normal/us/us_1_body.png",
		(101, 284), "images/sprites/normal/us/us_1_sport.png",
		(210, 124), "images/sprites/normal/us/us_1_sad.png",
	))
	image us sad swim = _sr(im.Composite((562, 660),
		(  0,   0), "images/sprites/normal/us/us_1_body.png",
		(159, 289), "images/sprites/normal/us/us_1_swim.png",
		(210, 124), "images/sprites/normal/us/us_1_sad.png",
	))
	image us shy dress = _sr(im.Composite((565, 660),
		(  0,   0), "images/sprites/normal/us/us_3_body.png",
		(158, 187), "images/sprites/normal/us/us_3_dress.png",
		(208, 107), "images/sprites/normal/us/us_3_shy.png",
	))
	image us shy pioneer = _sr(im.Composite((565, 660),
		(  0,   0), "images/sprites/normal/us/us_3_body.png",
		(124, 261), "images/sprites/normal/us/us_3_pioneer.png",
		(208, 107), "images/sprites/normal/us/us_3_shy.png",
	))
	image us shy sport = _sr(im.Composite((565, 660),
		(  0,   0), "images/sprites/normal/us/us_3_body.png",
		(129, 268), "images/sprites/normal/us/us_3_sport.png",
		(208, 107), "images/sprites/normal/us/us_3_shy.png",
	))
	image us shy swim = _sr(im.Composite((565, 660),
		(  0,   0), "images/sprites/normal/us/us_3_body.png",
		(161, 287), "images/sprites/normal/us/us_3_swim.png",
		(208, 107), "images/sprites/normal/us/us_3_shy.png",
	))
	image us shy2 dress = _sr(im.Composite((565, 660),
		(  0,   0), "images/sprites/normal/us/us_3_body.png",
		(158, 187), "images/sprites/normal/us/us_3_dress.png",
		(207, 112), "images/sprites/normal/us/us_3_shy2.png",
	))
	image us shy2 pioneer = _sr(im.Composite((565, 660),
		(  0,   0), "images/sprites/normal/us/us_3_body.png",
		(124, 261), "images/sprites/normal/us/us_3_pioneer.png",
		(207, 112), "images/sprites/normal/us/us_3_shy2.png",
	))
	image us shy2 sport = _sr(im.Composite((565, 660),
		(  0,   0), "images/sprites/normal/us/us_3_body.png",
		(129, 268), "images/sprites/normal/us/us_3_sport.png",
		(207, 112), "images/sprites/normal/us/us_3_shy2.png",
	))
	image us shy2 swim = _sr(im.Composite((565, 660),
		(  0,   0), "images/sprites/normal/us/us_3_body.png",
		(161, 287), "images/sprites/normal/us/us_3_swim.png",
		(207, 112), "images/sprites/normal/us/us_3_shy2.png",
	))
	image us smile dress = _sr(im.Composite((562, 660),
		(  0,   0), "images/sprites/normal/us/us_1_body.png",
		(156, 275), "images/sprites/normal/us/us_1_dress.png",
		(203, 133), "images/sprites/normal/us/us_1_smile.png",
	))
	image us smile pioneer = _sr(im.Composite((562, 660),
		(  0,   0), "images/sprites/normal/us/us_1_body.png",
		(119, 258), "images/sprites/normal/us/us_1_pioneer.png",
		(203, 133), "images/sprites/normal/us/us_1_smile.png",
	))
	image us smile sport = _sr(im.Composite((562, 660),
		(  0,   0), "images/sprites/normal/us/us_1_body.png",
		(101, 284), "images/sprites/normal/us/us_1_sport.png",
		(203, 133), "images/sprites/normal/us/us_1_smile.png",
	))
	image us smile swim = _sr(im.Composite((562, 660),
		(  0,   0), "images/sprites/normal/us/us_1_body.png",
		(159, 289), "images/sprites/normal/us/us_1_swim.png",
		(203, 133), "images/sprites/normal/us/us_1_smile.png",
	))
	image us surp1 dress = _sr(im.Composite((565, 660),
		(  0,   0), "images/sprites/normal/us/us_3_body.png",
		(158, 187), "images/sprites/normal/us/us_3_dress.png",
		(202, 108), "images/sprites/normal/us/us_3_surp1.png",
	))
	image us surp1 pioneer = _sr(im.Composite((565, 660),
		(  0,   0), "images/sprites/normal/us/us_3_body.png",
		(124, 261), "images/sprites/normal/us/us_3_pioneer.png",
		(202, 108), "images/sprites/normal/us/us_3_surp1.png",
	))
	image us surp1 sport = _sr(im.Composite((565, 660),
		(  0,   0), "images/sprites/normal/us/us_3_body.png",
		(129, 268), "images/sprites/normal/us/us_3_sport.png",
		(202, 108), "images/sprites/normal/us/us_3_surp1.png",
	))
	image us surp1 swim = _sr(im.Composite((565, 660),
		(  0,   0), "images/sprites/normal/us/us_3_body.png",
		(161, 287), "images/sprites/normal/us/us_3_swim.png",
		(202, 108), "images/sprites/normal/us/us_3_surp1.png",
	))
	image us surp2 dress = _sr(im.Composite((565, 660),
		(  0,   0), "images/sprites/normal/us/us_3_body.png",
		(158, 187), "images/sprites/normal/us/us_3_dress.png",
		(202, 109), "images/sprites/normal/us/us_3_surp2.png",
	))
	image us surp2 pioneer = _sr(im.Composite((565, 660),
		(  0,   0), "images/sprites/normal/us/us_3_body.png",
		(124, 261), "images/sprites/normal/us/us_3_pioneer.png",
		(202, 109), "images/sprites/normal/us/us_3_surp2.png",
	))
	image us surp2 sport = _sr(im.Composite((565, 660),
		(  0,   0), "images/sprites/normal/us/us_3_body.png",
		(129, 268), "images/sprites/normal/us/us_3_sport.png",
		(202, 109), "images/sprites/normal/us/us_3_surp2.png",
	))
	image us surp2 swim = _sr(im.Composite((565, 660),
		(  0,   0), "images/sprites/normal/us/us_3_body.png",
		(161, 287), "images/sprites/normal/us/us_3_swim.png",
		(202, 109), "images/sprites/normal/us/us_3_surp2.png",
	))
	image us surp3 dress = _sr(im.Composite((565, 660),
		(  0,   0), "images/sprites/normal/us/us_3_body.png",
		(158, 187), "images/sprites/normal/us/us_3_dress.png",
		(202, 109), "images/sprites/normal/us/us_3_surp3.png",
	))
	image us surp3 pioneer = _sr(im.Composite((565, 660),
		(  0,   0), "images/sprites/normal/us/us_3_body.png",
		(124, 261), "images/sprites/normal/us/us_3_pioneer.png",
		(202, 109), "images/sprites/normal/us/us_3_surp3.png",
	))
	image us surp3 sport = _sr(im.Composite((565, 660),
		(  0,   0), "images/sprites/normal/us/us_3_body.png",
		(129, 268), "images/sprites/normal/us/us_3_sport.png",
		(202, 109), "images/sprites/normal/us/us_3_surp3.png",
	))
	image us surp3 swim = _sr(im.Composite((565, 660),
		(  0,   0), "images/sprites/normal/us/us_3_body.png",
		(161, 287), "images/sprites/normal/us/us_3_swim.png",
		(202, 109), "images/sprites/normal/us/us_3_surp3.png",
	))
	image us upset dress = _sr(im.Composite((591, 663),
		(  0,   0), "images/sprites/normal/us/us_2_body.png",
		(158, 209), "images/sprites/normal/us/us_2_dress.png",
		(227, 109), "images/sprites/normal/us/us_2_upset.png",
	))
	image us upset pioneer = _sr(im.Composite((591, 663),
		(  0,   0), "images/sprites/normal/us/us_2_body.png",
		(116, 246), "images/sprites/normal/us/us_2_pioneer.png",
		(227, 109), "images/sprites/normal/us/us_2_upset.png",
	))
	image us upset sport = _sr(im.Composite((591, 663),
		(  0,   0), "images/sprites/normal/us/us_2_body.png",
		(123, 264), "images/sprites/normal/us/us_2_sport.png",
		(227, 109), "images/sprites/normal/us/us_2_upset.png",
	))
	image us upset swim = _sr(im.Composite((591, 663),
		(  0,   0), "images/sprites/normal/us/us_2_body.png",
		(167, 275), "images/sprites/normal/us/us_2_swim.png",
		(227, 109), "images/sprites/normal/us/us_2_upset.png",
	))
	
	image us angry dress far = _sr(im.Composite((444, 655),
		(  0,   0), "images/sprites/far/us/us_2_body.png",
		( 92, 157), "images/sprites/far/us/us_2_dress.png",
		(166,  75), "images/sprites/far/us/us_2_angry.png",
	))
	image us angry pioneer far = _sr(im.Composite((444, 655),
		(  0,   0), "images/sprites/far/us/us_2_body.png",
		( 87, 184), "images/sprites/far/us/us_2_pioneer.png",
		(166,  75), "images/sprites/far/us/us_2_angry.png",
	))
	image us angry sport far = _sr(im.Composite((444, 655),
		(  0,   0), "images/sprites/far/us/us_2_body.png",
		( 92, 198), "images/sprites/far/us/us_2_sport.png",
		(166,  75), "images/sprites/far/us/us_2_angry.png",
	))
	image us angry swim far = _sr(im.Composite((444, 655),
		(  0,   0), "images/sprites/far/us/us_2_body.png",
		(120, 207), "images/sprites/far/us/us_2_swim.png",
		(166,  75), "images/sprites/far/us/us_2_angry.png",
	))
	image us calml dress far = _sr(im.Composite((444, 655),
		(  0,   0), "images/sprites/far/us/us_2_body.png",
		( 92, 157), "images/sprites/far/us/us_2_dress.png",
		(168,  79), "images/sprites/far/us/us_2_calml.png",
	))
	image us calml pioneer far = _sr(im.Composite((444, 655),
		(  0,   0), "images/sprites/far/us/us_2_body.png",
		( 87, 184), "images/sprites/far/us/us_2_pioneer.png",
		(168,  79), "images/sprites/far/us/us_2_calml.png",
	))
	image us calml sport far = _sr(im.Composite((444, 655),
		(  0,   0), "images/sprites/far/us/us_2_body.png",
		( 92, 198), "images/sprites/far/us/us_2_sport.png",
		(168,  79), "images/sprites/far/us/us_2_calml.png",
	))
	image us calml swim far = _sr(im.Composite((444, 655),
		(  0,   0), "images/sprites/far/us/us_2_body.png",
		(120, 207), "images/sprites/far/us/us_2_swim.png",
		(168,  79), "images/sprites/far/us/us_2_calml.png",
	))
	image us cry dress far = _sr(im.Composite((424, 653),
		(  0,   0), "images/sprites/far/us/us_3_body.png",
		( 98, 140), "images/sprites/far/us/us_3_dress.png",
		(162,  84), "images/sprites/far/us/us_3_cry.png",
	))
	image us cry pioneer far = _sr(im.Composite((424, 653),
		(  0,   0), "images/sprites/far/us/us_3_body.png",
		( 85, 196), "images/sprites/far/us/us_3_pioneer.png",
		(162,  84), "images/sprites/far/us/us_3_cry.png",
	))
	image us cry sport far = _sr(im.Composite((424, 653),
		(  0,   0), "images/sprites/far/us/us_3_body.png",
		( 97, 202), "images/sprites/far/us/us_3_sport.png",
		(162,  84), "images/sprites/far/us/us_3_cry.png",
	))
	image us cry swim far = _sr(im.Composite((424, 653),
		(  0,   0), "images/sprites/far/us/us_3_body.png",
		(118, 216), "images/sprites/far/us/us_3_swim.png",
		(162,  84), "images/sprites/far/us/us_3_cry.png",
	))
	image us cry2 dress far = _sr(im.Composite((424, 653),
		(  0,   0), "images/sprites/far/us/us_3_body.png",
		( 98, 140), "images/sprites/far/us/us_3_dress.png",
		(163,  84), "images/sprites/far/us/us_3_cry2.png",
	))
	image us cry2 pioneer far = _sr(im.Composite((424, 653),
		(  0,   0), "images/sprites/far/us/us_3_body.png",
		( 85, 196), "images/sprites/far/us/us_3_pioneer.png",
		(163,  84), "images/sprites/far/us/us_3_cry2.png",
	))
	image us cry2 sport far = _sr(im.Composite((424, 653),
		(  0,   0), "images/sprites/far/us/us_3_body.png",
		( 97, 202), "images/sprites/far/us/us_3_sport.png",
		(163,  84), "images/sprites/far/us/us_3_cry2.png",
	))
	image us cry2 swim far = _sr(im.Composite((424, 653),
		(  0,   0), "images/sprites/far/us/us_3_body.png",
		(118, 216), "images/sprites/far/us/us_3_swim.png",
		(163,  84), "images/sprites/far/us/us_3_cry2.png",
	))
	image us dontlike dress far = _sr(im.Composite((444, 655),
		(  0,   0), "images/sprites/far/us/us_2_body.png",
		( 92, 157), "images/sprites/far/us/us_2_dress.png",
		(170,  75), "images/sprites/far/us/us_2_dontlike.png",
	))
	image us dontlike pioneer far = _sr(im.Composite((444, 655),
		(  0,   0), "images/sprites/far/us/us_2_body.png",
		( 87, 184), "images/sprites/far/us/us_2_pioneer.png",
		(170,  75), "images/sprites/far/us/us_2_dontlike.png",
	))
	image us dontlike sport far = _sr(im.Composite((444, 655),
		(  0,   0), "images/sprites/far/us/us_2_body.png",
		( 92, 198), "images/sprites/far/us/us_2_sport.png",
		(170,  75), "images/sprites/far/us/us_2_dontlike.png",
	))
	image us dontlike swim far = _sr(im.Composite((444, 655),
		(  0,   0), "images/sprites/far/us/us_2_body.png",
		(120, 207), "images/sprites/far/us/us_2_swim.png",
		(170,  75), "images/sprites/far/us/us_2_dontlike.png",
	))
	image us fear dress far = _sr(im.Composite((444, 655),
		(  0,   0), "images/sprites/far/us/us_2_body.png",
		( 92, 157), "images/sprites/far/us/us_2_dress.png",
		(168,  67), "images/sprites/far/us/us_2_fear.png",
	))
	image us fear pioneer far = _sr(im.Composite((444, 655),
		(  0,   0), "images/sprites/far/us/us_2_body.png",
		( 87, 184), "images/sprites/far/us/us_2_pioneer.png",
		(168,  67), "images/sprites/far/us/us_2_fear.png",
	))
	image us fear sport far = _sr(im.Composite((444, 655),
		(  0,   0), "images/sprites/far/us/us_2_body.png",
		( 92, 198), "images/sprites/far/us/us_2_sport.png",
		(168,  67), "images/sprites/far/us/us_2_fear.png",
	))
	image us fear swim far = _sr(im.Composite((444, 655),
		(  0,   0), "images/sprites/far/us/us_2_body.png",
		(120, 207), "images/sprites/far/us/us_2_swim.png",
		(168,  67), "images/sprites/far/us/us_2_fear.png",
	))
	image us grin dress far = _sr(im.Composite((423, 653),
		(  0,   0), "images/sprites/far/us/us_1_body.png",
		( 79, 207), "images/sprites/far/us/us_1_dress.png",
		(154,  85), "images/sprites/far/us/us_1_grin.png",
	))
	image us grin pioneer far = _sr(im.Composite((423, 653),
		(  0,   0), "images/sprites/far/us/us_1_body.png",
		( 90, 194), "images/sprites/far/us/us_1_pioneer.png",
		(154,  85), "images/sprites/far/us/us_1_grin.png",
	))
	image us grin sport far = _sr(im.Composite((423, 653),
		(  0,   0), "images/sprites/far/us/us_1_body.png",
		( 76, 213), "images/sprites/far/us/us_1_sport.png",
		(154,  85), "images/sprites/far/us/us_1_grin.png",
	))
	image us grin swim far = _sr(im.Composite((423, 653),
		(  0,   0), "images/sprites/far/us/us_1_body.png",
		(116, 217), "images/sprites/far/us/us_1_swim.png",
		(154,  85), "images/sprites/far/us/us_1_grin.png",
	))
	image us laugh dress far = _sr(im.Composite((423, 653),
		(  0,   0), "images/sprites/far/us/us_1_body.png",
		( 79, 207), "images/sprites/far/us/us_1_dress.png",
		(158,  97), "images/sprites/far/us/us_1_laugh.png",
	))
	image us laugh pioneer far = _sr(im.Composite((423, 653),
		(  0,   0), "images/sprites/far/us/us_1_body.png",
		( 90, 194), "images/sprites/far/us/us_1_pioneer.png",
		(158,  97), "images/sprites/far/us/us_1_laugh.png",
	))
	image us laugh sport far = _sr(im.Composite((423, 653),
		(  0,   0), "images/sprites/far/us/us_1_body.png",
		( 76, 213), "images/sprites/far/us/us_1_sport.png",
		(158,  97), "images/sprites/far/us/us_1_laugh.png",
	))
	image us laugh swim far = _sr(im.Composite((423, 653),
		(  0,   0), "images/sprites/far/us/us_1_body.png",
		(116, 217), "images/sprites/far/us/us_1_swim.png",
		(158,  97), "images/sprites/far/us/us_1_laugh.png",
	))
	image us laugh2 dress far = _sr(im.Composite((423, 653),
		(  0,   0), "images/sprites/far/us/us_1_body.png",
		( 79, 207), "images/sprites/far/us/us_1_dress.png",
		(158,  97), "images/sprites/far/us/us_1_laugh2.png",
	))
	image us laugh2 pioneer far = _sr(im.Composite((423, 653),
		(  0,   0), "images/sprites/far/us/us_1_body.png",
		( 90, 194), "images/sprites/far/us/us_1_pioneer.png",
		(158,  97), "images/sprites/far/us/us_1_laugh2.png",
	))
	image us laugh2 sport far = _sr(im.Composite((423, 653),
		(  0,   0), "images/sprites/far/us/us_1_body.png",
		( 76, 213), "images/sprites/far/us/us_1_sport.png",
		(158,  97), "images/sprites/far/us/us_1_laugh2.png",
	))
	image us laugh2 swim far = _sr(im.Composite((423, 653),
		(  0,   0), "images/sprites/far/us/us_1_body.png",
		(116, 217), "images/sprites/far/us/us_1_swim.png",
		(158,  97), "images/sprites/far/us/us_1_laugh2.png",
	))
	image us normal dress far = _sr(im.Composite((423, 653),
		(  0,   0), "images/sprites/far/us/us_1_body.png",
		( 79, 207), "images/sprites/far/us/us_1_dress.png",
		(158,  91), "images/sprites/far/us/us_1_normal.png",
	))
	image us normal pioneer far = _sr(im.Composite((423, 653),
		(  0,   0), "images/sprites/far/us/us_1_body.png",
		( 90, 194), "images/sprites/far/us/us_1_pioneer.png",
		(158,  91), "images/sprites/far/us/us_1_normal.png",
	))
	image us normal sport far = _sr(im.Composite((423, 653),
		(  0,   0), "images/sprites/far/us/us_1_body.png",
		( 76, 213), "images/sprites/far/us/us_1_sport.png",
		(158,  91), "images/sprites/far/us/us_1_normal.png",
	))
	image us normal swim far = _sr(im.Composite((423, 653),
		(  0,   0), "images/sprites/far/us/us_1_body.png",
		(116, 217), "images/sprites/far/us/us_1_swim.png",
		(158,  91), "images/sprites/far/us/us_1_normal.png",
	))
	image us sad dress far = _sr(im.Composite((423, 653),
		(  0,   0), "images/sprites/far/us/us_1_body.png",
		( 79, 207), "images/sprites/far/us/us_1_dress.png",
		(158,  93), "images/sprites/far/us/us_1_sad.png",
	))
	image us sad pioneer far = _sr(im.Composite((423, 653),
		(  0,   0), "images/sprites/far/us/us_1_body.png",
		( 90, 194), "images/sprites/far/us/us_1_pioneer.png",
		(158,  93), "images/sprites/far/us/us_1_sad.png",
	))
	image us sad sport far = _sr(im.Composite((423, 653),
		(  0,   0), "images/sprites/far/us/us_1_body.png",
		( 76, 213), "images/sprites/far/us/us_1_sport.png",
		(158,  93), "images/sprites/far/us/us_1_sad.png",
	))
	image us sad swim far = _sr(im.Composite((423, 653),
		(  0,   0), "images/sprites/far/us/us_1_body.png",
		(116, 217), "images/sprites/far/us/us_1_swim.png",
		(158,  93), "images/sprites/far/us/us_1_sad.png",
	))
	image us shy dress far = _sr(im.Composite((424, 653),
		(  0,   0), "images/sprites/far/us/us_3_body.png",
		( 98, 140), "images/sprites/far/us/us_3_dress.png",
		(156,  81), "images/sprites/far/us/us_3_shy.png",
	))
	image us shy pioneer far = _sr(im.Composite((424, 653),
		(  0,   0), "images/sprites/far/us/us_3_body.png",
		( 85, 196), "images/sprites/far/us/us_3_pioneer.png",
		(156,  81), "images/sprites/far/us/us_3_shy.png",
	))
	image us shy sport far = _sr(im.Composite((424, 653),
		(  0,   0), "images/sprites/far/us/us_3_body.png",
		( 97, 202), "images/sprites/far/us/us_3_sport.png",
		(156,  81), "images/sprites/far/us/us_3_shy.png",
	))
	image us shy swim far = _sr(im.Composite((424, 653),
		(  0,   0), "images/sprites/far/us/us_3_body.png",
		(118, 216), "images/sprites/far/us/us_3_swim.png",
		(156,  81), "images/sprites/far/us/us_3_shy.png",
	))
	image us shy2 dress far = _sr(im.Composite((424, 653),
		(  0,   0), "images/sprites/far/us/us_3_body.png",
		( 98, 140), "images/sprites/far/us/us_3_dress.png",
		(156,  84), "images/sprites/far/us/us_3_shy2.png",
	))
	image us shy2 pioneer far = _sr(im.Composite((424, 653),
		(  0,   0), "images/sprites/far/us/us_3_body.png",
		( 85, 196), "images/sprites/far/us/us_3_pioneer.png",
		(156,  84), "images/sprites/far/us/us_3_shy2.png",
	))
	image us shy2 sport far = _sr(im.Composite((424, 653),
		(  0,   0), "images/sprites/far/us/us_3_body.png",
		( 97, 202), "images/sprites/far/us/us_3_sport.png",
		(156,  84), "images/sprites/far/us/us_3_shy2.png",
	))
	image us shy2 swim far = _sr(im.Composite((424, 653),
		(  0,   0), "images/sprites/far/us/us_3_body.png",
		(118, 216), "images/sprites/far/us/us_3_swim.png",
		(156,  84), "images/sprites/far/us/us_3_shy2.png",
	))
	image us smile dress far = _sr(im.Composite((423, 653),
		(  0,   0), "images/sprites/far/us/us_1_body.png",
		( 79, 207), "images/sprites/far/us/us_1_dress.png",
		(153, 100), "images/sprites/far/us/us_1_smile.png",
	))
	image us smile pioneer far = _sr(im.Composite((423, 653),
		(  0,   0), "images/sprites/far/us/us_1_body.png",
		( 90, 194), "images/sprites/far/us/us_1_pioneer.png",
		(153, 100), "images/sprites/far/us/us_1_smile.png",
	))
	image us smile sport far = _sr(im.Composite((423, 653),
		(  0,   0), "images/sprites/far/us/us_1_body.png",
		( 76, 213), "images/sprites/far/us/us_1_sport.png",
		(153, 100), "images/sprites/far/us/us_1_smile.png",
	))
	image us smile swim far = _sr(im.Composite((423, 653),
		(  0,   0), "images/sprites/far/us/us_1_body.png",
		(116, 217), "images/sprites/far/us/us_1_swim.png",
		(153, 100), "images/sprites/far/us/us_1_smile.png",
	))
	image us surp1 dress far = _sr(im.Composite((424, 653),
		(  0,   0), "images/sprites/far/us/us_3_body.png",
		( 98, 140), "images/sprites/far/us/us_3_dress.png",
		(151,  82), "images/sprites/far/us/us_3_surp1.png",
	))
	image us surp1 pioneer far = _sr(im.Composite((424, 653),
		(  0,   0), "images/sprites/far/us/us_3_body.png",
		( 85, 196), "images/sprites/far/us/us_3_pioneer.png",
		(151,  82), "images/sprites/far/us/us_3_surp1.png",
	))
	image us surp1 sport far = _sr(im.Composite((424, 653),
		(  0,   0), "images/sprites/far/us/us_3_body.png",
		( 97, 202), "images/sprites/far/us/us_3_sport.png",
		(151,  82), "images/sprites/far/us/us_3_surp1.png",
	))
	image us surp1 swim far = _sr(im.Composite((424, 653),
		(  0,   0), "images/sprites/far/us/us_3_body.png",
		(118, 216), "images/sprites/far/us/us_3_swim.png",
		(151,  82), "images/sprites/far/us/us_3_surp1.png",
	))
	image us surp2 dress far = _sr(im.Composite((424, 653),
		(  0,   0), "images/sprites/far/us/us_3_body.png",
		( 98, 140), "images/sprites/far/us/us_3_dress.png",
		(151,  82), "images/sprites/far/us/us_3_surp2.png",
	))
	image us surp2 pioneer far = _sr(im.Composite((424, 653),
		(  0,   0), "images/sprites/far/us/us_3_body.png",
		( 85, 196), "images/sprites/far/us/us_3_pioneer.png",
		(151,  82), "images/sprites/far/us/us_3_surp2.png",
	))
	image us surp2 sport far = _sr(im.Composite((424, 653),
		(  0,   0), "images/sprites/far/us/us_3_body.png",
		( 97, 202), "images/sprites/far/us/us_3_sport.png",
		(151,  82), "images/sprites/far/us/us_3_surp2.png",
	))
	image us surp2 swim far = _sr(im.Composite((424, 653),
		(  0,   0), "images/sprites/far/us/us_3_body.png",
		(118, 216), "images/sprites/far/us/us_3_swim.png",
		(151,  82), "images/sprites/far/us/us_3_surp2.png",
	))
	image us surp3 dress far = _sr(im.Composite((424, 653),
		(  0,   0), "images/sprites/far/us/us_3_body.png",
		( 98, 140), "images/sprites/far/us/us_3_dress.png",
		(151,  82), "images/sprites/far/us/us_3_surp3.png",
	))
	image us surp3 pioneer far = _sr(im.Composite((424, 653),
		(  0,   0), "images/sprites/far/us/us_3_body.png",
		( 85, 196), "images/sprites/far/us/us_3_pioneer.png",
		(151,  82), "images/sprites/far/us/us_3_surp3.png",
	))
	image us surp3 sport far = _sr(im.Composite((424, 653),
		(  0,   0), "images/sprites/far/us/us_3_body.png",
		( 97, 202), "images/sprites/far/us/us_3_sport.png",
		(151,  82), "images/sprites/far/us/us_3_surp3.png",
	))
	image us surp3 swim far = _sr(im.Composite((424, 653),
		(  0,   0), "images/sprites/far/us/us_3_body.png",
		(118, 216), "images/sprites/far/us/us_3_swim.png",
		(151,  82), "images/sprites/far/us/us_3_surp3.png",
	))
	image us upset dress far = _sr(im.Composite((444, 655),
		(  0,   0), "images/sprites/far/us/us_2_body.png",
		( 92, 157), "images/sprites/far/us/us_2_dress.png",
		(171,  82), "images/sprites/far/us/us_2_upset.png",
	))
	image us upset pioneer far = _sr(im.Composite((444, 655),
		(  0,   0), "images/sprites/far/us/us_2_body.png",
		( 87, 184), "images/sprites/far/us/us_2_pioneer.png",
		(171,  82), "images/sprites/far/us/us_2_upset.png",
	))
	image us upset sport far = _sr(im.Composite((444, 655),
		(  0,   0), "images/sprites/far/us/us_2_body.png",
		( 92, 198), "images/sprites/far/us/us_2_sport.png",
		(171,  82), "images/sprites/far/us/us_2_upset.png",
	))
	image us upset swim far = _sr(im.Composite((444, 655),
		(  0,   0), "images/sprites/far/us/us_2_body.png",
		(120, 207), "images/sprites/far/us/us_2_swim.png",
		(171,  82), "images/sprites/far/us/us_2_upset.png",
	))
	
	image uv dontlike close = _sr(im.Composite((878, 737),
		(  0,  34), "images/sprites/close/uv/uv_1_body.png",
		(280, 372), "images/sprites/close/uv/uv_1_pioneer.png",
		(300,   0), "images/sprites/close/uv/uv_1_dontlike.png",
	))
	image uv grin close = _sr(im.Composite((535, 764),
		(  0,  62), "images/sprites/close/uv/uv_3_body.png",
		(124, 418), "images/sprites/close/uv/uv_3_pioneer.png",
		(179,   0), "images/sprites/close/uv/uv_3_grin.png",
	))
	image uv guilty close = _sr(im.Composite((546, 730),
		(  0,  18), "images/sprites/close/uv/uv_4_body.png",
		( 81, 381), "images/sprites/close/uv/uv_4_pioneer.png",
		(132,   0), "images/sprites/close/uv/uv_4_guilty.png",
	))
	image uv laugh close = _sr(im.Composite((535, 761),
		(  0,  59), "images/sprites/close/uv/uv_3_body.png",
		(124, 415), "images/sprites/close/uv/uv_3_pioneer.png",
		(173,   0), "images/sprites/close/uv/uv_3_laugh.png",
	))
	image uv normal close = _sr(im.Composite((523, 764),
		(  0,  56), "images/sprites/close/uv/uv_2_body.png",
		(135, 388), "images/sprites/close/uv/uv_2_pioneer.png",
		(144,   0), "images/sprites/close/uv/uv_2_normal.png",
	))
	image uv rage close = _sr(im.Composite((878, 747),
		(  0,  44), "images/sprites/close/uv/uv_1_body.png",
		(280, 382), "images/sprites/close/uv/uv_1_pioneer.png",
		(307,   0), "images/sprites/close/uv/uv_1_rage.png",
	))
	image uv sad close = _sr(im.Composite((878, 706),
		(  0,   3), "images/sprites/close/uv/uv_1_body.png",
		(280, 341), "images/sprites/close/uv/uv_1_pioneer.png",
		(268,   0), "images/sprites/close/uv/uv_1_sad.png",
	))
	image uv shocked close = _sr(im.Composite((878, 762),
		(  0,  59), "images/sprites/close/uv/uv_1_body.png",
		(280, 397), "images/sprites/close/uv/uv_1_pioneer.png",
		(311,   0), "images/sprites/close/uv/uv_1_shocked.png",
	))
	image uv smile close = _sr(im.Composite((522, 778),
		(  0,  70), "images/sprites/close/uv/uv_2_body.png",
		(135, 402), "images/sprites/close/uv/uv_2_pioneer.png",
		(149,   0), "images/sprites/close/uv/uv_2_smile.png",
	))
	image uv surprise close = _sr(im.Composite((465, 758),
		(  0,  46), "images/sprites/close/uv/uv_4_body.png",
		( 81, 409), "images/sprites/close/uv/uv_4_pioneer.png",
		(137,   0), "images/sprites/close/uv/uv_4_surprise.png",
	))
	image uv surprise2 close = _sr(im.Composite((528, 788),
		(  0,  86), "images/sprites/close/uv/uv_3_body.png",
		(124, 442), "images/sprites/close/uv/uv_3_pioneer.png",
		(181,   0), "images/sprites/close/uv/uv_3_surprise2.png",
	))
	image uv upset close = _sr(im.Composite((542, 718),
		(  0,   6), "images/sprites/close/uv/uv_4_body.png",
		( 81, 369), "images/sprites/close/uv/uv_4_pioneer.png",
		(126,   0), "images/sprites/close/uv/uv_4_upset.png",
	))
	
	image uv dontlike = _sr(im.Composite((703, 780),
		(  0,  28), "images/sprites/normal/uv/uv_1_body.png",
		(192, 298), "images/sprites/normal/uv/uv_1_pioneer.png",
		(240,   0), "images/sprites/normal/uv/uv_1_dontlike.png",
	))
	image uv grin = _sr(im.Composite((428, 801),
		(  0,  49), "images/sprites/normal/uv/uv_3_body.png",
		( 58, 334), "images/sprites/normal/uv/uv_3_pioneer.png",
		(143,   0), "images/sprites/normal/uv/uv_3_grin.png",
	))
	image uv guilty = _sr(im.Composite((437, 774),
		(  0,  14), "images/sprites/normal/uv/uv_4_body.png",
		( 30, 305), "images/sprites/normal/uv/uv_4_pioneer.png",
		(105,   0), "images/sprites/normal/uv/uv_4_guilty.png",
	))
	image uv laugh = _sr(im.Composite((428, 799),
		(  0,  47), "images/sprites/normal/uv/uv_3_body.png",
		( 58, 332), "images/sprites/normal/uv/uv_3_pioneer.png",
		(138,   0), "images/sprites/normal/uv/uv_3_laugh.png",
	))
	image uv normal = _sr(im.Composite((419, 801),
		(  0,  44), "images/sprites/normal/uv/uv_2_body.png",
		( 83, 310), "images/sprites/normal/uv/uv_2_pioneer.png",
		(115,   0), "images/sprites/normal/uv/uv_2_normal.png",
	))
	image uv rage = _sr(im.Composite((703, 788),
		(  0,  36), "images/sprites/normal/uv/uv_1_body.png",
		(192, 306), "images/sprites/normal/uv/uv_1_pioneer.png",
		(246,   0), "images/sprites/normal/uv/uv_1_rage.png",
	))
	image uv sad = _sr(im.Composite((703, 755),
		(  0,   3), "images/sprites/normal/uv/uv_1_body.png",
		(192, 273), "images/sprites/normal/uv/uv_1_pioneer.png",
		(215,   0), "images/sprites/normal/uv/uv_1_sad.png",
	))
	image uv shocked = _sr(im.Composite((703, 800),
		(  0,  48), "images/sprites/normal/uv/uv_1_body.png",
		(192, 318), "images/sprites/normal/uv/uv_1_pioneer.png",
		(249,   0), "images/sprites/normal/uv/uv_1_shocked.png",
	))
	image uv smile = _sr(im.Composite((418, 812),
		(  0,  55), "images/sprites/normal/uv/uv_2_body.png",
		( 83, 321), "images/sprites/normal/uv/uv_2_pioneer.png",
		(119,   0), "images/sprites/normal/uv/uv_2_smile.png",
	))
	image uv surprise = _sr(im.Composite((372, 796),
		(  0,  36), "images/sprites/normal/uv/uv_4_body.png",
		( 30, 327), "images/sprites/normal/uv/uv_4_pioneer.png",
		(109,   0), "images/sprites/normal/uv/uv_4_surprise.png",
	))
	image uv surprise2 = _sr(im.Composite((422, 821),
		(  0,  69), "images/sprites/normal/uv/uv_3_body.png",
		( 58, 354), "images/sprites/normal/uv/uv_3_pioneer.png",
		(144,   0), "images/sprites/normal/uv/uv_3_surprise2.png",
	))
	image uv upset = _sr(im.Composite((433, 765),
		(  0,   5), "images/sprites/normal/uv/uv_4_body.png",
		( 30, 296), "images/sprites/normal/uv/uv_4_pioneer.png",
		(101,   0), "images/sprites/normal/uv/uv_4_upset.png",
	))
	
	image uv dontlike far = _sr(im.Composite((527, 742),
		(  0,  20), "images/sprites/far/uv/uv_1_body.png",
		(128, 223), "images/sprites/far/uv/uv_1_pioneer.png",
		(180,   0), "images/sprites/far/uv/uv_1_dontlike.png",
	))
	image uv grin far = _sr(im.Composite((442, 758),
		(  0,  37), "images/sprites/far/uv/uv_3_body.png",
		(148, 250), "images/sprites/far/uv/uv_3_pioneer.png",
		(228,   0), "images/sprites/far/uv/uv_3_grin.png",
	))
	image uv guilty far = _sr(im.Composite((333, 738),
		(  0,  11), "images/sprites/far/uv/uv_4_body.png",
		( 13, 229), "images/sprites/far/uv/uv_4_pioneer.png",
		( 84,   0), "images/sprites/far/uv/uv_4_guilty.png",
	))
	image uv laugh far = _sr(im.Composite((442, 757),
		(  0,  36), "images/sprites/far/uv/uv_3_body.png",
		(148, 249), "images/sprites/far/uv/uv_3_pioneer.png",
		(224,   0), "images/sprites/far/uv/uv_3_laugh.png",
	))
	image uv normal far = _sr(im.Composite((324, 759),
		(  0,  34), "images/sprites/far/uv/uv_2_body.png",
		( 64, 233), "images/sprites/far/uv/uv_2_pioneer.png",
		( 96,   0), "images/sprites/far/uv/uv_2_normal.png",
	))
	image uv rage far = _sr(im.Composite((527, 748),
		(  0,  26), "images/sprites/far/uv/uv_1_body.png",
		(128, 229), "images/sprites/far/uv/uv_1_pioneer.png",
		(184,   0), "images/sprites/far/uv/uv_1_rage.png",
	))
	image uv sad far = _sr(im.Composite((527, 724),
		(  0,   2), "images/sprites/far/uv/uv_1_body.png",
		(128, 205), "images/sprites/far/uv/uv_1_pioneer.png",
		(161,   0), "images/sprites/far/uv/uv_1_sad.png",
	))
	image uv shocked far = _sr(im.Composite((527, 757),
		(  0,  35), "images/sprites/far/uv/uv_1_body.png",
		(128, 238), "images/sprites/far/uv/uv_1_pioneer.png",
		(187,   0), "images/sprites/far/uv/uv_1_shocked.png",
	))
	image uv smile far = _sr(im.Composite((323, 767),
		(  0,  42), "images/sprites/far/uv/uv_2_body.png",
		( 64, 241), "images/sprites/far/uv/uv_2_pioneer.png",
		( 99,   0), "images/sprites/far/uv/uv_2_smile.png",
	))
	image uv surprise far = _sr(im.Composite((285, 755),
		(  0,  28), "images/sprites/far/uv/uv_4_body.png",
		( 13, 246), "images/sprites/far/uv/uv_4_pioneer.png",
		( 87,   0), "images/sprites/far/uv/uv_4_surprise.png",
	))
	image uv surprise2 far = _sr(im.Composite((438, 773),
		(  0,  52), "images/sprites/far/uv/uv_3_body.png",
		(148, 265), "images/sprites/far/uv/uv_3_pioneer.png",
		(229,   0), "images/sprites/far/uv/uv_3_surprise2.png",
	))
	image uv upset far = _sr(im.Composite((331, 731),
		(  0,   4), "images/sprites/far/uv/uv_4_body.png",
		( 13, 222), "images/sprites/far/uv/uv_4_pioneer.png",
		( 81,   0), "images/sprites/far/uv/uv_4_upset.png",
	))
