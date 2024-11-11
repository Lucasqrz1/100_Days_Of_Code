def add(n1, n2):
    return n1 + n2

# TODO 1: Write out the other 3 functions - subtract, multiply and divide

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

#TODO 2: Add these four functions into a dictionary as the values. Keys = "+", "-", "*", "/"

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

#TODO 3: Use the dictionary operations to perform the calculations. Multiply 4 * 8 using the dictionary.
# result = operations["*"](4,8)
# print(result)

n1 = int(input("What's the first number? "))
print("""
+
-
*
/""")
operator = input("Pick an operation: ")
# if operator != "+" or "-" or "*" or "/" :
#     print("Wrong input. Restart and choose an operator")

n2 = int(input("Choose the second number: "))
if operator == "+":
    print(add(n1, n2))
elif operator == "-":
    print(subtract(n1, n2))
elif operator == "*":
    print(multiply(n1, n2))
elif operator == "/":
    print(divide(n1, n2))
else:
    print("Wrong input. Restart and choose an operator from the list. ")
