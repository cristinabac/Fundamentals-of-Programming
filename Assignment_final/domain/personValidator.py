'''
Created on Nov 10, 2018

@author: hp840
'''
import unittest

class personValidatorException(Exception):
    pass

class personValidator:
    
    def validate(self,personId,personName,personPhoneNumber,personAddress):
        '''
        Validates a person - verifies if the data format is ok
        Input: 4 strings
        Exception: The id must contain only digits
                   The name must contain only letters
                   The phone number must contain only digits
        '''
        
        err = []
        
        if personId.isdigit() == False:
            err.append("The id must contain only digits!")
        
        nameWithoutSpaces = personName.replace(" ","") #we remove the spaces
        if nameWithoutSpaces.isalpha() == False:       #because otherwise, the space will be taken as a non-letter
            err.append("The name must contain only letters!")
        
        if personPhoneNumber.isdigit() == False:
            err.append("The phone number must contain only digits!")
        
        if len(err) > 0:
            raise personValidatorException(err)
        
        
def testPersonValidator():
    try:
        personValidator.validate(1,"1","Jane2 Mary","0742111222","Street, town") #BECAUSE THE NAME CONTAINS DIGITS
        assert False
    except personValidatorException:
        pass
    
    try:
        personValidator.validate(1,"12a","Jane Mary","0742111222","Street, town") #BECAUSE THE ID CONTAINS LETTERS
        assert False
    except personValidatorException:
        pass
    
    try:
        personValidator.validate(1,"1","Jane Mary Lara","074211122a","Street, town") #BECAUSE THE PHONE NUMBER CONTAINS LETTERS
        assert False
    except personValidatorException:
        pass

testPersonValidator()


class unittestPersonValidator(unittest.TestCase):
    
    def setUp(self):
        self.validator = personValidator
        
        
    def test(self):
        
        self.assertRaises(personValidatorException, self.validator.validate, 1,"1","Jane2 Mary","0742111222","Street, town")
        self.assertRaises(personValidatorException, self.validator.validate, 1,"12a","Jane Mary","0742111222","Street, town")
        self.assertRaises(personValidatorException, self.validator.validate, 1,"1","Jane Mary Lara","074211122a","Street, town")