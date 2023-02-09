from Base.Animal import Animal
from abc import abstractmethod


class petAnimal(Animal):
    pass

    @abstractmethod
    def __init__(self, name, breed, eyeColor, height, weight, vaccination):
        super(petAnimal, self).__init__(eyeColor, height, weight)
        self.name = name
        self._breed = breed
        self.vaccination = vaccination

    @abstractmethod
    def getName(self):
        return self.name

    @abstractmethod
    def __set_name__(self, name, newName):
        self.name = newName

    @abstractmethod
    def make_sound(self):
        return super().make_sound()

    @abstractmethod
    def __str__(self):
        return "кличка:{}, порода:{}, {}, вакцинация {}".format(self.name,self._breed, super().__str__(),self.vaccination)
