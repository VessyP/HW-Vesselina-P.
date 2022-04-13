import BookShelf

class Profession:

    @staticmethod
    def get_user_role(user_role):
        if user_role == 1:
            return Librarian()
        elif user_role == 2:
            return Vendor()


class Librarian(Profession):
    """Virtual Library"""

    def __init__(self):
        self.name = input("How would you like to be called: ")

    def check_issued_books():
        issued_books_count = 0
        for book in BookShelf.books:
            for key, value in book.items():
                if book["issued"]:
                    issued_books_count += 1
                    break
                else:
                    continue
        print(f"The number of issued books is {issued_books_count}.")
        print()

    def search_for_book():
        list_of_all_values = list()
        for book in BookShelf.books:
            for value in book.values():
                list_of_all_values.append(value)

        searched_book = input("Which book are you searching for: ")
        if searched_book in list_of_all_values:
            print(f"{searched_book} is available.")
        else:
            print(f"{searched_book} is not available.")

    def verify_a_member():
        approved_universities = ["Sofia University", "Technical University", "New Bulgarian University"]
        user_univercity = input("Please enter the name of your university.")
        if user_univercity in approved_universities:
            print("You are verified as a member of our Library.")
        else:
            print("Your university is not on our members list.")
        print()

    def check_payments():
        payments = 0
        for book in BookShelf.books:
            for key, value in book.items():
                if book["issued"]:
                    payments += book["price"]
                    break
        print(f"The full payments made are {payments} BGN.")
        print()


class Vendor(Profession):
    """Virtual Library"""


    def __init__(self):
        self.name = input("How would you like to be called: ")


    def check_issued_books():
        issued_books_count = 0
        for book in BookShelf.books:
            for key, value in book.items():
                if book["issued"]:
                    issued_books_count += 1
                    break
                else:
                    continue
        print(f"The number of issued books is {issued_books_count}.")
        print()


    def payment_details():
        pass                                   #What is expected of this function to return ???
