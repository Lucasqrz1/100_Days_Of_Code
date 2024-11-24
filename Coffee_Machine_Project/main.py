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
water_available = 100
milk_available = 200
coffee_available = 100
money = 0

#Print report
def report():
    print(f"Water: {water_available}ml")
    print(f"Milk: {milk_available}ml")
    print(f"Coffee: {coffee_available}g")
    print(f"Money: ${money}")
report()

#Ask customer for order
order = input("What would you like? (espresso/latte/cappuccino):")

#Check resources sufficient?

#Process coins

#Check transaction successful?

#Make the coffee/deduct the resources

