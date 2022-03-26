#                                  Лекция 9 Множества и тупъли


# Задача 1. Да се напише програма, която сортира в нарастващ ред списък, чиито елементи
# са tuples. При сортирането да се взема предвид последният елемент във всеки tuple. В
# списъкът не трябва да се съдържат празни tuples


# list_tuples = []
# user_tuple = 1
#
# while user_tuple:
#         list_temp = 0
#         tuple_temp = 0
#         user_tuple = input("Please provide two numbers divided with a comma (e.g. 1,2): ")
#         if user_tuple == '':
#             break
#         else:
#             list_temp = user_tuple.split(",")
#             tuple_temp = tuple(list_temp)
#             list_tuples.append(tuple_temp)
#
#
# list_tuples = [[int(s) for s in sublist] for sublist in list_tuples]
#
# print(sorted(list_tuples, key=lambda x: x[1]))


# Задача 2. Да се напише програма, която да създаде множество от множества, което да
# съдържа: А - B, B, B-A, A-B + B-A, A & B, A | B, където A и B са два списъка, чиито
# елементи се въвеждат от клавиатурата.


# A = []
# B = []
#
#
# while True:
#     element_A = input("Please provide a word or number for the first set:")
#     if element_A == '':
#         break
#     else:
#         A.append(element_A)
#
# print()
#
# while True:
#     element_B = input("Please provide a word or number for the second set:")
#     if element_B == '':
#         break
#     else:
#         B.append(element_B)
#
# A = set(A)
# B = set(B)
# result = ((A-B) | B | (B-A) | ((A-B) | (B-A)) | (A & B) | (A | B))
# print(result)


# Задача 3. Да се напише програма, която да създава tuple (a, b), представящ броят на
# уникалните елементи в дадено множество и b представящо броят на дублицираните
# елементи в множеството. Множеството да се въвежда от клавиатурата.


# l = []
# b = 0
#
# while True:
#     element_A = input("Please provide a word or number: ")
#     if element_A == '':
#         break
#     else:
#         l.append(element_A)
#
# a = set(l)
# a = len(a)
#
# l_unique = []
# l_duplicates = []
# for el in l:
#     if el not in l_unique:
#         l_unique.append(el)
#     else:
#         l_duplicates.append(el)
#
# b = len(l_duplicates)
#
# print(tuple([a, b]))


# Задача 4. Да се напише програма, която създава речник, който да съдържа следните
# операции |, &, -, между две множества a и b. Множествата да се въвеждат от
# клавиатурата. Речникът да има за ключ конкретната операция, а за стойност полученият
# резултат от изпълнението на операцията.


# A = []
# B = []
# d = {}
#
# while True:
#     element_A = input("Please provide a word or number for the first set:")
#     if element_A == '':
#         break
#     else:
#         A.append(element_A)
#
# print()
#
# while True:
#     element_B = input("Please provide a word or number for the second set:")
#     if element_B == '':
#         break
#     else:
#         B.append(element_B)
#
# A = set(A)
# B = set(B)
#
#
# d["A|B"] = A | B
# d["A&B"] = A & B
# d["A-B"] = A - B
#
# print(d)


# Задача 5. Помолете потребителя да въведе координатите на дадена точка и да намери
# разстоянието на точката до началото (0, 0). За абсолютна стойност може да използвате
# вградената функция abs(). Формулата за намиране на разстояние
#
#       &
#
# Задача 6. Помолете потребителя да въведе две точки (x и y координати) и да намери
# разстоянието между тях.


# from math import sqrt
#
# coordinates_a = input("Please provide the coordinates of A divided with a comma (e.g. 1,2): ")
# coordinates_list_a = coordinates_a.split(",")
# coordinates_list_a = [int(s) for s in coordinates_list_a]
#
# x1 = abs(coordinates_list_a[0])
# y1 = abs(coordinates_list_a[1])
#
# coordinates_b = input("Please provide the coordinates of the B divided with a comma (e.g. 1,2): ")
# coordinates_list_b = coordinates_b.split(",")
# coordinates_list_b = [int(s) for s in coordinates_list_b]
#
# x2 = abs(coordinates_list_b[0])
# y2 = abs(coordinates_list_b[1])
#
#
#
# result = sqrt(((x1-x2)**2) + ((y1 - y2)**2))
#
# print(result)


# Задача 7. Ако имате въведени три точки (x1, y1), (x2, y2), (x3, y3) и те не са колинеарни,
# тогава намерете вида на триъгълника, образуван от тях (равностранен, равнобедрен или
# разностранен). Правилото за определяне дали се образува триъгълник е като му се
# намерят страните и се направят следните проверки c < a + b, b+ c < a, a+ c < b.


# from math import sqrt
#
# coordinates_a = input("Please provide the coordinates of A divided with a comma (e.g. 1,2): ")
# coordinates_list_a = coordinates_a.split(",")
# coordinates_list_a = [int(s) for s in coordinates_list_a]
#
# x1 = abs(coordinates_list_a[0])
# y1 = abs(coordinates_list_a[1])
#
# coordinates_b = input("Please provide the coordinates of the B divided with a comma (e.g. 1,2): ")
# coordinates_list_b = coordinates_b.split(",")
# coordinates_list_b = [int(s) for s in coordinates_list_b]
#
# x2 = abs(coordinates_list_b[0])
# y2 = abs(coordinates_list_b[1])
#
#
# coordinates_c = input("Please provide the coordinates of the C divided with a comma (e.g. 1,2): ")
# coordinates_list_c = coordinates_c.split(",")
# coordinates_list_c = [int(s) for s in coordinates_list_c]
#
# x3 = abs(coordinates_list_c[0])
# y3 = abs(coordinates_list_c[1])
#
#
# AB = sqrt(((x1-x2)**2) + ((y1 - y2)**2))      #c
# BC = sqrt(((x2-x3)**2) + ((y2 - y3)**2))      #a
# AC = sqrt(((x1-x3)**2) + ((y1 - y3)**2))      #b
#
#
#
# if AB == BC == AC:
#     print("Равностранен.")
# elif AB == BC != AC:
#     print("Равнобедрен")
# elif AB == AC != BC:
#     print("Равнобедрен")
# elif BC == AC != AB:
#     print("Равнобедрен")
# else:
#     print("Разностранен.")


# Задача 8. Използвайте задача 7 и проверете дали триъгълникът е с прав ъгъл.
# Използвайте sin теорема: sin(от даден ъгъл) = срещулежаща страна / хипотенузата.
# Използвайте функция math.asin да превърнете в радиани, и след това math.degrees за да
# превърнете в градуси. Като sin(90) = 1, sin(30) = ½ и т.н. Ако сборът на два от ъглите е
# 90 градуса, то автоматично третият е равен на 90 градуса.


# import math
#
# coordinates_a = input("Please provide the coordinates of A divided with a comma (e.g. 1,2): ")
# coordinates_list_a = coordinates_a.split(",")
# coordinates_list_a = [int(s) for s in coordinates_list_a]
#
# x1 = abs(coordinates_list_a[0])
# y1 = abs(coordinates_list_a[1])
#
# coordinates_b = input("Please provide the coordinates of the B divided with a comma (e.g. 1,2): ")
# coordinates_list_b = coordinates_b.split(",")
# coordinates_list_b = [int(s) for s in coordinates_list_b]
#
# x2 = abs(coordinates_list_b[0])
# y2 = abs(coordinates_list_b[1])
#
#
# coordinates_c = input("Please provide the coordinates of the C divided with a comma (e.g. 1,2): ")
# coordinates_list_c = coordinates_c.split(",")
# coordinates_list_c = [int(s) for s in coordinates_list_c]
#
# x3 = abs(coordinates_list_c[0])
# y3 = abs(coordinates_list_c[1])
#
#
# a = math.sqrt(((x3-x2)**2) + ((y3 - y2)**2))
# b = math.sqrt(((x1-x3)**2) + ((y1 - y3)**2))
# c = math.sqrt(((x2-x1)**2) + ((y2 - y1)**2))
#
# if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
#     print("This is a right angled triangle.")
# else:
#     print("This is not a right angled triangle.")


# Задача 9. В задача номер 7 намерете ъглите на триъгълника.


# import math
#
# coordinates_a = input("Please provide the coordinates of A divided with a comma (e.g. 1,2): ")
# coordinates_list_a = coordinates_a.split(",")
# coordinates_list_a = [int(s) for s in coordinates_list_a]
#
# x1 = abs(coordinates_list_a[0])
# y1 = abs(coordinates_list_a[1])
#
# coordinates_b = input("Please provide the coordinates of the B divided with a comma (e.g. 1,2): ")
# coordinates_list_b = coordinates_b.split(",")
# coordinates_list_b = [int(s) for s in coordinates_list_b]
#
# x2 = abs(coordinates_list_b[0])
# y2 = abs(coordinates_list_b[1])
#
#
# coordinates_c = input("Please provide the coordinates of the C divided with a comma (e.g. 1,2): ")
# coordinates_list_c = coordinates_c.split(",")
# coordinates_list_c = [int(s) for s in coordinates_list_c]
#
# x3 = abs(coordinates_list_c[0])
# y3 = abs(coordinates_list_c[1])
#
#
# a = math.sqrt(((x3-x2)**2) + ((y3 - y2)**2))
# b = math.sqrt(((x1-x3)**2) + ((y1 - y3)**2))
# c = math.sqrt(((x2-x1)**2) + ((y2 - y1)**2))
#
#
# degrees_c = round(180/math.pi * math.acos((a**2 + b**2 - c**2) / (2*a*b)))
# degrees_b = round(180/math.pi * math.acos((a**2 + c**2 - b**2) / (2*a*c)))
# degrees_a = round(180/math.pi * math.acos((b**2 + c**2 - a**2) / (2*b*c)))
#
#
# print(degrees_a, degrees_b, degrees_c)
# print(degrees_a + degrees_b + degrees_c)


# Задача 10. Помолете потребителя да въведе две точки и да открие дали те са на равни
# разстояния от началото на координатната система.


# import math
#
# coordinates_a = input("Please provide the coordinates of A divided with a comma (e.g. 1,2): ")
# coordinates_list_a = coordinates_a.split(",")
# coordinates_list_a = [int(s) for s in coordinates_list_a]
#
# x1 = abs(coordinates_list_a[0])
# y1 = abs(coordinates_list_a[1])
#
# coordinates_b = input("Please provide the coordinates of the B divided with a comma (e.g. 1,2): ")
# coordinates_list_b = coordinates_b.split(",")
# coordinates_list_b = [int(s) for s in coordinates_list_b]
#
# x2 = abs(coordinates_list_b[0])
# y2 = abs(coordinates_list_b[1])
#
# x3 = 0
# y3 = 0
#
# distance_1 = math.sqrt(((x1-x3)**2) + ((y1 - y3)**2))
# distance_2 = math.sqrt(((x2-x3)**2) + ((y2 - y3)**2))
#
#
# if distance_1 == distance_2:
#     print("The distance is equal.")
# elif distance_1 > distance_2:
#     print("The distance from A is bigger.")
# else:
#     print("The distance from B is bigger.")


# Задача 11. Помолете потребителя да въведе 4 точки и да ги подреди в зависимост от
# разстоянията им от началото на координатната система


# import math
#
# d = {}
#
# coordinates_a = input("Please provide the coordinates of A divided with a comma (e.g. 1,2): ")
# coordinates_list_a = coordinates_a.split(",")
# coordinates_list_a = [int(s) for s in coordinates_list_a]
#
# x1 = abs(coordinates_list_a[0])
# y1 = abs(coordinates_list_a[1])
#
# coordinates_b = input("Please provide the coordinates of the B divided with a comma (e.g. 1,2): ")
# coordinates_list_b = coordinates_b.split(",")
# coordinates_list_b = [int(s) for s in coordinates_list_b]
#
# x2 = abs(coordinates_list_b[0])
# y2 = abs(coordinates_list_b[1])
#
#
# coordinates_c = input("Please provide the coordinates of C divided with a comma (e.g. 1,2): ")
# coordinates_list_c = coordinates_c.split(",")
# coordinates_list_c = [int(s) for s in coordinates_list_c]
#
# x3 = abs(coordinates_list_c[0])
# y3 = abs(coordinates_list_c[1])
#
#
# coordinates_d = input("Please provide the coordinates of D divided with a comma (e.g. 1,2): ")
# coordinates_list_d = coordinates_d.split(",")
# coordinates_list_d = [int(s) for s in coordinates_list_d]
#
# x4 = abs(coordinates_list_d[0])
# y4 = abs(coordinates_list_d[1])
#
# x5 = 0
# y5 = 0
#
# distance_1 = math.sqrt(((x1-x5)**2) + ((y1 - y5)**2))
# distance_2 = math.sqrt(((x2-x5)**2) + ((y2 - y5)**2))
# distance_3 = math.sqrt(((x3-x5)**2) + ((y3 - y5)**2))
# distance_4 = math.sqrt(((x4-x5)**2) + ((y4 - y5)**2))
#
#
# d[distance_1] = coordinates_list_a
# d[distance_2] = coordinates_list_b
# d[distance_3] = coordinates_list_c
# d[distance_4] = coordinates_list_d
#
#
# d_sorted = dict(sorted(d.items()))
#
# for value in d_sorted.values():
#     print(value)


# Задача 12. Използвайте задача 11 и подредете точки по реда на техните x координати в
# низходящ ред.


# d = {}
#
# coordinates_a = input("Please provide the coordinates of A divided with a comma (e.g. 1,2): ")
# coordinates_list_a = coordinates_a.split(",")
# coordinates_list_a = [int(s) for s in coordinates_list_a]
#
# x1 = abs(coordinates_list_a[0])
# y1 = abs(coordinates_list_a[1])
#
# coordinates_b = input("Please provide the coordinates of the B divided with a comma (e.g. 1,2): ")
# coordinates_list_b = coordinates_b.split(",")
# coordinates_list_b = [int(s) for s in coordinates_list_b]
#
# x2 = abs(coordinates_list_b[0])
# y2 = abs(coordinates_list_b[1])
#
#
# coordinates_c = input("Please provide the coordinates of C divided with a comma (e.g. 1,2): ")
# coordinates_list_c = coordinates_c.split(",")
# coordinates_list_c = [int(s) for s in coordinates_list_c]
#
# x3 = abs(coordinates_list_c[0])
# y3 = abs(coordinates_list_c[1])
#
#
# coordinates_d = input("Please provide the coordinates of D divided with a comma (e.g. 1,2): ")
# coordinates_list_d = coordinates_d.split(",")
# coordinates_list_d = [int(s) for s in coordinates_list_d]
#
# x4 = abs(coordinates_list_d[0])
# y4 = abs(coordinates_list_d[1])
#
#
# d[x1] = y1
# d[x2] = y2
# d[x3] = y3
# d[x4] = y4
#
#
# d_sorted = dict(sorted(d.items()))
#
# for key,value in d_sorted.items():
#     print({key}, ":", {value})
