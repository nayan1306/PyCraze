def CaesarCipherEncrypt(PlainText,key):
    CipherText = ""
    for char in PlainText:
        if char.isalpha():
            key = key % 26
            shifted = ord(char) + key
            if char.islower():
                if shifted > ord('z'):
                    shifted -= 26
                CipherText+=chr(shifted)
            if char.isupper():
                if shifted > ord('Z'):
                    shifted-=26
                CipherText+=chr(shifted)
        else:
            CipherText+=char
    return CipherText


def CaesarCipherDecrypt(PlainText,key):
    return CaesarCipherEncrypt(PlainText=PlainText,key=-key)
    
                    
                        
# Example usage
plaintext = "HELLO"
shift = 3
encrypted = CaesarCipherEncrypt(plaintext, shift)
print(f"Encrypted: {encrypted}")
decrypted = CaesarCipherDecrypt(encrypted, shift)
print(f"Decrypted: {decrypted}")                    
                