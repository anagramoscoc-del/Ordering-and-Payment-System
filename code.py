#staff username: admin
#staff password: 123
import sys
from datetime import datetime

dish_name = ["Adobong Manok", "Calderetang Kambing", "Bulalo", "Tinolang Manok", "Rice"]
dish_price = [90.0, 90.0, 150.0, 90.0, 15.0]
dish_servings = [15, 15, 10, 15, 30]
drink_name = ["Coke One Liter", "Coke Mismo", "Sprite Mismo"]
drink_price = [55.0, 30.0, 30.0]
drink_quantity = [15, 20, 20]
archive_dish = []
archive_price = []
archive_serving = []
archive_drink = []
archive_drink_price = []
archive_drink_quantity = []
queue_number = 1
recorded_receipts = []
daily_sales = []          

STAFF_USER = "admin"
STAFF_PASS = "123"

def main_menu():
    while True:
        print("==============================")
        print("          MAIN MENU")
        print("==============================")
        print("1. Staff")
        print("2. Customer")
        print("==============================")
        choice = input("(Enter 0 to exit) Enter your choice: ").strip()
        if choice == "0":
            username = input("Enter Username: ").strip()
            if username == STAFF_USER:
                password = input("Enter Password: ").strip()
                if password == STAFF_PASS:
                    print("Exiting program...")
                    sys.exit()
                else:
                    print("Incorrect password.")
            else:
                print("Incorrect Username.")
        elif choice == "1":
            staff_login()
        elif choice == "2":
            customer_menu()
        else:
            print("Invalid choice.")

def staff_login():
    while True:
        username = input("Enter Username: ").strip()
        if username != STAFF_USER:
            print("Incorrect Username.")
            continue
        password = input("Enter Password: ").strip()
        if password == STAFF_PASS:
            staff_menu()
            break
        else:
            print("Incorrect password.")

def staff_menu():
    while True:
        print("==============================")
        print("          STAFF MENU")
        print("==============================")
        print("1. View Dish Menu")
        print("2. View Drinks Menu")
        print("3. Add new dish")
        print("4. Add new drink")
        print("5. View out of stock / Archive")
        print("6. Edit Menu (Dishes / Drinks)")
        print("7. View recorded receipts")
        print("8. Daily Sales Report / Summary")
        print("==============================")
        choice = input("(Enter 0 to logout) Enter your choice: ").strip()
        if choice == "0":
            y_n = input("Do you like to logout? (y/n): ").strip().lower()
            if y_n == "y":
                print("==============================")
                print("Returning to main menu...")
                return
            elif y_n == "n":
                continue
            else:
                print("Enter valid choice.")
        elif choice == "1":
            view_dish_menu()
        elif choice == "2":
            view_drink_menu()
        elif choice == "3":
            add_dish()
        elif choice == "4":
            add_drink()
        elif choice == "5":
            view_out_of_stock()
        elif choice == "6":
            edit()
        elif choice == "7":
            view_recorded_receipts()
        elif choice == "8":
            daily_sales_report()
        else:
            print("Invalid choice.")

def customer_menu():
    while True:
        print("==============================")
        print("        CUSTOMER MENU")
        print("==============================")
        print("1. View menu")
        print("2. Order")
        print("==============================")
        choice = input("(Enter 0 to exit) Enter your choice: ").strip()
        if choice == "0":
            y_n = input("Do you like to logout? (y/n): ").strip().lower()
            if y_n == "y":
                print("==============================")
                print("Returning to main menu...")
                return
            elif y_n == "n":
                continue
            else:
                print("Enter valid choice.")
        elif choice == "1":
            view_dish_menu()
            print()
            view_drink_menu()
        elif choice == "2":
            order()
        else:
            print("Invalid choice.")

def view_dish_menu():
    print("=================================================================")
    print("                         DISH MENU")
    print("=================================================================")
    print(f"{'No.':<5} | {'DISH NAME':<28} | {'PRICE':<12} | {'SERVINGS':<8}")
    print("-" * 65)
    if len(dish_name) == 0:
        print("No dishes available.")
    else:
        for i in range(len(dish_name)):
            print(f"{i+1:<5} | {dish_name[i]:<28} | ₱{dish_price[i]:<11.2f} | {dish_servings[i]:<8}")
    print("=================================================================")

def view_drink_menu():
    print("=================================================================")
    print("                        DRINKS MENU")
    print("=================================================================")
    print(f"{'No.':<5} | {'DRINK NAME':<28} | {'PRICE':<12} | {'QUANTITY':<8}")
    print("-" * 65)
    if len(drink_name) == 0:
        print("No drinks available.")
    else:
        for i in range(len(drink_name)):
            print(f"{i+1:<5} | {drink_name[i]:<28} | ₱{drink_price[i]:<11.2f} | {drink_quantity[i]:<8}")
    print("=================================================================")

def add_dish():
    print("==============================")
    print("         ADD NEW DISH")
    print("==============================")
    while True:
        new_dish_name = input("Enter dish name (Enter 0 to exit): ").strip()
        if new_dish_name == "0":
            print("Exiting... Returning to Staff Menu.")
            return
        if new_dish_name == "":
            print("Dish name cannot be empty.")
            continue
        if any(char.isdigit() for char in new_dish_name):
            print("Dish name cannot contain numbers.")
            continue
        if not all(char.isalpha() or char.isspace() for char in new_dish_name):
            print("Dish name cannot contain special characters.")
            continue
        parts = new_dish_name.split()
        if len(parts) > 1 and all(len(part) == 1 for part in parts):
            print("Invalid name format. Please enter a proper dish name.")
            continue
        if new_dish_name.lower() in [d.lower() for d in dish_name]:
            print("This dish already exists... Try Again")
            continue
        break
    while True:
        try:
            new_dish_price = float(input("Enter price: "))
            if new_dish_price <= 0:
                print("Invalid price... Try Again.")
                continue
            break
        except ValueError:
            print("Enter a valid number...")
    while True:
        try:
            new_dish_servings = int(input("Enter how many servings: "))
            if new_dish_servings <= 0:
                print("Invalid serving... Try Again.")
                continue
            break
        except ValueError:
            print("Enter a whole number...")
    dish_name.append(new_dish_name)
    dish_price.append(new_dish_price)
    dish_servings.append(new_dish_servings)
    print(f'Dish "{new_dish_name}" added successfully.')

def add_drink():
    print("==============================")
    print("         ADD NEW DRINK")
    print("==============================")
    while True:
        new_drink_name = input("Enter drink name (Enter 0 to exit): ").strip()
        if new_drink_name == "0":
            print("Exiting... Returning to Staff Menu.")
            return
        if new_drink_name == "":
            print("Drink name cannot be empty.")
            continue
        if any(char.isdigit() for char in new_drink_name):
            print("Drink name cannot contain numbers.")
            continue
        if not all(char.isalpha() or char.isspace() for char in new_drink_name):
            print("Drink name cannot contain special characters.")
            continue
        parts = new_drink_name.split()
        if len(parts) > 1 and all(len(part) == 1 for part in parts):
            print("Invalid name format. Please enter a proper drink name.")
            continue
        if new_drink_name.lower() in [d.lower() for d in drink_name]:
            print("This drink already exists... Try Again")
            continue
        break
    while True:
        try:
            new_drink_price = float(input("Enter price: "))
            if new_drink_price <= 0:
                print("Invalid price... Try Again.")
                continue
            break
        except ValueError:
            print("Enter a valid number...")
    while True:
        try:
            new_drink_qty = int(input("Enter quantity: "))
            if new_drink_qty <= 0:
                print("Invalid quantity... Try Again.")
                continue
            break
        except ValueError:
            print("Enter a whole number...")
    drink_name.append(new_drink_name)
    drink_price.append(new_drink_price)
    drink_quantity.append(new_drink_qty)
    print(f'Drink "{new_drink_name}" added successfully.')

def show_current_order(order_items, total):
    print("\n=================================================================")
    print("                     YOUR CURRENT ORDER")
    print("=================================================================")
    
    if not order_items:
        print("No items in your order.")
    else:
        print(f"{'No.':<5} | {'ITEM':<28} | {'QTY':<6} | {'AMOUNT':<10}")
        print("-" * 65)
        
        for i, (item_type, name, qty, price) in enumerate(order_items, 1):
            line_total = qty * price
            item_label = f"{name} ({item_type})"
            # Keep it clean if the name is too long
            if len(item_label) > 28:
                item_label = item_label[:25] + "..."
            print(f"{i:<5} | {item_label:<28} | {qty:<6} | ₱{line_total:<9.2f}")
        
        print("-" * 65)
        print(f"{'':<5}  {'':<28} | {'TOTAL':<6} | ₱{total:<9.2f}")
    
    print("=================================================================\n")

def staff_verify_payment():
    print("\n    STAFF VERIFICATION REQUIRED TO COMPLETE PAYMENT    ")
    while True:
        username = input("Staff Username: ").strip()
        password = input("Staff Password: ").strip()
        if username == STAFF_USER and password == STAFF_PASS:
            print("Payment verified by staff. Thank you!\n")
            return True
        else:
            print("Incorrect credentials. Please try again.\n")

def order():
    global queue_number
    if len(dish_name) == 0 and len(drink_name) == 0:
        print("The menu is empty...")
        return
    total = 0.0
    order_items = []
    while True:
        print("\n==============================")
        print("      ORDERING OPTIONS")
        print("==============================")
        print("di  - Order Dishes")
        print("dr  - Order Drinks")
        print("v   - View current order")
        print("0   - Proceed to Payment")
        print("==============================")
        choice = input("Enter your choice (di / dr / v / 0): ").strip().lower()
        if choice == "0":
            break
        elif choice == "v":
            show_current_order(order_items, total)
        elif choice == "di":
            while True:
                print()
                view_dish_menu()
                dish_choice = input("Enter dish number (0 to go back): ").strip()
                if dish_choice == "0":
                    break
                if not dish_choice.isdigit():
                    print("Enter a valid number.")
                    continue
                dish_num = int(dish_choice)
                if dish_num < 1 or dish_num > len(dish_name):
                    print("Invalid dish number.")
                    continue
                idx = dish_num - 1
                available = dish_servings[idx]
                print(f"Available servings: {available}")
                qty_input = input("Enter quantity: ").strip()
                if not qty_input.isdigit():
                    print("Enter a valid quantity.")
                    continue
                quantity = int(qty_input)
                if quantity <= 0:
                    print("Quantity must be greater than zero.")
                    continue
                if quantity > available:
                    print(f"Not enough servings. Only {available} left.")
                    continue
                unit_price = dish_price[idx]
                total += unit_price * quantity
                # Combine similar dishes
                found = False
                for i in range(len(order_items)):
                    if order_items[i][0] == "Dish" and order_items[i][1] == dish_name[idx]:
                        old_qty = order_items[i][2]
                        order_items[i] = ("Dish", dish_name[idx], old_qty + quantity, unit_price)
                        found = True
                        break
                if not found:
                    order_items.append(("Dish", dish_name[idx], quantity, unit_price))
                dish_servings[idx] -= quantity
                print(f"{quantity} x {dish_name[idx]} added to your order.")
                show_current_order(order_items, total)   # show after every addition
                check_and_archive_dish(idx)
        elif choice == "dr":
            while True:
                print()
                view_drink_menu()
                drink_choice = input("Enter drink number (0 to go back): ").strip()
                if drink_choice == "0":
                    break
                if not drink_choice.isdigit():
                    print("Enter a valid number.")
                    continue
                drink_num = int(drink_choice)
                if drink_num < 1 or drink_num > len(drink_name):
                    print("Invalid drink number.")
                    continue
                idx = drink_num - 1
                available = drink_quantity[idx]
                print(f"Available quantity: {available}")
                qty_input = input("Enter quantity: ").strip()
                if not qty_input.isdigit():
                    print("Enter a valid quantity.")
                    continue
                quantity = int(qty_input)
                if quantity <= 0:
                    print("Quantity must be greater than zero.")
                    continue
                if quantity > available:
                    print(f"Not enough stock. Only {available} left.")
                    continue
                unit_price = drink_price[idx]
                total += unit_price * quantity
                # Combine similar drinks
                found = False
                for i in range(len(order_items)):
                    if order_items[i][0] == "Drink" and order_items[i][1] == drink_name[idx]:
                        old_qty = order_items[i][2]
                        order_items[i] = ("Drink", drink_name[idx], old_qty + quantity, unit_price)
                        found = True
                        break
                if not found:
                    order_items.append(("Drink", drink_name[idx], quantity, unit_price))
                drink_quantity[idx] -= quantity
                print(f"{quantity} x {drink_name[idx]} added to your order.")
                show_current_order(order_items, total)
                check_and_archive_drink(idx)
        else:
            print("Invalid choice. Please type 'di', 'dr', 'v', or '0'.")
    if len(order_items) == 0:
        print("No orders placed.")
        return

    # Final review before payment
    print("\n =====   FINAL ORDER REVIEW   ===== ")
    show_current_order(order_items, total)
    confirm = input("Proceed to payment? (y/n): ").strip().lower()
    if confirm != "y":
        print("Order cancelled. Returning to Customer Menu.")
        return
    if not staff_verify_payment():
        print("Payment was not completed. Order cancelled.")
        return
    current_queue = queue_number
    queue_number += 1
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    receipt = {
        "queue": current_queue,
        "items": order_items,
        "total": total,
        "timestamp": timestamp,
        "paid": True
    }
    recorded_receipts.append(receipt)
    daily_sales.append(receipt)
    print("\n==============================")
    print(f"     QUEUE NUMBER: {current_queue:03d}")
    print("==============================")
    print("           RECEIPT")
    print("==============================")
    print(f"Date/Time : {timestamp}")
    for item_type, name, qty, price in order_items:
        line_total = qty * price
        print(f"{qty} x {name} ({item_type}) - ₱{line_total:.2f}")
    print("------------------------------")
    print(f"Total bill: ₱{total:.2f}")
    print(f"Your Queue Number is: {current_queue:03d}")
    print("Status: PAID")
    print("==============================")
    print("Please wait for your number to be called. Thank you!\n")

def check_and_archive_dish(index):
    if dish_servings[index] <= 0:
        name = dish_name[index]
        archive_dish.append(dish_name[index])
        archive_price.append(dish_price[index])
        archive_serving.append(dish_servings[index])
        print(f'"{name}" (Dish) is now out of stock and moved to archive.')

def check_and_archive_drink(index):
    if drink_quantity[index] <= 0:
        name = drink_name[index]
        archive_drink.append(drink_name[index])
        archive_drink_price.append(drink_price[index])
        archive_drink_quantity.append(drink_quantity[index])
        print(f'"{name}" (Drink) is now out of stock and moved to archive.')

def view_out_of_stock():
    print("\n==============================")
    print("     OUT OF STOCK / ARCHIVE")
    print("==============================")
    print("\n--- DISHES ARCHIVE ---")
    if len(archive_dish) == 0:
        print("No dishes are out of stock.")
    else:
        print(f"{'No.':<5} | {'Dish Name':<25} | {'Price':<10} | {'Servings':<8}")
        print("-" * 58)
        for i in range(len(archive_dish)):
            print(f"{i+1:<5} | {archive_dish[i]:<25} | ₱{archive_price[i]:<9.2f} | {archive_serving[i]:<8}")
    print("\n--- DRINKS ARCHIVE ---")
    if len(archive_drink) == 0:
        print("No drinks are out of stock.")
    else:
        print(f"{'No.':<5} | {'Drink Name':<25} | {'Price':<10} | {'Quantity':<8}")
        print("-" * 58)
        for i in range(len(archive_drink)):
            print(f"{i+1:<5} | {archive_drink[i]:<25} | ₱{archive_drink_price[i]:<9.2f} | {archive_drink_quantity[i]:<8}")
    print("==============================\n")

def view_recorded_receipts():
    print("\n==============================")
    print("      RECORDED RECEIPTS")
    print("==============================")
    if len(recorded_receipts) == 0:
        print("No receipts have been recorded yet.")
        print("==============================\n")
        return
    for receipt in recorded_receipts:
        print(f"\nQueue Number : {receipt['queue']:03d}")
        print(f"Date/Time    : {receipt.get('timestamp', 'N/A')}")
        print(f"Status       : {'PAID' if receipt.get('paid') else 'UNPAID'}")
        print("------------------------------")
        for item_type, name, qty, price in receipt["items"]:
            line_total = qty * price
            print(f"  {qty} x {name:<22} ({item_type}) ₱{line_total:>8.2f}")
        print("------------------------------")
        print(f"  TOTAL{' ' * 30} ₱{receipt['total']:>8.2f}")
        print("==============================")
    print(f"\nTotal recorded orders: {len(recorded_receipts)}")
    print("==============================\n")

def daily_sales_report():
    print("\n==================================================")
    print("           DAILY SALES REPORT / SUMMARY")
    print("==================================================")
    if not daily_sales:
        print("No paid sales recorded yet today.")
        print("==================================================\n")
        return
    total_revenue = 0.0
    total_orders = len(daily_sales)
    item_count = {}          
    item_revenue = {}        
    for sale in daily_sales:
        total_revenue += sale["total"]
        for item_type, name, qty, price in sale["items"]:
            key = f"{name} ({item_type})"
            item_count[key] = item_count.get(key, 0) + qty
            item_revenue[key] = item_revenue.get(key, 0.0) + (qty * price)
    print(f"Total Paid Orders : {total_orders}")
    print(f"Total Revenue     : ₱{total_revenue:.2f}")
    print("--------------------------------------------------")
    print("ITEM BREAKDOWN")
    print(f"{'Item':<30} | {'Qty Sold':<10} | {'Revenue':<12}")
    print("-" * 58)
    for name in sorted(item_count.keys()):
        print(f"{name:<30} | {item_count[name]:<10} | ₱{item_revenue[name]:<11.2f}")
    print("--------------------------------------------------")
    print("DETAILED ORDERS")
    for sale in daily_sales:
        print(f"  Queue {sale['queue']:03d} | {sale['timestamp']} | ₱{sale['total']:.2f}")
    print("==================================================\n")

def edit():
    while True:
        print("\n==============================")
        print("          EDIT MENU")
        print("==============================")
        print("0. Go back")
        print("1. Edit Dish Price")
        print("2. Edit Dish Servings")
        print("3. Rename Dish")
        print("4. Edit Drink Price")
        print("5. Edit Drink Quantity")
        print("6. Rename Drink")
        print("==============================")
        choice = input("Enter choice: ").strip()
        if choice == "0":
            return
        elif choice == "1":
            edit_dish_price()
        elif choice == "2":
            edit_dish_servings()
        elif choice == "3":
            rename_dish()
        elif choice == "4":
            edit_drink_price()
        elif choice == "5":
            edit_drink_quantity()
        elif choice == "6":
            rename_drink()
        else:
            print("Invalid choice.")

def edit_dish_price():
    view_dish_menu()
    if not dish_name:
        return
    choice = input("Enter dish number to edit price (0 to cancel): ").strip()
    if choice == "0" or not choice.isdigit():
        return
    idx = int(choice) - 1
    if idx < 0 or idx >= len(dish_name):
        print("Invalid number.")
        return
    current_price = dish_price[idx]
    while True:
        try:
            new_price = float(input(f"New price for {dish_name[idx]} (current: ₱{current_price:.2f}): "))
            if new_price <= 0:
                print("Price must be greater than 0.")
                continue
            if new_price == current_price:
                print("New price cannot be the same as the current price.")
                continue
            dish_price[idx] = new_price
            print("Price updated.")
            break
        except ValueError:
            print("Enter a valid number.")

def edit_dish_servings():
    view_dish_menu()
    if not dish_name:
        return
    choice = input("Enter dish number to edit servings (0 to cancel): ").strip()
    if choice == "0" or not choice.isdigit():
        return
    idx = int(choice) - 1
    if idx < 0 or idx >= len(dish_name):
        print("Invalid number.")
        return
    while True:
        try:
            new_serv = int(input(f"New servings for {dish_name[idx]}: "))
            if new_serv < 0:
                print("Cannot be negative.")
                continue
            dish_servings[idx] = new_serv
            print("Servings updated.")
            break
        except ValueError:
            print("Enter a whole number.")

def rename_dish():
    view_dish_menu()
    if not dish_name:
        return
    choice = input("Enter dish number to rename (0 to cancel): ").strip()
    if choice == "0" or not choice.isdigit():
        return
    idx = int(choice) - 1
    if idx < 0 or idx >= len(dish_name):
        print("Invalid number.")
        return
    old = dish_name[idx]
    while True:
        new_name = input(f"New name for '{old}': ").strip()
        if not new_name:
            print("Name cannot be empty.")
            continue
        if any(char.isdigit() for char in new_name):
            print("Dish name cannot contain numbers.")
            continue
        if not all(char.isalpha() or char.isspace() for char in new_name):
            print("Dish name cannot contain special characters.")
            continue
        parts = new_name.split()
        if len(parts) > 1 and all(len(part) == 1 for part in parts):
            print("Invalid name format. Please enter a proper dish name.")
            continue
        if new_name.lower() in [d.lower() for d in dish_name]:
            print("Name already exists.")
            continue
        dish_name[idx] = new_name
        print(f'Renamed to "{new_name}"')
        break

def edit_drink_price():
    view_drink_menu()
    if not drink_name:
        return
    choice = input("Enter drink number to edit price (0 to cancel): ").strip()
    if choice == "0" or not choice.isdigit():
        return
    idx = int(choice) - 1
    if idx < 0 or idx >= len(drink_name):
        print("Invalid number.")
        return
    current_price = drink_price[idx]
    while True:
        try:
            new_price = float(input(f"New price for {drink_name[idx]} (current: ₱{current_price:.2f}): "))
            if new_price <= 0:
                print("Price must be greater than 0.")
                continue
            if new_price == current_price:
                print("New price cannot be the same as the current price.")
                continue
            drink_price[idx] = new_price
            print("Price updated.")
            break
        except ValueError:
            print("Enter a valid number.")

def edit_drink_quantity():
    view_drink_menu()
    if not drink_name:
        return
    choice = input("Enter drink number to edit quantity (0 to cancel): ").strip()
    if choice == "0" or not choice.isdigit():
        return
    idx = int(choice) - 1
    if idx < 0 or idx >= len(drink_name):
        print("Invalid number.")
        return
    while True:
        try:
            new_qty = int(input(f"New quantity for {drink_name[idx]}: "))
            if new_qty < 0:
                print("Cannot be negative.")
                continue
            drink_quantity[idx] = new_qty
            print("Quantity updated.")
            break
        except ValueError:
            print("Enter a whole number.")

def rename_drink():
    view_drink_menu()
    if not drink_name:
        return
    choice = input("Enter drink number to rename (0 to cancel): ").strip()
    if choice == "0" or not choice.isdigit():
        return
    idx = int(choice) - 1
    if idx < 0 or idx >= len(drink_name):
        print("Invalid number.")
        return
    old = drink_name[idx]
    while True:
        new_name = input(f"New name for '{old}': ").strip()
        if not new_name:
            print("Name cannot be empty.")
            continue
        if any(char.isdigit() for char in new_name):
            print("Drink name cannot contain numbers.")
            continue
        if not all(char.isalpha() or char.isspace() for char in new_name):
            print("Drink name cannot contain special characters.")
            continue
        parts = new_name.split()
        if len(parts) > 1 and all(len(part) == 1 for part in parts):
            print("Invalid name format. Please enter a proper drink name.")
            continue
        if new_name.lower() in [d.lower() for d in drink_name]:
            print("Name already exists.")
            continue
        drink_name[idx] = new_name
        print(f'Renamed to "{new_name}"')
        break

main_menu()