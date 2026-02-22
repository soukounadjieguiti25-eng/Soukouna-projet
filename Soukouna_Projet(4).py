price = float(input("Enter item price: "))

if price >= 100000:
    discount = price * 0.10
else:
    discount = 0

total_payment = price - discount

print("Total payment =", total_payment)