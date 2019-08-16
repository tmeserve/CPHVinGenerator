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
    inp = ''
    is_valid = False
    recursion_depth = 1
    while True:
        if is_valid:
            break
        inp = input('Enter the last 6 OR 8 characters of the VIN.')
        while True:
            if len(inp) == 6:
                vinStart = 'CPH________'
                first_part = getRandomVinStart(vinStart)
                vin = first_part + inp
                valid = ValidateVIN(vin)
                if valid[0]:
                    is_valid = True
                    break
            elif len(inp) == 8:
                vinStart = 'CPH______'
                first_part = getRandomVinStart(vinStart)
                vin = first_part + inp
                valid = ValidateVIN(vin)
                if valid[0]:
                    is_valid = True
                    break
            else:
                print('Error: Input must be 6 OR 8 characters long.')
            
            recursion_depth += 1
    
    print('The vin, {0}, was generated with a recursion depth of {1}'.format(valid[1], recursion_depth))
    # print(vin)
    
if __name__ == '__main__':
    runner()