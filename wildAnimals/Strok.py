from wildAnimals.wildAnimal import wildAnimal

from Base.flyingBird import flyingBird


class Strok(flyingBird, wildAnimal):

    def __init__(self, eyeColor, height, weight, habitat, dateOfLocation, colorFeather, flightAltitude):

        wildAnimal.__init__(self, eyeColor, height, weight, habitat, dateOfLocation)
        flyingBird.__init__(self, colorFeather, flightAltitude)
        self.type = "Аист"

    def fly(self):
        return self.type+super(Strok, self).fly()

    def make_sound(self):
        return self.type +super().make_sound() + "кр-кр"

    def __str__(self):
        return "{}\n{}".format(self.type, super().__str__())



