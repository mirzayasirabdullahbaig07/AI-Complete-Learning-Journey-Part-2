# Contact Book Application using Classes and OOP in Python

# Define the Contact class which holds individual contact information
class Contact:
    def __init__(self, name, phone, email, address):
        # Constructor to initialize contact attributes
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

    def __str__(self):
        # Format how the contact details will be displayed when printed
        return f"Name: {self.name}\nPhone: {self.phone}\nEmail: {self.email}\nAddress: {self.address}\n"


# Define the ContactBook class that manages multiple contacts
class ContactBook:
    def __init__(self):
        # Constructor initializes an empty list to store contacts
        self.contacts = []

    def add_contact(self, contact):
        # Add a new contact to the list
        self.contacts.append(contact)
        print(f"Contact {contact.name} added.")

    def view_contact(self, name):
        # Search and display details of a contact by name
        for contact in self.contacts:
            if contact.name == name:
                print(contact)
                return
        print(f"Contact {name} not found.")

    def delete_contact(self, name):
        # Delete a contact from the list by name
        for contact in self.contacts:
            if contact.name == name:
                self.contacts.remove(contact)
                print(f"Contact {name} deleted.")
                return
        print(f"Contact {name} not found.")

    def list_contacts(self):
        # Display all contact names in the contact book
        if not self.contacts:
            print("No contacts found.")
            return
        for contact in self.contacts:
            print(f"Name: {contact.name}")

    def update_contact(self, name, new_phone=None, new_email=None, new_address=None):
        # Update contact details if the contact name matches
        for contact in self.contacts:
            if contact.name == name:
                if new_phone:
                    contact.phone = new_phone
                if new_email:
                    contact.email = new_email
                if new_address:
                    contact.address = new_address
                print(f"Contact {name} updated.")
                return
        print(f"Contact {name} not found.")


# Main function to run the contact book menu
def main():
    # Create an instance of ContactBook
    contact_book = ContactBook()

    # Start an infinite loop to keep the menu running
    while True:
        # Display menu options
        print("\nContact Book Menu:")
        print("1. Add Contact")
        print("2. View Contact")
        print("3. Delete Contact")
        print("4. List Contacts")
        print("5. Update Contact")
        print("6. Exit")

        # Get user input
        choice = input("Enter your choice: ")

        # Based on user choice, call appropriate method
        if choice == '1':
            # Add new contact
            name = input("Enter name: ")
            phone = input("Enter phone: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            contact = Contact(name, phone, email, address)
            contact_book.add_contact(contact)

        elif choice == '2':
            # View contact details
            name = input("Enter name to view: ")
            contact_book.view_contact(name)

        elif choice == '3':
            # Delete a contact
            name = input("Enter name to delete: ")
            contact_book.delete_contact(name)

        elif choice == '4':
            # List all contacts
            contact_book.list_contacts()

        elif choice == '5':
            # Update contact information
            name = input("Enter name to update: ")
            new_phone = input("Enter new phone (leave blank to skip): ")
            new_email = input("Enter new email (leave blank to skip): ")
            new_address = input("Enter new address (leave blank to skip): ")
            contact_book.update_contact(name, new_phone, new_email, new_address)

        elif choice == '6':
            # Exit the program
            break

        else:
            # Handle invalid menu input
            print("Invalid choice. Try again.")


# Ensure this runs only if the script is executed directly (not imported)
if __name__ == "__main__":
    main()
