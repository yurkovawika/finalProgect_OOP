
from petAnimals.petAnimal import petAnimal


class Cat(petAnimal):

    def __init__(self, name, breed, eyeColor, weight, height, vaccination, presenceOfWool):
        super().__init__(name, breed, eyeColor, height, weight, vaccination)
        self._type = "Кошка"
        self._presenceOfWool = presenceOfWool

    def getName(self):
        return super().getName()

    def __set_name__(self, name, newName):
        return super().__set_name__(name, newName)

    def make_sound(self):
        return self._type + super(Cat, self).make_sound() + " мяу"

    def __str__(self):
        return "{} {}, наличие шерсти {}".format(self._type, super().__str__(), self._presenceOfWool)



