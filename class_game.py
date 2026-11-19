import random
from class_card import Card
from class_player import Player
class Game:
    def __init__(self,player_name,computer):
        card = Card()
        players = Player(player_name,computer)
        self.player = players.player_cards
        self.computer = players.computer_cards
        self.card = card.cards
    def shuffling_cards(self):
        for i in range(1000):
            a = self.card.pop()            
            b = random.randint(0,len(self.card)-1)
            self.card.insert(b,a)
    def deal_cards(self):
        for i in range(len(self.card)):
            if i %2 == 0:
                self.player.append(self.card[i])
                
            else:
                self.computer.append(self.card[i])
                
        
            
    def performing_turn(self):
        p = self.player[0]
        com = self.computer[0]
        print(f"The player choice {p}")
        print(f"The computer choice {com}")
        if p > com:
            print("========== TURN ==========")
            print(f"• Player: {p} ")
            print(f"• Computer: {com}")
            print("• Player won the round!")
            self.player.append(com)
            self.computer.remove(com)
            if len(self.computer) == 0:
                print("The player won the game!")
                return
            
        elif com > p:
            print("========== TURN ==========")
            print(f"• Player: {p} ")
            print(f"• Computer: {com}")
            print("• Computer won the round!")
            self.computer.append(p)
            self.player.remove(p)
            if len(self.player) == 0:
                print("Computer won the game!")
                return
        elif com == p:
            print("========== TURN ==========")
            print(f"• Player: {p} ")
            print(f"• Computer: {com}")
            print("• Its a draw!")
