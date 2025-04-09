import random

# Базовый класс Героя
class Hero:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def take_damage(self, damage):
        # Уменьшение здоровья героя, если урон больше защиты
        actual_damage = max(damage , 0)
        self.health -= actual_damage
        return actual_damage

    def is_alive(self):
        return self.health > 0

    def __str__(self):
        return f"{self.name} (HP: {self.health}, ATK: {self.attack_power})"

# Класс для войны между героями
class Battle:
    def __init__(self, hero1, hero2):
        self.hero1 = hero1
        self.hero2 = hero2

    def fight(self):
        print("Начинается битва!")
        print(f"{self.hero1} VS {self.hero2}\n")

        # Пока оба героя живы
        while self.hero1.is_alive() and self.hero2.is_alive():
            self.turn(self.hero1, self.hero2)
            if not self.hero2.is_alive():
                print(f"\n{self.hero1.name} побеждает!")
                break

            self.turn(self.hero2, self.hero1)
            if not self.hero1.is_alive():
                print(f"\n{self.hero2.name} побеждает!")
                break

    def turn(self, attacker, defender):
        print(f"{attacker.name} атакует {defender.name}!")
        damage = attacker.attack_power
        actual_damage = defender.take_damage(damage)
        print(f"{attacker.name} наносит {actual_damage} урона. {defender.name} теперь имеет {defender.health} здоровья.\n")

hero1 = Hero("Player", 100, 20)
print(f"Создан герой: {hero1}")
hero2 = Hero("Computer", random.randint(80,120), random.randint(10,30))
print(f"Создан герой: {hero2}\n")

battle = Battle(hero1, hero2)
battle.fight()

