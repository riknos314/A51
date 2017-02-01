import A51

cipherA = A51.A51('1010101010101010101','1100110011001100110011','11100011100011100011100')

bits = ''
for i in range(8):
    bits += str(cipherA.getBit())
print(bits)


cipherB = A51.A51('1010101010101010101','1100110011001100110011','11100011100011100011100')

firstLetter = cipherB.encrypt('K')
print(firstLetter)

cipherC = A51.A51('1010101010101010101','1100110011001100110011','11100011100011100011100')

firstLetter = cipherC.decrypt(firstLetter)
print(firstLetter)





binStr = ''
for char in 'security':
    binStr += '0' + bin(ord(char))[2:]

newcipher = A51.A51(binStr[:18],binStr[18:40],binStr[40:])

bits = ''
for i in range(8):
    bits += str(newcipher.getBit())
print(bits)


