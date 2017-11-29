from individual_player import Player
from blackjack import Deck

#defines a game/table instance
class Table():

	def __init__(self):

		self.player1 = Player('player1')
		self.dealer = Player('dealer')

		self.playerList = [self.player1, self.dealer]

		self.deck = Deck()

	# iterate through playerList and draw cards
	def dealHand(self):
		for player in self.playerList:
			player.draw(self.deck)
			player.draw(self.deck)

	# Add up points using calculate method from individual_player
	def getPlayerScore(self):
		return self.player1.addUpTotal()

	def getDealerScore(self):
		return self.dealer.addUpTotal()

	# Step or iterate function that takes a table, points of both player and dealer, actions of both, and rewards for both
	def hitPlayer(self):
		self.player1.draw(self.deck)

	def playDealer(self):
		while self.getDealerScore() < 17:
			self.dealer.draw(self.deck)
