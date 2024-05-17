def generate_key(text, keyword):
    """
    Generates a key for the Vigenère cipher based on the provided text and keyword.

    Args:
        text (str): The text to be encrypted or decrypted.
        keyword (str): The keyword used for encryption or decryption.

    Returns:
        str: The generated key, repeating the keyword to match the length of the text.
    """
    key = keyword
    while len(key) < len(text):
        key += keyword
    return key[:len(text)]

def vigenere_cipher_encrypt(text, keyword):
    """
    Encrypts the given text using the Vigenère cipher with the provided keyword.

    Args:
        text (str): The plaintext to be encrypted.
        keyword (str): The keyword used for encryption.

    Returns:
        str: The encrypted ciphertext.
    """
    key = generate_key(text, keyword)
    encrypted_text = ""
    for i in range(len(text)):
        if text[i].isalpha():
            shift = ord(key[i].upper()) - ord('A')
            base = ord('A') if text[i].isupper() else ord('a')
            encrypted_char = chr((ord(text[i]) - base + shift) % 26 + base)
            encrypted_text += encrypted_char
        else:
            encrypted_text += text[i]
    return encrypted_text

def vigenere_cipher_decrypt(ciphertext, keyword):
    """
    Decrypts the given ciphertext using the Vigenère cipher with the provided keyword.

    Args:
        ciphertext (str): The ciphertext to be decrypted.
        keyword (str): The keyword used for decryption.

    Returns:
        str: The decrypted plaintext.
    """
    key = generate_key(ciphertext, keyword)
    decrypted_text = ""
    for i in range(len(ciphertext)):
        if ciphertext[i].isalpha():
            shift = ord(key[i].upper()) - ord('A')
            base = ord('A') if ciphertext[i].isupper() else ord('a')
            decrypted_char = chr((ord(ciphertext[i]) - base - shift + 26) % 26 + base)
            decrypted_text += decrypted_char
        else:
            decrypted_text += ciphertext[i]
    return decrypted_text

# Example usage
plaintext = "HELLO WORLD"
keyword = "KEY"
encrypted = vigenere_cipher_encrypt(plaintext, keyword)
print(f"Encrypted: {encrypted}")
decrypted = vigenere_cipher_decrypt(encrypted, keyword)
print(f"Decrypted: {decrypted}")
