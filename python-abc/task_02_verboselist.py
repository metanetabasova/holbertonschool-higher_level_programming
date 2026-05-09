#!/usr/bin/python3
class VerboseList(list):
    
    def append(self, item):
        #orjinal append metodunu cagirir
        super().append(item)
        print(f"Added [{item}] to the list.")

    def extend(self, x):
        # Orjinal extend metodunu cagiririq
        item_count = len(x)
        # Elave edilen elementlerin sayini hesablayiriq
        super().extend(x)
        print(f"Extend the list with [{item_count}] items.")

    def remove(self, item):
        # orjinal remove metodunu cagirir
        print(f"Removed [{item}] from the list.")
        # elementler silinmezden evvel mesaji cap edirik.
        super().remove(item)

    def pop(self, index = -1):
        # orjinal pop metodunu cagirir
        item = self[index]
        print(f"Popped [{item}] from the list.")
        # index uzre elementi tapiriq
        return super().pop(index)

# --- Test Hissesi ---
my_list = VerboseList([1, 2, 3])

my_list.append(4)
my_list.extend([5, 6])
my_list.remove(2)
my_list.pop()
