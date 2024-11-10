import random
from datetime import datetime
class MoneyMachine:
    CURRENCY = "₹"
    def __init__(self):
        self.profit = 0
        self.withdrawal_history = []
        self.admin_username = "admin"
        self.admin_password = "password123"
    def display_box_message(self, message):
        box_width = len(message.splitlines()[0]) + 4
        print("+" + "-" * (box_width - 2) + "+")
        for line in message.splitlines():
            print(f"| {line:<{box_width - 4}} |")
        print("+" + "-" * (box_width - 2) + "+")
    def process_upi_payment(self, cost):
        print(f"Please make the payment of {self.CURRENCY}{cost} through UPI.")
        inc_upi = random.randint(1000000000, 9999999999)
        print(f"Our UPI ID : {inc_upi}")
        done = input("Enter 'done' once payment is completed: ").strip().lower()
        if done == "done":
            return True
        else:
            print("Payment not completed. Returning to the main menu.")
            return False
    def make_payment(self, cost):
        if not self.process_upi_payment(cost):
            return False
        payment_message = f"Payment of {self.CURRENCY}{cost} received.\nPayment successful via UPI."
        self.display_box_message(payment_message)
        self.profit += cost
        return True
    def admin_login(self):
        username = input("Enter admin username: ")
        password = input("Enter admin password: ")
        if username == self.admin_username and password == self.admin_password:
            print("Login successful.")
            return True
        else:
            print("Invalid credentials.")
            return False
    def transfer_money(self, amount, upi_id):
        if amount <= self.profit:
            self.profit -= amount
            transaction_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            self.withdrawal_history.append((transaction_time, amount, upi_id))
            print(f"Successfully transferred {self.CURRENCY}{amount} to UPI ID {upi_id}.")
            return True
        else:
            print("Insufficient funds for transfer.")
            return False
    def view_withdrawal_history(self):
        if not self.withdrawal_history:
            print("No withdrawals have been made yet.")
            return
        print("Withdrawal History:")
        for transaction in self.withdrawal_history:
            print(f"Date & Time: {transaction[0]}, Amount: {self.CURRENCY}{transaction[1]}, UPI ID: {transaction[2]}")