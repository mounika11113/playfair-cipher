def encrypt(text, key):

    matrix = create_matrix(key)

    pairs = prepare_text(text).split()

    result = ""

    for pair in pairs:

        letter1 = pair[0]
        letter2 = pair[1]

        row1, col1 = find_position(matrix, letter1)
        row2, col2 = find_position(matrix, letter2)

        # Same Row
        if row1 == row2:

            cipher1 = get_letter(matrix, row1, (col1 + 1) % 5)
            cipher2 = get_letter(matrix, row2, (col2 + 1) % 5)

        # Same Column
        elif col1 == col2:

            cipher1 = get_letter(matrix, (row1 + 1) % 5, col1)
            cipher2 = get_letter(matrix, (row2 + 1) % 5, col2)

        # Rectangle Rule
        else:

            cipher1 = get_letter(matrix, row1, col2)
            cipher2 = get_letter(matrix, row2, col1)

        result += cipher1 + cipher2 + " "

    return result

def find_position(matrix, letter):

    index = matrix.index(letter)

    row = index // 5
    col = index % 5

    return row, col

def get_letter(matrix, row, col):
    return matrix[row * 5 + col]


def create_matrix(key):

    key = key.upper().replace("J", "I")

    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"

    result = ""

    for letter in key:
        if letter not in result and letter.isalpha():
            result += letter

    for letter in alphabet:
        if letter not in result:
            result += letter

    return result

def prepare_text(text):

    text = text.upper().replace(" ", "")

    result = ""

    i = 0

    while i < len(text):

        first = text[i]

        if i + 1 < len(text):
            second = text[i + 1]

            if first == second:
                result += first + "X "
                i += 1
            else:
                result += first + second + " "
                i += 2

        else:
            result += first + "X "
            i += 1

    return result

def format_matrix(matrix):

    result = ""

    for i in range(0, 25, 5):

        row = " ".join(matrix[i:i+5])

        result += row + "\n"

    return result

def decrypt(text, key):

    matrix = create_matrix(key)

    text = text.upper().replace(" ", "")

    if len(text) % 2 != 0:
        return "Cipher text must contain even number of letters"

    pairs = []

    for i in range(0, len(text), 2):
        pairs.append(text[i:i+2])

    result = ""

    for pair in pairs:

        letter1 = pair[0]
        letter2 = pair[1]

        row1, col1 = find_position(matrix, letter1)
        row2, col2 = find_position(matrix, letter2)

        # Same Row
        if row1 == row2:

            plain1 = get_letter(matrix, row1, (col1 - 1) % 5)
            plain2 = get_letter(matrix, row2, (col2 - 1) % 5)

        # Same Column
        elif col1 == col2:

            plain1 = get_letter(matrix, (row1 - 1) % 5, col1)
            plain2 = get_letter(matrix, (row2 - 1) % 5, col2)

        # Rectangle Rule
        else:

            plain1 = get_letter(matrix, row1, col2)
            plain2 = get_letter(matrix, row2, col1)

        result += plain1 + plain2 + " "

    return result