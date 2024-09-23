class ContactMaster:
    def __init__(self):

        self.contacts = {}

  
    def add_contact(self, person_name, phone_number):
        if person_name in self.contacts:
            print(f"Contact {person_name} already exists.")
        else:
            self.contacts[person_name] = phone_number
            print(f"Contact {person_name} added successfully.")

    # Method to delete a contact
    def delete_contact(self, person_name):
        if person_name in self.contacts:
            del self.contacts[person_name]
            print(f"Contact {person_name} deleted successfully.")
        else:
            print(f"Contact {person_name} not found.")

    # Method to search for a contact
    def find_contact(self, person_name):
        if person_name in self.contacts:
            print(f"Contact found: {person_name} - {self.contacts[person_name]}")
        else:
            print(f"Contact {person_name} not found.")

    # Method to display all contacts
    def show_contacts(self):
        if self.contacts:
            print("Contact List:")
            for name, phone in self.contacts.items():
                print(f"{name}: {phone}")
        else:
            print("No contacts available.")

# Main application loop
def main():
    cm = ContactMaster()
    
    while True:
        print("\n1. Add Contact")
        print("2. Delete Contact")
        print("3. Search Contact")
        print("4. Display Contacts")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter contact name: ")
            phone = input("Enter phone number: ")
            cm.add_contact(name, phone)
        
        elif choice == '2':
            name = input("Enter the name of the contact to delete: ")
            cm.delete_contact(name)

        elif choice == '3':
            name = input("Enter the name of the contact to search: ")
            cm.find_contact(name)

        elif choice == '4':
            cm.show_contacts()

        elif choice == '5':
            print("Exiting ContactMaster.")
            break

        else:
            print("Invalid option, please try again.")

if __name__ == "__main__":
    main()
