from re import search

my_contacts = {
    "mom": 987654321
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
    print("Introduce the contact you want to search")
    searched_name = input()
    try:
        print(my_contacts[searched_name])
    except:
        print("The name hasn't been found in your agenda!")
    start()

def add_contact():
    added_name = input("introduce the name of your new contact")
    added_phone = input("Introduce the number of your new contact")
    while len(added_phone)>11 or len(added_phone)<9:
        added_phone = input("Number incorrect, try to type it correctly again!")
    my_contacts[added_name] = added_phone
    start()

def update_contact():
    searched_name = input("Introduce the name of the contact you wish to update")
    try:
        print(my_contacts[searched_name])
    except:
        print("The contact hasn't been found!")
    else:
        new_phone = input("Type the new phone number for the contact")
        my_contacts.update({searched_name:new_phone})
    start()

def delete_contact():
    deleted_contact = input("Introduce the name of the contact you want to delete")
    try:
        del my_contacts[deleted_contact]
    except:
        print("The contact doesn't exist!")
    else:
        print("The contact has been deleted")
    start()

if __name__ == "__main__":
    start()