import unittest
from pracownik import Pracownik

class testPracownik(unittest):
    pracownik = Pracownik("Jan", "Kowalski", "Nauczyciel stażysta", 2000)
    def test_zwykly_awans(self):
        self.pracownik.zwykly_awans()
        self.assertEqual(self.pracownik.pensja, 2000*1.2)
    def test_degradacja_kierownicza(self):
        self.pracownik.degradacja_kierownicza()
        self.assertEqual(self.pracownik.pensja, 2000*0.8)
