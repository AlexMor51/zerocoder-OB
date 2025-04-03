class Animal():
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def make_sound(self):
        pass
    def eat(self):
        print(f"{self.name} кушает")
class Bird(Animal):
    def make_sound(self):
        print(f"кар-кар")

class Mammal(Animal):
    def make_sound(self):
        print(f"му-му")

class Reptile(Animal):
    def make_sound(self):
        print(f"п-шшш")

def animal_sound(animals):
    for animal in animals:
        animal.make_sound()

class Zoo():
    def __init__(self):
        self.animals = []
        self.staff = []
    def add_animal(self,animal):
        self.animals.append(animal)
        print(f"Животное {animal.name} добавлено в зоопарк")
    def add_staff(self,new_staff):
        self.staff.append(new_staff)
        print(f"Сотрудник {new_staff} добавлен в зоопарк")

class ZooKeeper():
    def feed_animal(self,animal):
        print(f"Сотрудник кормит {animal.name}")

class Veterinar():
    def heal_animal(self,animal):
        print(f"Ветеринар лечит {animal.name}")

bird1=Bird("Ворона",3)
mammal1=Mammal("Бык",5)
reptile1=Reptile("Гадюка", 7)

zoo=Zoo()
keeper1=ZooKeeper()
veterinar1=Veterinar()

zoo.add_animal(bird1)
zoo.add_animal(mammal1)
zoo.add_animal(reptile1)

zoo.add_staff(keeper1)
zoo.add_staff(veterinar1)

animal_sound(zoo.animals)

keeper1.feed_animal(bird1)
veterinar1.heal_animal(reptile1)

