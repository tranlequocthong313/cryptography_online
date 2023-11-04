def replace_duplicate(key):
    existed_chars = []
    for c in key:
        if c not in existed_chars:
            existed_chars.append(c)
    return "".join(existed_chars)


def generate_matrix(key):
    key = key.upper().replace("J", "I")
    key = replace_duplicate(key)
    key_chars = [char for char in key]
    key_chars = list(dict.fromkeys(key_chars))
    alphabet = [chr(ascii) for ascii in range(65, 91) if chr(ascii) != 'J']
    for char in key_chars:
        if char in alphabet:
            alphabet.remove(char)
    key_chars.extend(alphabet)
    matrix = [key_chars[i * 5:(i + 1) * 5] for i in range(5)]
    return matrix


def make_pairs(message):
    result = ''
    i = 0
    while i < len(message):
        if i + 1 >= len(message) or message[i] == message[i + 1]:
            result += message[i] + 'X'
        else:
            result += message[i] + message[i + 1]
            i += 1
        i += 1
    return result


def find_indexes(pairs, matrix):
    indexes = []
    for pair in pairs:
        index_pair = []
        for i in range(5):
            for j in range(5):
                if pair in matrix[i][j]:
                    index_pair.append([i, j])
        if pair[0] != matrix[index_pair[0][0]][index_pair[0][1]]:
            index_pair.reverse()
        indexes.extend(index_pair)
    return indexes


def shift_indexes(indexes, backward=False):
    direction = -1 if backward else 1
    shifted_indexes = indexes.copy()

    for i in range(0, len(shifted_indexes), 2):
        first = shifted_indexes[i]
        second = shifted_indexes[i + 1]

        if first[0] == second[0]:
            first[1] = (first[1] + direction) % 5
            second[1] = (second[1] + direction) % 5
        elif first[1] == second[1]:
            first[0] = (first[0] + direction) % 5
            second[0] = (second[0] + direction) % 5
        else:
            tmp = first[1]
            first[1] = second[1]
            second[1] = tmp

        shifted_indexes[i] = first
        shifted_indexes[i + 1] = second

    return shifted_indexes


def get_string(indexes, matrix):
    result = ''
    for i in range(0, len(indexes), 2):
        result += matrix[indexes[i][0]][indexes[i][1]]
        result += matrix[indexes[i + 1][0]][indexes[i + 1][1]]
    return result


def encrypt(message, key):
    message = message.upper().replace("J", "I")
    message = make_pairs(message)
    matrix = generate_matrix(key.upper())
    indexes = find_indexes(message, matrix)
    shifted_indexes = shift_indexes(indexes)
    return get_string(shifted_indexes, matrix)


def decrypt(encrypted_message, key):
    encrypted_message = encrypted_message.upper().replace("J", "I")
    encrypted_message = make_pairs(encrypted_message)
    matrix = generate_matrix(key.upper())
    indexes = find_indexes(encrypted_message, matrix)
    shifted_indexes = shift_indexes(indexes, backward=True)
    return get_string(shifted_indexes, matrix)


