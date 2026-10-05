# class Dog:
#     def __init__(self, name):
#         self.name = name

#     def bark(self):
#         print(f"{self.name} говорит: Гав!")


# my_dog = Dog("Sharik")
# my_dog2 = Dog("Bobik")
# my_dog.bark()
# my_dog2.bark()
# print(type(my_dog))


# class Animal:
#     def  __init__(self, name):
#         self.name = name

#     def breathe(self):
#         print("Дышу")

# class Dog(Animal):
#     def bark(self):
#         print("Гав!")

# my_dog = Dog("Шарик")
# my_dog.breathe()
# my_dog.bark()
# print(my_dog.name)



class Animal:
    def __init__(self, name):
        self.name = name
        print("Animal создан")

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed
        print("Dog создан")

my_dog = Dog("Шарик", "Лабрадор")
print(my_dog.name)
print(my_dog.breed)