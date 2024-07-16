from Organizmy.Roslina.Roslina import Roslina


class Jagody(Roslina):

    def __init__(self, x, y, swiat):
        super().__init__(x, y, 99, swiat)

    def __copy__(self):
        return Jagody(self.x, self.y, self.swiat)

    def defence(self, o):
        o.die()
        print("{0} zatruwa sie Jagodami".format(o.__class__.__name__))
        return False
