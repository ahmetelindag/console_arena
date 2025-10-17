#game/character.py

class Character:
    def __init__(self, name, health =100, level =1, experience = 0, attack_power = 10, defense = 5 ):
        self.name = name 
        self.health = health 
        self.max_health = health
        self.level = level 
        self.experience = experience
        self.experience_to_nextlevel = 100
        self.attack_power = attack_power
        self.defense = defense


    def check_status(self):
        print(f"-- {self.name} | LVL: {self.level} | Health: {self.health}/{self.max_health} | XP: {self.experience}/{self.experience_to_nextlevel} --")

class warrior(Character):
    def __init__(self, name):
        super().__init__(name, health =120, attack_power = 12, defense = 8)
        self.experience_to_next_level = 120 
        print(f"The Warrior {self.name}, joined the arena with high health and defense! ")

class wizard(Character):
    
    def __init__(self, name):
        
        super().__init__(name, health=80, attack_power=12, defense=4)
        print(f"The Wizard {self.name}, entered the arena with pure power !")