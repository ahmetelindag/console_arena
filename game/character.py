#game/character.py

class Character:
    def __init__(self, name, health =100, level =1, experience = 0):
        self.name = name 
        self.health = health 
        self.level = level 
        self.experience = experience

    def check_status(self):
        print(f"-- {self.name} | Health : {self.health} | Level : {self.level}| Experience : {self.experience}")
        


            