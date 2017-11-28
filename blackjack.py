import random


class Deck():

    class Card:
        def __init__(self, card_suit, card_rank):
            self.suit = card_suit
            self.rank = card_rank
            if card_rank in range(2,11):
                self.value = self.rank
            elif card_rank == 'Ace':
                self.value = 11
            else:
                self.value = 10

        def __str__(self):
            return str(self.rank) + " of " + str(self.suit)

    def __init__(self):
        suits = ['Diamonds', 'Hearts', 'Clubs', 'Spades']
        face_cards = ['Jack', 'Queen', 'King', 'Ace']

        self.contents = []

        for suit in suits:
            for x in range(2, 11):
                self.contents.append(self.Card(suit,x))

            for face in face_cards:
                self.contents.append(self.Card(suit,face))
        random.shuffle(self.contents)

    def draw(self):
        return self.contents.pop(0)


deck1 = Deck()

print(deck1.draw())

print(len(deck1.contents))
