class MenuItem:
    def __init__(self, name, cost):
        self.name = name
        self.cost = cost
class Menu:
    def __init__(self):
        self.menu = {
            "coffee": [
                MenuItem(name="Filter Coffee", cost=30),
                MenuItem(name="Instant Coffee", cost=25),
                MenuItem(name="Black Coffee", cost=20),
            ],
            "tea": [
                MenuItem(name="Tea", cost=20),
                MenuItem(name="Ginger Tea", cost=25),
                MenuItem(name="Lemon Tea", cost=23),
                MenuItem(name="Black Tea", cost=18),
            ],
            "milk": [
                MenuItem(name="Plain Milk", cost=15),
                MenuItem(name="Badam Milk", cost=18),
                MenuItem(name="Turmeric Milk", cost=18),
                MenuItem(name="Chocolate Milk", cost=20),
                MenuItem(name="Coconut Milk", cost=22),
            ]
        }
    def get_items(self):
        return "/".join(self.menu.keys())
    def get_sub_items(self, category):
        if category in self.menu:
            return [item.name for item in self.menu[category]]
        else:
            return []
    def find_drink(self, category, order_name):
        if category in self.menu:
            for item in self.menu[category]:
                if item.name.lower() == order_name.lower():
                    return item
        print("Sorry that item is not available.")
        return None