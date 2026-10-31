# Ordering and Payment System

A simple console-based restaurant ordering system written in Python.  
It supports **Staff** and **Customer** modes with menu management, ordering, stock tracking, receipts, and daily sales reports.

---

## Features

### Main Menu
- **Staff** – login required
- **Customer** – no login
- Exit program (requires staff credentials)

### Staff Menu
1. View Dish Menu  
2. View Drinks Menu  
3. Add new dish  
4. Add new drink  
5. View out of stock / Archive  
6. Edit Menu (price, servings/quantity, rename)  
7. View recorded receipts  
8. Daily Sales Report / Summary  

### Customer Menu
1. View menu (dishes + drinks)  
2. Order  
   - Order dishes or drinks  
   - View current order  
   - Stock is reduced in real time  
   - Items that reach 0 stock are moved to archive  
   - Final order review → staff payment verification → receipt with queue number  

---

## Default Login (Staff)

| Username | Password |
|----------|----------|
| `admin`  | `123`    |

---

## Default Menu

### Dishes
| Dish                | Price   | Servings |
|---------------------|---------|----------|
| Adobong Manok       | ₱90.00  | 15       |
| Calderetang Kambing | ₱90.00  | 15       |
| Bulalo              | ₱150.00 | 10       |
| Tinolang Manok      | ₱90.00  | 15       |
| Rice                | ₱15.00  | 30       |

### Drinks
| Drink           | Price  | Quantity |
|-----------------|--------|----------|
| Coke One Liter  | ₱55.00 | 15       |
| Coke Mismo      | ₱30.00 | 20       |
| Sprite Mismo    | ₱30.00 | 20       |

---

## How to Run

1. Make sure you have **Python 3** installed.
2. Save the code as a `.py` file (e.g. `restaurant.py`).
3. Run it:

```bash
python restaurant.py
```

or

```bash
python3 restaurant.py
```

---

## Key Behaviors

- **Stock management**: When a dish or drink reaches 0 servings/quantity, it is automatically moved to the archive.
- **Order combining**: Ordering the same item multiple times merges the quantities.
- **Payment verification**: A staff member must enter the correct username and password before an order is marked as paid.
- **Queue numbers**: Each successful paid order gets an incrementing queue number (001, 002, …).
- **Receipts & Sales**: All paid orders are stored and can be viewed later. The Daily Sales Report shows total revenue and item breakdown.
- **Input validation**: Names cannot contain numbers or special characters. Prices and quantities must be positive numbers.

---

## Project Structure (Single File)

All data is kept in memory using Python lists:

- `dish_name`, `dish_price`, `dish_servings`
- `drink_name`, `drink_price`, `drink_quantity`
- Archive lists for out-of-stock items
- `recorded_receipts` and `daily_sales` for transaction history

No external libraries or database are required — only the Python standard library (`sys` and `datetime`).

---

## Notes

- Data is **not persisted**. Everything resets when you close the program.
- This is a console / terminal application (text-based interface).
- Designed for simple classroom / project demonstration purposes.

---

## Author

Created as a student project.  
Feel free to improve it (add file saving, better UI, etc.).
