import random
import csv

class Card:
    def __init__(self, value, type):
        self.value = value
        self.type = type
    
    def __str__(self):
        signs = '♠♥♣♦'
        card = str(self.value)
        if self.value == 1:
            card = 'A'
        if (self.value == 13):
            card = 'K'
        if (self.value == 12):
            card = 'Q'
        if (self.value == 11):
            card = 'J'

        return card+signs[self.type]
    def __repr__(self):
        signs = '♠♥♣♦'
        card = str(self.value)
        if self.value == 1:
            card = 'A'
        if (self.value == 13):
            card = 'K'
        if (self.value == 12):
            card = 'Q'
        if (self.value == 11):
            card = 'J'

        return card+signs[self.type]

class Deck:
    def __init__(self):
        self.cards = [Card(i,j) for i in range(1,14) for j in range(0,4)]
    
    def __str__(self):
        return str(self.cards)

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self):
        top = self.cards[0]
        self.cards.pop(0)
        return top

class Player:
    def __init__(self, name):
        self.name = name
        self.cards = []
        self.money = 1000
    
    def __str__ (self):
        return self.name

    def __repr__ (self):
        return self.name
    
    def get_sum(self):
        return sum([card.value for card in self.cards])

    def add_card(self, card):
        self.cards.append(card)

class Game:
    def __init__(self, player):
        self.deck = Deck()
        self.player = player
        self.player.cards = []
        self.player.money -= 100
        self.deck.shuffle()
        print(' Welcome to the game! ')


    def turn(self):
        card = self.deck.deal()
        self.player.add_card(card)

        print('You cards: ' + str(self.player.cards))

        if (self.player.get_sum() > 21):
            return False
        elif (self.player.get_sum() <= 21):
            tem = []
            with open('cards.csv') as file:
                csv_reader = csv.reader(file, delimiter = ',')
                for data in csv_reader:
                    tem.append(data)
                
            for data in tem:
                if data[0] == self.player.name:
                    data.append(card)
            
            with open('cards.csv', 'w', newline='') as file:
                csv_writer = csv.writer(file, delimiter = ',')
                for row in tem:
                    csv_writer.writerow(row)

            return True
        
    
    def stop(self):
        s = self.player.get_sum()
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

        
        self.player.money += payoff
        
        return payoff

def load(name):
    tem = []
    result = []
    with open('cards.csv') as file:
        csv_reader = csv.reader(file, delimiter = ',')
        for data in csv_reader:
            tem.append(data)
    
    for each in tem:
        if each[0]==name:
            for i in range(1, len(each)):
                result.append(each[i])

    return result

def check_c(lists):
    result = 0
    for card in lists:
        num = card[0]
        if(num == 'A'):
            result += 1
        elif(num == 'K'):
            result += 13
        elif(num == 'Q'):
            result += 12
        elif(num == 'J'):
            result += 11
        else:
            result += int(num) 
    return result

def clear_c(name):
    tem = []
    result = []
    with open('cards.csv') as file:
        csv_reader = csv.reader(file, delimiter = ',')
        for data in csv_reader:
            tem.append(data)
    
    for each in tem:
        if each[0]==name:
            each = [name]
    
    with open('cards.csv', 'w', newline='') as file:
        csv_writer = csv.writer(file, delimiter = ',')
        for row in tem:
            csv_writer.writerow(row)
    
