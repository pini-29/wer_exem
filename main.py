from class_game import Game
def main():
    print("===WLCOME TO THE WAR GAME===")
    name = input("Enter your name")
    a = Game(name,"computer")
    a.shuffling_cards()
    a.deal_cards()
    while True:
        print("• 1. Play turn")
        print("• 2. Exit")
        choice = input("enter your choice")
        if choice == "1":
             
             print(f"Players cards {a.player}")
             print(f"Computer cards {a.computer}")
             a.performing_turn()
             print(a.player)
             print(a.computer)
        if choice == "2":
            continue



main()


