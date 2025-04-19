# Unlimited Arguments

def add(*args):
    sum = 0
    for n in args:
        print(n)
        sum+= n
    return sum

print(add(3,5,6))

# Unlimited keyword arguments
def calculate(n, **kwargs):
    print(kwargs)
    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)
    #     n += kwargs["add"]
    #     n *= kwargs["multiply"]
    #     print(n)

# print(kwargs["add"])

# calculate(add=3, multiply=5)

# Creating a class with keyword arguments
class Car:

    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.colour = kw.get("colour")
        self.seats = kw.get("seats")

my_car = Car(make="Honda", model="Fit", colour="Silver", seats="Five")
print(my_car.model)