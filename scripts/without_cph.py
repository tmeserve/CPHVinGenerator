import random
from util import ValidateVIN
import os, sys

transliterationString = "0123456789.ABCDEFGH..JKLMN.P.R..STUVWXYZ"
validChars = "0123456789ABCDEFGHJKLMNPRSTUVWXYZ"

# I O Q U Z

vinDigitPositionMultiplier = [ 8, 7, 6, 5, 4, 3, 2, 10, 0, 9, 8, 7, 6, 5, 4, 3, 2 ]
vinDigitValues = { 'A':1, 'B':2, 'C':3, 'D':4, 'E':5, 'F':6, 'G':7, 'H':8, 'J':1,
                        'K':2, 'L':3, 'M':4, 'N':5, 'P':7, 'R':9, 'S':2, 'T':3, 'U':4, 'V':5, 
                        'W':6, 'X':7, 'Y':8, 'Z':9, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, 
                        '7':7, '8':8, '9':9, '0':0}

class VinYear:
    def __init__(self, first8, year):
        self.First8 = first8
        self.Year = year
    
    def __repr__(self):
        return "First8: %s - Year: %s" % (self.First8, self.Year)

def getRandomVinStart(vinStart):
    vinStart_list = list(vinStart)
    for item in vinStart_list:
        if item == '_':
            char = random.choice(validChars)
            index = vinStart_list.index(item)
            if index == 8:
                vinStart[8] == '3'
            vinStart_list[index] = char
    return ''.join(vinStart_list)

def runner():
    # is_valid = False
    # recursion_depth = 1
    i = 0
    out_file = open('16CharVin' , 'w+')
    while i < 5000:
        is_valid = False
        recursion_depth = 1
        while True:
            vinStart = '________3________'
            first_part = getRandomVinStart(vinStart)
            vin = first_part
            valid = ValidateVIN(vin)
            if valid[0]:
                is_valid = True
                break
            recursion_depth += 1
    
        out_file.write('The vin, {0}, was generated with a recursion depth of {1}\n'.format(valid[1], recursion_depth))
        # print('The vin, {0}, was generated with a recursion depth of {1}'.format(valid[1], recursion_depth))
        i += 1
    # print(vin)
    
if __name__ == '__main__':
    runner()