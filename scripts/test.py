import unittest
from with_cph import getRandomVinChar, getCheckSumChar, getRandomVinStart
from util import ValidateVIN, calculateCheckDigit
import random

class Test(unittest.TestCase):
    
    def test_get_check_sum_char(self):
        vin = input('Enter the vin you wish to get the checksum character for.')
        
        if vin[8] == 'X':
            cd = 10
        else:
            cd = int(vin[8])
        
        check_sum_list = calculateCheckDigit(vin)
        value = random.choice(check_sum_list)
        
        self.assertTrue(value[0])
    
    def test_is_last6_generated_valid(self):
        inp = ''
        is_valid = False
        recursion_depth = 1
        while True:
            if recursion_depth == 500:
                break
            if is_valid:
                break
            inp = input('Please enter the last 6 characters of the VIN:\n')
        
            if len(inp) == 6:
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
                        v = '{0}{1}{2}{3}'.format(v[0:8], checkChar, v[9:], inp)
                    elif valid[2] == 'Invalid Checksum Character':
                        checkChar = getCheckSumChar(v)
                        v = '{0}{1}{2}'.format(v[0:8], checkChar, v[9:])
                    elif valid[2] == 'Unable to Generate':
                        print('Cannot generate a random vin based off the the characters you gave and the VDS selected.')
                        break
            else:
                print('Error: Make sure your input is 6 characters long.')
                recursion_depth += 1
        v = valid[1]
        self.assertTrue(v)
        
    def test_is_last_8_vin_valid(self):
        inp = ''
        while not len(inp) == 8:
            inp = input('Please enter the last 8 characters of the VIN:\n')
            
            if len(inp) == 8:
                
                vinYear = getRandomVinStart()
                char = getRandomVinChar()
                
                v = "CPH{0}{1}{2}".format(vinYear.First8[3:], char, inp)
                checkChar = getCheckSumChar(v)
                v = '{0}{1}{2}'.format(v[0:8], checkChar, v[9:])
                valid = ValidateVIN(v)
            else:
                print('Error: Make sure your input is 8 characters long.')
            
        self.assertTrue(valid[0])

if __name__ == '__main__':
    unittest.main()