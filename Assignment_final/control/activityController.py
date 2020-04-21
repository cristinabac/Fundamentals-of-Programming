from domain.activity import activity
from domain.activityValidator import activityValidatorException, activityValidator
import datetime
from repository.activityRepository import ActivityRepository, ActivityRepositoryException
import unittest
from repository.personRepository import PersonRepository, PersonRepositoryException
from domain.person import person
from control.undoController import *
from repository.iterable_assign9 import *

class activityControllerException(Exception):
    pass

class activityController:
    
    
    '''
          -----------------------
          FUNCTIONS ON ACTIVITIES
          -----------------------
    '''
    
    def __init__(self, repo, pers_repo, undoCtrl):
        self.__repository = repo
        self.__personRepo = pers_repo
        self.__undoController = undoCtrl
    
    
    def createActivity(self, aid, pids, adate, atime, adescr):
        '''
        Stores and returns a new activity
        Input : aid, adate, atime, adescr - 5 strings
                pids - a list of strings
                They must be valid! -> They are validated by activityValidator (verifies if they are the right data format)
        Exception : If the person id's does not exist in the list of persons
        Output : act - the activity
        '''
        try:
            activityValidator.validate(self, aid,pids,adate,atime,adescr)
        except activityValidatorException as ex:
            raise activityControllerException(ex)
        for i in pids:
            try:
                self.__personRepo.get(int(i))
            except PersonRepositoryException :
                raise activityControllerException("There are no persons with all the provided ID's")
        act = activity(aid,pids,adate, atime, adescr)
        self.__repository.store(act)
        
        undo = functionCall(self.remove, int(aid))
        redo = functionCall(self.createActivity,aid,pids, adate, atime, adescr)
        oper = operation(undo, redo)
        self.__undoController.addOperation(oper)
        
        return act
    
    
    def remove(self, aid):
        '''
        Removes an activity by its Id
        Input : aid - an integer
        Exception : If an activity with that id does not exist
        '''
        try:
            act = self.__repository.getAllActivities()[aid]
        except KeyError:
            pass
        
        self.__repository.remove(aid)
        
        redo = functionCall(self.remove, aid)
        undo = functionCall(self.createActivity,str(act.getId()), act.getPersonIds(), str(act.getDate()), str(act.getTime()), act.getDescription())
        oper = operation(undo, redo)
        self.__undoController.addOperation(oper)
        
    
    def getAllActivities(self):
        '''
        Returns all activities
        '''
        return self.__repository.getAllActivities()
    
    
    def update(self,aid,pids,adate,atime,adescr):
        '''
        Updates an activity. The activity is find by Id
        Input : aid, adate, atime, adescr - strings
                pids - a list of strings
        Exception : If any data does not respect the data format
                    If a person with that ID does not exist
        '''
        try:
            activityValidator.validate(self, aid, pids, adate, atime, adescr)
        except activityValidatorException as ex:
            raise activityControllerException(ex)
        try:
            for i in pids:
                self.__personRepo.get(int(i))
        except PersonRepositoryException :
            raise activityControllerException("There are no persons with all given Id's")
        act = activity(aid,pids,adate,atime,adescr)
        initial_activity = self.__repository.get(int(aid))
        self.__repository.modify(act)
        
        undo = functionCall(self.__repository.modify, initial_activity)
        redo = functionCall(self.__repository.modify, act)
        oper = operation(undo, redo)
        self.__undoController.addOperation(oper)
    
    
    def searchActivityByDate(self, date):
        '''
        Search for the activities with a given date or part of the date (partial string-matching)
        Input : date - string (can be substring of the activity date)
        Output : Returns all matching activities as a list of objects
                 Returns an empty list if no match was found
        '''
        activityDict = self.__repository.getAllActivities()
        matchList = []
        for i in activityDict:
            if date in str(activityDict[i].getDate()):
                matchList.append(activityDict[i])
        return matchList
    
    
    def searchActivityByTime(self, time):
        '''
        Search for the activities with a given time or part of the time (partial string-matching)
        Input : time - string (can be substring of the activity time)
        Output : Returns all matching activities as a list of objects
                 Returns an empty list if no match was found
        '''
        activityDict = self.__repository.getAllActivities()
        matchList = []
        for i in activityDict:
            if time in str(activityDict[i].getTime()):
                matchList.append(activityDict[i])
        return matchList
    
    
    def searchActivityByDescription(self, descr):
        '''
        Search for the activities with a given description or part of the description (case-insensitive, partial string-matching)
        Input : descr - string (can be substring of the activity description)
        Output : Returns all matching activities as a list of objects
                 Returns an empty list if no match was found
        '''
        activityDict = self.__repository.getAllActivities()
        matchList = []
        for i in activityDict:
            if descr.lower() in activityDict[i].getDescription().lower():
                matchList.append(activityDict[i])
        return matchList
    
    
    
    
    '''
          -------------------
          S T A T I S T I C S
          -------------------
    '''   
   
    # FIRST STATISTIC
    def activitiesDay_sortByDateTime(self, dayy):
        '''
        Sorts the activities (on a specific day) by their date and time
        Input : day - integer
        Returns a sorted list of objects
        '''
        activityDict = self.__repository.getAllActivities()
        #result = []
        result = iterableList()
        for i in activityDict:
            if activityDict[i].getDate().day == dayy:
                result.append(activitiesSort((activityDict[i]), activityDict[i].getDate(), activityDict[i].getTime()))
        
        #result.sort()
        #return result
        
        result.sort(dtoStatisic1cmp)
        lst  = []
        for i in result:
            lst.append(i)
        return lst
    
    
    # SECOND STATISTIC
    def busyestDays(self):
        '''
        Provide the list of upcoming days with activities, sorted in descending order of the number of activities in each day.
        '''
        activityDict = self.__repository.getAllActivities()
        #result = []
        result  = iterableList()
        
        aux = {}
        
        for i in activityDict:
            if activityDict[i].getDate() not in aux.keys(): # in the aux dictonary, the key will be the date
                aux[activityDict[i].getDate()] = 1
            else:
                aux[activityDict[i].getDate()] += 1
        
        noww = datetime.datetime.now().date()
        
        for i in aux: #i is the date
            if i > noww:
                result.append(activityDays(  aux[i], i ))
        
        #result.sort(key=None, reverse=True)
        #return result
        
        result.sort(dtoStatistic2cmp)
        lst  = []
        for i in result:
            lst.append(i)
        return lst
    
    #THIRD STATISTIC
    def activitiesForPerson(self, pid):
        '''
        Provides a list of all upcoming activities to which a given person will participate
        Input : pid - person's id - a string
        Exception : If there is no person with such Id
        '''
        try:
            self.__personRepo.get(int(pid))
        except KeyError :
            raise activityControllerException("There is no person with that ID")
        #result = []
        result = iterableList()
        activityDict = self.__repository.getAllActivities()
        #noww = datetime.datetime.now().date()
        
        for i in activityDict:
            if str(pid) in activityDict[i].getPersonIds():# and activityDict[i].getDate() > noww:
                result.append(activityDict[i])
        
        result = result.__filter__(self.dtoStatistic3filter)
        lst  = []
        for i in result:
            lst.append(i)
        return lst
        
        #return result
    
    
    #FOURTH STATISTIC
    def sortPersonsByNumberOfActivities(self):
        '''
        Provides a list of all persons in the address book, sorted in descending order of the number of upcoming activities to which they will participate.
        '''
        activityDict = self.__repository.getAllActivities()
        personDict = self.__personRepo.getAllPersons()
        
        aux = {}       # the key will be the person's Id;    the value will be the number of activities to which they will participate
        #result = []
        result = iterableList()
        noww = datetime.datetime.now().date()
        
        for i in activityDict:
            if activityDict[i].getDate() > noww:
                for j in range(len(activityDict[i].getPersonIds())):
                    if int(activityDict[i].getPersonIds()[j]) not in aux.keys():
                        aux[int(activityDict[i].getPersonIds()[j])] = 1
                    else:
                        aux[int(activityDict[i].getPersonIds()[j])] += 1
                    
        for i in personDict:
            if i not in aux.keys():
                aux[i] = 0
        
        for i in aux:
            result.append(personNumberOfAct(i,aux[i]))
        
        #result.sort(key=None, reverse=True)
        #return result
        result.sort(dtoStatistic4cmp)
        lst = []
        for i in result:
            lst.append(i)
            
        return lst
    
    def dtoStatistic3filter(self, a):
        '''
        Keep only activities that will take place in the future
        '''
        noww = datetime.datetime.now().date()
        return a.getDate() > noww
    
'''
Functions used for the sort function implemented by myself
Using an iterable list
'''
def dtoStatistic4cmp(a,b):
    '''
    Sorts descending by number of activities
    '''
    return a.getNumberOfAct() > b.getNumberOfAct()

def dtoStatisic1cmp(a,b):
    '''
    Sorts by date and time
    '''
    if a.getDatee() == b.getDatee():
        return a.getTimee() < b.getTimee()
    return a.getDatee() < b.getDatee()

def dtoStatistic2cmp(a,b):
    '''
    Sorts by number of activities
    '''
    return a.getNumberOfActivities() > b.getNumberOfActivities()




'''
               ---------------------------
               CLASSES USED FOR STATISTICS
               ---------------------------
               
    -> These are used if we need to sort, because we have to provide the rule for sorting, using the __lt__ (lower than) function 
'''
 
 
 
class activitiesSort:
    '''
    Used for the first statistic, which sorts the activities (on a specific day) by their date and time
    '''
    def __init__(self, act, date, time):
        self._act = act
        self._date = date
        self._time = time
    
    def __str__(self):
        return str(self._act)
    
    def __lt__(self, obj):
        if self._date == obj._date:
            return self._time < obj._time
        return self._date < obj._date
    
    def getTimee(self):
        return self._time
    
    def getDatee(self):
        return self._date


class activityDays:
    '''
    Used for the second statistic
    '''
    def __init__(self, numberOfActivities, day):
        self._activitiesNumber = numberOfActivities
        self._day = day
    
    def __str__(self):
        return 'day: ' + str(self._day) + ', number of activities: ' + str(self._activitiesNumber)
    
    def __lt__(self, obj):
        return self._activitiesNumber < obj._activitiesNumber
    
    def getNumberOfActivities(self):
        return self._activitiesNumber
    
class personNumberOfAct:
    '''
    Used for the fourth statistic, where we sort the persons by the number of activities to which they will participate
    '''
    def __init__(self,persId, numberOfActivities):
        self._persId = persId
        self._activitiesNumber = numberOfActivities
    
    def __str__(self):
        return 'person Id: ' + str(self._persId) + ', number of activities to which they will participate: ' + str(self._activitiesNumber)
    
    def __lt__(self, obj):
        return self._activitiesNumber < obj._activitiesNumber
    
    def getNumberOfAct(self):
        return self._activitiesNumber
    
    

'''
        -----------
        PY UNITTEST
        -----------
'''
   
   
   
class testActivityController(unittest.TestCase):
    
    def setUp(self):
        
        self.repo = ActivityRepository()
        self.personRepo = PersonRepository()
        self.undoCtrl = undoController()
        self.personRepo.store(person("1","Ana MAria","0742111111","Address aa"))
        self.repo.store(activity("10", "1", "2017-11-11", "08:00:00", "Description 1 lalaa"))
        self.controller = activityController(self.repo, self.personRepo, self.undoCtrl)
    
    
    def testAddActivity(self):
        
        self.assertRaises(ActivityRepositoryException, self.controller.createActivity, "10", ["1"], "2017-10-06", "12:00:00", "descr") #BECAUSE THE ID ALREADY EXISTS
        self.assertRaises(ActivityRepositoryException, self.controller.createActivity, "2", ["1"], "2017-11-11", "08:00:00", "descr") #BECAUSE THIS ACTIVITY OVERLAPS
        self.assertRaises(activityControllerException, self.controller.createActivity, "100", ["2"], "2017-10-11", "12:00:00", "descr") #BECAUSE THERE IS NO PERSON WITH ID=2
        self.assertRaises(activityControllerException, self.controller.createActivity, "100", ["1"], "2017-23-11", "12:00:00", "descr") #because of the date
        self.assertRaises(activityControllerException, self.controller.createActivity, "100", ["1","2"], "2017-10-11", "12:61:00", "descr") #because of the time
        
    
    def testRemoveActvity(self):
        
        self.assertRaises(ActivityRepositoryException, self.controller.remove, 2)
        self.controller.remove(10)
        
    
    def testUpdateActivity(self):
        
        self.assertRaises(ActivityRepositoryException, self.controller.update,"200", ["1"], "2013-11-11", "21:00:00", "descr")
        self.assertRaises(activityControllerException, self.controller.update,"10", ["1","2"], "2013-11-11", "21:00:00", "descr")
        self.assertRaises(activityControllerException, self.controller.update,"10", ["1"], "2013-13-11", "21:00:00", "descr")
        self.assertRaises(activityControllerException, self.controller.update,"10", ["1"], "2013-11-11", "21:67:00", "descr")
        self.controller.update("10", "1", "2013-11-11", "21:00:00", "descr")
        
    
    def testSearchActivityByDate(self):
        
        act1 = self.repo.get(10)
        act2 = activity("11",["1"],"2016-06-11","20:00:00","Descr iption aaa bb")
        self.repo.store(act2)
        
        self.assertEqual(self.controller.searchActivityByDate("11"), [act1,act2])
        self.assertEqual(self.controller.searchActivityByDate("2016"), [act2])
        self.assertEqual(self.controller.searchActivityByDate("17"), [act1])
        self.assertEqual(self.controller.searchActivityByDate("2018"), [])
        self.assertEqual(self.controller.searchActivityByDate("a"), [])
    
    
    def testSearchActivityByTime(self):
        
        act1 = self.repo.get(10)
        act2 = activity("11",["1"],"2016-06-11","20:30:00","Descr iption aaa bb")
        self.repo.store(act2)
        
        self.assertEqual(self.controller.searchActivityByTime("30"), [act2])
        self.assertEqual(self.controller.searchActivityByTime("30:00"), [act2])
        self.assertEqual(self.controller.searchActivityByTime("17"), [])
        self.assertEqual(self.controller.searchActivityByTime("00"), [act1, act2])
        self.assertEqual(self.controller.searchActivityByTime("08"), [act1])
        self.assertEqual(self.controller.searchActivityByTime("a"), [])
        
        
    def testSearchActivityByDescription(self):
        
        act1 = self.repo.get(10)
        act2 = activity("11",["1"],"2016-06-11","20:30:00","Descr iption aaa bb")
        self.repo.store(act2)
        
        self.assertEqual(self.controller.searchActivityByDescription("descr"), [act1,act2])
        self.assertEqual(self.controller.searchActivityByDescription("2"), [])
        self.assertEqual(self.controller.searchActivityByDescription("AA"), [act1,act2])
        self.assertEqual(self.controller.searchActivityByDescription("1"), [act1])
        self.assertEqual(self.controller.searchActivityByDescription("aAa"), [act2])