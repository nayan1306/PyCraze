def generate_key_square(keyword):
    """
    Generates a 5x5 key square matrix for the Playfair cipher using the provided keyword.

    Args:
        keyword (str): The keyword used to generate the key square.

    Returns:
        list: A 5x5 matrix (list of lists) representing the key square.
    """
    # Remove duplicate letters from the keyword while maintaining order
    keyword = ''.join(sorted(set(keyword.replace('J', 'I')), key=keyword.index))
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"  # I and J are combined
    key_square = []
    
    # Add unique characters from the keyword to the key square
    for char in keyword.upper():
        if char not in key_square and char in alphabet:
            key_square.append(char)
    
    # Add remaining characters from the alphabet to the key square
    for char in alphabet:
        if char not in key_square:
            key_square.append(char)
    
    # Create a 5x5 matrix from the key square list
    return [key_square[i:i+5] for i in range(0, 25, 5)]

def find_position(char, key_square):
    """
    Finds the position of a character in the key square.

    Args:
        char (str): The character to find.
        key_square (list): The 5x5 matrix representing the key square.

    Returns:
        tuple: A tuple (row, col) representing the position of the character in the key square.
    """
    for row in range(5):
        for col in range(5):
            if key_square[row][col] == char:
                return row, col
    return None, None  # Return (None, None) if char is not found

def playfair_encrypt(plaintext, keyword):
    """
    Encrypts a plaintext message using the Playfair cipher with the provided keyword.

    Args:
        plaintext (str): The plaintext message to encrypt.
        keyword (str): The keyword used to generate the key square.

    Returns:
        str: The encrypted ciphertext.
    """
    key_square = generate_key_square(keyword)
    plaintext = plaintext.upper().replace('J', 'I')
    
    # Remove non-alphabetic characters from plaintext
    plaintext = ''.join(char for char in plaintext if char.isalpha())
    
    # Pad the plaintext if its length is odd
    if len(plaintext) % 2 != 0:
        plaintext += 'X'
    
    pairs = [plaintext[i:i+2] for i in range(0, len(plaintext), 2)]
    ciphertext = ''
    
    # Encrypt each pair using the Playfair cipher rules
    for pair in pairs:
        row1, col1 = find_position(pair[0], key_square)
        row2, col2 = find_position(pair[1], key_square)
        
        if row1 is None or col1 is None or row2 is None or col2 is None:
            # If any character is not found, skip this pair
            continue
        
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
    """
    Decrypts a ciphertext message encrypted using the Playfair cipher with the provided keyword.

    Args:
        ciphertext (str): The ciphertext message to decrypt.
        keyword (str): The keyword used to generate the key square.

    Returns:
        str: The decrypted plaintext.
    """
    key_square = generate_key_square(keyword)
    ciphertext = ciphertext.upper().replace('J', 'I')
    pairs = [ciphertext[i:i + 2] for i in range(0, len(ciphertext), 2)]
    plaintext = ''
    
    # Decrypt each pair using the Playfair cipher rules
    for pair in pairs:
        row1, col1 = find_position(pair[0], key_square)
        row2, col2 = find_position(pair[1], key_square)
        
        if row1 is None or col1 is None or row2 is None or col2 is None:
            # If any character is not found, skip this pair
            continue
        
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
if __name__ == "__main__":
    keyword = "PLAYFAIR"
    plaintext = "HIDE THE GOLD IN THE TREE STUMP"
    
    encrypted = playfair_encrypt(plaintext, keyword)
    print(f"Encrypted: {encrypted}")
    
    decrypted = playfair_decrypt(encrypted, keyword)
    print(f"Decrypted: {decrypted}")
