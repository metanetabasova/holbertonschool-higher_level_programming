#!/usr/bin/python3
from abc import ABC, abstractmethod
# Mucerred Baza Sinifi
class Animal(ABC):
    @abstractmethod
    def sound(self):
        '''bu metod toreme siniflerde mutleq istifade olunmalidir'''
        pass

# Dog alt sinifi
class Dog(Animal):
    def sound(self):
        return "Bark"

# Cat alt sinifi
class Cat(Animal):
    def sound(self):
        return "Meow"

# Istifade numunesi:
dog = Dog()
cat = Cat()

print(f"Dog says: {dog.sound()}")
print(f"Cat says: {cat.sound()}")
