'''
Created on Dec 1, 2018

@author: hp840
'''
from repository.personRepository import PersonRepository
import pickle
from repository.activityRepository import ActivityRepository

class picklePersonFileRepository(PersonRepository):
    
    def __init__(self, filename = "persons.pickle"):
        PersonRepository.__init__(self)
        self.__filename = filename
        self.__loadFromFile()
        
    def store(self, pers):
        PersonRepository.store(self, pers)
        self.__storeToFile()
    
    def remove(self, persId):
        PersonRepository.remove(self, persId)
        self.__storeToFile()
    
    def modify(self, pers):
        PersonRepository.modify(self, pers)
        self.__storeToFile()
    
    def __loadFromFile(self):
        f = open(self.__filename, "rb")
        try:
            lst = pickle.load(f)
            for i in lst:
                self._persons[i.getId()] = i
        except EOFError:
            self._persons = {}
        except Exception as e:
            raise e
        finally:
            f.close()
            
    def __storeToFile(self):
        f = open(self.__filename,"wb")
        lst = []
        for i in self._persons:
            lst.append(self._persons[i])
        pickle.dump(lst, f)
        f.close()
        
        
class pickleActivityFileRepository(ActivityRepository):
    
    def __init__(self, filename = "activities.pickle"):
        ActivityRepository.__init__(self)
        self.__filename = filename
        self.__loadFromFile()
        
    def store(self, pers):
        ActivityRepository.store(self, pers)
        self.__storeToFile()
    
    def remove(self, persId):
        ActivityRepository.remove(self, persId)
        self.__storeToFile()
    
    def modify(self, pers):
        ActivityRepository.modify(self, pers)
        self.__storeToFile()
    
    def __loadFromFile(self):
        f = open(self.__filename, "rb")
        try:
            lst = pickle.load(f)
            for i in lst:
                self._activities[i.getId()] = i
        except EOFError:
            self._activities = {}
        except Exception as e:
            raise e
        finally:
            f.close()
            
    def __storeToFile(self):
        f = open(self.__filename,"wb")
        lst = []
        for i in self._activities:
            lst.append(self._activities[i])
        pickle.dump(lst, f)
        f.close()