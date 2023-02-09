from Base.Animal import Animal
from abc import abstractmethod


class wildAnimal(Animal):

    @abstractmethod
    def __init__(self, eyeColor, height, weight, habitat, dateOfLocation):
        super().__init__(eyeColor, height, weight)
        self.habitat = habitat
        self._dateOfLocation = dateOfLocation

    @abstractmethod
    def make_sound(self):
        return super().make_sound()

    @abstractmethod
    def __str__(self):
        return "{} , место обитания: {}, дата обнаружения: {}".format(super().__str__(), self.habitat,
                                                                      self._dateOfLocation)
