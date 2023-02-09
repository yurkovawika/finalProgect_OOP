from Base.Animal import Animal


class Zoo():

    def __init__(self):
        self.zoo = []

    def add_animal(self, animal):
        self.zoo.append(animal)

    def get_len(self):
        return len(self.zoo)

    def get_animal(self, idx):
        return self.zoo[idx - 1]

    def removed_animal(self, idx):
        try:
            self.zoo.remove(self.zoo[idx - 1])
        except IndexError as e:
            print(e)

    def make_sound(self, idx):
        print(self.zoo[idx - 1].make_sound())

    def make_sound_all(self):
        for i in self.zoo:
            if isinstance(i, Animal):
                print(i.make_sound())

    def get_info(self, idx):
        return self.zoo[idx - 1].__str__()

    def __str__(self):

        for i in range(0, len(self.zoo)):
            print(i + 1, ")", self.zoo[i])
