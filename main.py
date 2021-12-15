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
    "money": 50.00
}

print("Welcome to the Coffee Machine!")
power = True
order = ''
money = 0


def report():
    print("\nResources left:")
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"coffee: {resources['coffee']}ml")
    print(f"Money: ${resources['money']}")


def select_drink():
    global order
    order = input("\nWhat would you like? (espresso/latte/cappuccino) ")


def enter_coins():
    global money
    quarters = int(input("Please enter the amount of quarters you have: "))
    dimes = int(input("Please enter the amount of dimes you have: "))
    nickles = int(input("Please enter the amount of nickles you have: "))
    pennies = int(input("Please enter the amount of pennies you have: "))
    money = round((quarters*0.25)+(dimes*0.10)+(nickles*0.05)+(pennies*0.01), 2)


def check_money():
    global power
    while resources['money'] > money:
        if order == 'espresso':
            if float(money) >= MENU['espresso']['cost']:
                pass
            else:
                print(f"We're sorry, you don't have enough money to purchase an {order}.")
                power = False
        if order == 'latte':
            if float(money) >= MENU['latte']['cost']:
                pass
            else:
                print(f"We're sorry, you don't have enough money to purchase a {order}.")
                power = False
        if order == 'cappuccino':
            if float(money) >= MENU['cappuccino']['cost']:
                pass
            else:
                print(f"We're sorry, you don't have enough money to purchase a {order}.")
                power = False
        break
    else:
        print("We're sorry, the machine doesn't have enough money to provide change.")
        power = False


def check_ingredients():
    if order == 'espresso':
        if resources['water'] >= MENU['espresso']['ingredients']['water'] and\
                resources['coffee'] >= MENU['espresso']['ingredients']['coffee']:
            pass
        else:
            print("We're sorry, there's not enough ingredients.")
    elif order == 'latte':
        if resources['water'] >= MENU['latte']['ingredients']['water'] and\
                resources['coffee'] >= MENU['latte']['ingredients']['coffee'] and\
                resources['milk'] >= MENU['latte']['ingredients']['milk']:
            pass
        else:
            print("We're sorry, there's not enough ingredients.")
    elif order == 'cappuccino':
        if resources['water'] >= MENU['cappuccino']['ingredients']['water'] and\
                resources['coffee'] >= MENU['cappuccino']['ingredients']['coffee'] and\
                resources['milk'] >= MENU['cappuccino']['ingredients']['milk']:
            pass
        else:
            print("We're sorry, there's not enough ingredients.")
            report()


def make_coffee():
    select_drink()
    enter_coins()
    check_money()
    check_ingredients()
    while power:
        if order == 'espresso':
            resources['water'] = int(resources['water'] - MENU['espresso']['ingredients']['water'])
            resources['coffee'] = int(resources['coffee'] - MENU['espresso']['ingredients']['coffee'])
            resources['money'] = resources['money'] - MENU['espresso']['cost']
            change = round(money - MENU['espresso']['cost'], 2)
            print(f"\nPlease pick-up your {order.title()}!")
            print(f"Also don't forget to pick-up your change of ${change}")
            report()
        elif order == 'latte':
            resources['water'] = int(resources['water'] - MENU['latte']['ingredients']['water'])
            resources['coffee'] = int(resources['coffee'] - MENU['latte']['ingredients']['coffee'])
            resources['milk'] = int(resources['milk'] - MENU['latte']['ingredients']['milk'])
            resources['money'] = resources['money'] - MENU['latte']['cost']
            change = round(money - MENU['latte']['cost'], 2)
            print(f"\nPlease pick-up your {order.title()}!")
            print(f"Also don't forget to pick-up your change of ${change}")
            report()
        elif order == 'cappuccino':
            resources['water'] = int(resources['water'] - MENU['cappuccino']['ingredients']['water'])
            resources['coffee'] = int(resources['coffee'] - MENU['cappuccino']['ingredients']['coffee'])
            resources['milk'] = int(resources['milk'] - MENU['cappuccino']['ingredients']['milk'])
            resources['money'] = resources['money'] - MENU['cappuccino']['cost']
            change = round(money - MENU['cappuccino']['cost'], 2)
            print(f"\nPlease pick-up your {order.title()}!")
            print(f"Also don't forget to pick-up your change of ${change}")
            report()
        break
    else:
        pass


make_coffee()
