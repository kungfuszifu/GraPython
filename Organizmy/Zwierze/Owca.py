from Organizmy.Zwierze.Zwierze import Zwierze


class Owca(Zwierze):

    def __init__(self, x, y, swiat):
        super().__init__(x, y, 4, 4, swiat)

    def __copy__(self):
        return Owca(self.x, self.y, self.swiat)
