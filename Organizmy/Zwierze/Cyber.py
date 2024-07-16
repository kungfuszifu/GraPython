import math

from Organizmy.Zwierze.Zwierze import Zwierze
import Organizmy.Roslina.Barszcz as Bar


class Cyber(Zwierze):

    def __init__(self, x, y, swiat):
        super().__init__(x, y, 4, 11, swiat)

    def __copy__(self):
        return Cyber(self.x, self.y, self.swiat)

    def wystepuje_barszcz(self):
        for o in self.swiat.organizmy:
            if isinstance(o, Bar.Barszcz) and o.is_dead() is False:
                return True
        return False

    def znajdz_barszcz(self):
        x, y, mindist = self.x, self.y, 10000
        bar = None
        for o in self.swiat.organizmy:
            if isinstance(o, Bar.Barszcz) and o.is_dead() is False:
                dist = math.sqrt(pow(self.x - o.x, 2) + pow(self.y - o.y, 2))
                if dist < mindist:
                    mindist = dist
                    bar = o

        if bar is not None:
            if mindist == 0:
                return x, y
            if bar.x == self.x:
                if abs(y - 1 - bar.y) < abs(y - bar.y):
                    y -= 1
                else:
                    y += 1
            elif bar.y == self.y:
                if abs(x - 1 - bar.x) < abs(x - bar.x):
                    x -= 1
                else:
                    x += 1
            else:
                if y > bar.y and x > bar.x:  # lewa gora
                    y -= 1
                    x -= 1
                if y > bar.y and x < bar.x:  # prawa gora
                    y -= 1
                    x += 1
                if y < bar.y and x > bar.x:  # lewy dol
                    y += 1
                    x -= 1
                if y < bar.y and x < bar.x:  # prawy dol
                    y += 1
                    x += 1
        else:
            return self.move(1)
        return x, y

    def action(self):
        if self.wystepuje_barszcz() is True:
            x, y = self.znajdz_barszcz()
        else:
            x, y = self.move(1)
        o = self.swiat.znajdz_na_pozycji(x, y)
        if o is not None and o != self:
            if isinstance(o, Bar.Barszcz):
                o.die()
                self.x, self.y = x, y
                print("Barszcz zostal zjedzony przez Cyber Owce")
            else:
                self.colosion(o, x, y)
        else:
            self.setX(x)
            self.setY(y)
