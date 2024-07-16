class SaveMan:

    def __init__(self, swiat):
        self.swiat = swiat

    def save(self):
        f = open("save.txt", "w")
        for o in self.swiat.organizmy:
            if o.is_dead() is False:
                f.write("{0} {1} {2} {3} {4} {5} \n".format(o.__class__.__name__, o.x, o.y, o.stre, o.children, o.age))
        f.close()

    def load(self):
        f = open("save.txt", "r")
        self.swiat.organizmy.clear()
        for string in f:
            string = string.strip("\n")
            list = string.split(" ")
            o = self.swiat.name_dictionary(list[0])
            o.x, o.y, o.stre, o.children, o.age = int(list[1]), int(list[2]), int(list[3]), bool(list[4]), int(list[5])
            self.swiat.dodaj_organizm(o)
        f.close()
