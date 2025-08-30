# Product Stock Checker

stock_units = int(input("Enter number of stock units available: "))

if stock_units >= 5:
    print("Available")
elif stock_units < 5 and stock_units > 0:
    print("Last few left!")
elif stock_units == 0:
    print("Out of stock")
else:
    print("Wrong Input")
