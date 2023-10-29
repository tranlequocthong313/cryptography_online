def encrypt(message, key):
    message = message.upper()
    key = str(key)
    key = key.upper()
    encrypted_message = ''

    for i, char in enumerate(message):
        shifted_char = chr((((ord(char) - 65) + (ord(key[i % len(key)]) - 65)) % 26) + 65)
        encrypted_message += shifted_char

    return encrypted_message


def decrypt(encrypted_message, key):
    encrypted_message = encrypted_message.upper()
    key = str(key)
    key = key.upper()
    decrypted_message = ''

    for i, char in enumerate(encrypted_message):
        shifted_char = chr((((ord(char) - 65) - (ord(key[i % len(key)]) - 65) + 26) % 26) + 65)
        decrypted_message += shifted_char

    return decrypted_message
