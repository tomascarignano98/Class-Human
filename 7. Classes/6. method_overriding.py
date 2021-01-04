class Animal:
    def __init__(self):
        self.age = 1

    def eat(self):
        print("eat")


class Mammal(Animal):
    def __init__(self):
        self.weight = 2
        super().__init__()

    def walk(self):
        print("walk")


class Fish:
    def swim(self):
        print("swim")


cat = Mammal()
print(cat.age)
print(cat.weight)
