import random
from flask import Flask, render_template, request, redirect, url_for, session

class Card:
    def __init__(self, value, type):
        self.value = value
        self.type = type
    
    def __str__(self):
        signs = 'CDHS'
        card = str(self.value)
        if self.value == 1:
            card = 'A'
        if (self.value == 13):
            card = 'K'
        if (self.value == 12):
            card = 'Q'
        if (self.value == 11):
            card = 'J'

        return str(card+signs[self.type])
    def __repr__(self):
        signs = 'CDHS'
        card = str(self.value)
        if self.value == 1:
            card = 'A'
        if (self.value == 13):
            card = 'K'
        if (self.value == 12):
            card = 'Q'
        if (self.value == 11):
            card = 'J'

        return str(card+signs[self.type])
    
def return_sum(cards):
    result = 0
    for test in range(1, len(cards)):
        num = cards[test]
        if num[0] == 'A':
            result += 1
        elif num[0] == 'K':
            result += 13
        elif num[0] == 'Q':
            result += 12
        elif num[0] == 'J':
            result += 11
        elif len(num) == 3:
            result += 10
        else:
            result += int(num[0])

    return result

class Game:
    def __init__(self, player, deck, cards, money):
        self.name = name
        self.deck = deck
        self.player = player
        self.cards = cards
        print(' Welcome to the game! ')
        
    @staticmethod
    def stop(s):
        payoff = 0
        if (s>21):
            payoff = -200
        if (s==21):
            payoff = 500
        elif (s==20):
            payoff = 300
        elif (s==19):
            payoff = 200
        elif (s==18):
            payoff = 150
        elif (s==17):
            payoff = 50
        elif (s==16):
            payoff = 10
        elif (s==15):
            payoff = -10
        elif (s==14):
            payoff = -50
        elif (s==13):
            payoff = -100
        elif (s<13):
            payoff = -100
        
        return payoff

    @staticmethod
    def deal(cards):
        deck = [Card(i,j) for i in range(1,14) for j in range(0,4)]
        random.shuffle(deck)
        check = True
        num = 0
        while check == True:
            if deck[num] in cards:
                num += 1
            else:
                cards.append(str(deck[num]))
                check = False
        return cards

    @staticmethod
    def all_cards(cards):
        result = []
        for num in range(1, len(cards)):
            result.append(cards[num])
        return result