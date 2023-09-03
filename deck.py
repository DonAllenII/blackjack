class card_deck():
    def __init__(self):
        pass
    def create_deck(self):
        self.deck = [("♠️"+str(i), "♣️"+str(i), "♥️"+str(i), "♦️"+ str(i)) for i in range(2, 12) ]
        x = []
        for i in deck.deck:
            x += i
        self.deck = x


class dealer():
    def __init__(self):
        self.hand = []
        
    # deal initial hand to user
    def deal(self, deck):
        
        #self.dealt_user = deck.pop(random.randint(0, (len(deck) -1)))
        self.dealt_user = [deck.pop(random.randint(0, (len(deck) -1))) for i in range(0,2)]
        self.dealt_dealer = [deck.pop(random.randint(0, (len(deck) -1))) for i in range(0,2)]
    

    # deal 'hit' card to user
    def hit(self, deck):
        self.dealt_user.append(deck.pop(random.randint(0, (len(deck) -1))))

    

    # deal 'hit' card to dealer
    def hit_dealer(self, deck):
        self.dealt_dealer.append(deck.pop(random.randint(0, (len(deck) -1))))


class user_hand():
    def __init__(self):
        self.hand = []

    #list of cards the dealer has
    def update_user_hand(self, cards):
        self.hand += cards
