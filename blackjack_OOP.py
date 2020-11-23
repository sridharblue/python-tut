import random
#declaring global variables to store suits, ranks and values.
suits = ('Hearts', 'Culbs', 'Diamonds', 'Spades')
ranks = ('Two','Three' ,'Four' ,'Five' ,'Six' ,'Seven' ,'Eight' ,'Nine' ,'Ten' ,'Jack' ,'Queen' ,'King' ,'Ace')
values = {'Two':2,'Three':3 ,'Four':4 ,'Five':5 ,'Six':6 ,'Seven':7 ,'Eight':8 ,'Nine':9 ,'Ten':10 ,'Jack':11 ,'Queen':12 ,'King':13 ,'Ace':14}

playing = True

#class for a card in a deck
class Card():
    def __init__(self,rank,suit):
        self.rank = rank
        self.suit = suit
        self.value = values[rank]

    def __str__(self):
        return self.rank + ' of ' + self.suit

#testing the card class
# c= Card(ranks[0],suits[0]) # c variable has 'two of hearts'
# print(c)
# print(c.value)
# print(values[c.rank])

#class for deck of cards
class Deck():
    def __init__(self):
        self.deck_of_cards = [] #empty deck list to store cards
        for suit in suits:
            for rank in ranks:
                self.deck_of_cards.append(Card(rank,suit)) #appending the cards class value to deck
    
    def __str__(self):
        deck_comp = ''
        for card in self.deck_of_cards:
            deck_comp += '\n'+card.__str__()
        return 'Deck has: '+deck_comp

    def shuffle(self):
        random.shuffle(self.deck_of_cards)
                
    def deal_one(self):
        return self.deck_of_cards.pop()

# d = Deck()
# print(len(d.deck_of_cards))
# print(d)
# d.shuffle()
# print(d)
# my_card = d.deal_one()
# print('my card:', my_card)

#class for cards in the player's hand
class Hand:
    def __init__(self):
        self.cards = []  # empty list to store cards in hand
        self.value = 0   # value will be with no cards in hand
        self.aces = 0    # an attribute to keep track of aces
    
    def add_card(self,card):
        self.cards.append(card)
        self.value += values[card.rank]
        if card.rank == 'Ace':
            self.aces += 1 
    
    def adjust_for_ace(self):
        while self.value > 21 and self.aces > 0:
            self.value -= 10
            self.aces -= 1
         
# testd = Deck()
# testd.shuffle()
# pulled_card = testd.deal_one()
# print(pulled_card)
# testp = Hand()
# testp.add_card(pulled_card)
# print(testp.value)
# testp.add_card(testd.deal_one())
# print(testp.value)

#creating a class for chips
class Chips:
    
    def __init__(self):
        self.total = 100  # default number of chips will be 100
        self.bet = 0
        
    def win_bet(self):
        self.total  += self.bet
    
    def lose_bet(self):
        self.total -= self.bet

#function for taking bets 
def take_bet(chips):
    
    while True:
        try:
            chips.bet = int(input('How many chips would you like to bet?: '))
        except:
            print('Please enter an integer value')
        else:
            if chips.bet > chips.total:
                print(f'You do not enough chips, you have:{chips.total}')
            else:
                break
#function for taking hits   
def hit(deck,hand):
    
    single_card = deck.deal_one()
    hand.add_card(single_card)
    hand.adjust_for_ace()

#function prompting the Player to Hit or Stand
def hit_or_stand(deck,hand):
    global playing  # to control an upcoming while loop
    
    while True:
        x = input('Hit or Stand, Please enter h or s: ')
        if x[0].lower() == 'h':
            hit(deck,hand) # hit() function defined above
        elif x[0].lower() == 's':
            print("Player stands Dealer's turn")
            playing =False
        else:
            print('Invalid option, Please enter h or s only!')
            continue
        break

#functions to display cards
def show_some(player,dealer):
    print("\nDealer's Hand:")
    print(" <card hidden>")
    print('',dealer.cards[1])  
    print("\nPlayer's Hand:", *player.cards, sep='\n ')
    
def show_all(player,dealer):
    print("\nDealer's Hand:", *dealer.cards, sep='\n ')
    print("Dealer's Hand =",dealer.value)
    print("\nPlayer's Hand:", *player.cards, sep='\n ')
    print("Player's Hand =",player.value)

#functions to handle end of game scenarios
def player_busts(player,dealer,chips):
    print('PLAYER BUSTS!')
    chips.lose_bet()

def player_wins(player,dealer,chips):
    print('PLAYER WINS!!!')
    chips.win_bet()

def dealer_busts(player,dealer,chips):
    print('DEALER BUSTS!')
    chips.win_bet()
    
def dealer_wins(player,dealer,chips):
    print('DEALER WINS!!!')
    chips.lose_bet()
    
def push(player,dealer):
    print('PLAYER and DEALER TIE! PUSH')

while True:
    print('Welcome to BlackJack')
#Creates & shuffles the deck, deal two cards to each player
    deck = Deck()
    deck.shuffle()

    player_hand = Hand()
    player_hand.add_card(deck.deal_one())
    player_hand.add_card(deck.deal_one())

    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal_one())
    dealer_hand.add_card(deck.deal_one())

# Set up the Player's chips
    player_chips = Chips() #default will 100 chips

# Prompt the Player for their bet
    take_bet(player_chips)

# Show cards (but keeps one dealer card hidden)
    show_some(player_hand,dealer_hand)

    while playing: 
# Prompts for Player to Hit or Stand        
        hit_or_stand(deck,player_hand)

# Show cards (but keep one dealer card hidden)
        show_some(player_hand,dealer_hand)

# If player's hand exceeds 21, run player_busts() and break out of loop
        if player_hand.value > 21:
            player_busts(player_hand,dealer_hand,player_chips)
            break

# If Player hasn't busted, play Dealer's hand until Dealer reaches 17
    if player_hand.value <= 21:
        while dealer_hand.value < 17:
            hit(deck,dealer_hand)

 # Show all cards
        show_all(player_hand,dealer_hand)

# Run different winning scenarios
        if dealer_hand.value > 21:
            dealer_busts(player_hand,dealer_hand,player_chips)
        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_hand,dealer_hand,player_chips)
        elif dealer_hand.value < player_hand.value:
            player_wins(player_hand,dealer_hand,player_chips)
        else:
            push(player_hand, dealer_hand)

# Inform Player of their chips total
    print(f'Player total chips are at: {player_chips.total}')

 # Ask to play again
    new_game = input('Do you wanna play again y/n: ')
    if new_game[0].lower() == 'y':
        playing = True
        continue
    else:
        print('Thank you for playing BlackJack')
        break



            









        

