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
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0,
}

def check_resources(choose):
    for item in MENU[choose]['ingredients']:
        if MENU[choose]['ingredients'][item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


def process_coins():
    print("Please insert coins.")
    quarters = int(input("how many quarters?: "))
    dimes = int(input("how many dimes?: "))
    nickles = int(input("how many nickles?: "))
    pennies = int(input("how many pennies?: "))
    total = quarters * 0.25 + dimes * 0.1 + nickles * 0.05 + pennies * 0.01
    return total


def check_transaction_successful(total, choose):
    if total >= MENU[choose]['cost']:
        change = round(total - MENU[choose]['cost'], 2)
        print(f"Here is ${change} in change.")
        print(f"Here is your {choose} ☕️. Enjoy!")
        resources['money'] += MENU[choose]['cost']
        for item in MENU[choose]['ingredients']:
            resources[item] -= MENU[choose]['ingredients'][item]
    else:
        print("Sorry that's not enough money. Money refunded.")


while True:
    choose = input("What would you like? (espresso/latte/cappuccino): ")

    if choose == "off":
        break

    elif choose == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${resources['money']}")
           
    elif choose == "espresso" or choose == "latte" or choose == "cappuccino":
        if check_resources(choose):
            total = process_coins()
            check_transaction_successful(total, choose)
        else:
            print("Try another drink or come back later.")
    else:
        print("Invalid input")