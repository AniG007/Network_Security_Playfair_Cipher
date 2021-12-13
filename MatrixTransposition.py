def Cipher(plaintext, key):
    plaintext = plaintext.replace(" ", "%")

    key = key.split(",")

    columns = int(max(key))

    row_matrix = []
    matrix = []
    breaker = 0 # For iterating to the next row of the matrix

    # This loop produces the matrix which is used to produce the Cipher in the next loop
    for j in range(len(plaintext)):
        row_matrix.append(plaintext[j])
        breaker += 1
        if j == len(plaintext) - 1:
            if len(row_matrix) != columns:
                diff = columns - len(row_matrix)
                for i in range(diff):
                    row_matrix.append("%")
                matrix.append(row_matrix)
                break

        if breaker == columns:
            matrix.append(row_matrix)
            row_matrix = []
            breaker = 0

    cipher = ""
    rows = len(matrix)

    # This loop generates the cipher text
    for i in key:
        for j in range(rows):
            cipher += matrix[j][int(i) - 1]

    print("cipher text: ", cipher)


def Decipher(ciphertext, key):

    key = key.split(",")

    div = len(ciphertext)//int(max(key)) # No of columns

    row_matrix = []
    matrix = []
    breaker = 0 # For iterating to the next row of the matrix

    # Loop for generating the unordered matrix that is used to produce the actual matrix in the next loop
    for i in range(len(ciphertext)):
        row_matrix.append(ciphertext[i])
        breaker += 1
        if i == len(ciphertext) - 1:
            if len(row_matrix) != div:
                diff = div - len(row_matrix)
                for j in range(diff):
                    row_matrix.append("%")
                matrix.append(row_matrix)
                break

        if breaker == div:
            matrix.append(row_matrix)
            row_matrix = []
            breaker = 0

    plain = []
    # Loop for creating an empty matrix for insertion
    for i in range(len(matrix)):
        plain.append([])
    count = 0

    # The actual matrix being formed from the unordered matrix
    for i in key:
        plain[int(i)-1] = matrix[count]
        count += 1

    plaintext = ""

    # Generating the plaintext from the matrix
    for i in range(div):
        for j in range(int(max(key))):
            plaintext += plain[j][i]

    plaintext = plaintext.replace("%"," ")
    print("Plain Text: ", plaintext)