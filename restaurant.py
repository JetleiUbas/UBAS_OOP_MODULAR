
# ==========================================
# UBAS RESTAURANT ORDERING SYSTEM
# restaurant.py
# ==========================================


# ==========================================
# CLASS: MENU ITEM
# ==========================================

class MenuItem:
    def __init__(self, number, name, price):
        self.number = number
        self.name = name
        self.price = price


# ==========================================
# CLASS: ORDER
# ==========================================

class Order:
    def __init__(self, menu_item, quantity):
        self.menu_item = menu_item
        self.quantity = quantity

    def calculate_item_total(self):
        return self.menu_item.price * self.quantity


# ==========================================
# CLASS: RESTAURANT
# ==========================================

class Restaurant:

    def __init__(self):
        self.menu = {
            "1": MenuItem("1", "Ubas Burger", 85.00),
            "2": MenuItem("2", "Ubas Chicken Meal", 120.00),
            "3": MenuItem("3", "French Fries", 60.00),
            "4": MenuItem("4", "Ubas Spaghetti", 95.00),
            "5": MenuItem("5", "Pizza Slice", 75.00),
            "6": MenuItem("6", "Chicken Sandwich", 100.00),
            "7": MenuItem("7", "Soft Drink", 45.00),
            "8": MenuItem("8", "Iced Tea", 50.00)
        }

        self.orders = []

    # ==========================================
    # DISPLAY MENU
    # ==========================================

    def display_menu(self):
        print("\n==========================================")
        print("              UBAS RESTAURANT")
        print("                  MENU")
        print("==========================================")

        for number, item in self.menu.items():
            print(
                f"{number}. {item.name:20} "
                f"PHP {item.price:.2f}"
            )

        print("==========================================")

    # ==========================================
    # GET MENU CHOICE
    # ==========================================

    def get_menu_choice(self):
        while True:
            choice = input("Enter menu number: ").strip()

            if choice in self.menu:
                return self.menu[choice]

            print("Invalid menu number. Please try again.")

    # ==========================================
    # GET QUANTITY
    # ==========================================

    def get_quantity(self):
        while True:
            try:
                quantity = int(input("Enter quantity: "))

                if quantity > 0:
                    return quantity
                else:
                    print("Quantity must be greater than zero.")

            except ValueError:
                print("Please enter a valid number.")

    # ==========================================
    # GET ORDER
    # ==========================================

    def get_order(self):
        while True:
            self.display_menu()

            menu_item = self.get_menu_choice()
            quantity = self.get_quantity()

            order = Order(menu_item, quantity)
            self.orders.append(order)

            print(f"\nAdded {quantity} {menu_item.name}.")

            while True:
                another = input(
                    "Do you want to order another item? (yes/no): "
                ).lower().strip()

                if another == "yes" or another == "y":
                    break

                elif another == "no" or another == "n":
                    return

                else:
                    print("Please enter yes or no.")

    # ==========================================
    # CALCULATE TOTAL
    # ==========================================

    def calculate_total(self):
        subtotal = 0

        for order in self.orders:
            subtotal += order.calculate_item_total()

        return subtotal

    # ==========================================
    # CALCULATE DISCOUNT
    # ==========================================

    def calculate_discount(self, subtotal):
        if subtotal >= 500:
            discount = subtotal * 0.10
        else:
            discount = 0

        return discount

    # ==========================================
    # PRINT RECEIPT
    # ==========================================

    def print_receipt(self):
        subtotal = self.calculate_total()
        discount = self.calculate_discount(subtotal)
        total = subtotal - discount

        print("\n")
        print("==========================================")
        print("            UBAS RESTAURANT")
        print("                 RECEIPT")
        print("==========================================")

        print(
            f"{'ITEM':20} {'QTY':>5} "
            f"{'PRICE':>10} {'TOTAL':>10}"
        )

        print("------------------------------------------")

        for order in self.orders:
            item_name = order.menu_item.name
            quantity = order.quantity
            price = order.menu_item.price
            item_total = order.calculate_item_total()

            print(
                f"{item_name:20} {quantity:>5} "
                f"PHP {price:>7.2f} "
                f"PHP {item_total:>7.2f}"
            )

        print("------------------------------------------")
        print(f"{'Subtotal:':30} PHP {subtotal:>7.2f}")
        print(f"{'Discount:':30} PHP {discount:>7.2f}")
        print(f"{'TOTAL:':30} PHP {total:>7.2f}")
        print("==========================================")
        print("       Thank you for ordering!")
        print("          Come again soon!")
        print("==========================================")

    # ==========================================
    # START PROGRAM
    # ==========================================

    def start(self):
        print("==========================================")
        print("       WELCOME TO UBAS RESTAURANT")
        print("==========================================")

        while True:
            order_now = input(
                "Would you like to order? (yes/no): "
            ).lower().strip()

            if order_now == "yes" or order_now == "y":
                break

            elif order_now == "no" or order_now == "n":
                print("\nThank you for visiting UBAS Restaurant!")
                print("Goodbye!")
                return

            else:
                print("Please enter yes or no.")

        self.get_order()
        self.print_receipt()