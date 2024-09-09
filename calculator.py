#functions for addition
def add(a,b):   
    sum = a + b
    print ("The sum of ", a , " and ", b , " is ", sum)

#functions for subtraction
def subtraction(a,b):
    sub= a - b
    print ("The subtraction of ",a, " and ",b, " is ",sub)

#functions for multiplication
def multiplication(a,b):
    multi= a * b
    print ("The multiplication of ",a," and ",b, "is ", multi)

#functions for division
def division(a,b):
    div= a / b   
    print ("The division of ",a, " and ",b, "is ", div)

#main  function
def main():
     while True:
        print("\nSelect Calculator Operations :")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")   
        print("5. Exit") 

        user_choice = input("Select an option (1-5): ")

        if user_choice == '1':
            num1 = int(input("Enter the 1st Number : "))
            num2 = int(input("Enter the 2nd Number : "))
            add(num1,num2)
        
        elif user_choice == '2':
            num1 = int(input("Enter the 1st Number : "))
            num2 = int(input("Enter the 2nd Number : "))
            subtraction(num1,num2)

        elif user_choice == '3':
            num1 = int(input("Enter the 1st Number : "))
            num2 = int(input("Enter the 2nd Number : "))
            multiplication(num1,num2)

        elif user_choice == '4':
            num1 = int(input("Enter the 1st Number : "))
            num2 = int(input("Enter the 2nd Number : "))
            division(num1,num2)

        elif user_choice == '5':
            print("Exiting the Calculator. Have a productive day!")
            break

        else:
            print("Invalid option. Please select from 1 to 5.")

# Entry point of the program
if __name__ == "__main__":
    main()            
