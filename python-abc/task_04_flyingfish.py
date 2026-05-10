#!/usr/bin/python3
# Valideyn sinifleri yaratmaq
class Fish:
    def swim(self):
        print("The fish is swimming")

    def habitat(self):
        print("The fish lives in water")

class Bird:
    def fly(self):
        print("The bird is flying")

    def habitat(self):
        print("The bird lives in the sky")

# FlyingFish sinifinin yaradilmasi
class FlyingFish(Fish, Bird):
    def fly(self):
        print("The flying fish is soaring!")
    
    def swim(self):
        print("The flying fish is swimming!")

    def habitat(self):
        print("The flying fish lives both in water and the sky!")

# --- Test ---
my_fish = FlyingFish()

# Metodlari cagiririq
my_fish.fly()
my_fish.swim()
my_fish.habitat()

# MRO
print("\nMethod Resolution Order (MRO):")
print(FlyingFish.mro())
