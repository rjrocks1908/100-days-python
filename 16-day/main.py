from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

obj_menu = Menu()
obj_coffee_maker = CoffeeMaker()
obj_money_machine = MoneyMachine()


def make_coffee(drink):
    if obj_coffee_maker.is_resource_sufficient(drink):
        if obj_money_machine.make_payment(drink.cost):
            obj_coffee_maker.make_coffee(drink)


def machine():
    """Returns True if the machine is on, False otherwise"""
    action = input(f"What would you like? {obj_menu.get_items()}: ").lower()

    if action == "off":
        return False
    if action == "report":
        obj_coffee_maker.report()
        obj_money_machine.report()
    else:
        drink = obj_menu.find_drink(action)
        if drink:
            make_coffee(drink=drink)

    return True


while machine():
    pass
