from Organizmy.Zwierze.Zwierze import Zwierze


class Wilk(Zwierze):

    def __init__(self, x, y, swiat):
        super().__init__(x, y, 5, 9, swiat)

    def __copy__(self):
        return Wilk(self.x, self.y, self.swiat)


