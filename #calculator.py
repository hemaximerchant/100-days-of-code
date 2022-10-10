#addition
def add(n1,n2):
    return n1 + n2

#subtraction
def subtract(n1,n2):
    return n1 - n2

#multiplication
def multiply(n1,n2):
    return n1 * n2

#division
def divide(n1,n2):
    return n1 / n2

#assigning dictionary
operations = {
    '+' : add,
    '-' : subtract,
    '*' : multiply,
    '/' : divide
}

n1 = int(input("Enter any number:"))
n2 = int(input("Enter any number:"))

#iterating through dictionary
for i in operations:
    print(i)

symbol = input("Pick an operation for the above line:")

answer = operations[symbol]
result = answer(n1,n2)
print(n1,symbol,n2,"=",result)
