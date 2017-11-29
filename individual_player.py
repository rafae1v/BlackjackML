from blackjack import Deck

class Player():


	#identifiable name and initializes empty hand. Also introduces point system
	def __init__(self, name):

		self.hand = []
		self.name = name
		self.points = 0


	#Caclutes the points that a player currently has in his hand and handles the Ace dilema
	def addUpTotal(self):

		points = 0
		numberOfAces = 0

		for card in self.hand:
			#keeps track of number of aces
			if card.rank == 'Ace':
				numberOfAces +=1

			#add value of current card to points
			points += card.value

		#when there are aces and you have already busted, then it changes it to value of 1
		while numberOfAces > 0 and points > 21:
			numberOfAces -= 1
			points -= 10

		return points


		
	#Takes a card from the deck and stores it in hand. Also pops the card from the deck
	def draw(self, deck):
		self.hand.append(deck.draw())




