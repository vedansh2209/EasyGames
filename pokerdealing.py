from random import sample
import os

clear = lambda: os.system('cls')
cards = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
suits = ["Spades", "Clubs", "Hearts", "Diamonds"]

def generate_deck():
    deck = []
    for card in cards:
        for suit in suits:
            temp_card = [card, suit]
            deck.append(temp_card)
    return deck

ordered_deck = generate_deck()

def flip(deck):
    burn = []
    flop = []
    river = None
    turn = None

    for i in range(0, 8):
        if i == 0 or i == 4 or i == 6:
            burn.append(deck.pop())
        elif i == 1 or i == 2 or i == 3:
            flop.append(deck.pop())
        elif i == 5:
            turn = deck.pop()
        elif i == 7:
            river = deck.pop()

    print ("Flop:")
    for card in flop:
        print (card)
    print ("Turn:")
    print (turn)
    print ("River:")
    print (river)
    print ('\n')

def deal(me, cpus):
    print ('\n')
    shuffled_deck = sample(ordered_deck, len(ordered_deck))
    total_cpus = len(cpus)

    for i in range(0,2):
        me.append(shuffled_deck.pop())

    print ("My Hand: ")
    for card in me:
        print (card)
    print ('\n')

    for i in range(1, total_cpus +1):
        temp_hand = []
        for j in range(0,2):
            temp_hand.append(shuffled_deck.pop())
        cpus[i] = temp_hand

    for key, values in cpus.items():
        print ("CPU" + str(key))
        for value in values:
            print (value)
        print ('\n')

    flip(shuffled_deck)

def hand():
    players = int(input("How many players? (2-8): "))
    my_hand = []
    CPU_players = {}

    for i in range(1, players):
        CPU_players[i] = "CPU"
    #print (CPU_players)
    deal(my_hand, CPU_players)

def main():
    play = True
    while play:
        hand()
        play = 'y' in input("Deal Again? (y/n)").lower()
        clear()
main()
