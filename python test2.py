def add(num1,num2):
    return num1+num2

try:
    num1=int((input("Enter a number: ")))
    num2=int((input("Enter another number: ")))
    oper=(input("Enter the operation: "))
    result=num1+num2
    if oper=="+":
        print("The result is: ",result)
except ValueError:
    print("Invalid input")
add(num1,num2)

def sub(num1,num2):
    return num1-num2
try:
    num1=int((input("Enter a number: ")))
    num2=int((input("Enter another number: ")))
    oper=(input("Enter the operation: "))
    result=num1-num2
    if oper=="-":
        print("The result is: ",result)
except ValueError:
    print("Invaild Input")

def mul(num1,num2):
    return num1*num2
try:
    num1=int((input("Enter a number: ")))
    num2=int((input("Enter another number: ")))
    oper=(input("Enter the operation: "))
    result=num1*num2
    if oper=="*":
        print("The result is: ",result)
except ValueError:
    print("Invaild input")

def div(num1,num2):
    return num1/num2
try:
    num1=int((input("Enter a number: ")))
    num2=int((input("Enter another number: ")))
    oper=(input("Enter the operation: "))
    result=num1/num2
    if oper=="/":
        print("The result is: ",result)
except ValueError:
    print("Invalid input")
except ZeroDivisionError:
    print("This division is not possible")


   
    

