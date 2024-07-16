from Organizmy.Zwierze.Zwierze import Zwierze


class Lis(Zwierze):

    def __init__(self, x, y, swiat):
        super().__init__(x, y, 7, 3, swiat)

    def action(self):
        x, y = self.move(1)
        o = self.swiat.znajdz_na_pozycji(x, y)
        if o is not None and o != self:
            if o.getStr() > self.stre:
                self.setX(x)
                self.setY(y)
            else:
                self.colosion(o, x, y)
        else:
            self.setX(x)
            self.setY(y)

    def __copy__(self):
        return Lis(self.x, self.y, self.swiat)
