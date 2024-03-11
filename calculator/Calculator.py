# 1.add
# 2.subtract
# 3.multifly
# 4.divide

print("select an operation to perform:")
print("1.Add")
print("2.subtract")
print("3.multifly")
print("4.divide")

operation = input();
if operation == "1": #adding
    num1 = input("Enter first number: ")
    num2 = input("Enter second number: ")
    print("the sum is :" + str(int(num1) + int(num2)))
elif operation == "2": #subtract
    num1 = input("Enter first number: ")
    num2 = input("Enter second number: ")
    print("the subtract is :" + str(int(num1) - int(num2)))
elif operation == "3": #multifly
    num1 = input("Enter first number: ")
    num2 = input("Enter second number: ")
    print("the product is :" +str(int(num1) * int(num2)))
elif operation == "4": ##divide
    num1 = input("Enter first number: ")
    num2 = input("Enter second number: ")
    print("the division is :" + str(int(num1) / int(num2)))
else:
   print("Invalid Entry")


