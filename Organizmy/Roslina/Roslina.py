import random
from abc import abstractmethod
from Organizmy import Organizm


class Roslina(Organizm.Organizm):

    @abstractmethod
    def __init__(self, x, y, sila, swiat):
        super().__init__(x, y, 0, sila, swiat)

    def __copy__(self):
        return Roslina(self.x, self.y, self.swiat)

    def action(self):
        rand = random.Random()
        chance = rand.randint(1, 100)
        if 1 <= chance <= 2:
            self.have_child()

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

