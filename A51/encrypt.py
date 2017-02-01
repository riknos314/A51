
def encrypt(string, generator):

    cyphertext = ''
    bincytext = ''
    for char in string:
        charText = ''
        binChar = '0'+bin(ord(char))[2:]
        for d in binChar:
            charText += str(encryptBit(int(d), generator))

        bincytext += charText
        cyphertext += hex(int(charText,2))[2:]
        
    return cyphertext

def encryptBit(anInt, generator):
    return anInt ^ generator.getBit()

def decrypt(string, generator):
    # encrypt and decrypt do the same thing because XOR

    
    binString = ''
    for i in range(0,len(string),6):
        binString += '0' + bin(int(string[i:i+6],16))[2:]

    binPlaintext = ''
    for bit in binString:
        binPlaintext += bin(encryptBit(int(bit,2), generator))[2:]

    plaintext = ''
    for i in range(0, len(binPlaintext),8):
        char = binPlaintext[i:i+8]
        plaintext += chr(int(char,2))

    return plaintext
        

        
