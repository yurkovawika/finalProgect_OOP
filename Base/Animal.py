from abc import ABC, abstractmethod
from module.makeSound import makeSound

class Animal(ABC, makeSound):


    @abstractmethod
    def __init__(self, eyeColor, height, weight):
        self._eyeColor = eyeColor
        self.height = height
        self.weight = weight

    @abstractmethod
    def make_sound(self):
        return super().make_sound()

    @abstractmethod
    def __str__(self):
        return "цвет глаз:{}, рост: {} см, вес: {}кг".format(self._eyeColor, self.height, self.weight)