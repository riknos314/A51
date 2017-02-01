
class keyStreamGen:

    #x,y,z are strings of binary
    def __init__(self, x, y, z, key=False):

        self.regX = [int(i) for i in x]
        self.regY = [int(i) for i in y]
        self.regZ = [int(i) for i in z]


    def majority(self):

        values = [self.regX[8], self.regY[10], self.regZ[10]]

        if values.count(0) > 1:
            majority = 0

        else: majority = 1

        return majority


    def stepRegister(self, reg):
        # reg is string containing letter of register to be stepped

        newFirstBit = ''

        if reg == 'X':
            newFirstBit = self.regX[13]^self.regX[14]^self.regX[15]^self.regX[16]
            self.regX = [newFirstBit] + self.regX[:-1]
        if reg == 'Y':
            newFirstBit = self.regY[20]^self.regY[21]
            self.regY = [newFirstBit] + self.regY[:-1]
        if reg == 'Z':
            newFirstBit = self.regZ[7]^self.regZ[20]^self.regZ[21]^self.regZ[22]
            self.regZ = [newFirstBit] + self.regZ[:-1]


    def generateBit(self):
        
        return self.regX[-1] ^ self.regY[-1] ^ self.regZ[-1] 

    def getBit(self):
        
        majority = self.majority()
        if self.regX[8] == majority:
            self.stepRegister('X')
        if self.regY[10] == majority:
            self.stepRegister('Y')
        if self.regZ[10] == majority:
            self.stepRegister('Z')
        
        return self.generateBit()





