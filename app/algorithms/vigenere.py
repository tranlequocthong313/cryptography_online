def encrypt(message, key):
    message = message.upper()
    key = str(key)
    key = key.upper()
    encrypted_message = ''

    for i, char in enumerate(message):
        if 'A' <= char <= 'Z':
            shifted_char = chr(((ord(char) - 65 + ord(key[i % len(key)]) - 65) % 26) + 65)
            encrypted_message += shifted_char
        else:
            encrypted_message += char

    return encrypted_message


def decrypt(encrypted_message, key):
    encrypted_message = encrypted_message.upper()
    key = str(key)
    key = key.upper()
    decrypted_message = ''

    for i, char in enumerate(encrypted_message):
        if 'A' <= char <= 'Z':
            shifted_char = chr(((ord(char) - 65 - (ord(key[i % len(key)]) - 65) + 26) % 26) + 65)
            decrypted_message += shifted_char
        else:
            decrypted_message += char

    return decrypted_message
