names = []
numbers = []

# To add a new contact
def add_name(new_name):
    names.append(new_name)
    print(f"Name '{new_name}' successfully saved.")

# To add a new number
def add_number(add_number):
    numbers.append(add_number)
    print(f"Assigned number '{add_number}' successfully saved.")

# To delete an old contact
def delete_contact(name):
    if name in names:
        index = names.index(name)
        deleted_name = names.pop(index)
        deleted_number = numbers.pop(index)  # Remove both name and number
        print(f"Name '{deleted_name}' and Number '{deleted_number}' deleted.")
    else:
        print("Name not found in contact. Try again.")

# To update a contact
def update_contact():
    name = input("Enter the contact name you want to update: ")
    if name in names:
        index = names.index(name)  
        new_number = input(f"Enter the new number for '{name}': ")
        numbers[index] = new_number
        print(f"Contact for '{name}' updated successfully.")
    else:
        print(f"Contact for '{name}' not found.")

# To view contacts
def view_contact():
    if not names:
        print("No contacts available.")
    else:
        # Zip names and numbers, sort by names, then unzip them back
        sorted_contacts = sorted(zip(names, numbers), key=lambda contact: contact[0])
        sorted_names, sorted_numbers = zip(*sorted_contacts)

        # Display the sorted contacts
        for i, (name, number) in enumerate(zip(sorted_names, sorted_numbers)):
            print(f"{i + 1}. Name: {name} | Number: {number}")

# Main function to handle the contact operations
def contact_menu():
    while True:
        print("\nContact List Options Menu:")
        print("1. Add New Contact")
        print("2. Delete Contact")
        print("3. Update Contact")
        print("4. View All Contacts")
        print("5. Exit")

        user_choice = input("Select an option (1-5): ")

        if user_choice == '1':
            name_input = input("Enter the Name: ")
            number_input = input("Enter the Number: ")
            name_input = name_input.capitalize()  # Capitalize the name
            add_name(name_input)
            add_number(number_input)

        elif user_choice == '2':
            name = input("Enter the name to remove: ")  
            delete_contact(name)

        elif user_choice == '3':
            update_contact()

        elif user_choice == '4':
            view_contact()

        elif user_choice == '5':
            print("Exiting Contact Manager. Have a productive day!")
            break

        else:
            print("Invalid option. Please select from 1 to 5.")

# Entry point of the program
if __name__ == "__main__":
    contact_menu()
