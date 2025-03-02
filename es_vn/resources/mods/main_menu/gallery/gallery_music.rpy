init python:
	
	music_box = [
		("Opening Theme", "sound/music/everlasting_summer_op_edition.ogg"),
		("A Promise From Distant Days", "sound/music/a_promise_from_distant_days.ogg"),
		("A Promise From Distant Days v.2", "sound/music/a_promise_from_distant_days_v2.ogg"),
		("Afterword", "sound/music/afterword.ogg"),
		("Always Ready", "sound/music/always_ready.ogg"),
		("Awakening Power", "sound/music/awakening_power.ogg"),
		("Blow With The Fires", "sound/music/blow_with_the_fires.ogg"),
		("Confession", "sound/music/confession.ogg"),
		("Dance Of Fireflies", "sound/music/dance_of_fireflies.ogg"),
		("Doomed To Be Defeated", "sound/music/doomed_to_be_defeated.ogg"),
		("Door To Nightmare", "sound/music/door_to_nightmare.ogg"),
		("Drown", "sound/music/drown.ogg"),
		("Eat Some Trouble", "sound/music/eat_some_trouble.ogg"),
		("Eternal Longing", "sound/music/eternal_longing.ogg"),
		("Everlasting Summer", "sound/music/everlasting_summer.ogg"),
		("Feeling Good", "sound/music/feeling_good.ogg"),
		("Faceless", "sound/music/faceless.ogg"),
		("Farewell To The Past (Short ver.)", "sound/music/farewell_to_the_past_short.ogg"),
		("Farewell To The Past", "sound/music/farewell_to_the_past.ogg"),
		("Forest Maiden", "sound/music/forest_maiden.ogg"),
		("Gentle Predator", "sound/music/gentle_predator.ogg"),
		("Get To Know Me Better", "sound/music/get_to_know_me_better.ogg"),
		("Glimmering Coals", "sound/music/glimmering_coals.ogg"),
		("Goodbye Home Shores", "sound/music/goodbye_home_shores.ogg"),
		("Heather", "sound/music/heather.ogg"),
		("I Don't Blame You", "sound/music/i_dont_blame_you.ogg"),
		("I Want To Play", "sound/music/i_want_to_play.ogg"),
		("Into The Unknown", "sound/music/into_the_unknown.ogg"),
		("Just Think", "sound/music/just_think.ogg"),
		("Let's Be Friends", "sound/music/lets_be_friends.ogg"),
		("Lightness", "sound/music/lightness.ogg"),
		("Lightness (Radio edit)", "sound/music/lightness_radio.ogg"),
		("Meet Me There", "sound/music/meet_me_there.ogg"),
		("Memories", "sound/music/memories.ogg"),
		("Memories (Piano Outdoors)", "sound/music/memories_piano_outdoors.ogg"),
		("Miku Song", "sound/music/miku_song_voice.ogg"),
		("My Daily Life", "sound/music/my_daily_life.ogg"),
		("Mystery Girl", "sound/music/mystery_girl.ogg"),
		("No Tresspassing", "sound/music/no_tresspassing.ogg"),
		("Orchid", "sound/music/orchid.ogg"),
		("Pile", "sound/music/pile.ogg"),
		("Raindrops", "sound/music/raindrops.ogg"),
		("Reflection On Water", "sound/music/reflection_on_water.ogg"),
		("Reminiscences", "sound/music/reminiscences.ogg"),
		("Revenga", "sound/music/revenga.ogg"),
		("Scarytale", "sound/music/scarytale.ogg"),
		("She Is Kind", "sound/music/she_is_kind.ogg"),
		("Silhouette In Sunset", "sound/music/silhouette_in_sunset.ogg"),
		("Smooth Machine", "sound/music/smooth_machine.ogg"),
		("So Good To Be Careless", "sound/music/so_good_to_be_careless.ogg"),
		("Sparkles", "sound/music/sparkles.ogg"),
		("Sunny Day", "sound/music/sunny_day.ogg"),
		("Sweet Darkness", "sound/music/sweet_darkness.ogg"),
		("Take Me Beautifully", "sound/music/take_me_beautifully.ogg"),
		("That's Our Madhouse", "sound/music/that_s_our_madhouse.ogg"),
		("Timid Girl", "sound/music/timid_girl.ogg"),
		("Torture", "sound/music/torture.ogg"),
		("Trapped In Dreams", "sound/music/trapped_in_dreams.ogg"),
		("Tried To Bring It Back", "sound/music/tried_to_bring_it_back.ogg"),
		("Two Glasses Of Melancholy", "sound/music/two_glasses_of_melancholy.ogg"),
		("Waltz Of Doubts", "sound/music/waltz_of_doubts.ogg"),
		("Went Fishing Caught A Girl", "sound/music/went_fishing_caught_a_girl.ogg"),
		("What Do You Think Of Me", "sound/music/what_do_you_think_of_me.ogg"),
		("You Lost Me", "sound/music/you_lost_me.ogg"),
		("You Won't Let Me Down", "sound/music/you_won_t_let_me_down.ogg"),
		("Your Bright Side", "sound/music/your_bright_side.ogg"),
		("410", "sound/music/410.ogg"),
	]
	music_box.sort()
	
	music_page_size = 10
	music_page = 0
	music_page_max = math.ceil(len(music_box) / music_page_size)
	
	def get_music_on_page():
		start = music_page * music_page_size
		end   = start + music_page_size
		return music_box[start : end]
	
	def on_gallery_hided(screen_name):
		if screen_name == 'gallery' and renpy.music.get_playing('music') != main_menu_bgm:
			renpy.play(main_menu_bgm, fadeout = 1, fadein = 1)
	signals.add('hide_screen', on_gallery_hided)


init:
	style music_btn is title_btn:
		text_align 'left'
		xsize 0.6
		ysize 80 / 1080
	
	style music_btn_blocked is music_btn:
		mouse False
		color       '#4F4F4F'
		hover_color '#4F4F4F'


screen gallery_music:
	vbox:
		pos (0.235, 0.14)
		
		for name, path in get_music_on_page():
			textbutton name:
				style 'music_btn' if renpy.seen_audio(path) else 'music_btn_blocked'
				selected path == renpy.music.get_playing('music')
				action renpy.play(path, fadeout = 1, fadein = 1)
	
	if music_page:
		button:
			style 'gallery_prev_btn'
			action 'music_page -= 1'
		key 'LEFT' action 'music_page -= 1'
	
	if music_page != music_page_max - 1:
		button:
			style 'gallery_next_btn'
			action 'music_page += 1'
		key 'RIGHT' action 'music_page += 1'
	
	text (str(music_page + 1) + '/' + str(music_page_max)):
		style 'gallery_page'
