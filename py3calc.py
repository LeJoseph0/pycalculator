while True:
    # input first number
    while True:
        try:
            first_number = float(input("enter first number: "))
            break
        except ValueError:
            print("invalid input, enter a numeric value")

    # input operation type
    operation = input("enter operation type: ")

    # input second number
    while True:
        try:
            second_number = float(input("enter second number: "))
            break
        except ValueError:
            print("invalid input, enter a numeric value")

    # print the result

    if operation == "+":
        print(first_number + second_number)
    elif operation == "-":
        print(first_number - second_number)
    elif operation == "/":
        print(first_number / second_number)
    elif operation == "*":
        print(first_number * second_number)
    else:
        print("error")

    repeat = input("do you want to preforme another operation? (y/n): ")
    if repeat == "n":
        break

print("calculator closed..")
