#Calculator
choice=0
while choice!=5:
    print("Simple Calculator: ")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5 Exit")
    choice=int(input("Enter your choice: "))
    if choice==5:
        print("Exiting calculator")
        break
    elif choice==1:
         num1=float(input("Enter first number: "))
         num2= float(input("Enter second number: "))
         print("Addition is: ",num1+num2)
    elif choice==2:
        num1=float(input("Enter first number: "))
        num2= float(input("Enter second number: "))
        print("Subtraction is : ",num1-num2)
    elif choice==3:
        num1=float(input("Enter first number: "))
        num2= float(input("Enter second number: "))
        print("Multiplication is: ",num1*num2)
    elif choice==4:
        num1=float(input("Enter first number: "))
        num2= float(input("Enter second number: "))
        print("Division is: ",num1/num2)
    else:
        print("Invalid choice, please enter number between 1 and 5")
