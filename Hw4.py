# Задача 1. Принтирайте следният текст на екрана:
#  “23 4.5 False John”.

# print("\"23 4.5 False John\"")

# Задача 2. Попълнете празните полета, като използвате форматиращият метод format. Празните места запълнете с вашето име и любими активности.
# ”{ }’s favorite sports is { }.”
# “{ } is working on { } programming!”


# name = "Vessy"
# sport = "salsa"
# language = "Python"
#
# print("{}'s favourite sport is {}".format(name, sport))
# print("{} is working on {} programming".format(name, language))

#
# Задача 3. Създайте променлива, paragraph, която да съдържа следното съдържание:
# "Python is a great language!", said Fred. "I don't ever remember having this much fun before. "


# paragraph = ''' \"Python is a great language!\", said Fred. \"I don't ever remember having
# this much fun before. \" '''
#
# print(paragraph)


# Задача 4. Опитайте се да принтирате стринг изцяло с главни букви.

# dinosaur = " T-Rex"
# print(dinosaur.upper())


# Задача 5. Напишете програма, която да премахва ”$$” от името ”$$John Smith”. Опитайте с .lstrip и .strip().
# За да видите описанието на двете функции използвайте следното help(“ ”.strip).

# name = "$$John Smith"
# print(name.replace("$"," ").strip())


# Задача 6. Да се напише програма, която да принтира следната информация:


# print("*" * 50)
# print(" " * 15 + "Coding Temple, Inc.")
# print(" " * 15 + "283 Franklin St.")
# print(" " * 15 + "Boston MA")
# print("=" * 50)
# print(" " * 10 + "Product name    Product price")
# print(" " * 10 + "Books           $49.95")
# print(" " * 10 + "Computer        $579.99")
# print(" " * 10 + "Monitor         $124.89")
# print("=" * 50)
# print(" " * 26 + "Total")
# print(" " * 26 + "$754.83")
# print("=" * 50)
# print(" " * 10 + "Thanks for shopping with us today!")
# print("*" * 50)


# Задача 1. Да се напише if-конструкция, която проверява стойността на две целочислени
# променливи и разменя техните стойности, ако стойността на първата променлива е по-голяма
# от втората.

# a = 4
# b = 3
#
# if a > b:
#     print(b, a)
# else:
#     print(a, b)


# Задача 2. Напишете програма, която показва знака (+ или -) от частното на две реални числа,
# без да го пресмята.

# a = 3
# b = 4
#
# if a > b:
#     print("+")
# else:
#     print("-")


# Задача 3. Напишете програма, която намира най-голямото по стойност число, измежду три
# дадени числа.


# a = 9
# b = 5
# c = 7
#
# if a > b:
#     pass
#     if a > c:
#         print("a")
#     else:
#         print("c")
# elif a < b:
#     pass
#     if b > c:
#         print("b")
#     else:
#         print("c")
# elif a == b and a != c:
#     pass
#     if a > c:
#         print("a = b and is bigger than c.")
#     else:
#         print("a = b and is smaller than c.")
# else:
#     print("All numbers are equal.")


# Задача 4. Напишете програма, която за дадена цифра (0-9), зададена като вход, извежда името
# на цифрата на български език

# number = int(input("Please provide a number between 0 and 9: "))
#
# if number == 0:
#     print("нула")
# elif number == 1:
#     print("едно")
# elif number == 2:
#     print("две")
# elif number == 3:
#     print("три")
# elif number == 4:
#     print("четири")
# elif number == 5:
#     print("пет")
# elif number == 6:
#     print("шест")
# elif number == 7:
#     print("седем")
# elif number == 8:
#     print("осем")
# elif number == 9:
#     print("девет")
# else:
#     print("Please provide a number between 0 and 9.")



# Задача 5. Напишете програма, която при въвеждане на коефициентите (a, b и c) на квадратно
# уравнение ax^2+bx+c изчислява и извежда неговите реални корени.

# import math
#
# a = float(input("Please provide the value of a: "))
# b = float(input("Please provide the value of b: "))
# c = float(input("Please provide the value of c: "))
#
# x1 = (-b + math.sqrt((b**2) - (4*a*c))) / (2*a)
# x2 = (-b - math.sqrt((b**2) - (4*a*c))) / (2*a)
#
# print(x1)
# print(x2)


# Задача 6. Дадени са няколко цели числа. Напишете програма, която намира онези
# подмножества от тях, които имат сума 0. Примери:
# - Ако са дадени числата {-2, -1, 1}, сумата на -1 и 1 е 0.
# - Ако са дадени числата {3, 1, -7}, няма подмножества със сума 0.


# a = int(input("Please provide the value of a: "))
# b = int(input("Please provide the value of b: "))
# c = int(input("Please provide the value of c: "))
#
# if a + b == 0:
#     print("Сумата на ", a, "и", b, "е 0.")
# elif a + c == 0:
#     print("Сумата на ", a, "и", c, "е 0.")
# elif b + c == 0:
#     print("Сумата на ", b, "и", c, "е 0.")
# elif a + b + c == 0:
#     print("Сумата на ", a, ",", b, "и", c, "е 0.")
# else:
#     print("Няма подмножества със сума 0.")



# Задача 7. Напишете програма, която прилага бонус точки към дадени точки в интервала [1..9]
# чрез прилагане на следните правила:
# - Ако точките са между 1 и 3, програмата ги умножава по 10.
# - Ако точките са между 4 и 6, ги умножава по 100.
# - Ако точките са между 7 и 9, ги умножава по 1000.
# - Ако точките са 0 или повече от 9, се отпечатва съобщение за грешка.


# result = "[1..9]"
#
# if 1 <= result.count(".") <= 3:
#     print(result.replace(".", "."*10))
# elif 4 <= result.count(".") <= 6:
#     print(result.replace(".", "."*100))
# elif 7 <= result.count(".") <= 9:
#     print(result.replace(".", "."*1000))
# elif result.count(".") == 0 or result.count(".") > 9:
#     print("Грешка.")


# Задача 8. Напишете програма, която преобразува дадено число в интервала [0..999] в текст,
# съответстващ на българското произношение. Примери:
# -0 -> “Нула”
# -273 -> ”Двеста седемдесет и три”
# -400 -> ”Четиристотин”
# -501 -> “Петстотин и едно”
# -711 -> “Седемстотин и единадесет”



# number = input("Please provide a number between 0 and 999: ")
#
# if number[0] == 1:
#     pass

# ??????????????????????????????????????????????????



# Задача 9. Да се напише програма, която да превръща температура от целзий в фаренхайт.
# Формулата е следната: c/5 = f – 32/9, където c е температурата в целзий и f температурата в
# фаренхайт.
# Примерен изход:
# 60°C is 140 in Fahrenheit
# 45°F is 7 in Celsius

# t_celsius = float(input("Please provide temperature in Celsius: "))
#
# t_farenheit = (t_celsius * 1.8) + 32
# print(t_farenheit)

# t_farenheit = float(input("Please provide temperature in Farenheit: "))
#
# t_celsius = (t_farenheit - 32) * (5/9)
# print(t_celsius)

# Мисля, че формулата в условието е грешна.


# Задача 10. Напишете програма, която да изчислява възрастта на дадено куче в кучешки
# години. Забележка: За първите две години, една кучешка година е равна на 10.5 човешки.
# След това всяка следваща кучешка година се равнява на 4-ри човешки години.


# age = int(input("Възраст на кучето: "))
#
# if age == 1:
#     print("Възрастта в кучешки години е 10.5")
# elif age == 2:
#     print("Възрастта в кучешки години е 21.")
# elif age > 2:
#     dog_age = 21 + ((age-2) * 4)
#     print("Възрастта в кучешки години е {}".format(dog_age))
# else:
#     print("Кученцето е под едногодишна възраст.")


# Задача 11. Да се напише програма, която да намира медианата из между три стойности


# a = float(input("Please provide the value of a: "))
# b = float(input("Please provide the value of b: "))
# c = float(input("Please provide the value of c: "))
#
# if (a < b and b < c) or (c < b and b < a):
#     print(b)
# elif (b < a and a < c) or (c < a and a < b):
#     print(a)
# elif (a < c and c < b) or (b < c and c <  a):
#     print(c)
# else:
#     print("Не може да се определи медиана.")


# Задача 12. Напишете програма, която да използва следните променливи, възраст – age, пол
# (M или F), семейно положение (Y или N) за даден служител. Според следните правила,
# програмата да определя, къде може да работи конкретният служител.
# Правила:
# - Ако служителката е жена, тя може да работи само в градски райони.
# - Ако служителят е мъж на възраст между 20 до 40 години, той може да работи навсякъде
# - Ако служителят е мъж на възраст между 40 и 60 години, той ще работи само в градските
# райони
# За всяка друга възраст трябва да се отпечатва грешка


# age = int(input("Моля въведете Вашата възраст: "))
# gender = input("Моля въведете Вашия пол (M или F): ")
# family = input("Моля въведете Вашето семейно положене (Y или N): ")
#
# if gender == 'F' and 20 < age < 60:
#     print("Служителят може да работи само в градски райони")
# elif gender == 'M' and 20 < age < 40:
#     print("Служителят може да работи навсякъде.")
# elif gender == 'M' and 40 < age < 60:
#     print("Служителят може да работи само в градски райони")
# else:
#     print("Грешка.")


# Задача 13. Да се напише програма, която при дадено четири цифрено число го обръща
# отдясно наляво.
# Пример:
# Вход: 1234 Вход: 5982
# Изход: 4321 Изход: 2895


# num = int(input("Please provide a number: "))
# print(str(num)[::-1])


# Задача 14. Сортирайте 3 реални числа в намаляващ ред. Използвайте вложени if оператори.

#
# a = int(input("Please provide the value of a: "))
# b = int(input("Please provide the value of b: "))
# c = int(input("Please provide the value of c: "))
#
# if a > b and a > c:
#     pass
#     if b > c:
#         print(a, b, c)
#     else:
#         print(a, c, b)
# elif b > a and b > c:
#     pass
#     if a > c:
#         print(b, a, c)
#     else:
#         print(b, c, a)
# elif c > a and c > b:
#     pass
#     if a > b:
#         print(c, a, b)
#     else:
#         print(c, b, a)
# else:
#     print("Грешка.")



# Задача 15. Група запалянковци решили да си закупят билети за Евро 2016. Цената на
# билета се определя спрямо две категории:
# VIP – 499.99 лева
# Normal – 249.99 лева
# Запалянковците имат определен бюджет, a броят на хората в групата определя какъв
# процент от бюджета трябва да се задели за транспорт:
# От 1 до 4 – 75% от бюджета
# От 5 до 9 – 60% от бюджета
# От 10 до 24 – 50% от бюджета
# От 25 до 49 – 40% от бюджета
# 50 или повече – 25% от бюджета

# да си купят билети за избраната категория, както и колко пари ще им останат или ще са
# им нужни.
# Входни данни
# Входът се чете от конзолата и съдържа точно 3 реда:
# На първия ред е бюджетът – реално число в интервала [1 000.00 … 1 000 000.00.
# На втория ред е категорията – "VIP" или "Normal".
# На третия ред е броят на хората в групата – цяло число в интервала [1 … 200].
# Изходни данни
# Да се отпечата на конзолата един ред:
# Ако бюджетът е достатъчен:
# "Yes! You have {N} leva left." – където N са останалите пари на групата.
# Ако бюджетът НЕ Е достатъчен:
# "Not enough money! You need {М} leva." – където М е сумата, която не достига.
# Сумите трябва да са форматирани с точност до два символа след десетичния знак.

#
# budget = float(input("Please provide the group budget (between 1000.00 and 1000000.00): "))
# category = input("What category of tickets would you like to buy (VIP or Normal): ")
# number_of_visitors = int(input("Please provide the number of people in the group ( between 1 and 200): "))
# available_money = 0
# money_after_tickets = 0
# tickets_group = 0
# money_left = 0
# money_needed = 0
#
#
# if 1 <= number_of_visitors <= 4:
#     available_money = 0.25 * budget
# elif 5 <= number_of_visitors <= 9:
#     available_money = 0.4 * budget
# elif 10 <= number_of_visitors <= 24:
#     available_money = 0.5 * budget
# elif 25 <= number_of_visitors <= 49:
#     available_money = 0.6 * budget
# elif number_of_visitors <= 50:
#     available_money = 0.75 * budget
#
# if category == "VIP":
#     tickets_group = 499.99 * number_of_visitors
#     if available_money >= tickets_group:
#         money_left = available_money - tickets_group
#         print("You have {} leva left.".format(money_left))
#     else:
#         money_needed = tickets_group - available_money
#         print("Not enough money. You need {} leva.".format(money_needed))
#
# if category == "Normal":
#     tickets_group = 249.99 * number_of_visitors
#     if available_money >= tickets_group:
#         money_left = available_money - tickets_group
#         print("You have {} leva left.".format(money_left))
#     else:
#         money_needed = tickets_group - available_money
#         print("Not enough money. You need {} leva.".format(money_needed))




# month = input("Which month would you like to visit (May, June, July, August, September or October): ")
# stay = int(input("How many nights would you like to stay (from 0 to 200): "))
# studio_price = 0
# apartment_price = 0
#
# if month.lower() == "may" or month.lower() == "october":
#     pass
#     if 7 < stay < 14:
#         studio_price = (stay * 50) * 0.95
#         apartment_price = (stay * 65)
#         print("Total price for a studio is {}".format(studio_price))
#         print("Total price for an apartment is {}".format(apartment_price))
#     elif stay > 14:
#         studio_price = (stay * 50) * 0.70
#         apartment_price = (stay * 65) * 0.90
#         print("Total price for a studio is {}".format(studio_price))
#         print("Total price for an apartment is {}".format(apartment_price))
#
# if month.lower() == "june" or month.lower() == "september":
#     pass
#     if stay > 14:
#         studio_price = (stay * 75.20) * 0.8
#         apartment_price = (stay * 68.70) * 0.9
#         print("Total price for a studio is {}".format(studio_price))
#         print("Total price for an apartment is {}".format(apartment_price))
#     else:
#         studio_price = (stay * 75.20)
#         apartment_price = (stay * 68.70)
#         print("Total price for a studio is {}".format(studio_price))
#         print("Total price for an apartment is {}".format(apartment_price))
#
# if month.lower() == "july" or month.lower() == "august":
#     pass
#     if stay > 14:
#         studio_price = (stay * 76)
#         apartment_price = (stay * 77) * 0.9
#         print("Total price for a studio is {}".format(studio_price))
#         print("Total price for an apartment is {}".format(apartment_price))
#     else:
#         studio_price = (stay * 76)
#         apartment_price = (stay * 77)
#         print("Total price for a studio is {}".format(studio_price))
#         print("Total price for an apartment is {}".format(apartment_price))



# Задача 17. Напишете програма, която чете две цели числа (N1 и N2) и оператор, с който да се
# и з въ рш и д а д е н а м ат е м ат и ч е с к а о п е р а ц и я с тя х . В ъ зм ож н и т е о п е р а ц и и
# са: събиране (+), изваждане (-), умножение (*), деление (/) и модулно деление (%). При
# събиране, изваждане и умножение на конзолата трябва да се отпечата резултата и дали той
# е четен или нечетен. При обикновено деление – единствено резултата, а при модулно деление
# – остатъка. Трябва да се има предвид, че делителят може да е равен на нула (= 0), а на нула не
# се дели. В този случай трябва да се отпечата специално съобщение.


# a = float(input("Please provide a number: "))
# b = float(input("Please provide a second number: "))
# operator = input("Please provie an operatior ( +, - , * , / , % ): ")
#
# if operator == "+":
#     print(a + b)
#     if(a+b) % 2 == 0:
#         print("Резултатът е четно число.")
#     else:
#         print("Резултатът е нечетно число.")
#
# elif operator == "-":
#     print(a - b)
#     if(a-b) % 2 == 0:
#         print("Резултатът е четно число.")
#     else:
#         print("Резултатът е нечетно число.")
# elif operator == "*":
#     print(a * b)
#     if(a*b) % 2 == 0:
#         print("Резултатът е четно число.")
#     else:
#         print("Резултатът е нечетно число.")
# elif operator == "/":
#     pass
#     if b == 0:
#         print("Не може да се дели на 0.")
#     else:
#         print(a / b)
# elif operator == "%":
#     pass
#     if b == 0:
#         print("Не може да се дели на 0.")
#     else:
#         print(a % b)
# else:
#     print("Грешка.")





