init -50 python:
	class CardGameRival:
		def __init__(self, avatar, name):
			self.avatar = 'images/avatars/%s.webp' % (avatar, )
			self.name = name
		
		def pick_my_card_last(self):
			for i in range(n_cards):
				if cards_my[i].interesting:
					x = i
			return x
		
		def allow_to_take(self):
			for card in cards_rival:
				card.allow = True
		
		def allow_to_defend(self):
			return True
		
		def want_to_defend(self):
			return True
		
		def what_to_xchange(self):
			i = random.randrange(n_cards)
			j = i
			while j == i:
				j = random.randrange(n_cards)
			return (i, j)
		
		def give_away_card(self):
			return random.randrange(n_cards)
	
	
	class CardGameRivalUn(CardGameRival):
		def pick_my_card(self):
			while True:
				x = random.randrange(n_cards)
				if cards_my[x].name != name_of_none and not cards_my[x].interesting:
					return x
		
		def pick_my_card_last(self):
			return self.pick_my_card()
	
	
	class CardGameRivalUs(CardGameRival):
		def pick_my_card(self):
			if not cards_answer:
				return -1
			owner, index = cards_answer
			return index
		
		def allow_to_take(self):
			for card in cards_rival:
				card.allow = False
			while True:
				card = random.choice(cards_rival)
				if not card.hot:
					card.allow = True
					card.interesting = True
					return
		
		def want_to_defend(self):
			return False
		
		def allow_to_defend(self):
			return False
	
	
	class CardGameRivalDv(CardGameRival):
		def what_to_xchange(self):
			for i in range(n_cards):
				if cards_rival[i].interesting:
					break
			j = i
			while j == i:
				j = random.randrange(n_cards)
			return (i, j)
		
		def pick_my_card(self):
			x_set = []
			for i in range(n_cards):
				if cards_my[i].hot and cards_my[i].name != name_of_none:
					x_set.append(i)
			
			if x_set:
				return random.choice(x_set)
			
			while True:
				x = random.randrange(n_cards)
				if cards_my[x].name != name_of_none:
					return x
		
		def pick_my_card_last(self):
			return self.pick_my_card()