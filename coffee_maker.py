import random
from datetime import datetime
class CoffeeMaker:
    def __init__(self):
        self.resources = {
            "water": 3000,
            "milk": 2000,
            "coffee": 1000,
        }
        self.drink_preparation_times = {
            "Filter Coffee": 5,"Instant Coffee": 2,"Black Coffee": 3,"Tea": 3,"Ginger Tea": 4,"Lemon Tea": 4,"Black Tea": 3,"Plain Milk": 2,"Badam Milk": 5,"Turmeric Milk": 4,"Chocolate Milk": 3,"Coconut Milk": 4}
        self.order_number = 0
    def make_coffee(self, order, quantity):
        self.order_number += 1
        total_cost = order.cost * quantity
        prep_time = self.preparation_time(order.name)
        return total_cost, prep_time, self.order_number
    def preparation_time(self, drink_name):
        return self.drink_preparation_times.get(drink_name, "Unknown preparation time.")
    def generate_receipt(self, item_name, quantity, total_cost):
        transaction_id = random.randint(1000000000, 9999999999)
        order_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        receipt_message = (
            f"--- Receipt ---\n"
            f"Date & Time: {order_time}\n"
            f"Transaction ID: {transaction_id}\n"
            f"Item: {item_name}\n"
            f"Quantity: {quantity}\n"
            f"Total Cost: ₹{total_cost}\n"
            f"{'-' * 30}\n"
            f"Thank you for your purchase!"
        )
        print(receipt_message)