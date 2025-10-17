from game.character import warrior, wizard

def start_game():
    print("----Welcome to the console arena!----\n")
    print("Console Arena Begins!\n")
    

    player1 = warrior(name="try")
    
    print("-" * 30) # Ayraç
    
    player2 = wizard(name="Merlin")
    
    print("\n Characters created:")
    player1.check_status()
    player2.check_status()


if __name__ == "__main__":
    start_game()