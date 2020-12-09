class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __gt__(self, other):
        return self.age > other.age

    def __eq__(self, other):
        return self.name == other.name and self.age == other.age

    def __add__(self, other):
        return self.age + other.age

    def say_hi(self):
        print(
            f"Hi there! I'm {self.name}, and I'm {self.age} years old. Nice to meet you :D")


tomas = Human("Tomas Carignano", 22)
fede = Human("Federico Witthaus", 21)
combined = tomas + fede
print(combined)
