#  ------------------------------------------ зад 1 -----------------------------
# Да се създаде .csv файл, който да пази информацията от таблицата. Файлът
# да се казва “Books.csv”
#
#
# def save_books(filename, books):
#     with open(filename, 'w', newline='') as f:
#         w = csv.writer(f, delimiter="|", quotechar='"')
#         w.writerow(['BookTitle', 'Author', 'Year'])
#         w.writerows(books)
#
#
# books = [
#     ['To Kill a Mockingbird', 'Harper Lee', 1960],
#     ['Book 2', 'Author 2', 2000]
# ]
#
# save_books(filename='./books.csv', books=books)

# def load_books(filename):
#     books = list()
#     with open(filename, 'r', newline='') as f:
#         r = csv.reader(f, delimiter="|", quotechar='"')
#
#         first_line = True
#         for row in r:
#             if not first_line:
#                 books.append(row)
#             else:
#                 first_line = False
#
#     return books
#
#
# books = load_books(filename='./books.csv')
# print(books)
#
#
#  ------------------------------------------ зад 2 -----------------------------
# Използвайте създаденият файл Books.csv и накарайте потребителя да добави
# нов запис след всички останали редове във файла. Да се принтират всички редове от
# файла на отделен ред.
#
#
# import csv
#
#
# def save_books(filename, books):
#     with open(filename, 'a+', newline='') as f:
#         w = csv.writer(f, delimiter="|", quotechar='"')
#         w.writerows(books)
#
#
# new_book_name = input("Please provide the name of the book: ")
# new_book_author = input("Please provide the name of the author of book: ")
# new_book_year = input("Please provide the year when the book was published: ")
#
#
# new_book = [new_book_name, new_book_author, new_book_year]
#
# books = [new_book]
#
# save_books(filename='./books.csv', books=books)
#
#
#   ????????????????????????????????????????????????????????????????????????? Оставя 1 празен ред
#
#
#  ------------------------------------------ зад 3 -----------------------------
#
#  Използвайки файла Books.csv, попитайте потребителя колко записи иска да
# добави в списък и след това му разрешете да добави още толкова. След като всички
# данни са добавени, попитайте потребителя да въведе автор и принтирайте всички
# книги за този автор. Ако в списъка няма книги от този автор, покажете подходящо
# съобщение.
#
#
# import csv
#
#
# def save_books(filename, books):
#     with open(filename, 'a+', newline='') as f:
#         w = csv.writer(f, delimiter="|", quotechar='"')
#         w.writerows(books)
#
#
# count = int(input("How many new books yould you like to add: "))
# books = []
# for n in range(count):
#     new_book_name = input("Please provide the name of the book: ")
#     new_book_author = input("Please provide the name of the author of book: ")
#     new_book_year = input("Please provide the year when the book was published: ")
#     print()
#     new_book = [new_book_name, new_book_author, new_book_year]
#     books.append(new_book)
#
# save_books(filename='./books.csv', books=books)
#
# searched_author = input("Please provide the name of the author you are searching for: ")
#
#
# def load_books(filename):
#     books = list()
#     with open(filename, 'r', newline='') as f:
#         r = csv.reader(f, delimiter="|", quotechar='"')
#
#         first_line = True
#         for row in r:
#             if not first_line:
#                 books.append(row)
#             else:
#                 first_line = False
#
#         for book in books:
#             if book[1] == searched_author:
#                 print(book[0])
#
#
# books = load_books(filename='./books.csv')
#
# ?????????????????????????????????????????????????????????????? Ако има празни редове в csv file-а, кодът се чупи.
#
# #  ------------------------------------------ зад 4 -----------------------------
#
#
# Използвайки файла Books.csv, помолете потребителя да въведе начална и
# крайна година. Покажете всички книги, издадени между тези две години.
#
#
# import csv
#
#
# year_start = int(input("Please tell us the start year of your search: "))
# year_end = int(input("Please tell us the end year of your search: "))
#
#
# def load_books(filename):
#     books = list()
#     with open(filename, 'r', newline='') as f:
#         r = csv.reader(f, delimiter="|", quotechar='"')
#
#         first_line = True
#         for row in r:
#             if not first_line:
#                 books.append(row)
#             else:
#                 first_line = False
#
#         for book in books:
#             if year_start <= int(book[2]) <= year_end:
#                 print(book)
#
#
# books = load_books(filename='./books.csv')
#
# #  ------------------------------------------ зад 5 -----------------------------
#
#
# Използвайки файла Books.csv, покажете всички данни, както и номерът на
# реда.
#
#
# import csv
#
#
# def load_books(filename):
#     books = list()
#     count = 2
#     with open(filename, 'r', newline='') as f:
#         r = csv.reader(f, delimiter="|", quotechar='"')
#
#         first_line = True
#         for row in r:
#             if not first_line:
#                 books.append(row)
#             else:
#                 first_line = False
#
#         for book in books:
#             print(str(count) + str(book))
#             count += 1
#
# books = load_books(filename='./books.csv')
#
# #  ------------------------------------------ зад 6 -----------------------------
#
#
# Импортирайте данните от файла Books.csv в списък. Покажете списъка на
# потребителя. Помолете го да избере ред от списъка, който да бъде изтрит, и го
# премахнете от списъка. Попитайте потребителя, кои от данни, той иска да бъдат
# променени и го направете. Запишете данните обратно в оригиналния .csv файл, като
# презапишете съществуващите данни с променените данни.
#
#
# import csv
# import pandas as pd
#
#
# def load_books(filename):
#     books = list()
#     with open(filename, 'r', newline='') as f:
#         r = csv.reader(f, delimiter="|", quotechar='"')
#
#         first_line = True
#         for row in r:
#             if not first_line:
#                 books.append(row)
#             else:
#                 first_line = False
#
#         for book in books:
#             print(book)
#
#
# books = load_books(filename='./books.csv')
#
# # print()
# # row_to_delete = int(input("Which row would you like to delete: "))
# #
# # url = './books.csv'
# # df = pd.read_csv(url)
# #
# # df = df.drop(row_to_delete - 1)
# #
# # print(df)
# #
#
# r = csv.reader(open('./books.csv'))
# lines = list(r)
#
# print()
# row_to_change = int(input("On which row is the book you want to edit: "))
# item_to_change = int(input("Please enter 0 for Book name, 1 for Author, 2 for Year: "))
# new_item = input("Please provide the new value you want to add at that place: ")
#
# lines[row_to_change - 1][item_to_change] = new_item
#
# print(lines)
#
# # writer = csv.writer(open('./books.csv', 'w'))
# # writer.writerows(lines)
#
#
# # Последната част от задачата - имаме лист от листове и малките листове са  във формат, в който не мога да ги използвам.
#
# #  ------------------------------------------ зад 7 -----------------------------
#
#
# Създайте прост математически въпросник, който да подкани потребителя да
# въведе име и след това да се генерират два въпроса на случен принцип. Името,
# въпросите, отговорите и получените точки да се запишат в csv файл. Когато и да се
# стартира програмата, тя трябва да не презаписва информацията въведена във файла.
#
#
# import random
#
# questions = [["2+3", "5"], ["7*7", "49"], ["9-3", "6"], ["40/2", 20], ["10+3", "13"]]
# points = 0
#
#
# for i in range(3):
#     n = random.randint(0, 4)
#     print(questions[n][0])
#     print()
#     answer = int(input("Please provide your answer: "))
#
#     if answer == questions[n][1]:
#         points += 1
#
# print(f'You received {points} points out of 3.')
#

# ????????????????????????????????????????????????????? There is a bug but I will fix it.