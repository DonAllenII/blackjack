import random

class card_deck():
    def __init__(self):
        return
    def create_deck(self):
        self.deck = [("♠️"+str(i), "♣️"+str(i), "♥️"+str(i), "♦️"+ str(i)) for i in range(1, 14) ]
        x = []
        for i in self.deck:
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
        
        self.dealt_user = deck.pop(random.randint(0, (len(deck) -1)))

    

    # deal 'hit' card to dealer
    def hit_dealer(self, deck):
        #print(len(deck))
        hit_card = deck.pop(random.randint(0, (len(deck) -1)))
        self.dealt_dealer.append(hit_card)

    def value(self):
        value = 0
        for card in self.dealt_dealer: #iterate through hand
            pattern = re.compile('[0-9]+') #compile search group for numbers
            found = pattern.findall(card) # return all matches of number or multiple numbers
            #print(found)
            for f in found:
                #print(f)
                f = int(f)
                value += f
        self.hand_value = value


class user_hand():
    def __init__(self):
        self.hand = []

    #list of cards the dealer has
    def update_user_hand(self, cards):
        if isinstance(cards, list):
            self.hand += cards
        else: 
            self.hand.append(cards)
    
    def value(self):

        value = 0
        for card in self.hand: #iterate through hand
            pattern = re.compile('[0-9]+') #compile search group for numbers
            found = pattern.findall(card) # return all matches of number or multiple numbers
            #print(found)
            for f in found:
                #print(f)
                f = int(f)
                value += f
        self.hand_value = value
        #print(self.hand_value)