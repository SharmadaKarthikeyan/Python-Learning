try:
    a = int(input("Enter a number: "))
    b = int(input("Enter b number: "))
    print(a/b)
except ValueError:
    print("Enter numbers only")
except ZeroDivisionError:
    print("Cannot Divide by Zero")
    