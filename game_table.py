from individual_player import Player
from blackjack import Deck

#defines a game/table instance
def Table():

	def __init__(self):

		self.player1 = Player('player1')
		self.player2 = Player('player2')
		self.dealer = Player('dealer')

		self.playerList = [self.player1, self.player2, self.dealer]

		

		
