while True:
 try:
    num1, num2 = map(float, input("enter 2 numbers: ").split())
    operation = input("press +, -, *, /, %")
    if(operation == "+"):
        result = num1 + num2
    elif(operation == "-"):
        result = num1 - num2
    elif(operation == "*"):
            result = num1 * num2
    elif(operation == "/"):
          if num2==0:
              print("Cannot divided by 0")
                    
          else:
            result = num1 / num2
    elif(operation == "%"):
            result = num1 % num2
    else:
            print("Invalid operation")
            continue

    print("Result =", result)
    break
   
    
 except ValueError:
    print("Invalid input. Enter a number ")