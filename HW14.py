#                                  Лекция 12 Функции задачи


# Задача 1. Да се напише функция, която да търси в списък. Като параметър да приема
# списък и да принтира ако елементът е в списъка неговата позиция, ако ли не да
# принтира, че не е намерен.


# def data_list():
#     aList = list()
#     while True:
#         element = input("Please provide an element for the list: ")
#         aList.append(element)
#         if element == "":
#             break
#
#
# def data_search():
#     el = input("Please provide your search: ")
#
#
# def searchList():
#     return aList.index(el) if el in aList else print(f"{el} not found.")
#
#
# aList = data_list()
# print()
# el = data_search()
#
# print(type(aList))                                       # ????????????????? Non Type
# searchList()

# ?????????????????????????????????????????????????????????????????????????????
#  If hard coded, it works:
#
#
# result = searchList([1, 2, 5, 6, 'seven,', 'cat'], 5)
# print(result)


# Задача 3. Да се напише програма, която да пита потребителя да въведе едно число от
# клавиатурата и да покаже съответното число от редицата на Фибoначи. Задачата да се
# реши с рекурсивна функция.


# n = int(input("Please provide a number: "))
#
#
# def calc_Fiboncci(n):
#     if n in {0, 1}:
#         return n
#     return calc_Fiboncci(n - 1) + calc_Fiboncci(n - 2)
#
#
# result = calc_Fiboncci(n)
# print(f"Number {n} in the Fibonacci sequence is {result}.")


# Задача 4. Да се напише програма, която да пита потребителя да въведе число от
# клавиатурата и да пресметне факториелът на това число. Да се използва рекурсия.


# n = int(input("Please provide a number: "))
#
#
# def calc_Factorial(n):
#     if n == 1:
#         return n
#     else:
#         return n * calc_Factorial(n - 1)
#
#
# result = calc_Factorial(n)
# print(f"The factorial of {n} is {result}.")


# Задача 5. Да се създаде програма, която да реализира няколко функции: добавяне (Add),
# изтриване (Remove), изтриване на всичко (clear), показване (show), край на програмата
# (Quit). Програмата да реализира програмна логика за количка за пазаруване (като тези
# в онлайн магазините). Потребителят да въвежда от клавиатурата даден елемент, след
# което да има възможност да го добави, изтрие, да види какво е поръчал.


# basket = []
#
#
# def add():
#     product = input("Please provide the name of the product you would like to put in your basket: ")
#     basket.append(product)
#
#
# def remove():
#     remove_product = input("Provide the name of the product to be removed from your basket: ")
#     basket.remove(remove_product)
#
#
# def clear():
#     basket.clear()
#
#
# def show():
#     print(basket)
#
#
# def shopping():
#     while True:
#
#         choice = int(input('''What would you like to do:
# #          press 1 for  product,
# #          2 for remove product,
# #          3 for clear the basket,
# #          4 to see the basked,
# #          5 to quit: '''))
#         if choice == 1:
#             add()
#         elif choice == 2:
#             remove()
#         elif choice == 3:
#             clear()
#         elif choice == 4:
#             show()
#         elif choice == 5:
#             print("Thank you for shopping.")
#             break
#         else:
#             print("Please provide a valid number.")
#
# 
# shopping()


# Задача 6. Да се напише програма, която да сортира списък от tuples използвайки
# Lambda


# t = [(1, 2), (5, 6), (3, 4)]
#
# t.sort(key=lambda x: x[1])
# print(t)


# Задача 7. Да се напише програма, която да сортира списък от речници използвайки
# Lambda.


# d = {1: 2, 5: 6, 3: 4}
#
# d_new = dict(sorted(d.items(), key=lambda x: x[0]))
# print(d_new)


# Задача 8. Да се напише програма, която да намира сечението на два списъка
# използвайки lambda.


# l1 = [1, 2, 3, 4, 5, 6]
# l2 = [5, 6, 7, 8, 9]
#
#
# intersection = (list(filter(lambda x: x in l1, l2)))
# print(intersection)


# Задача 9. Да се напише програма, която да брои четните и нечетните числа в даден
# списък от цели числа, използвайки lambda.

# l = [1, 2, 3, 4, 5, 6, 7]
#
# count_even = list(filter(lambda x: (x%2 == 0), l))
# print(len(count_even))
#
# count_odd = list(filter(lambda x: (x%2 != 0), l))
# print(len(count_odd))
