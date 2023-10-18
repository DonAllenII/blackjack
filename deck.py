import random
from IPython.display import clear_output
import re


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


class Game():
    def __init__(self):
        pass

                    
    def run(self):
        while True:
            answer =  str(input("Press 'N' for a new game\nPress 'Q' to quit\n"))
            if answer.lower() == "q":
                break

            if answer.lower() == "n":
                
                deck = card_deck() #create new deck object
                deck.create_deck() #from deck object run create new deck

                user = user_hand() #create user object
                
                Dealer = dealer() #create new dealer object
                Dealer.deal(deck.deck) #dealer deals cards to user, dealer
                user.update_user_hand(Dealer.dealt_user) #user attributes dealt cards from dealer
                
                clear_output()     
                
                while True:
                    #clear_output()
                    print("Dealer's hand:\n{dValue}".format(dValue = Dealer.dealt_dealer[0])) #show dealer 1st card
                    print("\n\nUser's hand:\n{uValue}\n".format(uValue = user.hand)) #show usr hand

                    #check if usr hand equals 21, if true usr wins
                    user.value()
                    if user.hand_value == 21:
                        print("User has BlackJack!!! You win!!")
                        break
                         
                    action = str(input("Would you like to hit/stay?\nPress H for hit/ Press S to stand\n"))
                    if action.lower() == "h":
                        Dealer.hit(deck.deck)  #dealer deals from the deck
                        user.update_user_hand(Dealer.dealt_user)  #usr hand updates to reflect dealt card
                        user.value() #calculate usr hand value
                        clear_output()
                        print("Dealer's hand:\n{dValue}".format(dValue = Dealer.dealt_dealer[0]))
                        print("\n\nUser's hand:\n{uValue}\n".format(uValue = user.hand))
                        
                        if user.hand_value == 21:
                            print("User has 21!!! You win!!")
                            break
                        if user.hand_value > 21:
                            print("User Busts!!!!\n Sorry you lose!")
                            break
            

                    if action.lower() == "s":
                        clear_output()
                        print("Dealer's hand:")
                        print(Dealer.dealt_dealer)
            
                        while True:
                            clear_output()
                            print("Dealer's hand:")
                            print(Dealer.dealt_dealer)
                            print("\n")
                            print("\n\nUser's hand:\n{uValue}".format(uValue = user.hand))
                            Dealer.value()
                            user.value()
                            #print(f'dealer value is {Dealer.hand_value}')
                            if Dealer.hand_value > 21:
                                print("Dealer busts!!!!\n You win!!!")
                                break
                            if Dealer.hand_value <= 21 & Dealer.hand_value > user.hand_value:
                                print("Dealer has {dValue}.\nUser has {uValue}. You lose!!".format(dValue = Dealer.hand_value, uValue = user.hand_value))
                                break
                            if Dealer.hand_value == 21 and user.hand_value == 21:
                                print("push!!")
                            Dealer.hit_dealer(deck.deck)
                        break
                        
            #if answer.lower() == "rules":

            #if answer.lower() == "help":

game = Game()

game.run()