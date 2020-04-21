'''
Created on Nov 10, 2018

@author: hp840
'''
import unittest
from domain.person import person

class PersonRepositoryException(Exception):
    pass

class PersonRepository:
    '''
    Stores the persons in the memory
    '''
    
    def __init__(self):
        self._persons = {}
    
    def clear(self):
        '''
        Clears all persons
        '''
        self._persons = {}
    
    def store(self, pers):
        '''
        Stores a person in the memory
        pers - the person
        Exception : If the id already exists
        '''
        if pers.getId() in self._persons:
            raise PersonRepositoryException("The specified ID already exists")
        else:
            self._persons[pers.getId()] = pers
        
    def remove(self, persId):
        '''
        Removes the person with the specified id
        persId - the specified id
        Exception : A person with the specified ID does not exist
        '''
        try: 
            #self._persons.pop(persId)
            del self._persons[persId]
        except KeyError:
            raise PersonRepositoryException("A person with the specified ID does not exist")
        
    def size(self):
        '''
        Returns the number of objects
        '''
        return len(self._persons)
    
    def get(self, Id):
        try:
            self._persons[Id]
        except KeyError:
            raise PersonRepositoryException("The Id does not exist")
        return self._persons[Id]
      
    def getAllPersons(self):
        '''
        Returns all objects
        '''
        return self._persons
    
    def modify(self, pers):
        '''
        Modifies a person
        pers - Person
        Exception : A person with the specified ID does not exist
        '''
        try:
            self._persons[pers.getId()]
        except KeyError:
            raise PersonRepositoryException("A person with the specified ID does not exist")
        self._persons[pers.getId()] = pers
        

class testPersonRepo(unittest.TestCase):
    
    def setUp(self):
        
        self.repo = PersonRepository()
        testList = [person("1","Ana","0742123456","Addressss"), person("2","Ana Maria","0734111222","Address 2 laala ss")]
        for i in testList:
            self.repo.store(i)
            self.assertEqual(self.repo.get(i.getId()), i)
    
    
    def testStore(self):
        
        self.assertRaises(PersonRepositoryException, self.repo.store, person("1","Maria","0724111111","adresaaaa"))
        self.assertRaises(PersonRepositoryException, self.repo.store, person("2","Maria","0724111111","adresaaaa"))
        self.repo.store(person("3","Maria","0724111111","adresaaaa"))
    
    
    def testRemove(self):
        
        self.assertEqual(self.repo.size(),2)
        self.repo.remove(1)
        self.assertEqual(self.repo.size(),1)
        self.assertRaises(PersonRepositoryException, self.repo.remove, 1)
        self.assertRaises(PersonRepositoryException, self.repo.remove, person("99","Maria","0724111111","adresaaaa"))
    
    
    def testModify(self):
        
        self.assertEqual(self.repo.get(1).getId(),1)
        self.assertEqual(self.repo.get(1).getName(),"Ana")
        self.assertEqual(self.repo.get(1).getPhone(),"0742123456")
        self.assertEqual(self.repo.get(1).getAddress(),"Addressss")
        
        self.assertRaises(PersonRepositoryException, self.repo.modify, person("99","Maria","0724111111","adresaaaa"))
        self.repo.modify(person("1","Maria","0724111111","adresaaaa"))
        

    
    