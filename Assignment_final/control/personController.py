'''
Created on Nov 10, 2018

@author: hp840
'''
from domain.person import person
from domain.personValidator import personValidator,personValidatorException
import datetime
import unittest
from repository.personRepository import PersonRepository,PersonRepositoryException
from repository.activityRepository import ActivityRepository
from control.undoController import functionCall, operation, undoController,\
    cascadeOperation

class personControllerException(Exception):
    pass

class personController:
    
    def __init__(self, repo, act_repo, undoContr):
        self.__repository = repo
        self.__activityRepo = act_repo
        self.__undoController = undoContr
            
    
    def createPerson(self, pid, name, phone, address):
        '''
        Stores and returns a new person
        Input : pid, name, phone, address - 4 strings
                These must be valid! -> They are validated by personValidator (verifies if they are the right data format)
        Output : pers - the person
        '''
        try:
            personValidator.validate(self, pid,name,phone,address)
        except personValidatorException as ex:
            raise personControllerException(ex)
        pers = person(pid,name,phone,address)
        self.__repository.store(pers)
        
        undo = functionCall(self.remove, int(pid))
        redo = functionCall(self.createPerson,pid, name, phone, address)
        oper = operation(undo, redo)
        self.__undoController.addOperation(oper)
        
        
        return pers
    
    
    def remove(self, pid):
        '''
        Removes a person by their Id
        Input : pid - an integer
        Exception : If a person with that id does not exist -> repository exception
            ! When we remove a person, we also remove him from the activities he participates to
             If the there are activities where only he participates, the activity will be removed
        '''
        pers = self.__repository.get(int(pid))
        self.__repository.remove(pid)
        activityDict = self.__activityRepo.getAllActivities()
        activities_to_update =[]
        activities_to_add =[]
        #idsToRemove =[]
        for act in activityDict:
            if str(pid) in activityDict[act].getPersonIds():
                if len(activityDict[act].getPersonIds()) == 1:
                    #idsToRemove.append(act)
                    activities_to_add.append(activityDict[act])
                else:
                    activities_to_update.append(activityDict[act])
                    #lst = activityDict[act].getPersonIds()
                    #lst.remove(str(pid))
                    #activityDict[act].setPersonIds(lst)
        #for i in idsToRemove:
        #    self.__activityRepo.remove(i)
        
        redo = functionCall(self.__repository.remove,pid)
        undo = functionCall(self.__repository.store, pers)
        oper = operation(undo, redo)
        
        co = cascadeOperation()
        co.add(oper)
        
        for act in activities_to_update:
            self.__activityRepo.removesPersonIdFromAnActivity(act.getId(), pid)
            redo = functionCall(self.__activityRepo.removesPersonIdFromAnActivity,act.getId(), pid)
            undo = functionCall(self.__activityRepo.addPersonIdToAnActivity, act.getId(), pid)
            oper = operation(undo, redo)
            co.add(oper)
            
        for activity in activities_to_add:
            self.__activityRepo.remove(activity.getId())
            undo = functionCall(self.__activityRepo.store, activity)
            redo = functionCall(self.__activityRepo.remove,activity.getId() )
            oper = operation(undo, redo)
            co.add(oper)
        
        self.__undoController.addOperation(co)        
        
    def getAllPersons(self):
        '''
        Returns all persons
        '''
        return self.__repository.getAllPersons()
    
    
    def update(self, pid,name,phone,address):
        '''
        Updates a person. The person is find by Id
        Input : pid, name, phone, address - strings
        Exception : If any data - person id's, name, phone or address - does not respect the data format
        '''
        try:
            personValidator.validate(self, pid,name,phone,address)
        except personValidatorException as ex:
            raise personControllerException(ex)
        pers = person(pid,name,phone,address)
        initial_person = self.__repository.get(int(pid))
        self.__repository.modify(pers)
        
        undo = functionCall(self.update, str(initial_person.getId()), initial_person.getName(), initial_person.getPhone(), initial_person.getAddress())
        redo = functionCall(self.update,str(pers.getId()), pers.getName(), pers.getPhone(), pers.getAddress())
        oper = operation(undo, redo)
        self.__undoController.addOperation(oper)
        
        
    def searchPersonByName(self, name):
        '''
        Search for the persons with a given name or part of the name (case-insensitive, partial string-matching)
        Input : name - string (can be substring of the name)
        Output : Returns all matching persons as a list of objects
                 Returns an empty list if no match was found
        '''
        personDict = self.__repository.getAllPersons()
        matchList = []
        for i in personDict:
            if name.lower() in personDict[i].getName().lower():
                matchList.append(personDict[i])
        return matchList
        
        
    def searchPersonByPhone(self, phone):
        '''
        Search for the persons with a given phone or part of the phone (partial string-matching)
        Input : phone - string (can be substring of the person's phone number)
        Output : Returns all matching persons as a list of objects
                 Returns an empty list if no match was found
        '''
        personDict = self.__repository.getAllPersons()
        matchList = []
        for i in personDict:
            if phone in personDict[i].getPhone():
                matchList.append(personDict[i])
        return matchList


class testPersonController(unittest.TestCase):
    
    def setUp(self):
        
        self.repo = PersonRepository()
        self.act_repo = ActivityRepository()
        undoCtrl = undoController()
        self.repo.store(person("1","Ana MAria","0742111111","Address aa"))
        self.controller = personController(self.repo, self.act_repo, undoCtrl)
    
    
    def testAddPerson(self):
        
        self.assertRaises(PersonRepositoryException, self.controller.createPerson, "1", "Carina", "0222222", "Another address")
        self.controller.createPerson("2", "Paula", "0264111111", "Address anajaj")
        self.assertRaises(personControllerException, self.controller.createPerson,"a", "Carina", "0222222", "Another address")
        self.assertRaises(personControllerException, self.controller.createPerson,"5", "Carina", "02222b22", "Another address")
        self.assertRaises(personControllerException, self.controller.createPerson,"5", "Carina 2 Ana", "0222222", "Another address")
    
    
    def testRemovePerson(self):
        
        self.assertRaises(PersonRepositoryException, self.controller.remove, 6)
        self.controller.remove(1)
    
    
    def testUpdatePerson(self):
        
        self.assertRaises(PersonRepositoryException, self.controller.update, "3", "Name", "0766666", "Addressss")
        self.assertRaises(personControllerException, self.controller.update, "1", "Name7", "0766666", "Addressss")
        self.assertRaises(personControllerException, self.controller.update, "1", "Name", "076a6666", "Addressss")
        self.controller.update("1", "New Name", "444", "address")
    
    
    def testSearchPersonByName(self):
        
        pers1 = self.repo.get(1) #gets the person with id 1
        pers2 = person("2","Maria","072222222","Address abcd")
        self.repo.store(pers2)
        
        self.assertEqual(self.controller.searchPersonByName("maria"), [pers1, pers2])
        self.assertEqual(self.controller.searchPersonByName("ana"), [pers1])
        self.assertEqual(self.controller.searchPersonByName("alexandra"), [])
        self.assertEqual(self.controller.searchPersonByName("4"), [])
    
    
    def testSearchPersonByPhone(self):
        
        pers1 = self.repo.get(1) #gets the person with id 1
        pers2 = person("2","Maria","072222222","Address abcd")
        self.repo.store(pers2)
        
        self.assertEqual(self.controller.searchPersonByPhone("07"), [pers1, pers2])
        self.assertEqual(self.controller.searchPersonByPhone("ana"), [])
        self.assertEqual(self.controller.searchPersonByPhone("222222"), [pers2])
        self.assertEqual(self.controller.searchPersonByPhone("1"), [pers1])