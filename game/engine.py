# game/engine.py
from game.character import Character
from game import settings
import time

class GameEngine:
    
    # Manages the main game loop and combat mechanics.
    
    def __init__(self, player1: Character, player2: Character):
        self.player1 = player1
        self.player2 = player2
        self.round = 1
        print("\n Fighters are ready!")

    def start_battle(self):
        """
        Starts the combat loop, which continues until one character is defeated.
        """
        print("\n" + "="*30)
        print(f"BATTLE BEGINS: {self.player1.name} vs {self.player2.name}")
        print("="*30)
        
        self.player1.check_status()
        self.player2.check_status()

        #  assume player1 always starts for now
        current_attacker = self.player1
        current_defender = self.player2

        # Main Combat Loop
        while self.player1.is_alive and self.player2.is_alive:
            print(f"\n--- ROUND {self.round} ---")
            
            # Attacker's turn
            input(f"It's {current_attacker.name}'s turn. Press Enter to attack...")
            current_attacker.attack(current_defender)
            
            time.sleep(0.5) # Wait 0.5 seconds

            # Check if the defender was defeated
            if not current_defender.is_alive:
                self.end_battle(winner=current_attacker, loser=current_defender)
                break
            
            
            current_attacker, current_defender = current_defender, current_attacker
            self.round += 1
        
        print("\n" + "="*30)
        print("BATTLE OVER!")
        print("="*30)

    def end_battle(self, winner: Character, loser: Character):
        """
        Announces the winner and grants XP.
        """
        print(f"\n WINNER: {winner.name}! ")
        
        # Grant XP: Read base gain from settings
        xp_gain = settings.BASE_XP_GAIN + (loser.level * 15) 
        winner.gain_experience(xp_gain)
        
        # Show final status
        print("\n--- FINAL BATTLE STATUS ---")
        winner.check_status()
        loser.check_status()