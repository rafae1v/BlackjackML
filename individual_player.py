from blackjack import deck

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

			#splits the card (which is really just a string) at the first space
			temp = card.split()

			#if the first index of the returned list is a number and not a face, then add the total value
			if temp[0].isdigit():
				points += int(temp[0])

			#keeps track of number of aces and defaults to a value of 11 until bust
			elif temp[0] == 'Ace':
				points += 11
				numberOfAces +=1

			#any face card is value of 10
			else:
				points += 10

		#when there are aces and you have already busted, then it changes it to value of 1
		while numberOfAces > 0 and points > 21:
			numberOfAces -= 1
			points -= 10

		return points


		
	#Takes a card from the deck and stores it in hand. Also pops the card from the deck
	def draw(self, deck):

		self.hand.append(deck.contents[0])

		deck.draw_delete()




