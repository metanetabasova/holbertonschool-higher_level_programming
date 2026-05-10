#!/usr/bin/python3
# Mixin siniflerinin yaradilmasi
class SwimMixin:
    def swim(self):
        print("The creature swims!")

class FlyMixin:
    def fly(self):
        print("The creature flies!")

# Dragon sinfinin konstruksiyasi
class Dragon(SwimMixin, FlyMixin):
    def roar(self):
        print("The dragon roars!")

# Test 
draco = Dragon()

draco.swim()
draco.fly()
draco.roar()
