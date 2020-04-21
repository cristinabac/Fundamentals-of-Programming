'''
Created on Nov 10, 2018

@author: hp840
'''
from domain.person import person
from repository.personRepository import PersonRepositoryException
from repository.activityRepository import ActivityRepositoryException
from domain.activity import activity
from control.activityController import activityControllerException
from control.personController import personControllerException

class Menu:
    
    def __init__(self, controller_person,controller_activity, controller_undo):
        self.__controller_person = controller_person
        self.__controller_activity = controller_activity
        self.__controller_undo = controller_undo
    
    def __add_person(self):
        pid = input("Person id :")
        pname = input("Person name :")
        pphone = input("Person phone :")
        paddress = input("Person address :")
        try:
            pers = self.__controller_person.createPerson(pid,pname,pphone,paddress)
            print("Person '" + pers.getName() +"' saved" )
        except personControllerException as ex:
            print(ex)
        except PersonRepositoryException as ve:
            print (ve)
    
    def __remove_person(self):
        pid = input("Person id :")
        
        try:
            pid=int(pid)
            self.__controller_person.remove(pid)
            print ("Person successfully removed")
        except PersonRepositoryException as ve:
            print(ve)
        except ValueError:
            print("Id should be integer")
    
    def __list_persons(self):
        dictionary = self.__controller_person.getAllPersons()
        for i in dictionary:
            print(dictionary[i])
    
    def __update_person(self):
        pid = input("Person id :")
        pname = input("Person new name :")
        pphone = input("Person new phone :")
        paddress = input("Person new address :")
        try:
            self.__controller_person.update(pid,pname,pphone,paddress)
        except PersonRepositoryException as ve:
            print (ve)   
        except personControllerException as ex:
            print(ex)
          
        
    def __add_activity(self):
        aid = input("Activity id :")
        apids = input("Person id's (separated by spaces):")
        adate = input("Activity date :")
        atime = input("Activity time :")
        adescr = input("Activity description :")
        apids = apids.split(" ")
        try:
            self.__controller_activity.createActivity(aid,apids,adate,atime,adescr)
            print("Activity saved")
        except activityControllerException as ve:
            print(ve)
        except ActivityRepositoryException as ve:
            print(ve)
    
    def __list_activities(self):
        dictionary = self.__controller_activity.getAllActivities()
        for i in dictionary:
            print(dictionary[i])
    
    def __remove_activity(self):
        aid = input("Activity id :")
        try:
            aid = int(aid)
            self.__controller_activity.remove(aid)
            print ("Activity successfully removed")
        except ActivityRepositoryException as ve:
            print(ve)
        except ValueError:
            print("Id should be integer")
            
    def __update_activity(self):
        aid = input("Activity id :")
        apids = input("Person new id's (separated by spaces) :")
        adate = input("Activity new date :")
        atime = input("Activity new time :")
        adescr = input("Activity new description :")
        apids = apids.split(" ")
        try:
            self.__controller_activity.update(aid,apids,adate,atime,adescr)
        except ActivityRepositoryException as ve:
            print(ve)
        except activityControllerException as ve:
            print(ve)
    
    def __searchPersonByName(self):
        name = input("The searched name:")
        if name.isalpha()==False:
            raise ValueError ("The entered name must contain only letters")
        lst = self.__controller_person.searchPersonByName(name)
        for i in lst:
            print(i)
    
    def __searchPersonByPhone(self):
        phone = input("The searched phone number:")
        if phone.isdigit()==False:
            raise ValueError ("The entered phone number must contain only digits")
        lst = self.__controller_person.searchPersonByPhone(phone)
        for i in lst:
            print(i)
    
    def __searchActivityByDate(self):
        date = input("The searched date:")
        lst = self.__controller_activity.searchActivityByDate(date)
        for i in lst:
            print(i)
    
    def __searchActivityByTime(self):
        time = input("The searched time:")
        lst = self.__controller_activity.searchActivityByTime(time)
        for i in lst:
            print(i)
            
    def __searchActivityByDescription(self):
        descr = input("The searched description:")
        lst = self.__controller_activity.searchActivityByDescription(descr)
        for i in lst:
            print(i)
    
    def __activitiesForGivenDay(self):
        day = input("The day: ")
        if day.isdigit() == False:
            raise ValueError ("The day should be an integer!")
        day = int(day)
        if day <1 or day > 31:
            raise ValueError ("The day should be between 1 and 31")
        lst = self.__controller_activity.activitiesDay_sortByDateTime(day)
        for i in lst:
            print(i)
            
    def __busyestDays(self):
        lst = self.__controller_activity.busyestDays()
        for i in lst:
            print(i)
    
    def __activitiesForGivenPerson(self):
        pid = input("Person's ID: ")
        if pid.isdigit() == False:
            raise ValueError ("The person's ID should be an integer!")
        pid = int(pid)
        try:
            lst = self.__controller_activity.activitiesForPerson(pid)
            print("The person with the ID - " + str(pid) + " - will participate to the following activities: ")
            for i in lst:
                print(i)
        except activityControllerException as ex:
            print(ex)
    
    def __sortPersonsByNumberOfActivities(self):
        lst = self.__controller_activity.sortPersonsByNumberOfActivities()
        for i in lst:
            print(i)
        
    def show(self):
        while True:
            print("1. Add person")
            print("2. List persons")
            print("3. Remove person by id")
            print("4. Add activity")
            print("5. List activities")
            print("6. Remove activity by id")
            print("7. Update a person (by id)")
            print("8. Update an activity (by id)")
            print("9. Search for persons by name")
            print("10. Search for persons by phone number")
            print("11. Search for activities by date")
            print("12. Search for activities by time")
            print("13. Search for activities by description")
            print("14. List the activities for a given day, in orer of their date")
            print("15. Busiest days. This will provide the list of upcoming days with activities, sorted in descending order of the number of activities in each day.")
            print("16. Activities with a given person. List all upcoming activities to which a given person will participate. The person is given by ID.")
            print("17. List all persons in the address book, sorted in descending order of the number of upcoming activities to which they will participate.")
            print("18. Undo")
            print("19. Redo")
            print("0. Exit")
            cmd = input("Enter your command: ")
            print('\n')
            if cmd == "1":
                self.__add_person()
            
            elif cmd == "2":
                print('\n')
                self.__list_persons()
                print('\n')
            
            elif cmd == "3":
                self.__remove_person()
            
            elif cmd == "4":
                self.__add_activity()
            
            elif cmd == "5":
                print('\n')
                self.__list_activities()
                print('\n')
                
            elif cmd == "6":
                self.__remove_activity()
                
            elif cmd == "7":
                self.__update_person()
            
            elif cmd == "8":
                self.__update_activity()
                
            elif cmd == "9":
                print('\n')
                try:
                    self.__searchPersonByName()
                except ValueError as ve:
                    print(ve)
                print('\n')
            
            elif cmd == "10":
                print('\n')
                try:
                    self.__searchPersonByPhone()
                except ValueError as ve:
                    print(ve)
                print('\n')
            
            elif cmd == "11":
                print('\n')
                self.__searchActivityByDate()
                print('\n')
                
            elif cmd == "12":
                print('\n')
                self.__searchActivityByTime()
                print('\n')
            
            elif cmd == "13":
                print('\n')
                self.__searchActivityByDescription()
                print('\n')
            
            elif cmd == "14":
                print('\n')
                try:
                    self.__activitiesForGivenDay()
                except ValueError as ve:
                    print(ve)
                print('\n')
            
            elif cmd == "15":
                print('\n')
                self.__busyestDays()
                print('\n')
            
            elif cmd == "16":
                print('\n')
                try:
                    self.__activitiesForGivenPerson()
                except ValueError as ve:
                    print(ve)
                print('\n')
            
            elif cmd == "17":
                print('\n')
                self.__sortPersonsByNumberOfActivities()
                print('\n')
            
            elif cmd == "0":
                return
            
            elif cmd == "18":
                if self.__controller_undo.undo() == False:
                    print("No more undos!")
            
            elif cmd == "19":
                if self.__controller_undo.redo() == False:
                    print("No more redos!")
            
            else:
                print("INVALID COMMAND!")
                
            print('\n')
        