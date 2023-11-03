def encrypt(message, key):
    message = message.upper()
    key = int(key)
    encrypted_message = ''

    for char in message:
        if 'A' <= char <= 'Z':
            shifted_char = chr(((ord(char) - 65 + key) % 26) + 65)
            encrypted_message += shifted_char
        else:
            encrypted_message += char

    return encrypted_message


def decrypt(encrypted_message, key):
    encrypted_message = encrypted_message.upper()
    key = int(key)
    decrypted_message = ''

    for char in encrypted_message:
        if 'A' <= char <= 'Z':
            shifted_char = chr(((ord(char) - 65 - key + 26) % 26) + 65)
            decrypted_message += shifted_char
        else:
            decrypted_message += char

    return decrypted_message
