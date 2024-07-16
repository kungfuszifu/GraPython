import random

from Organizmy.Roslina.Roslina import Roslina


class Mlecz(Roslina):

    def __init__(self, x, y, swiat):
        super().__init__(x, y, 0, swiat)

    def __copy__(self):
        return Mlecz(self.x, self.y, self.swiat)

    def action(self):
        rand = random.Random()
        for i in range(3):
            chance = rand.randint(1, 100)
            if 1 <= chance <= 2:
                if self.children is True:
                    self.have_child()
                    break
