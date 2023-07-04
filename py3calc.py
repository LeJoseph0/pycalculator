while True:
    # input first number
    while True:
        try:
            first_number = float(input("enter first number: "))
            break
        except ValueError:
            print("invalid input, enter a numeric value")

    # input operation type
    while True:
      try:
        operation = input("enter operation type: ")
        if operation in ("+", "-", "/", "*"):
          break
        else:
          raise ValueError
      except ValueError:
          print("invalid operator, please use +,-,/,*")

    # input second number
    while True:
        try:
            second_number = float(input("enter second number: "))
            break
        except ValueError:
            print("invalid input, enter a numeric value")

    # print the result

    if operation == "+":
        result = first_number + second_number
    elif operation == "-":
        result = first_number - second_number
    elif operation == "/":
        result = first_number / second_number
    elif operation == "*":
        result = first_number * second_number
    else:
        result = None

    if result != None:
        print("result is:", result)
    else:
        print("unexpected error.")

    repeat = input("do you want to preforme another operation? (y/n): ")
    if repeat == "n":
        break

print("calculator closed..")
