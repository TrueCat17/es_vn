init python:
	jump_to, replay = persistent.jump_to, persistent.replay
	persistent.jump_to = persistent.replay = None

label start:
	if jump_to:
		call expression jump_to
		return
	
	call prologue
