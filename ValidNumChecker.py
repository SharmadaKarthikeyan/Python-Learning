try:
    num = int(input("Enter a number: "))
except ValueError:
    print("Invalid Input")
else:
    print("Valid Number:", num)
    