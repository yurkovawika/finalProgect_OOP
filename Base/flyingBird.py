from Base.Animal import Animal, abstractmethod



class flyingBird(Animal):

    @abstractmethod
    def __init__(self, colorFeather, flightAltitude):
        self.colorFeather = colorFeather
        self.flightAltitude = flightAltitude

    @abstractmethod
    def fly(self):
        return " летит на высоте {} м".format(self.flightAltitude)

    @abstractmethod
    def __str__(self):
        return "{}, цвет перьев: {}, высота полёта: {}".format(super().__str__(), self.colorFeather,self.flightAltitude)
