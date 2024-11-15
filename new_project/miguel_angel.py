my_contacts = {
    "mom": 987654321,
    "dad": 123456789
}

def menu():
    print("1. Search a contact")
    print("2. Add a new contact")
    print("3. Update an existent contact")
    print("4. Delete a contact")
    print("5. Quit")

def start():
    print("What would you like with your agenda?")
    menu()
    option = int(input())
    if option == 1:
        search_contact()
    elif option == 2:
        add_contact()
    elif option == 3:
        update_contact()
    elif option == 4:
        delete_contact()
    elif option == 5:
        exit()
    else:
        print("The option you introduced doesn't exist!")
        start()

def search_contact():
    print("Introduce the contact you want to search \n")
    searched_name = input()
    try:
        print(my_contacts[searched_name])
    except KeyError:
        print("The name hasn't been found in your agenda! \n")
    start()

def add_contact():
    added_name = input("Introduce the name of your new contact \n" )
    try:
        added_phone = int(input("Introduce the number of your new contact \n"))
    except ValueError:
        print("The phone number must be numbers! Try again.")
        add_contact()
    else:
        while len(str(added_phone))>11 or len(str(added_phone))<9:
            added_phone = input("Number incorrect, try to type it correctly again!")
        my_contacts[added_name] = added_phone
        print("The contact has been saved")
        start()

def update_contact():
    searched_name = input("Introduce the name of the contact you wish to update \n")
    try:
        print(my_contacts[searched_name])
    except KeyError:
        print("The contact hasn't been found!")
        update_contact()
    else:
        try:
            new_phone = int(input("Type the new phone number for the contact \n"))
        except ValueError:
            print("The phone number must be numbers! Please type it correctly \n")
            update_contact()
        while len(str(new_phone))>11 or len(str(new_phone))<9:
            new_phone = input("Number incorrect, try to type it correctly again! \n")
        my_contacts.update({searched_name:new_phone})
        print("The contact has been updated \n")


    start()

def delete_contact():
    deleted_contact = input("Introduce the name of the contact you want to delete \n")
    try:
        del my_contacts[deleted_contact]
    except KeyError:
        print("The contact doesn't exist! \n")
        start()
    else:
        print("The contact has been deleted \n")
    start()

if __name__ == "__main__":
    start()