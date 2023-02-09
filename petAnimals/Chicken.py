from petAnimals.petAnimal import petAnimal
from Base.notFlyingBird import notFlyingBird


class Chicken(notFlyingBird, petAnimal):

    def __init__(self, name, breed, eyeColor, height, weight, vaccination, colorFeather):
        notFlyingBird.__init__(self, colorFeather)
        petAnimal.__init__(self, name, breed, eyeColor, height, weight, vaccination)
        self._type = "Курица"

    def getName(self):
        return super().getName()

    def __set_name__(self, name, newName):
        return super().__set_name__(name, newName)

    def make_sound(self):
        return super().make_sound() + "ко-ко"

    def __str__(self):
        return "{}\n{}".format(self._type, super().__str__())


# chik = Chicken("Чика", "бройлер", "синий", 12, 0.560, True, "черный")

