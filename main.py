import Swiat
import Renderer
import SaveMan


s = Swiat.swiat()
save = SaveMan.SaveMan(s)
renderer = Renderer.Renderer(s, save)
print("Ruch postaci: strzalki   Umiejetnosc: f   Zapis: s   Wczytanie: d")

renderer.run()
