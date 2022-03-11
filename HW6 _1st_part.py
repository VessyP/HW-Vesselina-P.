#                                                 Лекция 6 Цикли
#
#
# Задача 1. Да се напише програма, която да намира тези числа, които се делят на 7 и на
# 5, между 1500 и 2700.

# for num in range(1500, 2700):
#     if num % 7 == 0 and num % 5 == 0:
#         print(num)


# Задача 2. Да се състави програма, която ще изчисли сумата на 5, въведени от
# клавиатурата, естествени числа от интервала [10 ..5555].
# Вход: 1,2,3,4,5
# Изход: 15


# a = int(input("Моля въведете цяло положително число: "))
# b = int(input("Моля въведете цяло положително число: "))
# c = int(input("Моля въведете цяло положително число: "))
# d = int(input("Моля въведете цяло положително число: "))
# e = int(input("Моля въведете цяло положително число: "))
#
# while a >= 0 and b >= 0 and c >= 0 and d >= 0 and e >= 0:
#     sum = (a + b + c + d + e)
#     print(sum)
#     break


# Задача 3. Да се напише програма, която да създаде следният шаблон:
# *
# * *
# * * *
# * * * *
# * * * * *
# * * * *
# * * *
# * *
# *

# num = 0
#
# while num <= 5:
#     print(num * " *")
#     num+=1
#
# num = 4
#
# while num >0:
#     print(num * " *")
#     num -= 1


# Задача 4. Да се напише програма, която да обръща буквите на дадена дума на обратно.
# Думата да бъде въведена от клавиатурата. Като за целта използвате цикъл.


# word = input("Please provide a word: ")
# word = word[::-1]
#
#
# for l in word:
#     print(l, end="")


# Задача 5. Да се напише програма, която да намира броят на четните и нечетните числа
# от списък от цели числа.


# numbers = [23, 44, 2, 55, 61, 9, 7, 12, 66, 13]
#
# even = 0
# odd = 0
#
#
# for num in numbers:
#     if num % 2 == 0:
#         even += 1
#     elif num % 2 != 0:
#         odd += 1
#
#
# print(f"Number of even numbers: {even}")
# print(f"Number of odd numbers: {odd}")


# Задача 6. Да се напише програма, която да принтира всички числа от 0 до 6, без да
# включва 3 и 6.


# for num in range(0, 7):
#     if num == 3 or num == 6:
#         continue
#     print(num)


# Задача 7. Да се напише програма, която принтира редицата на Фибуначи между 0 и 50.
# Редицата на Фибуначи е: 0, 1, 1, 2, 3, 5, 8, 13, 21, … Всяко следващо число е сумата от
# предходните две.


# a = 1
# b = 0
# print(b)
# print(a)
#
# while a <= 50:
#     c = b
#     b = a
#     a = c + b
#     if (c + b) > 50:       #Този ред не би трябвало да е нужен, но без него последната стойност излизаше 55, което е извън рейнджа.
#         break
#     print(a)


# Задача 8. Да се принтира буквата A на екрана както е дадено по-долу:


# print(" *** ")
#
# for i in range(0,2):
#     print("*   *")
#
# print(5 * "*")
#
# for i in range(0, 3):
#     print("*   *")


# Задача 9. Да се напише програма, която принтира следният шаблон:
# 1
# 22
# 333
# 4444
# 55555
# 666666
# 7777777
# 88888888
# 999999999


# num = 1
# while num <= 9:
#     print(num * str(num))
#     num += 1



# Задача 10. Да се състави програма, която изчислява сумата на произведенията от 1 до
# въведено едноцифрено число.
# Сумата се формира така:
# 1*2 + 2*3*4 +..+n*(n+1)*(n+2)*..*2*n


# n = int(input("Pleae provide a number from 1 to 9: "))
#
# num = 1
# while n >= 1:
#     num = num * n
#     n = n - 1
# print(num)


# Задача 11: Да се състави програма, която извежда всички цели числа от интервала [1-
# 50], които удовлетворяват проверка на следното условие:
# c^3 = a^2 + b^2


# a = 0
# b = 0
# c = 0
#
# while a in range(0, 51) and b in range(0, 51) and c in range(0, 51):
#     a += 1
#     b += 1
#     c += 1
#
#     if c**3 != (a**2) + (b**2):
#         continue
#         print(a, b, c)


########################################################

# import random
#
# a = 0
# b = 0
# c = 0
# result = 0
#
# while True:
#     a = random.randint(0, 51)
#     b = random.randint(0, 51)
#     c = random.randint(0, 51)
#     result = ((a**2) + (b**2)) - ((random.randint(0, 51))**3)
#     while result:
#         print(result)
#         if not result:
#             continue


# ????????????????????????????????????????


# Задача 12. Да се състави програма, която извежда числов триъгълник изобразяващ
# следната последователност:
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5
# 1 2 3 4 5 6
# 1 2 3 4 5 6 7
# 1 2 3 4 5 6 7 8
# 1 2 3 4 5 6 7 8 9


# for i in range(9):                               # rows
#     for j in range(i + 1):                       # columns
#         print(j+1, end=" ")
#     print()



# Задача 13. Да се състави програма, чрез която се извежда квадрат от цифри. Сумите от
# елементите на произволен ред или стълб са равни на 45.
# Пример:
# 1 2 3 4 5 6 7 8 9 0
# 2 3 4 5 6 7 8 9 0 1
# 3 4 5 6 7 8 9 0 1 2
# 4 5 6 7 8 9 0 1 2 3
# 5 6 7 8 9 0 1 2 3 4
# 6 7 8 9 0 1 2 3 4 5
# 7 8 9 0 1 2 3 4 5 6
# 8 9 0 1 2 3 4 5 6 7
# 9 0 1 2 3 4 5 6 7 8
# 0 1 2 3 4 5 6 7 8 9


# n = 9
#
# for i in range(n):
#     for j in range(n):
#         print(j+1, end=" ")
#         j += 1
#     print(i + 1)
#
#
#     ??????????????????????????


# Задача 14. Да се напише програма, която да генерира число на случен принцип и да
# подкани потребителя да познае това число. Да извежда следните стойности too low, too
# high, или exactly right, в случай, че потребителя е познал, или не числото.


# import random
#
# number = random.randint(1, 101)
# guess = 0
#
# while guess != number:
#     guess = int(input("Try to guess the number between 0 and 100: "))
#
#     if guess > number:
#         print("Too high.")
#     elif guess < number:
#         print("Too low.")
#     else:
#         print("Exactly right.")
#         print(f"The correct number is {number}.")



# Задача 15. Да се напише програма, която подканва потребителя да въведе число и
# програмата да провери дали то е просто или не.

# prime = True
# number = int(input("Please provide a number: "))
#
#
# if number == 1:
#     print(f"{number} is prime")
# elif number > 1:
#     for i in range(2, number):
#         if number % i == 0:
#            prime = False
#            break
#
#
# if prime == True:
#     print(f"{number} is prime")
# else:
#     print(f"{number} is not prime")




# Задача 17. Да се напише програма, която да приема от клавиатурата цяло число n и като
# резултат да принтира всички числа до въведеното.


# number = int(input("Please provide a number: "))
#
# for i in range(1, number+1):
#     print(i, end="-")         # НЕ мога да махна последното тире.





# Задача 19. Да се напише програма, която приема като вход текст и обръща буквите от
# дясно наляво на само на думите, чиято дължина е нечетна, тези които са с четен брой
# си остават така като са.

# odd = False
# word = input("Please provide a text: ")
#
#
# if len(word) % 2 != 0:
#     odd = True
#     if odd:
#         word = word[::-1]
# for l in word:
#     print(l, end ="")
#
#
#
#     ?????????? Програмата ми обръща цялото изрерчение в зависимост от броя символи, не думитее по отделно.





# Задача 21. Да се напише програма, която да принтира буквата M:

# for i in range(2):
#     print("*", 5 * " ", "*")
# print("* *   * *")
# print("*   *   *")
# for i in range(3):
#     print("*", 5 * " ", "*")



# Задача 22. Да се напише програма, която да принтира буквата D:


# print(4 * "*")
# for i in range(5):
#     print("*",  * " ", "*")
# print(4 * "*")



# Задача 23. Напишете програма, която пресмята N!/K! за дадени N и K (1<K<N). Без да се
# ползват вградени функции.

# n = int(input("Please provide a number for n from 1 to 9: "))
# k = int(input("Please provide a number for k from 1 to 9: "))
#
# if 1 < k < n:
#     num = 1
#     while n >= 1:
#         num = num * n
#         n = n - 1
#
#     res = 1
#     while k >= 1:
#         res = res * k
#         k = k - 1
#
#
#     result = num / res
#     print(int(result))
#
#
# elif k == 0 and n == 0:
#     print("Невалиден вход.")
#
# else:
#     print("K трябва да е по-малко от N.")



# Задача 24. Напишете програма, която пресмята N!*K!/(N-K)! за дадени N и K (1<K<N).
# Без да се ползват вградени функции.


# n = int(input("Please provide a number for n from 1 to 9: "))
# k = int(input("Please provide a number for k from 1 to 9: "))
# d = n - k
#
# if 1 < k < n:
#     num = 1
#     while n >= 1:
#         num = num * n
#         n = n - 1
#
#     res = 1
#     while k >= 1:
#         res = res * k
#         k = k - 1
#
#     denominator = 1
#     while d >= 1:
#         res = denominator * d
#         d = d - 1
#
#
#
#     result = ((num * res) / denominator)
#     print(int(result))
#
#
# elif k == 0 and n == 0:
#     print("Невалиден вход.")
#
# else:
#     print("K трябва да е по-малко от N.")



# Задача 25. Напишете програма, която за дадено цяло число n, пресмята сумата: S = 1 + 1!/x + 2! / X**2 +...+n!/x**n


# n = int(input("Please provide a number for n from 1 to 9: "))
# x = int(input("Please provide a number for n from 1 to 9: "))
#
# for i in range(n):
#     num = 1
#     while n >= 1:
#         num = num * n
#         n = n - 1
#         S = 1 + num / x**n
#
# print(S)


# Задача 26. Напишете програма, която чете от конзолата положително цяло число N (N <
# 20) и отпечатва матрица с числа като на фигурата по-долу:


# n = int(input("Please provide a number for n from 1 to 9: "))
#
# for i in range(n):
#     for j in range(n):
#         print(j+1, end=" ")
#     print()


# Не мога да направя всеки ред да стартира от по-голямо число.