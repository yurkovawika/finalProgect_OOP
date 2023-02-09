from wildAnimals.wildAnimal import wildAnimal


class Wolf(wildAnimal):

    def __init__(self, eyeColor, height, weight, habitat, dateOfLocation, packLeader):
        wildAnimal.__init__(self, eyeColor, height, weight, habitat, dateOfLocation)
        self.packLeader = packLeader
        self._type = "Волк"

    def make_sound(self):
        return self._type + super().make_sound() + "АУУУ!"

    def __str__(self):
        return "{}\n{}".format(self._type, super().__str__())


