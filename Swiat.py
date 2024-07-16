import random

from Organizmy.Zwierze.Wilk import Wilk
from Organizmy.Zwierze.Lis import Lis
from Organizmy.Zwierze.Czlowiek import Czlowiek
from Organizmy.Zwierze.Owca import Owca
from Organizmy.Zwierze.Antylopa import Antylopa
from Organizmy.Zwierze.Cyber import Cyber
from Organizmy.Roslina.Trawa import Trawa
from Organizmy.Roslina.Mlecz import Mlecz
from Organizmy.Roslina.Barszcz import Barszcz
from Organizmy.Roslina.Guarana import Guarana
from Organizmy.Roslina.Jagody import Jagody


class swiat:
    def __init__(self):
        self.MAP_SIZE = 20
        self.organizmy = []

        rand = random.Random()
        x, y = rand.randint(0, self.MAP_SIZE-1), rand.randint(0, self.MAP_SIZE-1)
        self.dodaj_organizm(Czlowiek(x, y, self))
        for i in range(self.MAP_SIZE):
            o = self.name_dictionary(self.index_dictionary(i % 10))
            x, y = 0, 0
            while self.znajdz_na_pozycji(x, y) is not None:
                x = rand.randint(0, self.MAP_SIZE-1)
                y = rand.randint(0, self.MAP_SIZE-1)
            o.x, o.y = x, y
            self.organizmy.append(o)

    def name_dictionary(self, name):
        arr = {"Czlowiek": Czlowiek(0, 0, self),
               "Wilk": Wilk(0, 0, self),
               "Lis": Lis(0, 0, self),
               "Owca": Owca(0, 0, self),
               "Antylopa": Antylopa(0, 0, self),
               "Cyber": Cyber(0, 0, self),
               "Trawa": Trawa(0, 0, self),
               "Mlecz": Mlecz(0, 0, self),
               "Guarana": Guarana(0, 0, self),
               "Jagody": Jagody(0, 0, self),
               "Barszcz": Barszcz(0, 0, self)}
        return arr[name]

    def index_dictionary(self, index):
        arr = {-1: "Czlowiek",
               0: "Wilk",
               1: "Lis",
               2: "Owca",
               3: "Antylopa",
               4: "Cyber",
               5: "Trawa",
               6: "Mlecz",
               7: "Guarana",
               8: "Jagody",
               9: "Barszcz"}
        return arr[index]

    def dodaj_organizm(self, o):
        self.organizmy.append(o)

    def znajdz_na_pozycji(self, x, y):
        for o in self.organizmy:
            xx = o.getX()
            yy = o.getY()
            if xx == x and yy == y and o.is_dead() is False:
                return o
        return None

    def tura(self, key):
        for o in self.organizmy:
            if o.is_dead() is True:
                self.organizmy.remove(o)
        self.organizmy.sort(reverse=True)
        size = self.organizmy.__len__()
        for i in range(size):
            o = self.organizmy[i]
            if o.is_dead() is False:
                if isinstance(o, Czlowiek):
                    o.key = key
                o.action()
                o.age += 1

    def czlowiek_zyje(self):
        for o in self.organizmy:
            if isinstance(o, Czlowiek):
                return o.is_dead()

    def znajdz_czlowiek(self):
        for o in self.organizmy:
            if isinstance(o, Czlowiek):
                return o
