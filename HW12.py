#                 Лекция 10 Итератори и генератори



# Задача 1. Да се напише програма, която да реализира генератор на четни числа

# start = int(input("Enter a starting number for the range: "))
# end = int(input("Enter an ending number for the range: "))
#
# if end > 0:
#     for num in range(start, end+1):
#         if num%2==0:
#             print(num)
# else:
#     for num in range(start, end-1, -1):
#         if num%2==0:
#             print(num)


# Задача 2. Да се напише програма, която да реализира генератор на нечетните числа.


# start = int(input("Enter a starting number for the range: "))
# end = int(input("Enter an ending number for the range: "))
#
# if end > 0:
#     for num in range(start, end+1):
#         if num%2!=0:
#             print(num)
# else:
#     for num in range(start, end-1, -1):
#         if num%2!=0:
#             print(num)


# Задача 3. Да се напише програма, която да реализира генератор на прости числа.


# start = int(input("Enter a starting number for the range: "))
# end = int(input("Enter an ending number for the range: "))
#
# if end > 0:
#     for num in range(start, end+1):
#         for x in range(2, num):
#             if num%x == 0:
#                 break
#             else:
#                 print(num)
#                 break


# Задача 4. Да се напише програма, която да реализира итератор на четни числа.


# start = int(input("Enter a starting number for the range: "))
# end = int(input("Enter an ending number for the range: "))
#
#
# if end > 0 and start % 2 == 0:
#     pass
# elif end < 0 and start % 2 == 0:
#     pass
# elif end < 0 and start % 2 != 0:
#     start += 1
# else:
#     start -= 1
#
#
# class Even:
#     if end > 0:
#         last = start - 2
#     else:
#         last = start + 2
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if end > 0:
#             self.last += 2
#         else:
#             self.last -= 2
#
#         if 0 < end < self.last:
#             raise StopIteration
#         if 0 > end > self.last:
#             raise StopIteration
#
#         return self.last
#
# even_numbers = Even()
#
# for num in even_numbers:
#     print(num)



# Задача 5. Да се напише програма, която да реализира итератор на нечетни числа.


# start = int(input("Enter a starting number for the range: "))
# end = int(input("Enter an ending number for the range: "))
#
#
# if end > 0 and start % 2 != 0:
#     pass
# elif end < 0 and start % 2 != 0:
#     pass
# elif end < 0 and start % 2 == 0:
#     start += 1
# else:
#     start -= 1
#
#
# class Even:
#     if end > 0:
#         last = start - 2
#     else:
#         last = start + 2
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if end > 0:
#             self.last += 2
#         else:
#             self.last -= 2
#
#         if 0 < end < self.last:
#             raise StopIteration
#         if 0 > end > self.last:
#             raise StopIteration
#
#         return self.last
#
# even_numbers = Even()
#
# for num in even_numbers:
#     print(num)



# Задача 6. Да се напише програма, която от даден списък да прехвърля положителните
# числа в един списък и отрицателните в друг.

# l_positive = []
# l_negative = []
#
# while True:
#     number = int(input("Please provide a number: "))
#     if number == 0:
#         break
#     elif number > 0:
#         l_positive.append(number)
#     else:
#         l_negative.append(number)
#
#
# print(l_positive)
# print(l_negative)


# Задача 7. Да се промени 6та задача така, че да използва итератор


# user_numbers = []
#
# while True:
#     number = int(input("Please provide a number: "))
#     if number == 0:
#         break
#     else:
#         user_numbers.append(number)
#
#
# def positive_numbers(nums):
#     for i in nums:
#         if i > 0:
#             yield i
#
# nums = list(positive_numbers(user_numbers))
#
# print("Positive numbers: ")
# print(nums)
#
#
# def negative_numbers(nums):
#     for i in nums:
#         if i < 0:
#             yield i
#
# nums = list(negative_numbers(user_numbers))
#
# print("Negative numbers: ")
# print(nums)


# Задача 8. Да се напише програма, която да кара потребителят да въвежда стринг от
# клавиатурата и да поставя всички гласни в едни списък и всички съгласни в друг.

# vowels = ["a", "e", "i", "o", "u"]
# l_vowel = []
# l_consonant = []
#
# word = input("Please provide a word: ")
#
#
# for letter in word:
#     if letter in vowels:
#         l_vowel.append(letter)
#     else:
#         l_consonant.append(letter)
#
# print(l_vowel)
# print(l_consonant)


# Задача 9. Да се промени задача 8 така, че да използва итератор.


# word = input("Please provide a word: ")
#
#
# def vowels(letters):
#     for letter in letters:
#         if letter == "a" or letter == "e" or letter == "i" or letter == "o" or letter == "u":
#             yield letter
#
#
# letters = list(vowels(word))
# print("Vowel: ")
# print(letters)
#
#
# def consonant(letters):
#     for letter in letters:
#         if letter != "a" and letter != "e" and letter != "i" and letter != "o" and letter != "u":
#             yield letter
#
#
# letters = list(consonant(word))
# print("Consonant: ")
# print(letters)


# Задача 10. Да се напише програма, която да конкатенира два списъка и след това да ги
# сортира.


# l_1 = []
# l_2 = []
#
# while True:
#     x = input("Please provide a number or a word for list 1: ")
#     if x == "":
#         break
#     else:
#         l_1.append(x)
#
#
# print()
#
# while True:
#     y = input("Please provide a number or a word for list 2: ")
#     if y == "":
#         break
#     else:
#         l_2.append(y)
#
#
# print(sorted(l_1 + l_2))


# Задача 11. Напишете генератор, който да намира аритметична прогресия, като
# потребителят въвежда началото, стъпката на прогресия и колко числа да покаже от
# редицата.


# a = int(input("Enter a starting number for the range: "))
# d = int(input("What would you like to be the step: "))
# n = int(input("How many numbers would you like to see: "))
# x = 0
#
# def aritmetic_progression():
#     for i in range(1, n + 1):
#          x = a + (i - 1) * d
#          print(x)
#
#
# AP = aritmetic_progression()


# Задача 12. Да се напише генератор, който да намира геометрична прогресия, като
# потребителят въвежда началото, стъпката и колко числа да покаже.


# a = int(input("Enter a starting number for the range: "))
# q = int(input("What would you like to be the step: "))
# n = int(input("How many numbers would you like to see: "))
# x = 0
#
#
# def geometric_progression():
#     for i in range(1, n + 1):
#         x = a*q**(i-1)
#         print(x)
#
# GP = geometric_progression()


# Задача 13. Да се реализира декартово произведение на две множества, като се използва
# съкратен запис за създаването на списъкът с крайните елементи


# numbers1 = [1, 3, 5, 7, 9]
# numbers2 = [2, 4, 6, 8, 10]
# d = {}
#
# for x in numbers1:
#     for y in numbers2:
#         for index in range(0, len(numbers1)):
#             d[numbers1[index]] = numbers2[index]
# print(d)


# Задача 14. Да се промени задача 13 така, че да използва itertools.product.


# numbers1 = [1, 3, 5, 7, 9]
# numbers2 = [2, 4, 6, 8, 10]
#
# iter1 = iter(numbers1)
# iter2 = iter(numbers2)
#
#
# while True:
#     try:
#         print((next(iter1)), ":", next(iter2))
#     except StopIteration:
#         break
