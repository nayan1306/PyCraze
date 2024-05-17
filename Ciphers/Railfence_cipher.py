def RailFenceEncrypt(PlainText):
    """
    Encrypts the given plaintext using the Rail Fence cipher.

    Args:
        PlainText (str): The plaintext to be encrypted.

    Returns:
        str: The encrypted ciphertext.
    """
    CipherText = ""
    temp = ""
    for i in range(len(PlainText)):
        if i % 2 != 0:
            CipherText += PlainText[i]
        else:
            temp += PlainText[i]
    
    return CipherText + temp

def RailFenceDecrypt(CipherText):
    """
    Decrypts the given ciphertext using the Rail Fence cipher.

    Args:
        CipherText (str): The ciphertext to be decrypted.

    Returns:
        str: The decrypted plaintext.
    """
    PlainText = ""
    CipherText1 = CipherText[0:(len(CipherText)//2)]
    CipherText2 = CipherText[(len(CipherText)//2):]
    for i in range(len(CipherText)//2 + 1):
        PlainText += CipherText2[i]
        if i < (len(CipherText)//2):
            PlainText += CipherText1[i]
        
    return PlainText

# Example usage
plaintext = "HELLO"
encrypted = RailFenceEncrypt(plaintext)
print(f"Encrypted: {encrypted}")
decrypted = RailFenceDecrypt(encrypted)
print(f"Decrypted: {decrypted}")
