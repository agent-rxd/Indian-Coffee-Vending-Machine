from menu import Menu
from money_machine import MoneyMachine
from coffee_maker import CoffeeMaker
money_machine = MoneyMachine()
menu = Menu()
coffee_maker = CoffeeMaker()
is_on = True
coffee_maker.order_history = []
while is_on:
    main_options = menu.get_items()
    choice = input(f"What would you like to have? ({main_options}): ").strip().lower()
    if choice == "off":
        is_on = False
    elif choice == "report":
        money_machine.report()
    elif choice == "admin":
        if money_machine.admin_login():
            admin_menu_on = True
            while admin_menu_on:
                print("\n1. View Cash Collected")
                print("2. Transfer Money")
                print("3. View Order History")
                print("4. View Withdrawal History")
                print("5. Return to Main Menu")
                admin_choice = input("Select an option (1/2/3/4/5): ").strip()
                if admin_choice == "1":
                    money_machine.view_cash_collected()
                elif admin_choice == "2":
                    amount = float(input("Enter amount to transfer: "))
                    upi_id = input("Enter UPI ID for transfer: ")
                    money_machine.transfer_money(amount, upi_id)
                elif admin_choice == "3":
                    if coffee_maker.order_history:
                        print("Order History:")
                        for order in coffee_maker.order_history:
                            print(order)
                    else:
                        print("No orders have been placed yet.")
                elif admin_choice == "4":
                    money_machine.view_withdrawal_history()
                elif admin_choice == "5":
                    admin_menu_on = False
                else:
                    print("Invalid option. Please select again.")
    else:
        sub_items = menu.get_sub_items(choice)
        if sub_items:
            print(f"Available options for {choice.capitalize()}:")
            for item in sub_items:
                print(f"- {item}")
            drink_choice = input(f"Which {choice} would you like? ").strip()
            selected_drink = menu.find_drink(choice, drink_choice)
            if selected_drink:
                quantity = int(input("How many would you like to order? "))
                total_cost, prep_time, order_number = coffee_maker.make_coffee(selected_drink, quantity)
                print(f"Estimated preparation time: {prep_time} minutes.")
                if money_machine.make_payment(total_cost):
                    coffee_maker.order_history.append((selected_drink.name, quantity, total_cost))
                    receipt_request = input("Would you like a printed receipt? (yes/no): ").strip().lower()
                    if receipt_request == 'yes':
                        coffee_maker.generate_receipt(selected_drink.name, quantity, total_cost)
                    print(f"Order Place ! Your Order Number is {order_number} ")
                    print(f"Collect your {quantity} cups of {selected_drink.name} after {prep_time} minutes.")
            else:
                print("Sorry, that item is not available.")
        else:
            print("Sorry, that item is not available.")