#                       Лекция 13 Класове задачи
#
#
# Задача 1. Дефинирайте клас Student, който съдържа следната информация за
# студентите: трите имена, курс, специалност, университет, електронна поща и телефонен
# номер.
#
#
# class Student():
#     def __init__(self, name, curse, subject, university, email, phone):
#         self.name = name
#         self.curse = curse
#         self.subject = subject
#         self.university = university
#         self.email = email
#         self.phone = phone
#
#
# Задача 2. Декларирайте конструктор за класа Student, които да инициализира всички
# атрибути на класа. Данните за полетата, които не са известни трябва да се
# инициализират съответно със стойности с None, 0, или “”.
#
#
# class Student:
#     def __init__(self, name="", curse=None, subject="", university="", email="", phone=None):
#         self.name = name
#         self.curse = curse
#         self.subject = subject
#         self.university = university
#         self.email = email
#         self.phone = phone
#
#
# Задача 3. Добавете статично поле в класа Student, в което се съхранява броя на
# създадените обекти от този клас.
#
#
# class Student:
#     count = 0
#
#     def __init__(self, name="", curse=None, subject="", university="", email="", phone=None):
#         self.name = name
#         self.curse = curse
#         self.subject = subject
#         self.university = university
#         self.email = email
#         self.phone = phone
#         Student.count += 1
#
#
# Pesho = Student()
# Maria = Student()
# print(Student.count)
#
#
# Задача 4. Добавете метод в класа Student, който извежда пълна информация за
# студента.
#
#
# class Student:
#     count = 0
#
#     def __init__(self, name="", curse=None, subject="", university="", email="", phone=None):
#         self.name = name
#         self.curse = curse
#         self.subject = subject
#         self.university = university
#         self.email = email
#         self.phone = phone
#         Student.count += 1
#
#     def representation(self):
#         print(f'Name: {self.name}')
#         print(f'Curse: {self.curse}')
#         print(f'Subject: {self.subject}')
#         print(f'University: {self.university}')
#         print(f'E-mail: {self.email}')
#         print(f'Phone: {self.phone}')
#
#
# pesho = Student()
# pesho.name = "Petar Ivanov Petrov"
# pesho.curse = 2
# pesho.subject = "Applied mathematics"
# pesho.university = "UMF"
# pesho.email = "p.petrov@gmail.com"
# pesho.phone = "08787123456"
#
# pesho.representation()
#
#
#
# Задача 5. Модифицирайте текущия код на класа Student така, че да капсулирате данните
# в класа чрез свойства.
#
#
# class Student:
#     count = 0
#
#     def __init__(self, name="", curse=None, subject="", university="", email="", phone=None):
#         self._name = name
#         self.curse = curse
#         self.subject = subject
#         self.university = university
#         self.email = email
#         self.phone = phone
#         Student.count += 1
#
#     def set_name(self, new_name):
#         self._name = new_name
#
#     def get_name(self):
#         return self._name
#
#
# maria = Student()
# maria.set_name("Mimi")
# print(maria.get_name())
#
#
#
#
# Задача 6. Напишете клас StudentTest, който да тества функционалността на класа
# Student.
#
#
# class Student():
#     number_of_students = 0
#
#     def __init__(self, name='', course=None, specialisation='', university='', email=None, phone=None):
#         self.name = name
#         self.course = course
#         self.specialisation = specialisation
#         self.university = university
#         self.__email = email
#         self.phone = phone
#
#     # getter
#     @property
#     def email(self):
#         return self.__email
#
#     # setter
#     @email.setter
#     def email(self, x):
#         if isinstance(x, str):
#             self.__email = x
#         else:
#             raise Exception(f'{x} is not string!')
#
#     def get_info(self):
#         print(f'{self.name} is a student of {self.university} in {self.course}\
# 		 with {self.specialisation}.\nContacts: {self.email}, {self.phone}')
#
#     def get_name(self):
#         print(f'Name of the student is: {self.name}')
#
#     def get_specialisation_info(self):
#         print(f'Course: {self.course} Specialisation: {self.specialisation}, University: {self.university}')
#
#     def get_contact(self):
#         print(f"Student's contact info is phone: {self.phone}, email: {self.email}")
#
#
# class TestStudent():
#
#     def __init__(self, student):
#         self.studentClass = student
#
#     def test_name(self, name):
#         test_student = self.studentClass(name)
#         if name == test_student.name:
#             print('OK')
#         else:
#             print('Error')
#
#     test_students = []
# #
#
# Задача 7. Добавете статичен метод в класа StudentTest, който създава няколко обекта от
# тип Student и ги съхранява в статични полета. Създайте статично свойство на класа, което
# да ги достъпва. Напишете тестова програма, която да извежда информацията за тях в
# конзолата.
#
#
#     @staticmethod
# 	def create_students(studentClass):
#
# 		TestStudent.test_students.append(studentClass('Gosho', 'Python', 'Programing', 'NetIT', 'python@org.bg', '089888888'))
# 		TestStudent.test_students.append(studentClass('Pesho', 'Java', 'Programing', 'NetIT', 'java@org.bg', '087888888'))
# 		TestStudent.test_students.append(studentClass('Acho', 'JavaScript', 'Programing', 'NetIT', 'jacasvript@org.bg', '089888888'))
# 		TestStudent.test_students.append(studentClass('Spas', 'Ruby', 'Programing', 'NetIT', 'ruby@org.bg', '098888888'))
# 		return TestStudent.test_students
#
# 	def get_students(self):
# 		for student in self.create_students():
# 			print(student.name)
#
#
# test1 = TestStudent(Student)
# test1.test_name('Gosho')
#
# for test_student in TestStudent.create_students(Student):
# 	print(test_student.name)
#
#
# test1.get_students()
# test1_students = test1.create_students().copy()

#
# Задача 8. Дефинирайте клас, който съдържа информация за мобилен телефон: модел,
# производител, цена, собственик, характеристики на батерията (модел, idle time и часове
# разговор /hours talk/) и характеристики на екрана (големина и цветове).
#
#
# class Phone:
#     def __init__(self, model, manufacturer, prise, owner):
#         self.model = model
#         self.manufacturer = manufacturer
#         self.prise = prise
#         self.owner = owner
#
#
# class Battery:
#     def __init__(self, model, idle_time, hours_talk):
#         self.model = model
#         self.idle_time = idle_time
#         self.hours_talk = hours_talk
#
#
# class Screen:
#     def __init__(self, size, colors):
#         self.size = size
#         self.colors = colors
#
#
# galaxy_s9 = Phone("Galaxy S9", "Samsung", 700, "Pesho")
#
# battery_s9 = Battery("Li-Ion 3000 mAh, non-removable (11.55 Wh)", 45, 32)
#
# screen_s9 = Screen("5.8 inches", "sRGB / Rec. 709 Color Gamut")
#
#
# Задача 9. Декларирайте конструктор за всеки от създадените класове от предходната
# задача. Данните за полетата, които не са известни трябва да се инициализират
# съответно със стойности с None, 0, или “”.
#
#
# class Phone:
#     def __init__(self, model="", manufacturer="", prise=0, owner=""):
#         self.model = model
#         self.manufacturer = manufacturer
#         self.prise = prise
#         self.owner = owner
#
#
# class Battery:
#     def __init__(self, model="", idle_time=0, hours_talk=0):
#         self.model = model
#         self.idle_time = idle_time
#         self.hours_talk = hours_talk
#
#
# class Screen:
#     def __init__(self, size=0, colors=""):
#         self.size = size
#         self.colors = colors
#
#
# Задача 10. Към класа за мобилен телефон от предходните две задачи, добавете
# статично поле nokiaN95, което да съхранява информация за мобилен телефон модел
# Nokia 95. Добавете метод, в същия клас, който извежда информация за това статично
# поле.
#
# #
#
# class Phone:
#     def __init__(self, model="", manufacturer="", prise=0, owner=""):
#         self.model = model
#         self.manufacturer = manufacturer
#         self.prise = prise
#         self.owner = owner
#
#     phones = []
#
#     @staticmethod
#     def create_phone():
#         Phone.phones.append("nokiaN95", "Nokia", 200, "Pesho")
#         return Phone.phones
#
#
#     def get_phone(self):
#         for phone in self.create_phone():
#             print(phone.model)
#
#
#
# Задача 11. Добавете изброим тип BatteryType, който съдържа стойности за тип на
# батерията (Li-Ion, NiMH, NiCd, …) и го използвайте като ново поле за класа Battery.
#
#
#
# from enum import Enum
#
# BatteryType = {
# 	'LiIon':1,
# 	'NiMH':2,
# 	'NiCd':3
# }
#
# # class BatteryType(Enum):
# # 	LiIon=1
# # 	NiMH=2
# # 	NiCd=3
#
# class Battery:
# 	def __init__(self, battery_type) -> None:
# 		self.battery_type = battery_type
#
#
# bat1 = Battery(BatteryType['NiMH'])
#
# print(bat1.battery_type)
#
#
#
# Задача 12. Добавете метод в класа GSM, който да връща информация за обекта под
# формата на string.
#
#
# class Phone:
#     def __init__(self, model="", manufacturer="", prise=0, owner=""):
#         self.model = model
#         self.manufacturer = manufacturer
#         self.prise = prise
#         self.owner = owner
#
#     def __str__(self):
#         return f'Model: {self.model}, manufacturer: {self.manufacturer}, prise: {self.prise}, owner: {self.owner}.'
#
#
# Nokia = Phone(3310, 'Nokia', 200, 'Ivan')
# print(Nokia)
#
#
#
# Задача 13. Дефинирайте свойства, за да капсулирате данните в класовете GSM, Battery
# и Display.
#
#
# class Phone:
#     def __init__(self, model="", manufacturer="", prise=0, owner=""):
#         self._model = model
#         self.manufacturer = manufacturer
#         self.prise = prise
#         self.owner = owner
#
#     def set_model(self, new_model):
#         self._model = new_model
#
#     def get_model(self):
#         return self._model
#
#
# galaxy = Phone()
# galaxy.set_model("S9")
# print(galaxy.get_model())
#
# class Battery:
#     def __init__(self, model="", idle_time=0, hours_talk=0):
#         self._model = model
#         self.idle_time = idle_time
#         self.hours_talk = hours_talk
#
#     def set_model(self, new_model):
#         self._model = new_model
#
#     def get_model(self):
#         return self._model
#
#
# class Screen:
#     def __init__(self, size=0, colors=""):
#         self._size = size
#         self.colors = colors
#
#     def set_size(self, new_size):
#         self._size = new_size
#
#     def get_size(self):
#         return self._size
#
#
#
# Задача 14. Напишете клас GSMTest, който тества функционалностите на класа GSM.
# Създайте няколко обекта от дадения клас и ги запазете в списък. Изведете информация
# за създадените обекти. Изведете информация за статичното поле nokiaN95.
#
#
# class Phone:
#     def __init__(self, model="", manufacturer="", prise=0, owner=""):
#         self.model = model
#         self.manufacturer = manufacturer
#         self.prise = prise
#         self.owner = owner
#
#
# class GSMTest():
#
#     def __init__(self, phone):
#         self.phoneClass = phone
#
#     def test_model(self, model):
#         test_phone = self.phoneClass(model)
#         if model == test_phone.model:
#             print('OK')
#         else:
#             print('Error')
#
#     test_model = []
#
#
# tests = []
# test_1 = GSMTest
# test_2 = GSMTest
# test_3 = GSMTest
#
# tests.append(test_1)
# tests.append(test_2)
# tests.append(test_3)
#
# print(tests)
#
#
# Задача 15. Създайте клас Call, който съдържа информация за разговор, осъществен
# през мобилен телефон. Той трябва да съдържа информация за датата, времето на
# започване и продължителността на разговора.
#
#
#
# class Call:
#
#     def __init__(self, date, time, duration):
#         self.date = date
#         self.time = time
#         self.duration = duration
#
#
#
# Задача 16. Добавете свойство архив с обажданията – callHistory, което да пази списък
# от осъществените разговори.
#
#
# class Call:
#
#     callHistory = list()
#
#     def __init__(self, date, time, duration):
#         self.date = date
#         self.time = time
#         self.duration = duration
#         callData = list()
#         callData.append(date)
#         callData.append(time)
#         callData.append(duration)
#         Call.callHistory.append(callData)
#
#
# pesho = Call("14.04.2022", "15:30", 14)
# maria = Call("15.04.2022", "18:10", 25)
# print(Call.callHistory)
#
#
#
# Задача 17. В класа GSM добавете методи за добавяне и изтриване на обаждания (Call)
# в архива с обаждания на мобилния телефон. Добавете метод, който изтрива всички
# обаждания от архива.
#
#
# class Call:
#     callHistory = list()
#
#     def __init__(self, date, time, duration):
#         self.date = date
#         self.time = time
#         self.duration = duration
#         callData = list()
#         callData.append(date)
#         callData.append(time)
#         callData.append(duration)
#         Call.callHistory.append(callData)
#
#
# class Phone:
#     def __init__(self, model="", manufacturer="", prise=0, owner=""):
#         self.model = model
#         self.manufacturer = manufacturer
#         self.prise = prise
#         self.owner = owner
#
#     def add_call():
#         call = list()
#         call_date = input("Please add the date of the call you would like to add: ")
#         call_time = input("Please add the time of the call you would like to add: ")
#         call_duration = input("Please add the duration of the call you would like to add: ")
#         call.append(call_date)
#         call.append(call_time)
#         call.append(call_duration)
#         Call.callHistory.append(call)
#
#     def delete_call():
#         Call.callHistory.pop()
#
#
#     def clear_call_history():
#         Call.callHistory.clear()
#
#
# Phone.add_call()
# print(Call.callHistory)
# print(20 * '*')
# Phone.add_call()
# print(Call.callHistory)
# print(20 * '*')
# Phone.add_call()
# print(Call.callHistory)
# print(20 * '*')
# Phone.delete_call()
# print(Call.callHistory)
# print(20 * '*')
# Phone.clear_call_history()
# print(Call.callHistory)
#
#
#
# Задача 18. В класа GSM добавете метод, който пресмята общата сума на обажданията
# (Call) от архива с обаждания на телефона (callHistory) като нека цената за едно обаждане
# се подава като параметър на метода.
#
#
class Call:
    callHistory = list()

    def __init__(self, date, time, duration):
        self.date = date
        self.time = time
        self.duration = duration
        callData = list()
        callData.append(date)
        callData.append(time)
        callData.append(duration)
        Call.callHistory.append(callData)


class Phone:
    price = 0

    def __init__(self, model="", manufacturer="", prise=0, owner=""):
        self.model = model
        self.manufacturer = manufacturer
        self.prise = prise
        self.owner = owner


    def total_prise(prise_min):
        total_duration = 0
        for el in Call.callHistory:
            for x in range(0, (len(Call.callHistory) - 1)):
                total_duration += int(el[x][2])
        Phone.prise = total_duration * int(prise_min)


pesho = Call("14.04.2022", "15:30", 14)
maria = Call("15.04.2022", "18:10", 25)

Phone.total_prise(2)
#
# # ERROR ?????????????????????????????????????????????????
#
#
#
# Задача 19. Създайте клас GSMCallHistoryTest, с който да се тества функционалността на
# класа GSM, от задача 12, като обект от тип GSM. След това, към него добавете няколко
# обаждания (Call). Изведете информация за всяко едно от обажданията. Ако допуснем,
# че цената за минута разговор е 0.37, пресметнете и отпечатайте общата цена на
# разговорите. Премахнете най-дългият разговор от архива с обаждания и пресметнете
# общата цена за всички разговори отново. Най-накрая изтрийте архива с обаждания.
#
# ?????????????????????????????????????????????????????????????????????????????????????????
#
#
# Задача 20. Нека е дадена библиотека с книги. Дефинирайте класове съответно за
# библиотека и книга. Библиотеката трябва да съдържа име и списък от книги. Книгите
# трябва да съдържат информация за заглавие, автор, издателство, година на издаване и
# ISBN-номер. В класа, който описва библиотека, добавете методи за добавяне на книга
# към библиотеката, търсене на книга по предварително зададен автор, извеждане на
# информация за дадена книга и изтриване на книга от библиотеката.
#
#
#
# class Library:
#     def __init__(self, name, books_list=None):
#         self.name = name
#         if books_list is None:
#             self.books_list = []
#         else:
#             self.books_list = books_list
#
#     def add_book(self, book):
#         self.books_list = list()
#         self.books_list.append(book)
#
#     def search_book():
#         searched_author = input("Please provide the name of the author you are searching for: ")
#         for book in Library.books_list:
#             if book[1] == searched_author:
#                 print(book[1])
#
#
# class Book:
#     def __init__(self, title, author, publisher, publication_year, ISBN_number):
#         self.title = title
#         self.author = author
#         self.publisher = publisher
#         self.publication_year = publication_year
#         self.ISBN_number = ISBN_number
#
#
# def __str__(self): return f'''Book title: {self.title}, author: {self.author}, publisher: {self.publisher},
# publication year: {self.publication_year}, ISBN number: {self.ISBN_number}.'''
#
#
# def remove_book(self, book):
#     self.books_list.remove(book)
#
#
# library = Library("Sofia's Library", "Fantasy books")
# book1 = Book("Harry Potter and the Philosopher\'s Stone", "J.K.Rowling", "Bloomsbury", 1997, 9780747532743)
# library.add_book(book1)
#
# Library.search_book()
#
# print(book1)
#
# Library.remove_bok(book1)
#
#
# # ???????????????????????????????????????????????????
#
#
# Задача 21. Напишете тестов клас, който създава обект от тип библиотека, добавя
# няколко книги към него и извежда информация за всяка една от тях. Имплементирайте
# тестова функционалност, която намира всички книги, чийто автор е Стивън Кинг и ги
# изтрива. Накрая, отново изведете информация за всяка една от оставащите книги.
#
#
# # ???????????????????????????????????????????????????
#
#
# Задача 22. Дадено ни е училище. В училището имаме класове и ученици. Всеки клас
# има множество от преподаватели. Всеки преподавател има множество от дисциплини,
# по които преподава. Учениците имат име и уникален номер в класа. Класовете имат
# уникален текстов идентификатор. Дисциплините имат име, брой уроци и брой
# упражнения. Трябва да декларирате класове заедно с техните полета, свойства, методи
# и конструктори. Дефинирайте и тестов клас, който демонстрира, че останалите класове
# работят коректно.
#
#
# class Teacher:
#     def __init__(self, subject):
#         self.subject = subject
#
#
# class Student:
#     def __init__(self, name, number):
#         self.name = name
#         self.number = number
#
# class School_Class:
#     def __init__(self, identification):
#         self.identification = identification
#
#
# class Subject:
#     def __init__(self, name, amount_lectures, amount_labs):
#         self.name = name
#         self.amount_lectures = amount_lectures
#         self.amount_labs = amount_labs
#
#     # Test ?????????????????????????????????????????????????
