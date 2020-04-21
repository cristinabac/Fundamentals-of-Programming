'''
Created on Dec 1, 2018

@author: hp840
'''
from repository.personRepository import PersonRepository,\
    PersonRepositoryException
from repository.memoryListInitialize import initializeActivityList
from domain.person import person
from repository.activityRepository import ActivityRepository,\
    ActivityRepositoryException
from domain.activity import activity


class PersonFileRepository(PersonRepository):
    
    def __init__(self, filename="persons.txt"):
        PersonRepository.__init__(self)
        self.__filename = filename
        self.__loadFromFile()
    
    def __loadFromFile(self):
        try:
            f = open(self.__filename,"r")
            line = f.readline().strip()
            while line != "":
                myline = line.split(",")
                pers = person(myline[0],myline[1],myline[2],myline[3].strip())
                PersonRepository.store(self, pers)
                line = f.readline().strip()
        except IOError as e:
            raise PersonRepositoryException("Cannot load file : "+ str(e))
        finally:
            f.close()
    
    def store(self, pers):
        PersonRepository.store(self, pers)
        self.__storeToFile()
    
    def remove(self, persId):
        PersonRepository.remove(self, persId)
        self.__storeToFile()
    
    def modify(self, pers):
        PersonRepository.modify(self, pers)
        self.__storeToFile()
        
    def __storeToFile(self):
        try:
            f = open(self.__filename, "w")
            persons = PersonRepository.getAllPersons(self)
            for i in persons:
                f.write( str(persons[i].getId()) + ',' + persons[i].getName() + ',' + persons[i].getPhone() + ',' + persons[i].getAddress() + '\n' )
        except IOError as e:
            raise PersonRepositoryException("Cannot store to file : "+ str(e))
        f.close()
        
        
class ActivityFileRepository(ActivityRepository):
    
    def __init__(self, _filename = "activities.txt"):
        ActivityRepository.__init__(self)
        self.__filename = _filename
        self.__loadFromFile()
    
    def __loadFromFile(self):
        if self.__filename == "":
            initializeActivityList(self)
        else:
            try:
                f = open(self.__filename,"r")
                line = f.readline().strip()
                while line != "":
                    myline = line.split(",")
                    myline[1] = myline[1].split(" ")
                    act = activity(myline[0],myline[1],myline[2],myline[3],myline[4].strip())
                    ActivityRepository.store(self, act)
                    line = f.readline().strip()
            except IOError as e:
                raise ActivityRepositoryException("Cannot load file : " + str(e))
            finally:
                f.close()
    
    def store(self, pers):
        PersonRepository.store(self, pers)
        self.__storeToFile()
    
    def remove(self, actId):
        ActivityRepository.remove(self, actId)
        self.__storeToFile()
    
    def modify(self, act):
        ActivityRepository.modify(self, act)
        self.__storeToFile()
        
    def __storeToFile(self):
        try:
            f = open(self.__filename, "w")
            activities = ActivityRepository.getAllActivities(self)
            for i in activities:
                f.write( str(activities[i].getId()) + ',' + " ".join(activities[i].getPersonIds()) + ',' + str(activities[i].getDate()) + ',' + str(activities[i].getTime()) + ',' + activities[i].getDescription() + '\n' )
        except IOError as e:
            raise ActivityRepositoryException("Cannot store to file : " + str(e))
        finally:
            f.close()
        