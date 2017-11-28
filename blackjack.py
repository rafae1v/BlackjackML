import random 

class Deck():

	def __init__(self):
		suits = ['Diamonds', 'Hearts', 'Clubs', 'Spades']
		face_cards = ['Jack', 'Queen', 'King', 'Ace'] 

		self.contents = []

		for suit in suits:

			for x in range(2,11):
				self.contents.append(str(x) + ' of ' + suit)

			for face in face_cards:
				self.contents.append(face + ' of ' + suit)


		random.shuffle(self.contents)

	def draw(self):

		self.contents.pop(0)




deck1 = Deck()

print(deck.draw())

print(len(deck1.contents))


