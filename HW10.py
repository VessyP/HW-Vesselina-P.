#                               Лекция 8 Речници задачи


# Задача 1. Да се преработи следната задача, така че да използва речник.
# Напишете програма, която преобразува дадено число в интервала [0..999] в текст,
# съответстващ на българското произношение. Примери:
# -0 -> “Нула”
# -273 -> ”Двеста седемдесет и три”
# -400 -> ”Четиристотин”
# -501 -> “Петстотин и едно”
# -711 -> “Седемстотин и единадесет”

# numbers = {0: "Нула",
#            273: "Двеста седемдесет и три",
#            400: "Четиристотин",
#            501: "Петстотин и едно",
#            711: "Седемстотин и единадесет"}
#
# number = int(input("Please provide one of the following numbers(0, 273, 400, 501, 711: "))
#
# try:
#      print(numbers[number])
# except:
#      print("The number you provided is not on the list.")


# Задача 2. Да се преработи следната задача, така че да използва речник. Да се напише
# програма, която да изчислява дневният калориен прием на даден потребител, като
# данните се въвеждат от клавиатурата. Необходимите данни са: възраст, пол (‘f’, ‘m’),
# височина (в сантиметри), тегло (в килограми), ниво на физическа активност (някоя от
# стойностите от 1 до 6 по-долу). Ниво на физическа активност се определя в следните
# няколко категории:
# 1 – базална метаболитна скорост
# 2 - заседнал – малка или никаква активност
# 3 - лека активност (1-3 пъти седмично) BMR * 1.2 BMR * 1.375
# 4 - средна активност(3-5 пъти седмично) BMR * 1.55
# 5 - висока активност (6-7 пъти седмично) BMR * 1.725
# 6-многовисокаактивност (6–7пъти седмично + тежка физическа работа). BMR*1.9
# Да се изчисли и какъв трябва да бъде дневният прием на калории ако:
# - за да запазите сегашното си тегло
# - за да сваляте по 0.5 кг на седмица
# - за да сваляте по 1 кг. на седмица
# - за да качвате по 0.5 кг. на седмица
# - за да качвате по 1 кг. на седмица
# Да се принтират данните на потребителя, както и калорийният прием спрямо горните
# няколко точки.
# Формула за изчисление на BMR при мъже:
# BMR = 66.47 + ( 13.75 × weight in kg ) + ( 5.003 × height in cm ) − ( 6.755 × age in years )
# Формула за изчисление на BMR при жени:
# BMR = 655.1 + ( 9.563 × weight in kg ) + ( 1.85 × height in cm ) − ( 4.676 × age in years )


# age = int(input("Please provide your age: "))
# gender = input("Plese provide your gender (f or m ):")
# height = int(input("Please provide your height in sm: "))
# weight = float(input("Please provide your weight in kg: "))
# active = int(input('''Please enter the number corresponding to your level of activness:
#  1 – базална метаболитна скорост
#  2 - заседнал – малка или никаква активност
#  3 - лека активност (1-3 пъти седмично)
#  4 - средна активност(3-5 пъти седмично)
#  5 - висока активност (6-7 пъти седмично)
#  6-многовисокаактивност (6–7пъти седмично + тежка физическа работа).: '''))
#
# BMR_active = {1:1,
#               2:1.2,
#               3:1.375,
#               4:1.55,
#               5:1.725,
#               6:1.9}
#
# if gender == "m":
#     BMR = (66.47 + (13.75 * weight) + (5.003 * height) - (6.755 * age))
#     BMR = BMR*BMR_active[active]
# else:
#     BMR = (655.1 + (9.563 * weight) + (1.85 * height) - (4.676 * age))
#     BMR = BMR * BMR_active[active]
#
#
# calories_decrease_half = BMR - 500
# calories_decrease_1 = BMR - 1000
#
# calories_increase_half = BMR + 500
# calories_increase_1 = BMR + 1000
#
# print(f'''Имате нужда от {BMR.__round__(2)} Калории на ден за да поддържате теглото си
# Имате нужда от {calories_decrease_half.__round__(2)} Калории на ден за да сваляте по 0.5 кг на седмица
# Имате нужда от {calories_decrease_1.__round__(2)} Калории на ден за да сваляте по 1 кг на седмица
# Имате нужда от {calories_increase_half.__round__(2)} Калории на ден за да качвате по 0.5 кг на седмица
# Имате нужда от {calories_increase_1.__round__(2)} Калории на ден за да качвате по 1 кг на седмица''')




# Задача 3. Да се създаде речник, който да съдържа информацията за дадено меню на
# ресторант. Ключовете му трябва да са стрингове, а стойностите цените. Програмата ще
# по иска от потребителя да въведе следната информация:
# - Ако потребителят въведе името на дадено ястие от менюто, тогава програмата
# да принтира цената и колко е общата цена до момента. След това да пита
# отново дали потребителят не иска да въведе нещо друго.
# - Ако потребителят въведе име на ястие, което не е в менюто, тогава програмата
# да изведе подходящо съобщение. След което отново програмата да пита
# потребителя да избере нещо друго от менюто.
# - Ако потребителят въведе празен стринг, тогава програмата да спре да подканва
# потребителя да избира от менюто и да изведе на екрана общата крайна сума.


# menu = {"sandwich": 10,
#         "tea": 7,
#         "steak": 20,
#         "beer": 8,
#         "soup": 5,
#         "water": 2}
#
# order = 1
# price_order = 0
# price_all = 0
#
#
# while order:
#     order = input("What would you like to order from the menu(sandwich, tea, steak, beer, soup or water): ")
#     if order == "":
#         print(f"The total price is {price_all}")
#         break
#     elif order not in menu:
#         print(f"We are out of {order} today.")
#     else:
#         price_order = menu[order]
#         price_all += price_order
#         print(f"The price of {order} is {price_order}.")
#         print(f"The total price is {price_all}")





# Задача 4. Да се напише програма, която да проследява валежите в редица градове.
# Потребителят да може да въвежда името на град; ако името на града е празно,
# програмата излиза и принтира отчет. Ако името на града не е празно, потребителят
# ще трябва да въведе информация за количеството дъжд за конкретният
# град(обикновено се измерва в милиметри). След въвеждане на количеството дъжд,
# потребителят има възможност да въвежда следващ град и количество дъжд и това
# ще го прави докато не натисне „Enter“, вместо да напише името на града.
# Пример:
# Boston
# 5
# New York
# 7
# Boston
# 5
# [Enter; blank line]
# Изход:
# Boston: 10
# New York: 7


# town = 1
# rain = 0
# rain_statistic = {}
#
#
# while town:
#     town = input("Please provide a town name: ")
#     if town == "":
#         for key, value in rain_statistic.items():
#             print("{}:{}".format(key,value))
#         break
#     else:
#         rain = int(input("Please provide amount of rain in mm: "))
#         if town in rain_statistic:
#             rain_statistic[town] += rain
#         else:
#             rain_statistic[town] = rain




# Задача 5. Да се напише програма, която да намира разликата между два речника.
# Като резултат програмата да генерира нов речник, който да съдържа разликата
# между двата речника. Ако няма разлика между речниците да се принтира празен
# речник. За всяка двойка ключ-стойност, която се различава, да се запазят
# различаващите се стойности в списък, а списъкът да се запази в речник, като
# ключът да съвпада с текущият. Ако някой от речниците не съдържат даденият
# ключ, то в списъкът, той трябва да бъде записан като None.


# import dictdiffer
#
#
# d1 = {}
# d2 = {}
# key_1 = 1
# key_2 = 1
#
#
# while key_1:
#     key_1 = input("Please provide a key for dictionary 1: ")
#     if key_1 == "":
#         break
#     else:
#         value = input("Please provide a value for this key: ")
#         d1[key_1] = value
#
#
# while key_2:
#     key_2 = input("Please provide a key for dictionary 2: ")
#     if key_2 == "":
#         break
#     else:
#         value = input("Please provide a value for this key: ")
#         d2[key_2] = value
#
#
# for diff in list(dictdiffer.diff(d1, d2)):
#     print(diff)
#
#





# Задача 6. Да се напише програма, която да реализира тълковен речник. Програмата да
# може да търси по въведена дума, като например, ако речникът е френско-английски, то
# речника да може да предостави по въведена английска дума, съответният й еквивалент
# на френски. Ако английската дума се среща в речникът няколко пъти, то резултатът да
# бъде записан в списък, който след това да бъде принтиран. Ако думата не съществува да
# се изведе празен списък.


# empty_list = []
#
# en_de_dict = {"cat": "die Katze",
#               "dog": "der Hund",
#               "animal": "das Tier",
#               "squirrel": "das Eichhörnchen"}
#
#
#
# translation_request = input("Please provide a word in English that you would like to get translated in German: ")
#
# if translation_request in en_de_dict:
#     print(en_de_dict[translation_request])
# else:
#     print(empty_list)




# ???????????????? "Ако английската дума се среща в речникът няколко пъти":
# Не може да им повтарящи ключове, нито да търсим ключ по валю. Ако изкарам клюовете в лист, повторенията не се показват.




# Задача 7. Да се напише програма, която да симулира 1000 завъртания на два зара (от 6
# числа). Програмата да съдържа два речника, единият да е с очакваните вероятности, а
# другият ще пази броят на числата, които са се паднали.


# import random
# from collections import defaultdict
#
# for n in range(1, 7):
#     probability = ((n / 36) * 100).__round__(2)
#     print(n, ":", probability)
#
# for n in range(5, 0, -1):
#     probability = ((n / 36) * 100).__round__(2)
#     print(n, ":", probability)
#
# print()
# print()
#
#
# dice_sum = defaultdict(int)
# n = 1000
#
#
# for num in range(n):
#     dice_1 = random.randint(1, 6)
#     dice_2 = random.randint(1, 6)
#     dice_sum[dice_1 + dice_2] += 1
#
#
#
# for key, value in dice_sum.items():
#     print("{} : {}".format(key, value/10))
#
#



# Задача 8. Създайте програма, която определя и показва броя на уникалните символи в
# низ, въведен от потребителя. Например, “Здравей, Свят!” има 13 уникални знака, докато
# “zzz” има само един уникален символ. Използвайте речник за решаването на този
# проблем.


# text_dict = {}
# text = input("Please provide a text: ")
#
#
# for t in text:
#     if t not in text_dict:
#         text_dict[t] = 0
#
#
# length =len(text_dict.keys())
# print(f"The number of unique symbols in the string is {length}.")




# Задача 9. Две думи са анаграми, ако всичките им букви са еднакви, но в различен ред.
# Например “evil” и “live” са анаграми. Създайте програма, която чете два низа от
# потребителя, дали са анаграми или не.


# word1 = input("Please provide a word: ")
# word2 = input("Please provide a second word: ")
#
# if len(word1) != len(word2):
#     print(f"The words {word1} and {word2} are not anagrams.")
# else:
#     for w in word1:
#         if w not in word2:
#             break
#         else:
#             print(f"The words {word1} and {word2} are anagrams.")
#             break




# Задача 10. ВВ играта на Scrabble всяка буква има точно определени зададени точки.
# Общият резултат за една дума е сборът от точките за всяка една от нейните букви. Почесто срещаните букви имат по-малко точки, докато по-малките букви имат повече.
# Точките, свързани с всяка буква, са показани по-долу:

# Напишете програма, която изчислява и показва резултата от Scrabble за дадена дума.
# Създайте речник, който преобразува от букви в точки. След това използвайте речника,
# за да изчислите резултата.


# word = input("Please provide a word: ")
# total_points = 0
#
# letters = {'a': 1,
#            'b': 3,
#            'c': 3,
#            'd': 2,
#            'e': 1,
#            'f': 4,
#            'g': 2,
#            'h': 4,
#            'i': 1,
#            'j': 8,
#            'k': 5,
#            'l': 1,
#            'm': 3,
#            'n': 1,
#            'o': 1,
#            'p': 3,
#            'q': 10,
#            'r': 1,
#            's': 1,
#            't': 1,
#            'u': 1,
#            'v': 4,
#            'w': 4,
#            'x': 8,
#            'y': 4,
#            'z': 10}
#
#
# for w in word:
#     total_points = total_points + letters[w]
#
#
# print(f"The total score is {total_points}.")





# Задача 11. Карта Бинго се състои от 5 колони от 5 числа. Колоните са обозначени с
# буквите B, I, N, G и O. Има 15 числа, които могат да се появят под всяка буква. Поспециално, числата, които могат да се появят под B варират от 1 до 15, числата, които
# могат да се появят под I, варират от 16 до 30, числата, които могат да се появят под N
# диапазон от 31 до 45, и така нататък. Напишете програма, която създава произволна
# бинго карта и я съхранява в речник. Ключовете ще бъдат буквите B, I, N, G и O.
# Стойностите ще бъдат списъците на пет числа, които се появяват под всяка буква. Да се
# принтира картата Бинго заедно с колоните, обозначени по подходящ начин.


# import random
#
# bingo_card = []
# bingo_dict = {}
# B = []
# I = []
# N = []
# G = []
# O = []
#
#
# for n in range(15):
#     number = random.randint(1, 75)
#     bingo_card.append(number)
#
# # print(bingo_card)
#
# for b in bingo_card:
#     if b <= 15:
#         B.append(b)
#     elif 15 < b <= 30:
#         I.append(b)
#     elif 30 < b <= 45:
#         N.append(b)
#     elif 45 < b <= 60:
#         G.append(b)
#     elif 60 < b <= 75:
#         O.append(b)
#
#
# bingo_dict['B'] = B
# bingo_dict['I'] = I
# bingo_dict['N'] = N
# bingo_dict['G'] = G
# bingo_dict['O'] = O
#
# print(bingo_dict)




# Задача 12. Да се напише програма, която да създава речник от стринг. Ключовете на
# речника трябва да бъдат буквите от стринга, а стойностите броят на повторение на
# буквите в стринга.


# text_dict = {}
#
# text = input("Please provide a text: ")
#
# for t in text:
#     text_dict[t] = text.count(t)
#
# print(text_dict)





# Задача 13. Да се напише програма, която да групира думи по броят на главните букви в
# тях. Резултатът да се запази в речник, чиито ключове трябва да са броят на главните
# букви, а стойностите списък с думите. Думите не трябва да се повтарят в списъка.


# words = ["HaPPy", "mOOdy", "yummy", "mayBE"]
# code = 0
# count = 0
#
#
#
# for el in words:
#     for letter in el:
#         code = ord(letter)
#         if code < 133:
#             count+=1


# ????????????????????????????????????????????????????????


# Задача 14. Даден е речник, съдържащ тримесечни стойности на продажбите за една
# година. Трябва да се напише програма, която да създава bar chart по зададеният речник.
# Ключовете на речника трябва да са: Q1, Q2, Q3, Q4. В графиката стойностите трябва да
# се показват в низходящ ред. Ако има стойности, които са равни те трябва да бъдат
# показани както са постъпи през годината.


# year_sales = {"Q4": 250, "Q1": 300, "Q2": 150, "Q3": 0}
# n = 5
#
# sorted_dict = dict(sorted(year_sales.items(),
#                            key=lambda item: item[1],
#                            reverse=True))
#
# for key, value in sorted_dict.items():
#     print(f"{key}|", n* "#", f"{value}")
#     n -= 2






# Задача 15. Google стартира мрежа от автономни дронове за доставка на пица и иска да
# създадете гъвкава система за награди (Pizza Points ™), която може да бъде настроена в
# бъдеще. Правилата са прости: ако клиент е направил поне N поръчки на най-малко Y
# цена, той получава БЕЗПЛАТНА пица!


# customers = {
#  "Batman": [22, 30, 11, 17, 15, 52, 27, 12],
#  "Spider-Man": [5, 17, 30, 33, 40, 22, 26, 10, 11, 45]
# }
#
# orders = 0
#
# min_price = int(input("Please provide a minimum price: "))
# min_orders = int(input("Please provide a minimum number of orders: "))
#
#
# list_Batman = customers["Batman"]
#
# for el in list_Batman:
#     if el > min_price:
#         orders += 1
#     if orders > min_orders:
#         print("Batman")
#         break
#
#
# list_Spider_Man = customers["Spider-Man"]
#
# for el in list_Spider_Man:
#     if el > min_price:
#         orders += 1
#     if orders > min_orders:
#         print("Spider-Man")
#         break


# Не е оптимизирано ?????????????????????????????????????????



# Задача 16. Дадено е стандартно класиране на конкуренцията (известно също като „1224“
# класиране) от някакво спортно състезание. Даден е речник, съдържащ имената и
# оценките на 5 състезатели, както и име на състезател, трябва да се напише програма,
# която да връща ранга на въведеният състезател. Рангът се изчислява като на найвисоката позиция в класирането се задава ранг 1, всеки следващ състезател получава
# предходният ранг увеличен с 1. Това може да се види на следващите примери.


# competitors = {
#     "George": 96,
#     "Emily": 96,
#     "Susan": 93,
#     "Jane": 89,
#     "Brett": 82
# }
#
# list_names = []
# list_scores = []
# list_places = []
# index = 0
# place = 1
# competitors_new = {}
#
# for key, value in competitors.items():
#     list_names.append(key)
#     list_scores.append(value)
#
# for score in list_scores:
#     if score[index] == score[index+1]:
#         list_places.append(place)
#     else:
#         place += 1
#         list_places.append(place)
#
# for name in list_names:
#     for place in list_places:
#         competitors_new[name] = place
#
#
# print(competitors_new)




??????????????????????????????????????????????????????????????     MISTAKE





# Задача 17 Даден е речник студенти и техните точки от тест. Имената на студентите са
# ключове на речника, а техните точки са запазени в списък. Да се напише програма, която
# да изчислява средните точки на всеки един от студентите и да извежда на екрана този,
# който има най-висок среден резултат.


#
# student_scores = {
#  "John": [100, 90, 80],
#  "Bob": [100, 70, 80]
# }
#
#
# John_avg = ((student_scores["John"][0]) +(student_scores["John"][1]) + (student_scores["John"][2])) / 3
# Bob_avg = ((student_scores["Bob"][0]) +(student_scores["Bob"][1]) + (student_scores["Bob"][2])) / 3
#
#
# if John_avg > Bob_avg:
#     print("John")
# elif John_avg == Bob_avg:
#     print("The results are equal.")
# else:
#     print("Bob")


# Не е оптимизирано ??????????????????????????????????


# probvah i ne stana:

# total = 0

# for key in student_scores.keys():
#     key = student_scores[key]
#
#
#
#
# for el in range(0, len(key)):
#     total = total + key[el]
#
#
# print(total)


# for key in student_scores.keys():
#     for value in student_scores.values():
#         print(value)
