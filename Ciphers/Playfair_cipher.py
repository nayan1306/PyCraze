def generate_key_square(keyword):
    keyword = ''.join(sorted(set(keyword), key=keyword.index))  # Remove duplicates and maintain order
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"  # I and J are combined
    key_square = []
    for char in keyword.upper():
        if char not in key_square and char in alphabet:
            key_square.append(char)
    for char in alphabet:
        if char not in key_square:
            key_square.append(char)
    return [key_square[i:i+5] for i in range(0, 25, 5)]

def find_position(char, key_square):
    for row in range(5):
        for col in range(5):
            if key_square[row][col] == char:
                return row, col
    return None

def playfair_encrypt(plaintext, keyword):
    key_square = generate_key_square(keyword)
    plaintext = plaintext.upper().replace('J', 'I')
    pairs = []
    i = 0
    while i < len(plaintext):
        a = plaintext[i]
        if i + 1 < len(plaintext):
            b = plaintext[i + 1]
        else:
            b = 'X'
        if a == b:
            pairs.append(a + 'X')
            i += 1
        else:
            pairs.append(a + b)
            i += 2
    ciphertext = ''
    for pair in pairs:
        row1, col1 = find_position(pair[0], key_square)
        row2, col2 = find_position(pair[1], key_square)
        if row1 == row2:
            ciphertext += key_square[row1][(col1 + 1) % 5]
            ciphertext += key_square[row2][(col2 + 1) % 5]
        elif col1 == col2:
            ciphertext += key_square[(row1 + 1) % 5][col1]
            ciphertext += key_square[(row2 + 1) % 5][col2]
        else:
            ciphertext += key_square[row1][col2]
            ciphertext += key_square[row2][col1]
    return ciphertext

def playfair_decrypt(ciphertext, keyword):
    key_square = generate_key_square(keyword)
    ciphertext = ciphertext.upper()
    pairs = [ciphertext[i:i + 2] for i in range(0, len(ciphertext), 2)]
    plaintext = ''
    for pair in pairs:
        row1, col1 = find_position(pair[0], key_square)
        row2, col2 = find_position(pair[1], key_square)
        if row1 == row2:
            plaintext += key_square[row1][(col1 - 1) % 5]
            plaintext += key_square[row2][(col2 - 1) % 5]
        elif col1 == col2:
            plaintext += key_square[(row1 - 1) % 5][col1]
            plaintext += key_square[(row2 - 1) % 5][col2]
        else:
            plaintext += key_square[row1][col2]
            plaintext += key_square[row2][col1]
    return plaintext

# Example usage
keyword = "PLAYFAIR"
plaintext = "HIDE THE GOLD IN THE TREE STUMP"
encrypted = playfair_encrypt(plaintext, keyword)
print(f"Encrypted: {encrypted}")
decrypted = playfair_decrypt(encrypted, keyword)
print(f"Decrypted: {decrypted}")
