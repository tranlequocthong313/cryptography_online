from algorithms import caesar
from algorithms import vigenere
from algorithms import playfair


def main_menu():
    print("\nMAIN MENU")
    print("1. Caesar Cipher\n2. Vigenere Cipher\n3. Playfair Cipher\n4. Exit")
    return input("Enter your choice: ")


def caesar_menu():
    print("\nCaesar Cipher Menu")
    print("1. Encrypt\n2. Decrypt\n3. Return to main menu")
    return input("Enter your choice: ")


def vigenere_menu():
    print("\nVigenere Cipher Menu")
    print("1. Encrypt\n2. Decrypt\n3. Return to main menu")
    return input("Enter your choice: ")


def playfair_menu():
    print("\nPlayfair Cipher Menu")
    print("1. Encrypt\n2. Decrypt\n3. Return to main menu")
    return input("Enter your choice: ")


def caesar_handler(choice):
    if choice == "1":
        print("\nCaesar Encryption")
        message = input("Enter the message: ")
        key = int(input("Enter the key: "))
        print(f"Encrypted message: {caesar.encrypt(message, key)}")
    elif choice == "2":
        print("\nCaesar Decryption")
        message = input("Enter the message: ")
        key = int(input("Enter the key: "))
        print(f"Decrypted message: {caesar.decrypt(message, key)}")


def vigenere_handler(choice):
    if choice == "1":
        print("\nVigenere Encryption")
        message = input("Enter the message: ")
        key = input("Enter the key: ")
        print(f"Encrypted message: {vigenere.encrypt(message, key)}")
    elif choice == "2":
        print("\nVigenere Decryption")
        message = input("Enter the message: ")
        key = input("Enter the key: ")
        print(f"Decrypted message: {vigenere.decrypt(message, key)}")


def playfair_handler(choice):
    if choice == "1":
        print("\nPlayfair Encryption")
        message = input("Enter the message: ")
        key = input("Enter the key: ")
        print(f"Encrypted message: {playfair.encrypt(message, key)}")
    elif choice == "2":
        print("\nPlayfair Decryption")
        message = input("Enter the message: ")
        key = input("Enter the key: ")
        print(f"Decrypted message: {playfair.decrypt(message, key)}")


def main():
    while True:
        choice = main_menu()
        if choice == "1":
            while True:
                caesar_choice = caesar_menu()
                if caesar_choice in ("1", "2"):
                    caesar_handler(caesar_choice)
                elif caesar_choice == "3":
                    break
                else:
                    print("Invalid choice. Please try again.")
        elif choice == "2":
            while True:
                vigenere_choice = vigenere_menu()
                if vigenere_choice in ("1", "2"):
                    vigenere_handler(vigenere_choice)
                elif vigenere_choice == "3":
                    break
                else:
                    print("Invalid choice. Please try again.")
        elif choice == "3":
            while True:
                playfair_choice = playfair_menu()
                if playfair_choice in ("1", "2"):
                    playfair_handler(playfair_choice)
                elif playfair_choice == "3":
                    break
                else:
                    print("Invalid choice. Please try again.")
        elif choice == "4":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
