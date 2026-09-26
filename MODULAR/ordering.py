# ==========================================
# ORDERING FUNCTIONS
# ==========================================

from menu import menu
from display import display_menu


def get_yes_or_no(prompt):
    while True:
        answer = input(prompt).lower().strip()

        if answer in ("yes", "y"):
            return True
        elif answer in ("no", "n"):
            return False
        else:
            print("Please enter yes or no.")


def get_order():
    orders = []

    while True:
        display_menu()

        # Get valid menu number
        while True:
            choice = input("Enter menu number: ").strip()

            if choice in menu:
                break

            print("Invalid menu number. Please try again.")

        # Get valid quantity
        while True:
            try:
                quantity = int(input("Enter quantity: "))

                if quantity > 0:
                    break

                print("Quantity must be greater than zero.")

            except ValueError:
                print("Please enter a valid number.")

        item_name = menu[choice][0]
        price = menu[choice][1]

        orders.append((item_name, quantity, price))

        # Ask if customer wants another item
        another = get_yes_or_no(
            "Do you want to order another item? (yes/no): "
        )

        if not another:
            return orders