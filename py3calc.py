while True:  
  # input first number
  
  first_number = float(input("enter first number: "))
  
  # input operation type
  operation = input("enter operation type: ")
  
  # input second number
  second_number = float(input("enter second number: "))
  
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

