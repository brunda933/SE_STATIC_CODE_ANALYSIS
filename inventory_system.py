"""
Inventory System Module
------------------------
This module manages an inventory of items — allowing users to add, remove,
save, load, and display items with quantity tracking. It also checks for
low-stock items and performs basic input validation.
"""

import json
from datetime import datetime

# Global inventory dictionary
stock_data = {}


def add_item(item="default", qty=0, logs=None):
    """Add a new item and quantity to the inventory."""
    if logs is None:
        logs = []
    if not item:
        return
    if not isinstance(item, str) or not isinstance(qty, (int, float)):
        print("Invalid input types. 'item' must be string, 'qty' must be number.")
        return
    stock_data[item] = stock_data.get(item, 0) + qty
    logs.append(f"{datetime.now()}: Added {qty} of {item}")


def remove_item(item, qty):
    """Remove the specified quantity of an item from the inventory."""
    try:
        stock_data[item] -= qty
        if stock_data[item] <= 0:
            del stock_data[item]
    except KeyError:
        print(f"Item '{item}' not found in stock.")
    except TypeError:
        print("Invalid quantity type; must be numeric.")


def get_qty(item):
    """Return the available quantity for a specific item."""
    return stock_data.get(item, 0)


def load_data(file_name="inventory.json"):
    """Load inventory data from a JSON file."""
    try:
        with open(file_name, "r", encoding="utf-8") as file:
            data = json.load(file)
            stock_data.clear()
            stock_data.update(data)
    except FileNotFoundError:
        print("Inventory file not found; starting with empty stock.")
    except json.JSONDecodeError:
        print("Error reading inventory file; using empty stock.")


def save_data(file_name="inventory.json"):
    """Save current inventory data into a JSON file."""
    with open(file_name, "w", encoding="utf-8") as file:
        json.dump(stock_data, file, indent=4)


def print_data():
    """Display all items and their current quantities."""
    print("\nItems Report")
    for item, qty in stock_data.items():
        print(f"{item} -> {qty}")


def check_low_items(threshold=5):
    """Return a list of items with quantity below the given threshold."""
    return [item for item, qty in stock_data.items() if qty < threshold]


def main():
    """Main function to demonstrate inventory operations."""
    add_item("apple", 10)
    add_item("banana", 2)
    add_item("orange", 0)
    remove_item("apple", 3)
    remove_item("mango", 1)
    print(f"Apple stock: {get_qty('apple')}")
    print(f"Low items: {check_low_items()}")
    save_data()
    load_data()
    print_data()


if __name__ == "_main_":
    main()
