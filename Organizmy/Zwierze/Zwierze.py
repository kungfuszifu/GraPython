from abc import abstractmethod
from Organizmy.Organizm import Organizm


class Zwierze(Organizm):

    @abstractmethod
    def __init__(self, x, y, ini, stre, swiat):
        super().__init__(x, y, ini, stre, swiat)

    @abstractmethod
    def __copy__(self):
        pass

    def action(self):
        x, y = self.move(1)
        o = self.swiat.znajdz_na_pozycji(x, y)
        if o is not None and o != self:
            self.colosion(o, x, y)
        else:
            self.setY(y)
            self.setX(x)

    def atack(self, o):
        if o.stre <= self.stre:
            return True
        else:
            return False

    def defence(self, o):
        if o.stre >= self.stre:
            return False
        else:
            return True
