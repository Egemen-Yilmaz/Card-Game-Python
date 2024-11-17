#!/usr/bin/env python
# coding: utf-8

# In[86]:


# We'll use this later
import random 


# In[87]:


suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 
            'Nine':9, 'Ten':10, 'Jack':11, 'Queen':12, 'King':13, 'Ace':14}


# In[88]:


class Card:
    
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]
        
    def __str__(self):
        return self.rank + ' of ' + self.suit
        


# In[89]:


class Deck:
    
    def __init__(self):
        
        self.all_cards = []
        
        for suit in suits:
            for rank in ranks:
                #Create the card object
                create_card = Card(suit,rank)
                
                self.all_cards.append(create_card)
   
    def shuffle(self):
        # Note this doesn't return anything
        random.shuffle(self.all_cards)
        
    
    def deal_one(self):
        # Note we remove one card from the list of all_cards
        return self.all_cards.pop()        


# In[90]:


new_deck = Deck()


# In[91]:


bottom_card = new_deck.all_cards[-1]


# In[92]:


for card_object in new_deck.all_cards:
    print(card_object)


# In[93]:


class Player:
    
    def __init__(self,name):
        
        self.name = name
        self.all_cards = []
        
    def remove_one(self):
        return self.all_cards.pop(0)
    
    def add_cards(self,new_cards):
        
        if type(new_cards) == type([]):
            # List of multiple Card objects
            self.all_cards.extend(new_cards)
        else:
            # For a single card object
            self.all_cards.append(new_cards)
    
    
    def __str__(self):
        return f'Player {self.name} has {len(self.all_cards)} cards'
    


# In[104]:


# GAME SETUP
player_one = Player(input('Who is player 1 ?  :'))
player_two = Player(input('Who is player 2 ?  :'))

# shuffle deck
new_deck = Deck()
new_deck.shuffle()


for x in range(26):
    player_one.add_cards(new_deck.deal_one())
    player_two.add_cards(new_deck.deal_one())
    
    


# In[105]:


game_on = True

round_num = 0

# while game_on
while game_on:
    
    round_num += 1
    print(f"Round {round_num}")
    
    if len(player_one.all_cards) == 0:
        print(f'{player_one}, out of cards! {player_two} Wins!')
        game_on = False
        break
        
    if len(player_two.all_cards) == 0:
        print(f'{player_two}, out of cards! {player_one} Wins!')
        game_on = False
        break
        
        
        
    # START A NEW ROUND
    # cards on table:
    player_one_cards = []
    player_one_cards.append(player_one.remove_one())
    
    player_two_cards = []
    player_two_cards.append(player_two.remove_one())
    
    
    

    #while at_war
    at_war = True
    
    while at_war:
        
        if player_one_cards[-1].value > player_two_cards[-1].value:
        
            player_one.add_cards(player_one_cards)
            player_one.add_cards(player_two_cards)
            
            at_war = False
            
        elif player_one_cards[-1].value < player_two_cards[-1].value:
        
            player_two.add_cards(player_one_cards)
            player_two.add_cards(player_two_cards)
            
            at_war = False
            
        else:
            print('WAR!!')
            
            if len(player_one.all_cards) < 5:
                print(f"{player_one} unable to declare war.")
                print(f"{player_two} WİNS!")
                game_on = False
                break
            
            elif len(player_two.all_cards) < 5:
                print(f"{player_two} unable to declare war.")
                print(f"{player_one} WINS!")
                game_on = False
                break
                
            else:
                for num in range(5):
                    player_one_cards.append(player_one.remove_one())
                    player_two_cards.append(player_two.remove_one())
                

