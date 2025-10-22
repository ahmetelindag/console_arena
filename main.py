from game.character import Warrior, Wizard

def start_game():
    print("----Welcome to the console arena!----\n")
    print("Console Arena Begins!\n")
    

    player1 = Warrior(name="try")
    player2 = Wizard(name="Merlin")
    
    print("-" * 30) 
    print("War is Begin!")
    print("="*30)
    
#  First status of characters
    player2.check_status()
   

    player1.attack(player2)
    
    # Check the situation (If Merlin is not dead)
    if player2.is_alive:
        #  Player 2 attacks Player 1
        player2.attack(player1)

    print("\n" + "="*30)
    print("FIRST ROUND IS OVER!")
    print("="*30)
    
    # Latest status of characters
    player1.check_status()
    player2.check_status()


if __name__ == "__main__":
    start_game()