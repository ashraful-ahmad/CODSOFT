import random 
list = ["Rock" , "Paper" , "Scissors"]

#for rock
def rock():      
    x = random.choice(list)
    print (x)
    if x == "Scissors" :
        print ("Hurrah! You Win")
    elif x=="Rock":
        print("Its a Draw")    
    else :
        print("Oops! you Loosse")    


#for paper
def paper(): 
    y = random.choice(list)
    print (y)
    if y == "Rock" :
        print ("Hurrah! You Win")
    elif y=="Paper":
        print("Its a Draw")     
    else :
        print ("Oops! you Loosse")

#for scissors
def scissors(): 
    z = random.choice(list)
    print (z)
    if z == "Paper" :
        print ("Hurrah! You Win")
    elif z=="Scissors":
        print("Its a Draw") 
    else :
        print ("Oops! you Loosse")    

#main function
def main():
    while True:
        print("\nGame Options Menu :")
        print("1. Rock")
        print("2. Paper")
        print("3. Scissors")
        print("4. Exit")

        user_choice = input("Select an option (1-4): ")

        if user_choice == '1':
            rock()
            choice_2 = input("Want to Play Again (yes/no): ")
            if choice_2 == "yes":
                continue 
            elif choice_2=="no":
                break
            else :
                print ("Invalid Option Play Again!") 

        elif user_choice == '2':
            paper() 
            choice_2 = input("Want to Play Again (yes/no): ")
            if choice_2 == "yes":
                continue 
            elif choice_2=="no":
                break
            else :
                print ("Invalid Option Play Again!") 

        elif user_choice == '3':
            scissors()
            choice_2 = input("Want to Play Again (yes/no): ")
            if choice_2 == "yes":
                continue 
            elif choice_2=="no":
                break
            else :
                print ("Invalid Option. Play Again!") 

        elif user_choice == '4':
            print("Thank you For Playing.")
            break
        else:
            print ("Invalid Option Try Again!") 

# Entry point of the program
if __name__ == "__main__":
    main()                 
