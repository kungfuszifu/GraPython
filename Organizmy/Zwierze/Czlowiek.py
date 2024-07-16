import random

from Organizmy.Zwierze.Zwierze import Zwierze
import pygame


class Czlowiek(Zwierze):

    def __init__(self, x, y, swiat):
        self.cd = 0
        self.key = None
        super().__init__(x, y, 4, 5, swiat)

    def __copy__(self):
        return Czlowiek(self.x, self.y, self.swiat)

    def action(self):
        rand = random.Random()
        range = 1
        if self.cd > 0:
            print("Pozostalo {0} uzyc".format(self.cd))
            if 0 < self.cd <= 2:
                chance = rand.randint(0, 1)
                if chance == 0:
                    range = 2
            elif 2 < self.cd <= 5:
                range = 2
            self.cd -= 1

        x = self.x
        y = self.y
        if self.key == pygame.K_UP:
            y = self.y - range
        elif self.key == pygame.K_DOWN:
            y = self.y + range
        elif self.key == pygame.K_LEFT:
            x = self.x - range
        elif self.key == pygame.K_RIGHT:
            x = self.x + range

        if x < 0:
            x = 0
        elif x >= self.swiat.MAP_SIZE:
            x = self.swiat.MAP_SIZE-1
        if y < 0:
            y = 0
        elif y >= self.swiat.MAP_SIZE:
            y = self.swiat.MAP_SIZE-1

        o = self.swiat.znajdz_na_pozycji(x, y)
        if o is not None and o != self:
            self.colosion(o, x, y)
        else:
            self.setX(x)
            self.setY(y)

    def umiejetnosc(self):
        if self.cd > 0:
            print("Umiejetnosc w uzyciu")
            return
        self.cd = 5
        print("Uzyto umiejetnosci")
