from Organizmy.Roslina.Roslina import Roslina

class Trawa(Roslina):

    def __init__(self, x, y, swiat):
        super().__init__(x, y, 0, swiat)

    def __copy__(self):
        return Trawa(self.x, self.y, self.swiat)
