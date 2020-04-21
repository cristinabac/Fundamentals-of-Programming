'''
Created on Nov 10, 2018

@author: hp840
'''
import unittest
from domain.activity import activity

class ActivityRepositoryException(Exception):
    pass


class ActivityRepository:
    '''
    Stores the activities in the memory
    '''
    
    def __init__(self):
        self._activities = {}
    
    def clear(self):
        '''
        Clears all activities
        '''
        self._activities = {}
    
    def size(self):
        '''
        Returns the number of objects
        '''
        return len(self._activities)
    
    def store(self, act):
        '''
        Stores an activity in the memory
        act - the activity
        Exception : If an activity with that id already exists
                    Activities must not overlap!  - do not have the same date and time
        '''
        for i in self._activities:
            if self._activities[i].getDate() == act.getDate() and self._activities[i].getTime() == act.getTime():
                raise ActivityRepositoryException("Activities must not overlap! They should not have the same date and time!")
        if act.getId() in self._activities:
            raise ActivityRepositoryException("The specified ID already exists")
        else:
            self._activities[act.getId()] = act
    
    def addPersonIdToAnActivity(self, actId, persId):
        '''
        Adds a new person to the list of person id's for a specified activity (given by Id)
        '''
        for i in self._activities:
            if i == actId:
                lst = self._activities[i].getPersonIds()
                lst.append(str(persId))
                self._activities[i].setPersonIds(lst)
    
    def removesPersonIdFromAnActivity(self, actId, persId):
        for i in self._activities:
            if i == actId:
                lst = self._activities[i].getPersonIds()
                lst.remove(str(persId))
                self._activities[i].setPersonIds(lst)
        
    def get(self, Id):
        try:
            return self._activities[Id]
        except KeyError:
            raise ActivityRepositoryException("The Id does not exist")
    
    def remove(self,actId):
        '''
        Removes the activity with the specified id
        actId - the spcified id
        Exception : An activity with the specified ID does not exist
        '''
        if actId in self._activities:
            self._activities.pop(actId)
        else:
            raise ActivityRepositoryException("An activity with the specified ID does not exist")
    
    def getAllActivities(self):
        '''
        Returns all objects
        '''
        return self._activities
    
    def modify(self, act):
        '''
        Modifies an activity
        act - Activity
        Exception : If an activity with the specified ID does not exist
        '''
        try:
            self._activities[act.getId()]
        except KeyError:
            raise ActivityRepositoryException("An activity with the specified ID does not exist")
        self._activities[act.getId()] = act



class testActivityRepo(unittest.TestCase):
    
    def setUp(self):
        self.repo = ActivityRepository()
        testList = [activity("1", ["1"], "2017-11-11", "08:00:00", "Description 1 lala"), activity("2", ["1"], "2016-11-06", "09:00:00", "Description 2 aa")]
        for i in testList:
            self.repo.store(i)
            self.assertEqual(self.repo.get(i.getId()), i)
            
            
    def testStore(self):
        
        self.assertRaises(ActivityRepositoryException, self.repo.store, activity("1", ["1"], "2018-11-06", "09:00:00", "Sport aaa"))
        self.repo.store(activity("15", ["1"], "2018-11-06", "09:00:00", "Sport aaa"))
    
    
    def testRemove(self):
        
        self.assertRaises(ActivityRepositoryException, self.repo.remove, 27)
        self.assertEqual(self.repo.size(),2)
        self.repo.remove(1)
        self.assertEqual(self.repo.size(),1)
        self.assertRaises(ActivityRepositoryException, self.repo.remove, 1)
        
    
    def testModify(self):
        
        self.assertEqual(self.repo.get(1).getId(),1)
        self.assertEqual(self.repo.get(1).getDescription(),"Description 1 lala")
        
        self.assertRaises(ActivityRepositoryException, self.repo.modify, activity("3", ["1"], "2018-11-06", "09:00:00", "Sport aaa"))
        self.repo.modify(activity("1", ["1","2"], "2018-11-06", "09:00:00", "Sport aaa"))

            