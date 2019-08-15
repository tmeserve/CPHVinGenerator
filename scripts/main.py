import random
from util import ValidateVIN
import os, sys

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

def getCheckSumChar(vin):
    # generate the check sum
    checkSumTotal = 0

    # if (len(vin) < 17):
    #     print("Invalid Length: %s" % len(vin))
    #     return -1

    for i in range(len(vin)):
        if (vinDigitValues.get(vin[i], "-1") != "-1"):
            checkSumTotal += int(vinDigitValues[vin[i]]) * vinDigitPositionMultiplier[i];
        else:
            #Characters not in the VinDigitValues list are not valid VIN characters - return false (invalid)
            print("Illegal Character: %s" % vin[i])
            print(vin)
            return -1

    remain = checkSumTotal % 11
    char = str(remain)
    if remain == 10:
        char = 'X'

    return char

def getRandomVinStart():
    
    vinFile = open('VinPrefixes.txt')
    count = 0
    lines = vinFile.readlines()
    length = len(lines)
    lineToRead = int(random.random() * length)
    
    line = lines[lineToRead]
    fields = line.split()
    return VinYear(fields[0].strip(), fields[1].strip())

def getRandomVinChar():
    i = int(random.random() * len(vinDigitValues))
    return list(vinDigitValues.keys())[i]

def runner():
    inp = ''
    while True:
        inp = input('Please enter the last 6 or 8 characters of the VIN:\n')
    
        if len(inp) == 6:
            char10 = "3"
            vinYear = getRandomVinStart()
            char = getRandomVinChar()
            v = '{0}{1}{2}'.format(vinYear.First8, char, char10)
            valid = ValidateVIN(v)
            while not valid[0]:
                if len(v) == 17:
                    valid = ValidateVIN(v)
                    
                if valid[2] == 'Invalid Length':
                    vin = '{0}{1}{2}'.format(vinYear.First8, char, char10)
                    for i in range(1):
                        v += getRandomVinChar()
                    checkChar = getCheckSumChar(v)
                    v = '{0}{1}{2}'.format(v[0:8], checkChar, v[9], inp)
                elif valid[2] == 'Invalid Checksum Character':
                    checkChar = getCheckSumChar(v)
                    v = '{0}{1}{2}{3}'.format(v[0:8], checkChar, v[9], inp)
            break
        elif len(inp) == 8:
            vinYear = getRandomVinStart()
            char = getRandomVinChar()
            
            v = "{0}{1}{2}".format(vinYear.First8, char, inp)
            checkChar = getCheckSumChar(v)
            v = '{0}{1}{2}'.format(v[0:8], checkChar, v[9:])
            valid = ValidateVIN(v)
            break
        else:
           print('Error: Make sure your input is either 6 OR 8 characters long.')
    
    print(v)
    print(len(v))
    print(valid[0])

if __name__ == '__main__':
    runner()