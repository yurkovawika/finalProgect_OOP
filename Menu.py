from Zoo import Zoo
from petAnimals.Chicken import Chicken
from petAnimals.Cat import Cat
from petAnimals.Dog import Dog
from wildAnimals.Strok import Strok
from wildAnimals.Tiger import Tiger
from wildAnimals.Wolf import *

class Menu():

    def __init__(self):
        self.__zoo = Zoo()
        pass

    def main_menu(self):
        while True:
            print("Меню :\n" +
                  "\t1. Посмотреть информацию о всех животных;\n" +
                  "\t2. Посмотреть информацию о конретном животном;\n" +
                  "\t3. Добавить новое животное;\n" +
                  "\t4. Заставить издать звук конкретное животное;\n" +
                  "\t5. Заставить все животных издать звук;\n" +
                  "\t6. Убрать животное из зоопарка;\n" +
                  "\t7. Выйти.\n" +
                  "\n***Введите ваш выбор ----->> ")
            try:
                choice = int(input())
                match choice:
                    case 1:
                        print("В зоопарке сейчас ",self.__zoo.get_len(), "животных")
                        self.__zoo.__str__()
                    case 2:
                        idx = int(input("Введите индекс животного: "))
                        print(self.__zoo.get_info(idx))
                    case 3:
                        print("Выберите какое животное хотите добавить и введите его индекс:\n" +
                              "\t1. Кошка;\n" +
                              "\t2. Собака;\n" +
                              "\t3. Тигр;\n" +
                              "\t4. Волк;\n" +
                              "\t5. Курица;\n" +
                              "\t6. Аист\n" +
                              "\t7. Выйти обратно в меню\n" +
                              "\n***Введите ваш выбор ----->> ")
                        idx = int(input())
                        Menu._addAnimal(self, idx)
                    case 4:
                        i = int(input("Введите индекс животного: "))
                        self.__zoo.make_sound(i)
                    case 5:
                        self.__zoo.make_sound_all()
                    case 6:
                        idx = int(input("Введите индекс животного для удаления: "))
                        self.__zoo.removed_animal(idx)
                        print("Животное удалено")
                    case 7:
                        break
            except (Exception):
                print("Ошибка. Операция не выполнена.")

    def _addAnimal(self, idx):
        try:
            match idx:
                case 1:
                    self.__zoo.add_animal(
                        Cat(input("Кличка: "), input("Порода: "), input("Цвет глаз: "), input("Рост: "), input("Вес: "),
                            input("Вакцинация: "), input("Наличие шерсти: ")))

                case 2:
                    self.__zoo.add_animal(
                        Dog(input("Кличка: "), input("Порода: "), input("Цвет глаз: "), input("Рост: "), input("Вес: "),
                            input("Вакцинация: "), input("Дрессировка: ")))

                case 3:
                    self.__zoo.add_animal(
                        Tiger(input("Цвет глаз: "), input("Рост: "), input("Вес: "), input("Место обитания: "),
                              input("Дата обнаружения: "),
                              ))
                case 4:
                    self.__zoo.add_animal(
                        Wolf(input("Цвет глаз: "), input("Рост: "), input("Вес: "), input("Место обитания: "),
                             input("Дата обнаружения: "), input("Вожак стаи?: ")))
                case 5:
                    self.__zoo.add_animal(
                        Chicken(input("Кличка: "), input("Порода: "), input("Цвет глаз: "), input("Рост: "),
                                input("Вес: "),
                                input("Вакцинация: "), input("Цвет оперения: ")))
                case 6:
                    self.__zoo.add_animal(
                        Strok(input("Цвет глаз: "), input("Рост: "), input("Вес: "),
                              input("Место обитания: "), input("Дата обнаружения: "), input("Цвет оперения: "),
                              input("Высота полёта: ")))
                case 7:
                    self.main_menu()

        except (Exception):
            print("Ошибка. Операция не выполнена.")