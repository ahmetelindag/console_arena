from game.helpers import roll_die  
from game import settings 

class Character:
    """Base class for all entities in the game."""
    def __init__(self, name, health=100, level=1, experience=0, attack_power=10, defense=5):
        self.name = name 
        self.health = health 
        self.max_health = health
        self.level = level 
        self.experience = experience
        self.experience_to_nextlevel = 100
        self.attack_power = attack_power
        self.defense = defense
        self.is_alive = True # Tracks whether the character is alive
        self.special_cooldown = 0

    def check_status(self):
        """Prints the current status of the character."""
        print(f"-- {self.name} | LVL: {self.level} | Health: {self.health}/{self.max_health} | XP: {self.experience}/{self.experience_to_nextlevel} --")
        

    def tick_turn(self):
    
        if self.special_cooldown > 0:
         self.special_cooldown -= 1
         print(f"({self.name}'s special attack recharges in {self.special_cooldown} turns)")

    def special_attack(self, target):
    
        print(f"\n{self.name} doesn't have a special attack!")

    def get_attack_choice(self):
    
   
        if self.special_cooldown > 0:
         print(f"Special Attack is on cooldown! ({self.special_cooldown} turns left)")
         return "1" # Özel saldırı beklemedeyse, otomatik olarak normal saldırı seç
        else:
            while choice not in ["1", "2"]:
                choice = input(f"Choose your move (1: Normal Attack, 2: Special Attack): ")
                if choice == "2":
                    print(f"{self.name} prepares a special attack! ")
                elif choice == "1": 
                    print(f"{self.name} prepares a normal attack! ")
                else:
                    print("invalid choice ")
                    
                    
                return choice


    def attack(self, target):
        # Attacks the target character. Damage is calculated with a dice roll.
        if not self.is_alive:
            print(f"{self.name} cannot attack because they are not alive!")
            return

        # Add a luck factor to the attack (dice roll between 1-6)
        roll = roll_die(6)
        damage = self.attack_power + roll
        
        print(f"\n{self.name} is attacking {target.name}!")
        print(f"Dice rolled: {roll} | Total Damage: {damage}")
        
        # Apply damage to the target
        target.take_damage(damage)

    def take_damage(self, damage):
        """
        Allows the character to take damage. Defense reduces the damage.
        """
        if not self.is_alive:
            return

        # Defense reduces damage, damage cannot be less than 0
        net_damage = max(0, damage - self.defense)
        self.health -= net_damage
        
        print(f"{self.name} took {net_damage} damage! Remaining Health: {self.health}")

        # Health check
        if self.health <= 0:
            self.health = 0
            self.is_alive = False
            print(f"❌ {self.name} has been defeated!")

    def gain_experience(self, amount):
        # Adds XP to the character and checks for level-up.
        if not self.is_alive:
            return
            
        self.experience += amount
        print(f"✨ {self.name} gained {amount} XP! (Total XP: {self.experience})")
        
        if self.experience >= self.experience_to_nextlevel:
            self.level_up()

    def level_up(self):
        # Increases the character's level and enhances their stats.
        self.level += 1
        self.experience = self.experience - self.experience_to_nextlevel # Carry over remaining XP
        self.experience_to_nextlevel = int(self.experience_to_nextlevel * settings.LEVEL_UP_XP_MULTIPLIER)

        # Enhance stats
        self.max_health += settings.LEVEL_UP_HEALTH_GAIN
        self.attack_power += settings.LEVEL_UP_ATTACK_GAIN
        self.defense += settings.LEVEL_UP_DEFENSE_GAIN
        self.health = self.max_health # Restore health

        print(f" LEVEL UP! {self.name} reached level {self.level}! ")
        self.check_status() # Display new status

# --- SUBCLASSES ---

class Warrior(Character):
    # Warrior Class: High health and defense stats.
    def __init__(self, name):
        super().__init__(name, 
                         health=settings.WARRIOR_HEALTH, 
                         attack_power=settings.WARRIOR_ATTACK, 
                         defense=settings.WARRIOR_DEFENSE)
        self.experience_to_nextlevel = settings.WARRIOR_XP_TARGET 
        print(f"Warrior {self.name} joined the arena with high health and defense!")

    def special_attack(self, target):

        #power strike 2x attack 2x cooldown 
        print(f"\n{self.name} uses POWER STRIKE!")
        damage = (self.attack_power * 2) + roll_dice(4) 

        print(f"A devastating blow deals {damage} damage!")
        target.take_damage(damage)

        # Cooldown
        self.special_cooldown = 2 # 2 tur bekleme süresi

class Wizard(Character):
    # Wizard Class: High attack power, low health.
    def __init__(self, name):
        super().__init__(name, 
                         health=settings.WIZARD_HEALTH, 
                         attack_power=settings.WIZARD_ATTACK, 
                         defense=settings.WIZARD_DEFENSE)
        self.experience_to_nextlevel = settings.WIZARD_XP_TARGET
        print(f"Wizard {self.name} entered the arena with pure power!")