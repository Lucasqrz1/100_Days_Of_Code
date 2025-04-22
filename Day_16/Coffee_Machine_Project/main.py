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
}
profit = 0

#Print report
def report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${profit}")


#Check resources sufficient?
def check_resources(order):
    for item in MENU[order]["ingredients"]:
        if resources[item] < MENU[order]["ingredients"][item]:
                print(f"Sorry, there is not enough {item}.")
                return False
    return True

#Process coins
def process_coins():
    print("Please insert coins.")
    quarters = int(input("How many quarters? :")) * 0.25
    dimes = int(input("How many dimes?: ")) * 0.10
    nickles = int(input("how many nickles?: ")) * 0.05
    pennies = int(input("How many pennies?: ")) * 0.01
    total = quarters + dimes + nickles + pennies
    return total


#Check transaction successful?
def transaction_successful(money_received, drink_cost):
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        global profit
        profit += drink_cost
        if change == 0:
            print("No change needed.")
        else:
            print(f"Here is your change: ${change}. Thanks for coming!")
        return True
    else:
        print("Sorry. You don't have enough money.")
        return False

#Deduct the resources
def deduct_resources(order):
    for item in MENU[order]['ingredients']:
        resources[item] -= MENU[order]['ingredients'][item]



#Make the coffee
def make_coffee(order):
    deduct_resources(order)
    print(f"Here's your {order}. Have a good day! ")


#Main loop
should_continue = True
while should_continue:
    order = str(input("What would you like? (espresso/latte/cappuccino):")).lower()
    if order == "report":
        report()
    elif order == "off":
        should_continue = False
    else:
        if order in MENU:
            if check_resources(order):
                payment = process_coins()
                if transaction_successful(payment, MENU[order]['cost']):
                    make_coffee(order)
        else:
            print("Sorry, we don't have that option.")
