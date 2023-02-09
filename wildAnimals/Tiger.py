from wildAnimals.wildAnimal import wildAnimal

class Tiger( wildAnimal):

    def __init__(self, eyeColor, height, weight, habitat, dateOfLocation):
        wildAnimal.__init__(self, eyeColor, height, weight, habitat, dateOfLocation)
        self._type = "Тигр"

    def make_sound(self):
        return  self._type + super().make_sound() + "РРРР!"

    def __str__(self):
        return "{}\n{}".format(self._type, super().__str__())
