#                         Лекция 14 Наследяване задачи
#
#
#
# 1. Дефинирайте клас Human със свойства "собствено име" и "фамилно име".
# Дефинирайте клас Student, наследяващ Human, който има свойство "оценка".
# Дефинирайте клас Worker, наследяващ Human, със свойства "надница" и "изработени
# часове". Имплементирайте и метод "изчисли надница за 1 час", който смята колко
# получава работникът за 1 час работа, на базата на надницата и изработените часове.
# Напишете съответните конструктори и методи за достъп до полетата (свойства).
# A) направете списък от 10 студента
# Б) направете списък от 10 работника
# Вход:
# На първия ред на входа ще бъде подадено цяло число N, което ще представлява броя
# на редовете които трябва да бъдат прочетени. На всеки от следващите N реда ще бъде
# подадена информация за работник в следната последователност: Име Фамилия
# Надница
# 3
# Petar Dimitrov 16 91
# Nikolay Dimitrov 29 17
# Georgi Georgiev 17 23
# Изход:
# На изхода се очаква да се изпишат въведени работници и изчислената им надница.
# Примерен изход:
# Petar Dimitrov 0.1758241758241758241758241758
# Nikolay Dimitrov 1.7058823529411764705882352941
# Georgi Georgiev 0.739130434782608695652173913
#
#
#
# class Human:
#     def __init__(self, name, surname):
#         self.name = name
#         self.surname = surname
#
#
# class Student(Human):
#     def __init__(self, name, surname, evaluation):
#         super().__init__(name, surname)
#         self.evaluation = evaluation
#
#
# class Worker(Human):
#
#     def __init__(self, name, surname, wage, hours_worked, workers_data=list(), workers_list=list()):
#         super().__init__(name, surname)
#         self.wage = wage
#         self.hours_worked = hours_worked
#         workers_data.append(Worker)
#         workers_list.append(workers_data)
#
#     def hourly_wage(self, wage, hours):
#         return wage / hours
#
#
#
#
#
# amount_of_workers = int(input("Please add the amount of workers between 0 and 10: "))
#
#
# for i in range(amount_of_workers):
# 	data = input('Enter data:')
# 	for d in data.split(' '):
# 		print(d)
#
# ----------------------------------------------------E.g.--------------------------------------------
#
# Ben = Worker("Ben", "Smith", 100, 8)
# John = Worker("John", "Doe", 120, 9)
# Rick = Worker("Rick", "Becker", 90, 7)
# Amanda = Worker("Amanda", "Johnes", 80, 8)
# Linda = Worker("Linda", "Walker", 100, 10)
# Maria = Worker("Maria", "Dias", 110, 9)
# Carlos = Worker("Carlos", "Vargas", 90, 9)
# Marco = Worker("Marco", "Dias", 130, 11)
# Vanesa = Worker("Vanesa", "Lopez", 80, 7)
#
#
# 2. Дефинирайте клас Shape със само един метод calculateSurface() и полета width и
# height. Дефинирайте два нови класа за триъгълник и правоъгълник, които
# имплементират споменатият метод. Този метод трябва да връща площта на
# правоъгълника (height*width) и триъгълника (height*width/2). Дефинирайте клас за
# кръг с подходящ конструктор, при когото при инициализация и двете полета (height и
# width) са с еднаква стойност (радиуса), и имплементирайте метод за изчисляване на
# площта. Направете списък от различни фигури и сметнете площта на всичките в друг
# списък.
# Вход:
# На първия ред ще се намира цяло число броя на фигурите които трябва да бъдат
# прочетени. Първата дума ще обозначава вида на фигурата ( „Circle“, „Triangle“ и
# “Rectangle” ). Ако фигурата е кръг след това добавяме едно дробно число показващо
# диаметъра му. Ако фигурата е триъгълник или правоъгълник ще следват две дробни
# числа – широчинат и височината му. (Всеки елемент от входа е разделен от другите
# чрез празно поле)
# Изход:
# На отделен ред да се изпише дробно число показващо площта на всяка въведена
# фигура.
#
#
# import math
#
#
# class Shape:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#
#     def calculateSurface(self, x, y):
#         return self.width * self.height
#
#
# class Rectangle(Shape):
#     def __init__(self, width, height):
#         super().__init__(width, height)
#
#
# class Triangle(Shape):
#     def __init__(self, width, height):
#         super().__init__(width, height)
#
#     def calculateSurface(self, x, y):
#         return (self.width * self.height) / 2
#
#
# class Circle:
#     def __init__(self, r):
#         self.r = r
#
#     def calculateSurface(self, r):
#         return math.pi * (r ** 2)
#
#
# number_of_shapes = int(input("How many shapes would you like to see: "))
#
# for i in range(number_of_shapes-1):
#     shape = input('Enter a shape: ')
#     if shape == 'rectangle':
#         height = float(input("Please provide the height in cm: "))
#         width = float(input("Please provide the width in cm: "))
#         shape = Rectangle
#         Rectangle.calculateSurface(height, width)
#     elif shape == 'triangle':
#         height = float(input("Please provide the height in cm: "))
#         width = float(input("Please provide the width in cm: "))
#         shape = Triangle
#         Triangle.calculateSurface(height, width)
#     elif shape == 'circle':
#         radius = float(input("Please provide the radius in cm: "))
#         shape = Circle
#         Circle.calculateSurface(radius)

#
# ??????????????????????????????????????????????????????????????????????   TypeError: Circle.calculateSurface() missing 1 required positional argument: 'r'
#
#
# 3. Имплементирайте следните обекти: куче (Dog), жаба (Frog), котка (Cat), котенце
# (Kitten), котарак (Tomcat). Всички те са животни (Animal). Животните се характеризират
# с възраст (age), име (name) и пол (gender). Всяко животно издава звук (метод на
# Animal).
# Cat = Miauuu!, Tomcat = Miau!, Kitten = Miauuuuuu!, Dog = Bauuu!, Frog = Kwak!
# Направете списък от различни животни и за всяко изписвайте на конзолата името,
# възрастта и звука, който издава.
# Вход:
# Входните данни ще бъдат прочетени от конзолата.
# Първата линия ще зададе стойност за n – общият брой животни в списъка.
# На следващите n на брой редове ще бъдат зададени данните в формат „Вид“, „Име“,
# „Години“ и „Пол“ - разделени с интервал.
# Входните данни винаги ще бъдат валидни и в описаният формат.
# Няма нужда от допълнителна проверка за верността им.
# Изход:
# Изхода трябва да бъде отпечатан на конзолата.
# На всяка n линия трябва да бъде отпечатан списък като имената на животните, техните
# години и звука, който издават.
#
#
#
# class Animal:
#     def __init__(self, species, age, name, gender, sound):
#         self.sound = None
#         self.species = species
#         self.age = age
#         self.name = name
#         self.gender = gender
#
#     def make_sound(self, sound):
#         if self.species == "Cat":
#             self.sound = "Miauuu!"
#         elif self.species == "Tomcat":
#             self.sound = "Miau!"
#         elif self.species == "Kitten":
#             self.sound = "Miauuuuuu!"
#         elif self.species == "Dog":
#             self.sound = "Bauuu!"
#         elif self.species == "Frog":
#             self.sound = "Kwak!"
#         else:
#             print("Unknown sound.")
#
#
# amount_of_animals = int(input("Please add the amount of animals: "))
#
# for i in range(amount_of_animals):
#     data = input('Enter data regarding species, age, name, gender:')
#     animals = []
#     for d in data.split(','):
#         animals.append(d)
#     print(animals)


# ????????????????????????????????? sound
