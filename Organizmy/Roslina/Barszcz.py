from Organizmy.Roslina.Roslina import Roslina
import Organizmy.Zwierze.Cyber as Cyb


class Barszcz(Roslina):

    def __init__(self, x, y, swiat):
        super().__init__(x, y, 10, swiat)

    def __copy__(self):
        return Barszcz(self.x, self.y, self.swiat)

    def aura(self):
        xl, xr, yu, yd = 1, 1, 1, 1
        if self.x - 1 < 0:
            xl = 0
        if self.x + 1 >= self.swiat.MAP_SIZE:
            xr = 0
        if self.y - 1 < 0:
            yu = 0
        if self.y + 1 >= self.swiat.MAP_SIZE:
            yd = 0
        for x in range(self.x - xl, self.x + xr + 1, 1):
            for y in range(self.y - yu, self.y + yd + 1, 1):
                if x == self.x and y == self.y:
                    continue

                o = self.swiat.znajdz_na_pozycji(x, y)
                if o is not None and o != self and isinstance(o, Roslina) is False \
                        and isinstance(o, Cyb.Cyber) is False:
                    o.die()
                    print("{0} umiera od barszczu".format(o.__class__.__name__))

    def action(self):
        self.aura()
        super().action()
