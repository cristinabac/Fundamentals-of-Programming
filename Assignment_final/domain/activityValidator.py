'''
Created on Nov 10, 2018

@author: hp840
'''
import datetime
import unittest

class activityValidatorException(Exception):
    pass

class activityValidator:
    
    def validate(self, aid,pids,adate,atime,adescr):
        '''
        Validates an activity - verifies if the format of every data is ok
        Input: aid, adate, atime,adescr - strings
               pids - a list of strings
        Exception: The activity id and person id's must contain only digits
                   The date format must be: YYYY-MM-DD
                   The time format must be HH:MM:SS
        '''
        
        err = []
        
        if aid.isdigit() == False:
            err.append("The id must contain only digits!")
        
        for i in pids:
            if i.isdigit() == False:
                err.append("The person id's must contain only digits!")
        
        try:
            if datetime.datetime.strptime(adate, '%Y-%m-%d') == False:
                err.append("Incorrect data format, should be YYYY-MM-DD")
        except ValueError :
            err.append("Incorrect data format, should be YYYY-MM-DD")
        
        try:
            if datetime.datetime.strptime(atime, '%H:%M:%S') == False:
                err.append("Incorrect time format, should be hour:minutes:seconds")
        except ValueError :
            err.append("Incorrect time format, should be hour:minutes:seconds - HH:MM:SS")
            
        if len(err) > 0:
            raise activityValidatorException(err)

def testActivityValidator():
    try:
        activityValidator.validate(1, "1", ["2","1"], "2012-13-10","20:30:00","Description") # BECAUSE THE MONTH IS 13
        assert False
    except activityValidatorException:
        pass
    
    try:
        activityValidator.validate(1, "a", ["2"], "2012-12-10","20:30:00","Description") # BECAUSE THE ID DOES NOT CONTAIN ONLY DIGITS
        assert False
    except activityValidatorException:
        pass
    
    try:
        activityValidator.validate(1, "1", ["2","3"], "2012-12-10","20:64","Description") # BECAUSE THE MINUTES ARE 64
        assert False
    except activityValidatorException:
        pass
    
    try:
        activityValidator.validate(1, "1", ["2"], "10.10.2012","20:30:00","Description") # BECAUSE OF THE DATA FORMAT
        assert False
    except activityValidatorException:
        pass
    
    try:
        activityValidator.validate(1, "1", ["23a5","3","4"], "2012-11-10","20:30:00","Description") # BECAUSE THE PERSON ID'S CONTAINS LETTERS
        assert False
    except activityValidatorException:
        pass
    
    try:
        activityValidator.validate(1, "1", "2", "2012-12-10","12AM:13","Description") # BECAUSE OF THE TIME FORMAT
        assert False
    except activityValidatorException:
        pass
    
testActivityValidator()



class unittestActivityValidator(unittest.TestCase):
    
    
    def setUp(self):
        self.validator = activityValidator
    
    def test(self):
        
        self.assertRaises(activityValidatorException, self.validator.validate, 1,"1", ["2"], "2012-13-10","20:30:00","Description")
        self.assertRaises(activityValidatorException, self.validator.validate, 1, "a", ["2"], "2012-12-10","20:30:00","Description")
        self.assertRaises(activityValidatorException, self.validator.validate, 1, "1", ["2"], "2012-12-10","20:64","Description")
        self.assertRaises(activityValidatorException, self.validator.validate, 1, "1", ["2"], "10.10.2012","20:30:00","Description")
        self.assertRaises(activityValidatorException, self.validator.validate, 1, "1", ["23a5"], "2012-11-10","20:30:00","Description")
        self.assertRaises(activityValidatorException, self.validator.validate, 1, "1", ["2"], "2012-12-10","12AM:13","Description")
