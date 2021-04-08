import unittest
from django_lab.konto import zwykleKonto, VIPKonto, firmoweKonto

class zwykleKontoTest(unittest.TestCase):
    zwykleKonto = zwykleKonto(100, 200)
    def test_wyplacenie(self):
        self.assertTrue(self.zwykleKonto.wyplac, 100)
    def test_przekroczenie_debetu(self):
        self.zwykleKonto.stan = -201
        self.assertRaises(Exception, self.zwykleKonto.wyplac, 1)
    def test_przekroczenie_kwoty_maksymalnej(self):
        self.zwykleKonto.stan = 0
        self.assertRaises(Exception, self.zwykleKonto.wyplac, 301)
    def test_do_kwoty_maksymalnej(self):
        self.zwykleKonto.stan = 0
        self.assertTrue(self.zwykleKonto.wyplac, 300)

class VIPKontoTest(unittest.TestCase):
    VIPKonto = VIPKonto(100, 200)
    def test_wyplacenie(self):
        self.assertTrue(self.VIPKonto.wyplac, 100)
    def test_przekroczenie_debetu(self):
        self.VIPKonto.stan = -201
        self.assertRaises(Exception, self.VIPKonto.wyplac, 1)
    def test_przekroczenie_kwoty_maksymalnej(self):
        self.VIPKonto.stan = 0
        self.assertRaises(Exception, self.VIPKonto.wyplac, 200+2001)
    def test_przekroczenie_kwoty_maksymalnej_z_ujemnego_stanu(self):
        self.VIPKonto.stan = -100
        self.assertRaises(Exception, self.VIPKonto.wyplac, 100+2001)
    def test_do_kwoty_maksymalnej(self):
        self.VIPKonto.stan = 0
        self.assertTrue(self.VIPKonto.wyplac, 300)

class firmoweKontoTest(unittest.TestCase):
    firmoweKonto = firmoweKonto(100, 200)
    def test_wyplacenie(self):
        self.assertTrue(self.firmoweKonto.wyplac, 100)
    def test_przekroczenie_debetu(self):
        self.firmoweKonto.stan = -201
        self.assertRaises(Exception, self.firmoweKonto.wyplac, 1)
    def test_przekroczenie_kwoty_maksymalnej(self):
        self.firmoweKonto.stan = 0
        self.assertRaises(Exception, self.firmoweKonto.wyplac, 200+2001)
    def test_do_kwoty_maksymalnej(self):
        self.firmoweKonto.stan = 0
        self.assertTrue(self.firmoweKonto.wyplac, 200+2000)

if __name__ == '__main__':
    unittest.main()
