import pygame
from Organizmy.Zwierze.Czlowiek import Czlowiek
from Organizmy.Zwierze.Zwierze import Zwierze
from Organizmy.Roslina.Roslina import Roslina

White = (200, 200, 200)
Black = (0, 0, 0)
Green = (0, 255, 0)
Orange = (255, 140, 0)
Red = (255, 0, 0)
BlockSize = 20


class Renderer:

    def __init__(self, swiat, save):
        pygame.init()
        self.Width = swiat.MAP_SIZE * 20
        self.Height = self.Width
        self.Screen = pygame.display.set_mode((self.Height, self.Width))
        self.Clock = pygame.time.Clock()
        self.Screen.fill(White)
        self.Font = pygame.font.SysFont("Arial", 16)
        self.swiat = swiat
        self.save = save

    def draw_map(self):
        for x in range(0, self.Width, BlockSize):
            for y in range(0, self.Height, BlockSize):
                color = White
                xx = int(x/20)
                yy = int(y/20)
                o = self.swiat.znajdz_na_pozycji(xx, yy)
                if isinstance(o, Czlowiek):
                    color = Red
                elif isinstance(o, Zwierze):
                    color = Orange
                elif isinstance(o, Roslina):
                    color = Green
                pygame.draw.rect(self.Screen, color, pygame.Rect(x, y, BlockSize, BlockSize))
                if o is not None:
                    self.Screen.blit(self.Font.render(o.__class__.__name__[0], True, Black), (x+2, y+2))

    def run(self):
        run = True
        while run:
            self.draw_map()

            for event in pygame.event.get():

                if event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_LEFT or event.key == pygame.K_UP or \
                            event.key == pygame.K_RIGHT or event.key == pygame.K_DOWN:
                        self.swiat.tura(event.key)
                        if self.swiat.czlowiek_zyje() is True:
                            run = False

                    if event.key == pygame.K_q:
                        run = False

                    if event.key == pygame.K_s:
                        self.save.save()

                    if event.key == pygame.K_d:
                        self.save.load()
                        pygame.display.flip()
                        self.draw_map()

                    if event.key == pygame.K_f:
                        c = self.swiat.znajdz_czlowiek()
                        c.umiejetnosc()

                if event.type == pygame.QUIT:
                    run = False

            pygame.display.flip()
            self.Clock.tick(144)

        pygame.quit()
        exit(0)
