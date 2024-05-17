def RailFenceEncrypt(PlainText):
    CipherText = ""
    temp = ""
    for i in range(len(PlainText)):
        if i%2 != 0:
            CipherText+=PlainText[i]
        else:
            temp += PlainText[i]
    
    return CipherText+temp



def RailFenceDecrypt(CipherText):
    
    PlainText = ""
    CipherText1 = CipherText[0:(len(CipherText)//2)]
    CipherText2 = CipherText[(len(CipherText)//2):]
    for i in range(len(CipherText)//2+1):
        PlainText += CipherText2[i]
        if i < (len(CipherText)//2):
            PlainText += CipherText1[i]
        
    return PlainText    
    
    


                       
# Example usage
plaintext = "HELLO"
shift = 3
encrypted = RailFenceEncrypt(plaintext)
print(f"Encrypted: {encrypted}")
decrypted = RailFenceDecrypt(encrypted)
print(f"Decrypted: {decrypted}")                    
                