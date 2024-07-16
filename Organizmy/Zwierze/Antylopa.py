import random

from Organizmy.Zwierze.Zwierze import Zwierze


class Antylopa(Zwierze):

    def __init__(self, x, y, swiat):
        super().__init__(x, y, 4, 4, swiat)

    def __copy__(self):
        return Antylopa(self.x, self.y, self.swiat)

    def action(self):
        x, y = self.move(2)
        o = self.swiat.znajdz_na_pozycji(x, y)
        if o is not None and o != self:
            rand = random.Random()
            chance = rand.randint(0, 1)
            if chance == 0:
                self.colosion(o, x, y)
        else:
            self.setX(x)
            self.setY(y)

    def defence(self, o):
        rand = random.Random()
        chance = rand.randint(0, 1)
        if chance == 0:
            return True
        else:
            if o.getStr() >= self.stre:
                return False
            return True
