class card_deck():
    def __init__(self):
        pass
    def create_deck(self):
        self.deck = [("♠️"+str(i), "♣️"+str(i), "♥️"+str(i), "♦️"+ str(i)) for i in range(2, 12) ]
        x = []
        for i in deck.deck:
            x += i
        self.deck = x