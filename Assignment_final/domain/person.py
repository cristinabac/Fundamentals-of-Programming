'''
Created on Nov 10, 2018

@author: hp840
'''
import unittest

class person:
    '''    
    parameter - !exception! - how is stored
    
    personId - !only digits! - INT
    personName - !only letters!  - STRING
    personPhoneNumber - !only digits! - STRING
    personAddress - STRING
    '''
    
    def __init__(self, personId, personName, personPhoneNumber,personAddress):
        
        self._id = int(personId) #The id will be an integer
        self._name = personName
        self._phone = personPhoneNumber #The phone number will not be an integer because it can begin with 0
        self._address = personAddress
    
    def getId(self):
        return self._id
    
    def getName(self):
        return self._name
    
    def getPhone(self):
        return self._phone
    
    def getAddress(self):
        return self._address
    
    def setId(self, newId):
        self._id = int(newId)
    
    def setName(self, newName):
        self._name = newName
    
    def setPhone(self, newPhone):
        self._phone = newPhone
        
    def setAddress(self, newAddress):
        self._address = newAddress
    
    def __str__(self):
        return str(self._id) + '  -  ' + self._name + '  -  ' + str(self._phone) + '  -  ' + self._address

def testPerson():
    person1 = person("1234", "Gigi", "28446661", "Street ABC")
    assert person1.getId() == 1234
    assert person1.getName() == "Gigi"
    assert person1.getPhone() == "28446661"
    assert person1.getAddress() == "Street ABC"
    assert person1.__str__() == "1234  -  Gigi  -  28446661  -  Street ABC"
    
    person1.setId("1")
    assert person1.getId() == 1
    person1.setName("Mary Russ")
    assert person1.getName() == "Mary Russ"
    person1.setPhone("0742111222")
    assert person1.getPhone() == "0742111222"
    person1.setAddress("Town, street, number")
    assert person1.getAddress() == "Town, street, number"
    assert person1.__str__() == "1  -  Mary Russ  -  0742111222  -  Town, street, number"
    
testPerson()



class unittestPerson(unittest.TestCase):
    
    
    def testperson(self):
        
        person1 = person("1234", "Gigi", "28446661", "Street ABC")
        self.assertEqual(person1.getId(),1234)
        self.assertEqual( person1.getName(),"Gigi")
        self.assertEqual( person1.getPhone(),"28446661")
        self.assertEqual(person1.getAddress(), "Street ABC")
        self.assertEqual(person1.__str__(), "1234  -  Gigi  -  28446661  -  Street ABC")
        
        person1.setId("1")
        self.assertEqual(person1.getId(),1)
        person1.setName("Mary Russ")
        self.assertEqual(person1.getName(),"Mary Russ")
        person1.setPhone("0742111222")
        self.assertEqual(person1.getPhone(),"0742111222")
    