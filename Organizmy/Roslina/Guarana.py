from Organizmy.Roslina.Roslina import Roslina


class Guarana(Roslina):

    def __init__(self, x, y, swiat):
        super().__init__(x, y, 0, swiat)

    def __copy__(self):
        return Guarana(self.x, self.y, self.swiat)

    def defence(self, o):
        o.stre += 3
        print("Sila {0} wzrosla o 3".format(o.__class__.__name__))
        return False
