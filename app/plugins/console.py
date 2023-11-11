from algorithms import caesar, vigenere, playfair, affine


def main_menu():
    print("\nMAIN MENU")
    print("1. Caesar Cipher\n2. Vigenere Cipher\n3. Playfair Cipher\n4. Affine Cipher\n5. Exit")
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


def show_matrix(matrix):
    for row in matrix:
        print(' '.join(row))


def playfair_handler(choice):
    if choice == "1":
        print("\nPlayfair Encryption")
        message = input("Enter the message: ")
        key = input("Enter the key: ")
        print("Matrix:")
        show_matrix(playfair.generate_matrix(key))
        print(f"Encrypted message: {playfair.encrypt(message, key)}")
    elif choice == "2":
        print("\nPlayfair Decryption")
        message = input("Enter the message: ")
        key = input("Enter the key: ")
        print("Matrix:")
        show_matrix(playfair.generate_matrix(key))
        print(f"Decrypted message: {playfair.decrypt(message, key)}")


def main_menu():
    print("\nMAIN MENU")
    print("1. Caesar Cipher\n2. Vigenere Cipher\n3. Playfair Cipher\n4. Affine Cipher\n5. Exit")
    return input("Enter your choice: ")


def affine_menu():
    print("\nAffine Cipher Menu")
    print("1. Encrypt\n2. Decrypt\n3. Return to main menu")
    return input("Enter your choice: ")


def affine_handler(choice):
    if choice == "1":
        print("\nAffine Encryption")
        message = input("Enter the message: ")
        a = int(input("Enter the value of a: "))
        b = int(input("Enter the value of b: "))
        print(f"Encrypted message: {affine.encrypt(message, (a, b))}")
    elif choice == "2":
        print("\nAffine Decryption")
        message = input("Enter the message: ")
        a = int(input("Enter the value of a: "))
        b = int(input("Enter the value of b: "))
        print(f"Decrypted message: {affine.decrypt(message, (a, b))}")


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
            while True:
                affine_choice = affine_menu()
                if affine_choice in ("1", "2"):
                    affine_handler(affine_choice)
                elif affine_choice == "3":
                    break
                else:
                    print("Invalid choice. Please try again.")
        elif choice == "5":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
