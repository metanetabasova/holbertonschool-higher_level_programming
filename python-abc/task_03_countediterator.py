#!/usr/bin/python3
class CountedIterator:
    def __init__(self, iterable):
        #orjinal iteratoru yaradiriq
        self.iterator = iter(iterable)
        # Saygaci sifirlayiriq
        self.count = 0

    def get_count(self):
        # Cari sayi qaytarir
        return self.count

    def __next__(self):
        try:
            # Orijinal iteratordan novbeti elementi aliriq
            item = next(self.iterator)
            # Eger element varsa, saygaci artiririq
            self.count += 1
            return item
        except StopIteration:
            # Eger element bitibse, stopIteration xetasini otururuk
            raise StopIteration
            
    def __iter__(self):
        # Obyektin ozunu iterator kimi qaytaririq
        return self

# --- Test hissesi ---
if __name__ == "__main__":
    data = ["alma", "armud", "gilas"]
    counted_iter = CountedIterator(data)

    try:
        print(next(counted_iter))
        print(next(counted_iter))
        print(f"Cari say: {counted_iter.get_count()}")

        print(next(counted_iter))
        print(f"Yekun say: {counted_iter.get_count()}")

        # Bu setir StopIteration xetasi verecek cunki element bitdi
        print(next(counted_iter))
    except StopIteration:
        print("Iterasiya bitdi.")
