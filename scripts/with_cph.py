import random
from util import ValidateVIN, calculateCheckDigit
import os, sys, time

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
    recursion_depth = 0
    lines = vinFile.readlines()
    length = len(lines)
    lineToRead = int(random.random() * (length - 1)) + 1
    
    line = lines[lineToRead]
    fields = line.split()
    vinFile.close()
    return VinYear(fields[0].strip(), fields[1].strip())

def getRandomVinChar():
    i = int(random.random() * len(vinDigitValues))
    return list(vinDigitValues.keys())[i]

def generate_cph_vin(num):
    is_valid = False
    recursion_depth = 1
    while True:
        if recursion_depth == 500:
            break
        if is_valid:
            break
        # inp = input('Please enter the last 6 or 8 characters of the VIN:\n')
    
        if len(num) == 6:
            char10 = "3"
            vinYear = getRandomVinStart()
            char = getRandomVinChar()
            v = 'CPH{0}{1}{2}'.format(vinYear.First8[3:], char, char10)
            valid = ValidateVIN(v)
            # CPH120EG03P111111
            while not valid[0]:
                if len(v) == 17:
                    valid = ValidateVIN(v)
                    if valid[0]:
                        is_valid = True
                        break
                    
                if valid[2] == 'Invalid Length':
                    v = 'CPH{0}{1}{2}'.format(vinYear.First8[3:], char, char10)
                    for i in range(1):
                        v += getRandomVinChar()
                    checkChar = getCheckSumChar(v)
                    v = '{0}{1}{2}{3}'.format(v[0:8], checkChar, v[9:], num)
                elif valid[2] == 'Invalid Checksum Character':
                    checkChar = getCheckSumChar(v)
                    v = '{0}{1}{2}'.format(v[0:8], checkChar, v[9:])
                elif valid[2] == 'Unable to Generate':
                    # return (False, valid[1], 'Unable to Generate')
                    # print('Cannot generate a random vin based off the the characters you gave and the VDS selected.')
                    break
        # CPHNL12E639111111
        elif len(num) == 8:
            vinYear = getRandomVinStart()
            char = getRandomVinChar()
            
            v = "CPH{0}{1}{2}".format(vinYear.First8[3:], char, num)
            checkChar = getCheckSumChar(v)
            v = '{0}{1}{2}'.format(v[0:8], checkChar, v[9:])
            valid = ValidateVIN(v)
            break
        else:
            print('Error: Make sure your input is either 6 OR 8 characters long.')
            recursion_depth += 1
    v = valid[1]
    # print('It took {0} time(s) to get a vin.'.format(recursion_depth))
    if valid[0]:
        # print('The vin, {0}, is validated'.format(v))
        return (valid[0], 'The vin, {0}, is validated'.format(v), recursion_depth)
    else:
        # print('The vin, {0}, is not validated'.format(v))
        return (valid[0], 'The vin, {0}, is not validated'.format(v), recursion_depth)

def runner():
    six_char_vins = open('CPH_6Char_Vins.txt', 'w+')
    eight_char_vins = open('CPH_8Char_Vins.txt', 'w+')
    times = time.time()
    for item in random.sample(range(100000, 999999), 5000):
        cph_vin_result = generate_cph_vin(str(item))
        
        six_char_vins.write('{0} with a recursion depth of {1}.\n'.format(cph_vin_result[1], cph_vin_result[2]))
    print('Finished 6 character generation')
    time1 = time.time()
    for item in random.sample(range(10000000, 99999999), 5000):
        cph_vin_result = generate_cph_vin(str(item))
        
        eight_char_vins.write('{0} with a recursion depth of {1}.\n'.format(cph_vin_result[1], cph_vin_result[2]))
    
    time2 = time.time()
    print(time2 - times, ' the enter time')
    print(time1 - times, ' 6 chars')
    print(time2 - time1, ' eight chars')
    six_char_vins.close()
    eight_char_vins.close()

if __name__ == '__main__':
    runner()