from data import MENU, resources
earnings = 0
ingredients = ["water", "milk", "coffee"]
on = True


def ingredients_checker(flavour):
    for i in range(3):
        if flavour['ingredients'][ingredients[i]] > resources[ingredients[i]]:
            print(f"Sorry there is not enough {ingredients[i]}.")
            return False
        else:
            return True


def payment(price):
    print(f"Payable amount: ${price}")
    quarter = int(input("How many quarters: "))
    dime = int(input("How many dimes: "))
    nickel = int(input("How many nickels: "))
    penni = int(input("How many pennies: "))

    total = quarter*0.25 + dime*0.10 + nickel*0.05 + penni*0.01

    if total < price:
        print("Insufficient money.Amount refunded ")
        return False
    else:
        change = round(total - price, 2)
        print(f"Payment successful.${change} change refunded.")
        return True


def deduct_resources(flavour):
    for i in range(3):
        resources[ingredients[i]] = resources[ingredients[i]] - flavour['ingredients'][ingredients[i]]


while on:
    choice = input("What would you like? (espresso/latte/cappuccino): ")

    if choice == "report":
        print(f"\nwater = {resources['water']}ml\nmilk = {resources['milk']}ml\ncoffee = {resources['coffee']}g")
        print(f"earnings = ${earnings}\n")
    elif choice == "off":
        print("Machine turned off.")
        on = False
    elif choice in MENU:
        drink = MENU[choice]
        cost = drink["cost"]
        if ingredients_checker(drink):
            if payment(cost):
                earnings += cost
                deduct_resources(drink)
                print("Your Coffee is ready.")
                print(" ")
