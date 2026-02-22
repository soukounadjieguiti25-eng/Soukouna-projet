number1 = float(input("Enter first number: "))
number2 = float(input("Enter second number: "))

if number1 > number2:
    print("Largest number is:", number1)
elif number2 > number1:
    print("Largest number is:", number2)
else:
    print("Both numbers are equal")