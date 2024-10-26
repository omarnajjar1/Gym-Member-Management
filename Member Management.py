import os
import time


def clear_terminal():
    os.system("cls" if os.name == "nt" else "clear")


class Member():
    def __init__(self, first_name, last_name, membership_id, membership_status = "inactive"):
        self.first_name = first_name
        self.last_name = last_name
        self.membership_id = membership_id
        self.membership_status = membership_status

    def display_members(self):
        clear_terminal()
        print ("Displaying all members ...."), time.sleep(1)
        print (f"First Name: {self.first_name}")
        print (f"Last Name: {self.last_name}")
        print (f"Membership ID: {self.membership_id}")
        print (f"Membership status: {self.membership_status}")
        print ('_' * 20)


def create_member():
    first_name = input ("Enter first name: ").capitalize()
    last_name = input ("Enter last name: ").capitalize()
    membership_id = input ("Enter membership ID: ").zfill(3)
    membership_status = input ("Enter membership status, or click enter: ").lower()
    if not membership_status:
       membership_status = "inactive"
    return Member(first_name, last_name, membership_id, membership_status)


def search_member():
    clear_terminal()
    print("\nSearch by: \n") 
    print("1. Membership ID")  
    print("2. First name")
    print("3. Membership status")

    search_choice = input("Enter you choice: ").strip()

    found_members = []

    if search_choice == "1":
        search_id = input("Entre the membership ID to search: ").zfill(3)
        for x in members:
            if x.membership_id == search_id:
                found_members.append(x)
                break
    elif search_choice == "2":
        first_name = input("Enter the first name to search: ").capitalize()
        for x in members:
            if x.first_name == first_name:
                found_members.append(x)
    elif search_choice == "3":
            membership_status = input("Enter the membership status to search (active/inactive): ").lower()
            for x in members:
               if x.membership_status == membership_status:
                  found_members.append(x)
    else:
        print("Invalid choice")
        time.sleep(2)

    if found_members:
        clear_terminal()
        print("Members found: ")
        for x in found_members:
          x.display_members()
          time.sleep(5)
    else:
        print("Membmer not found!")
        time.sleep(2)

              
members = []
while True:
    clear_terminal()
    print("\nWelcome to Gym Membership Management \n")
    print("\nChoose an Action \n ")
    print("1. Add new member")
    print("2. Display all members ")
    print("3. Search for a member")
    print("4. Exit \n")

    choice = input("Enter you choice: ").strip()

    if choice == "1":
        members.append(create_member())
        print("Member added successfully!")
        time.sleep(3)

    elif choice == "2":
        clear_terminal()
        if members:
           for key in members:
               key.display_members()
           time.sleep(5)
        else:
           print ("No member to display")
           time.sleep(2)

    elif choice == "3":
        if members:
           search_member()
        else:
           print("There aren't members to display!")
           time.sleep(2)

    elif choice == "4":
        quit()

    else:
        print ("Invalid choice.")
        time.sleep(2)
