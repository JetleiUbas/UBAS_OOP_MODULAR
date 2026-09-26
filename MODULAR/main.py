# ==========================================
# UBAS RESTAURANT ORDERING SYSTEM
# MAIN PROGRAM
# ==========================================

from display import display_welcome, display_goodbye
from ordering import get_yes_or_no, get_order
from billing import print_receipt


def main():
    display_welcome()

    order_now = get_yes_or_no(
        "Would you like to order? (yes/no): "
    )

    if not order_now:
        display_goodbye()
        return

    orders = get_order()

    print_receipt(orders)


if __name__ == "__main__":
    main()