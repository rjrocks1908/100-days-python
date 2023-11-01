import os

os.system("cls")

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    },
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0.0,
}

# Constants
ESPRESSO = "espresso"
LATTE = "latte"
CAPPUCCINO = "cappuccino"
WATER = "water"
MILK = "milk"
COFFEE = "coffee"
COST = "cost"
INGREDIENTS = "ingredients"
MONEY = "money"


def getReport():
    """Returns the report of the coffee machine"""
    return f"Water: {resources[WATER]}ml\nMilk: {resources[MILK]}ml\nCoffee: {resources[COFFEE]}g\nMoney: ${resources[MONEY]}"


def checkResources(coffeeType):
    """Returns True if there are enough resources to make the coffee, False otherwise"""
    availableWater = resources[WATER]
    if coffeeType != ESPRESSO:
        availableMilk = resources[MILK]
    availableCoffee = resources[COFFEE]

    requiredWater = MENU[coffeeType][INGREDIENTS][WATER]
    if coffeeType != ESPRESSO:
        requiredMilk = MENU[coffeeType][INGREDIENTS][MILK]
    requiredCoffee = MENU[coffeeType][INGREDIENTS][COFFEE]

    if availableWater < requiredWater:
        print("Sorry there is not enough water.")
        return False
    elif coffeeType != ESPRESSO and availableMilk < requiredMilk:
        print("Sorry there is not enough milk.")
        return False
    elif availableCoffee < requiredCoffee:
        print("Sorry there is not enough coffee.")
        return False

    return True


def makeCoffee(coffeeType):
    """Makes the coffee and it does not return anything"""
    if checkResources(coffeeType):
        print("Please insert coins.")
        quarters = int(input("How many quarters?: "))
        dimes = int(input("How many dimes?: "))
        nickles = int(input("How many nickles?: "))
        pennies = int(input("How many pennies?: "))
        total = quarters * 0.25 + dimes * 0.10 + nickles * 0.05 + pennies * 0.01

        if total < MENU[coffeeType][COST]:
            print("Sorry that's not enough money. Money refunded.")
        else:
            change = total - MENU[coffeeType][COST]
            print(f"Here is ${round(change, 2)} in change.")
            print(f"Here is your {coffeeType} ☕️. Enjoy!")
            resources[WATER] -= MENU[coffeeType][INGREDIENTS][WATER]
            if coffeeType != ESPRESSO:
                resources[MILK] -= MENU[coffeeType][INGREDIENTS][MILK]
            resources[COFFEE] -= MENU[coffeeType][INGREDIENTS][COFFEE]
            resources[MONEY] += MENU[coffeeType][COST]


def machine():
    """Returns True if the machine is on, False otherwise"""
    action = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if action == "report":
        print(getReport())
    elif action == ESPRESSO or action == LATTE or action == CAPPUCCINO:
        makeCoffee(action)
    elif action == "off":
        return False
    return True


while machine():
    pass
