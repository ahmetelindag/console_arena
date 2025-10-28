from game.character import Warrior, Wizard
from game.engine import GameEngine
import time

def create_character(player_num):
    """A function to create a character based on user input."""
    print(f"\n--- Player {player_num} Character Creation ---")
    
    name = input("Enter your character's name: ")
    
    class_choice = ""
    # Keep asking until user enters 1 or 2
    while class_choice not in ['1', '2']:
        class_choice = input("Choose your class (1: Warrior, 2: Wizard): ")
        if class_choice not in ['1', '2']:
            print("Invalid choice! Please enter 1 or 2.")
    
    if class_choice == '1':
        print(f"Player {player_num} has chosen Warrior {name}.")
        return Warrior(name)
    else:
        print(f"Player {player_num} has chosen Wizard {name}.")
        return Wizard(name)

def start_game():
    """The main entry point for the game."""
    print("Welcome to the Console Arena!\n")
    
    # --- Step 1: Create Characters ---
    player1 = create_character(1)
    player2 = create_character(2)

    time.sleep(1)

    # --- Step 2: Set up the Game Engine and Start ---

    engine = GameEngine(player1, player2)
    engine.start_battle()

    print("\nThanks for playing!")


if __name__ == "__main__":
    start_game()