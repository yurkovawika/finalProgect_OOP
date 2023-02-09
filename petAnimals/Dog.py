from petAnimals.petAnimal import petAnimal
from module.makeSound import makeSound


class Dog(petAnimal, makeSound):

    def __init__(self, name, breed, eyeColor, height, weight, vaccination, trained):
        super().__init__(name, breed, eyeColor, height, weight, vaccination)
        self._type = "Собака"
        self._trained = trained

    def getName(self):
        return super().getName()

    def __set_name__(self, name, newName):
        return super().__set_name__(name, newName)

    def make_sound(self):
        return self._type + super(Dog, self).make_sound() + " гаф"

    def __str__(self):
        return "{} {}, наличие дрессировки: {}".format(self._type, super().__str__(), self._trained)

    def train(self):
        if self._trained:
            return "{} обучен.".format(self.name)
        else:
            self._trained = True
            return "{} начал тренировку".format(self.name)

