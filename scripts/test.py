import unittest
from without_cph import getRandomVinStart
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
    
    def test_is_16_char_valid(self):
        while True:
            vinStart = '________3________'
            first_part = getRandomVinStart(vinStart)
            vin = first_part
            valid = ValidateVIN(vin)
            if valid[0]:
                is_valid = True
                break
        self.assertTrue(valid[0])

if __name__ == '__main__':
    unittest.main()