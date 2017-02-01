from A51 import generator
from A51 import encrypt
class A51:
    def __init__(self, X,Y,Z):
        self.gen = generator.keyStreamGen(X,Y,Z)


    def encrypt(self,string):
        return encrypt.encrypt(string, self.gen)

    def decrypt(self, string):
        return encrypt.decrypt(string, self.gen)
    
    def getBit(self):
        return self.gen.getBit()




        
