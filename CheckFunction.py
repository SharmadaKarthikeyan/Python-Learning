def check_result(mark):
    if mark > 40:
        print("Pass")
    else:
        print("Fail")

mark = int(input("Enter mark: "))
check_result(mark)
