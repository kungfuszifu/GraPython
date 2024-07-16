from Organizmy.Zwierze.Zwierze import Zwierze


class Zolw(Zwierze):

    def __init__(self, x, y, swiat):
        super().__init__(x, y, 1, 2, swiat)

    def __copy__(self):
        return Zolw(self.x, self.y, self.swiat)

    def defence(self, o):
        if o.getStr() < 5:
            return True
        return False
