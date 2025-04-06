from abc import ABC, abstractmethod

class Weapon(ABC):
     @abstractmethod
     def attack(self,player):
         pass

class Sword(Weapon):
    def __init__(self):
        self.type_weapon = "меч"
    def attack(self,monster):
        print("Боец наносит удар мечом")
        monster.change_life(10)

class Bow(Weapon):
    def __init__(self):
        self.type_weapon = "лук"
    def attack(self,monster):
        print("Боец наносит удар из лука")
        monster.change_life(5)

class Fighter():
    def __init__(self,name,weapon):
        self.name = name
        self.weapon = weapon

    def change_weapon(self,weapon):
        self.weapon = weapon
        print(f"{self.name} выбирает {self.weapon.type_weapon} ")

    def battle(self,monster):
        self.weapon.attack(monster)

class Monster():
    def __init__(self):
        self.life = 10

    def change_life(self,life):
        self.life -= life
        if self.life > 0:
            print(f"У монстра жизней:{self.life}")
        else: print("Монстр побежден")

fighter=Fighter("Боец",Bow())
monster = Monster()
fighter.change_weapon(Bow())
fighter.battle(monster)
fighter.battle(monster)





