def modinv(a, m = 26):
    matrix = [
        [m, 0, None], 
        [a, 1, m//a]
    ]
    while matrix[len(matrix)-1][0] != 1:
        matrix.append([0,0,0])
        last_index = len(matrix)-1
        matrix[last_index][0] = matrix[last_index-2][0] % matrix[last_index-1][0]
        matrix[last_index][2] = matrix[last_index-1][0] // matrix[last_index][0]
        matrix[last_index][1] = matrix[last_index-2][1] - (matrix[last_index-1][1] *  matrix[last_index-1][2])

    return (matrix[len(matrix)-1][1] + m) % m


def encrypt(message, key):
    # E(x) = (ax+b) % 26
    message = message.upper()
    a = int(key[0]) % 26
    b = int(key[1]) % 26
    encrypted_message = ''

    for char in message:
        if 'A' <= char <= 'Z':
            x = ord(char) - 65
            x = (a*x+b) % 26
            shifted_char = chr(x + 65)
            encrypted_message += shifted_char
        else:
            encrypted_message += char

    return encrypted_message


def decrypt(encrypted_message, key):
    # D(x) = a^-1 * (y-b) % 26
    encrypted_message = encrypted_message.upper()
    a = int(key[0]) % 26
    b = int(key[1]) % 26
    inverse = modinv(a, 26)
    message = ''

    for char in encrypted_message:
        if 'A' <= char <= 'Z':
            y = ord(char) - 65
            x = inverse * (y - b) % 26
            shifted_char = chr(x + 65)
            message += shifted_char
        else:
            message += char

    return message
