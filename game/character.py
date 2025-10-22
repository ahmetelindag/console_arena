from game.helpers import roll_die  

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

    def check_status(self):
        """Prints the current status of the character."""
        print(f"-- {self.name} | LVL: {self.level} | Health: {self.health}/{self.max_health} | XP: {self.experience}/{self.experience_to_nextlevel} --")

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
        self.experience_to_nextlevel = int(self.experience_to_nextlevel * 1.5) # Increase target by 50%

        # Enhance stats
        self.max_health += 20
        self.attack_power += 5
        self.defense += 2
        self.health = self.max_health # Restore health

        print(f" LEVEL UP! {self.name} reached level {self.level}! ")
        self.check_status() # Display new status

# --- SUBCLASSES ---

class Warrior(Character):
    # Warrior Class: High health and defense stats.
    def __init__(self, name):
        super().__init__(name, health=120, attack_power=8, defense=8)
        self.experience_to_nextlevel = 120 
        print(f"Warrior {self.name} joined the arena with high health and defense!")

class Wizard(Character):
    # Wizard Class: High attack power, low health.
    def __init__(self, name):
        super().__init__(name, health=80, attack_power=12, defense=4)
        print(f"Wizard {self.name} entered the arena with pure power!")