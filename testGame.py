from game_table import Table

# Simulates a game of blackjack
print("Leggo......")

table = Table()
table.dealHand()

busted = False

print("Dealer is showing:")
print(table.dealer.hand[0])
print("Player's hand:")
score = table.getPlayerScore()
if table.player1.numberOfAces > 0:
    print(table.player1.hand[0], ",", table.player1.hand[1], ": soft", score)
else:
    print(table.player1.hand[0],",", table.player1.hand[1], ":", score)
print()
response = input("Would you like to hit or stay? (h/s)")
while response == 'h':
    table.player1.draw(table.deck)
    if table.getPlayerScore() > 21:
        busted = True
        print("Player's hand:")
        for card in table.player1.hand:
            print(card,end=', ')
        print()
        print("You busted with a score of", table.getPlayerScore())
        break
    else:
        print("Player's hand:")
        for card in table.player1.hand:
            print(card, end=', ')
        print()
        score = table.getPlayerScore()
        if table.player1.numberOfAces > 0:
            print("Current score: soft", score)
        else:
            print("Current score:", score)
    print()
    response = input("Would you like to hit or stay? (h/s)")

if not busted:
    table.playDealer()
    print("Dealer's hand:")
    for card in table.dealer.hand:
        print(card, end=', ')
    print(":", table.getDealerScore())
    if table.getPlayerScore() == 21 and table.getDealerScore() < table.getPlayerScore():
        print("BLACKJACK... YOU WIN!")
    elif table.getDealerScore() > 21:
        print("Dealer busted... YOU WIN!")
    elif table.getDealerScore() > table.getPlayerScore():
        print("You lose")
    elif table.getPlayerScore() == table.getDealerScore():
        print("push")
    else:
        print("YOU WIN!")
