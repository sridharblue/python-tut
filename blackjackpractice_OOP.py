import random
suits = ('Hearts', 'Culbs', 'Diamonds', 'Spades')
ranks = ('Two','Three' ,'Four' ,'Five' ,'Six' ,'Seven' ,'Eight' ,'Nine' ,'Ten' ,'Jack' ,'Queen' ,'Kings' ,'Ace')
values = {'Two':2,'Three':3 ,'Four':4 ,'Five':5 ,'Six':6 ,'Seven':7 ,'Eight':8 ,'Nine':9 ,'Ten':10 ,'Jack':11 ,'Queen':12 ,'Kings':13 ,'Ace':14}

#class for a card in a deck
class Card():
    def __init__(self,rank,suit):
        self.rank = rank
        self.suit = suit
        self.value = values[rank]

    def __str__(self):
        return self.rank + ' of ' + self.suit

c= Card(ranks[0],suits[0]) # c variable has 'two of hearts'
# print(c)
# print(c.value)
# print(values[c.rank])

#class for deck of cards
class Deck():
    def __init__(self):
        self.deck_of_cards = []
        for suit in suits:
            for rank in ranks:
                self.deck_of_cards.append(Card(rank,suit))
    
    def shuffle(self):
        random.shuffle(self.deck_of_cards)
                
    def deal_one(self):
        return self.deck_of_cards.pop()

d = Deck()
# print(len(d.deck_of_cards))
# print(d.deck_of_cards[0])
# d.shuffle()
# print(d.deck_of_cards[0])
# my_card = d.deal_one()
# print('my card:', my_card)

#class for Player
class Player():
    def __init__(self,name):
        self.name = name
        #new player has no cards
        self.deck_of_cards = []
    
    def remove_one(self):
        return self.deck_of_cards.pop(0)
    
    def add_cards(self,new_cards):
        if type(new_cards) == type([]):
            self.deck_of_cards.extend(new_cards)
        else:
            self.deck_of_cards.append(new_cards)

    def __str__(self):
        return f'Player {self.name} has {len(self.deck_of_cards)} cards.'

sri = Player('Sridhar')
print(sri)
sri.add_cards(c)
print(sri)
sri.add_cards([c,c,c])
print(sri)

#War Game Logic
player_one = Player("One")
player_two = Player("Two")

#Setup New Game
new_deck = Deck()
#shuffle the deck
new_deck.shuffle()

#Split the Deck between players
print(len(new_deck.deck_of_cards)/2)
for x in range(26):
    player_one.add_cards(new_deck.deal_one())
    player_two.add_cards(new_deck.deal_one())

print(len(new_deck.deck_of_cards))
print(len(player_one.deck_of_cards))
print(len(player_two.deck_of_cards))




