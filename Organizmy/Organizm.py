import random
from abc import ABC, abstractmethod


class Organizm(ABC):

    @abstractmethod
    def __init__(self, x, y, ini, stre, swiat):
        self.x = x
        self.y = y
        self.ini = ini
        self.stre = stre
        self.swiat = swiat
        self.children = True
        self.dead = False
        self.age = 0
        super().__init__()

    @abstractmethod
    def __copy__(self):
        pass

    def __lt__(self, other):
        return self.ini < other.ini

    def move(self, range):
        r = random.Random()
        movex, movey = 0, 0
        while movex == 0 and movey == 0:
            movex = r.randint(-1 * range, 1 * range)
            movey = r.randint(-1 * range, 1 * range)
        if self.x + movex < 0:
            x = 0
        elif self.x + movex >= self.swiat.MAP_SIZE:
            x = self.swiat.MAP_SIZE-1
        else:
            x = self.x + movex
        if self.y + movey < 0:
            y = 0
        elif self.y + movey >= self.swiat.MAP_SIZE:
            y = self.swiat.MAP_SIZE-1
        else:
            y = self.y + movey
        return x, y

    @abstractmethod
    def action(self):
        pass

    @abstractmethod
    def atack(self, o):
        pass

    @abstractmethod
    def defence(self, o):
        pass

    def colosion(self, o, x, y):
        if o.is_dead():
            return
        if self.__class__.__name__ == o.__class__.__name__:
            if self.children is not False and o.children is not False:
                self.have_child()
        else:
            a = self.atack(o)
            d = o.defence(self)
            if a is True and d is not True:
                o.die()
                self.x, self.y = x, y
                print("{0} zabija {1}".format(self.__class__.__name__, o.__class__.__name__))
            elif a is not True and d is True:
                self.die()
                print("{0} broni sie przed {1}".format(o.__class__.__name__, self.__class__.__name__))

    def have_child(self):
        o = self.__copy__()
        x, y = o.move(1)
        len, i = 1, 0
        t = self.swiat.znajdz_na_pozycji(x, y)
        while t is not None and t != self and t != o:
            x, y = o.move(len)
            t = self.swiat.znajdz_na_pozycji(x, y)
            i += 1
            if i == 4:
                i = 0
                len += 1
        o.x, o.y = x, y
        self.children = False
        o.children = False
        self.swiat.dodaj_organizm(o)
        print("{0} rozmnaza sie".format(self.__class__.__name__))

    def setX(self, x):
        self.x = x

    def setY(self, y):
        self.y = y

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def getStr(self):
        return self.stre

    def get_ini(self):
        return self.ini

    def die(self):
        self.dead = True

    def is_dead(self):
        return self.dead
