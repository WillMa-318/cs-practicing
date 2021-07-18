from blackjack import Card, Game, return_sum
from user import User
class check:
    def __init__ (self, a, b = 0):
        self.a = a
        self.b = b

def main():
    cards = ['Ks', 'Js', '6A', '8D']
    print (return_sum(cards))

    cards = ['malin']
    Game.deal(cards)
    cards.append('KS')
    print(cards)
    show = Game.all_cards(cards)
    sum_card = return_sum(cards)
    
if __name__ == "__main__":
    main()