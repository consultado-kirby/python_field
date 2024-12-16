import os
os.system('cls')

class Customer:
    def __init__(self, name, brand, model, date, price):
        self.name = name
        self.brand = brand
        self.model = model
        self.date = date
        self.price = price

    def display_customer(self):
        print(f"The name of the customer is {self.name}.")

    def display_car(self):
        print(f"The brand of car he bought is {self.brand} {self.model}.")

    def display_date(self):
        print(f"The car was purchased on {self.date}")

    def display_price(self):
        print(f"The {self.brand} {self.model} was sold for {self.price} pesos.")

    def display_receipt(self):
        print("Car Sale Receipt\n")
        print(f"Customer Name\t|\t{self.name}")
        print(f"Car Purchased\t|\t{self.brand} {self.model}")
        print(f"Date of Purchase\t|\t{self.date}")
        print(f"Unit Price\t|\t{self.price}")

def information():
    name = input("Enter your name: ")
    brand = input("Enter the brand: ")
    model = input("Enter the model: ")
    date = input("Enter the date of purchase: ")
    price = input("Enter the unit price: ")

    return Customer(name, brand, model, date, price)

def display_menu():
    os.system('cls')
    print("Purchase Information\n")
    print("1 - Customer name")
    print("2 - Car's brand and model")
    print("3 - Date of purchase")
    print("4 - Unit price")
    print("5 - Purchace receipt")
    print("\n             0 - Exit")

    return input("Enter your choice: ")

def purchase_info(choice, customer):
    match choice:
        case '1':
            customer.display_customer()
            input("\nPress enter to continue.")
        case '2':
            customer.display_car()
            input("\nPress enter to continue.")
        case '3':
            customer.display_date()
            input("\nPress enter to continue.")
        case '4':
            customer.display_price()
            input("\nPress enter to continue.")
        case '5':
            customer.display_receipt()
            input("\nPress enter to continue.")
        case '0':
            pass # exit
        case _:
            input("Invalid choice. ")

unset_option = -1
exit_option = 0
def kirby():
    customer = information()
    choice = unset_option
    while choice != exit_option:
        choice = display_menu()
        purchase_info(choice, customer)
        os.system("cls")

kirby()