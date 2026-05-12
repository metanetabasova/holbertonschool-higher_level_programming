#!/usr/bin/python3
"""
Bu modul pickle modulu vasitəsilə fərdi obyektlərin
seriyalaşdırılması və deserilizasiyasını həyata keçirir.
"""
import pickle


class CustomObject:
    """
    Fərdi məlumatları saxlayan və pickle dəstəkləyən sinif.
    """

    def __init__(self, name, age, is_student):
        """Obyekti başlanğıcılaşdırır."""
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Obyektin atributlarını tələb olunan formatda çap edir."""
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """
        Cari obyekti pickle vasitəsilə fayla yazır.
        Xəta baş verərsə None qaytarır.
        """
        try:
            with open(filename, 'wb') as f:
                pickle.dump(self, f)
        except (OSError, pickle.PickleError):
            return None

    @classmethod
    def deserialize(cls, filename):
        """
        Fayldan obyekti yükləyir və CustomObject instansiyası kimi qaytarır.
        Fayl tapılmasa və ya korlanıbsa None qaytarır.
        """
        try:
            with open(filename, 'rb') as f:
                return pickle.load(f)
        except (FileNotFoundError, EOFError, pickle.PickleError, OSError):
            return None
