from Base.Animal import Animal, abstractmethod


class notFlyingBird(Animal):

    @abstractmethod
    def __init__(self, colorFeather):
        self.colorFeather = colorFeather

    @abstractmethod
    def __str__(self):
        return "{}, цвет перьев:{}".format(super().__str__(),self.colorFeather)
