# ==========================================
# BILLING FUNCTIONS
# ==========================================

def calculate_total(orders):
    subtotal = 0

    for order in orders:
        item_name, quantity, price = order
        item_total = quantity * price
        subtotal += item_total

    return subtotal


def calculate_discount(subtotal):
    if subtotal >= 500:
        discount = subtotal * 0.10
    else:
        discount = 0

    return discount


def print_receipt(orders):
    subtotal = calculate_total(orders)
    discount = calculate_discount(subtotal)
    total = subtotal - discount

    print("\n")
    print("==========================================")
    print("            UBAS RESTAURANT")
    print("                 RECEIPT")
    print("==========================================")
    print(f"{'ITEM':20} {'QTY':>5} {'PRICE':>10} {'TOTAL':>10}")
    print("------------------------------------------")

    for order in orders:
        item_name, quantity, price = order
        item_total = quantity * price

        print(
            f"{item_name:20} {quantity:>5} "
            f"PHP {price:>7.2f} PHP {item_total:>7.2f}"
        )

    print("------------------------------------------")
    print(f"{'Subtotal:':30} PHP {subtotal:>7.2f}")
    print(f"{'Discount:':30} PHP {discount:>7.2f}")
    print(f"{'TOTAL:':30} PHP {total:>7.2f}")
    print("==========================================")
    print("       Thank you for ordering!")
    print("          Come again soon!")
    print("==========================================")