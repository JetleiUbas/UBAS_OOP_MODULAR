# ==========================================
# DISPLAY FUNCTIONS
# ==========================================

from menu import menu


def display_menu():
    print("\n==========================================")
    print("              UBAS RESTAURANT")
    print("                  MENU")
    print("==========================================")

    for number, item in menu.items():
        print(f"{number}. {item[0]:20} PHP {item[1]:.2f}")

    print("==========================================")


def display_welcome():
    print("==========================================")
    print("       WELCOME TO UBAS RESTAURANT")
    print("==========================================")


def display_goodbye():
    print("\nThank you for visiting UBAS Restaurant!")
    print("Goodbye!")