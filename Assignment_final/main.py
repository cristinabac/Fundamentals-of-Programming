from control.personController import personController
from control.activityController import activityController
from repository.activityRepository import ActivityRepository
from repository.personRepository import PersonRepository
from ui.ui import Menu
from control.undoController import undoController
from repository.memoryListInitialize import initializePersonList,\
    initializeActivityList
from repository.fileRepository import PersonFileRepository,\
    ActivityFileRepository
from repository.pickleFileRepository import picklePersonFileRepository,\
    pickleActivityFileRepository
'''
repository_person = PersonRepository()
repository_activity = ActivityRepository()

initializePersonList(repository_person)
initializeActivityList(repository_activity)

controller_undo = undoController()
controller_person = personController(repository_person, repository_activity, controller_undo)
controller_activity = activityController(repository_activity, repository_person, controller_undo)
'''

'''
controller_person.createPerson("1", "Ana", "0742123456", "Address 1 , Romania")
controller_person.createPerson("2", "Maria", "0742123123", "Address 2 , Romania")
controller_person.createPerson("3", "Baciu Ana", "0743111111", "Address 3 , Romania")
controller_person.createPerson("4", "Pop Anamaria", "0742111111", "Address 4 , Romania")
controller_person.createPerson("5", "Popescu Ion", "0742123456", "Address 5 , Romania")
controller_person.createPerson("6", "John", "0742112233", "Address 6, lla, aaa")
controller_person.createPerson("7", "Mary Anna", "0742998877", "Address 7, ahaha , Romania")
controller_person.createPerson("8", "Brown Brad", "0742654321", "Address 8, street b, ap. b , Romania")
controller_person.createPerson("9", "Moldovan Ionel", "0742558877", "Address 9, street 9, ap. 999")
controller_person.createPerson("10", "Ana Maria", "0742777999", "Address 10, street Abc, number 123")

controller_person.createPerson("11", "Gigi", "0742775699", "Romania, Cluj")
controller_person.createPerson("12", "Marry Judy", "0742777966", "Romania, Brasov")
controller_person.createPerson("13", "Anna Brown", "0742577999", "Romania, street abc")
controller_person.createPerson("14", "Victoria Harsh", "0742997999", "Cluj, street Abc, number 123")
controller_person.createPerson("15", "Jane Eyre", "0742775544", "Brasov, street A22, number 1")
controller_person.createPerson("16", "Catherine Blue", "0742777343", "Bucharest, street 2, number 13")
controller_person.createPerson("17", "Marry Marry", "0742771199", "Bucharest, street x, number 5")
controller_person.createPerson("18", "Pop Corina", "0742777991", "Bucharest, street c, number 7")
controller_person.createPerson("19", "Popescu Ana", "0742777992", "Bucharest, street w, number 23")
controller_person.createPerson("20", "Marian Alex", "0742777993", "Cluj-Napoca, street qqq, number 134")
controller_person.createPerson("21", "Radu Marin", "0742777994", "Arad, street waaa, number 15")
controller_person.createPerson("22", "Alin Vasile", "0742777995", "Campeni, street c, number 156")
controller_person.createPerson("23", "Popan Alexandru", "0742777996", "Bacau, street Abc, number 45")
controller_person.createPerson("24", "Vasilescu Ion", "0742777997", "Valcele, street Abc, number 23")
controller_person.createPerson("25", "Mara Lara", "0742777998", "Turda, street Abc, number 12")
controller_person.createPerson("26", "Ionescu Adrian", "0742777990", "Turda, street Abc, number 33")
controller_person.createPerson("27", "Ion Ionel", "0742777123", "Address 10, street Abc, number 123")
controller_person.createPerson("28", "Thomas Anders", "0742777234", "Address 280")
controller_person.createPerson("29", "Marry Anderson", "0742777456", "Address 290")
controller_person.createPerson("30", "Cathy Lake", "0742777567", "Address 300")
controller_person.createPerson("31", "Mariana", "0742777678", "Address 310")
controller_person.createPerson("32", "George", "0742777789", "Address 320")
controller_person.createPerson("33", "Andrei", "0742123999", "Address 33")
controller_person.createPerson("34", "Daniel", "0742122999", "Address 34")
controller_person.createPerson("35", "Adrian", "0742133999", "Address 35")
controller_person.createPerson("36", "Amanda", "0742144999", "Address 36")
controller_person.createPerson("37", "Adina", "0742155999", "Address 37")
controller_person.createPerson("38", "Vlad", "0742166999", "Address 38")
controller_person.createPerson("39", "Sorin", "0742445999", "Address 39")
controller_person.createPerson("40", "Tom", "0742446999", "Address 40")
controller_person.createPerson("41", "Bob", "0742121234", "Address 41")
controller_person.createPerson("42", "Tommy", "0742114321", "Address 42")
controller_person.createPerson("44", "Bobby", "0742673904", "Address 44")
controller_person.createPerson("45", "Anna Karenina", "0742770099", "Address 450")
controller_person.createPerson("46", "Sarah", "0742700099", "Address 460")
controller_person.createPerson("47", "Samantha", "0742707999", "Address 470")
controller_person.createPerson("48", "Harold", "0742077999", "Address 480")
controller_person.createPerson("49", "Josh", "0740777999", "Address 490")
controller_person.createPerson("50", "Anisoara", "0740077999", "Address 500")
'''


'''
controller_activity.createActivity("1", ["1","2"], "2017-11-11", "08:00:00", "Description 1 lala")
controller_activity.createActivity("2", ["1"], "2016-11-06", "09:00:00", "Description 2 aa")
controller_activity.createActivity("13", ["2"], "2017-11-11", "18:00:00", "Description bbb cc ")
controller_activity.createActivity("14", ["3"], "2018-05-11", "12:30:00", "Description alala ssy aa bb")
controller_activity.createActivity("15", ["1"], "2018-11-06", "09:00:00", "Sport aaa")
controller_activity.createActivity("16", ["1"], "2019-11-06", "10:00:00", "Activity for students")
controller_activity.createActivity("17", ["2"], "2017-11-11", "11:00:00", "Sport aAa")
controller_activity.createActivity("18", ["2"], "2016-11-10", "12:00:00", "Sport bbb")
controller_activity.createActivity("19", ["1"], "2016-05-20", "19:00:00", "Description abc def")
controller_activity.createActivity("20", ["1"], "2019-12-25", "18:00:00", "Description Yes No")
controller_activity.createActivity("21", ["5","4"], "2019-05-20", "20:00:00", "Description aaa eee")
controller_activity.createActivity("22", ["7","5"], "2019-05-20", "09:00:00", "Description cccc")
controller_activity.createActivity("23", ["8"], "2019-05-20", "08:00:00", "Description abc vvvvvv")
controller_activity.createActivity("24", ["9","1","3"], "2019-05-20", "06:00:00", "Descr alalalala")
controller_activity.createActivity("25", ["8","2"], "2019-07-20", "13:00:00", "Aaaaaaaaaa")
controller_activity.createActivity("26", ["10","3"], "2019-08-20", "12:00:00", "SportAaa")
controller_activity.createActivity("27", ["9","1","2"], "2019-09-20", "11:00:00", "Descr iption")
controller_activity.createActivity("28", ["9"], "2019-10-20", "10:00:00", "a b c d ")
controller_activity.createActivity("29", ["9"], "2019-05-20", "23:00:00", "zz zzz zz")

controller_activity.createActivity("101", ["1","2","3","4"], "2019-05-20", "01:00:00", "Sport")
controller_activity.createActivity("102", ["9","10","11","23","25","33"], "2019-06-20", "23:00:00", "Reading")
controller_activity.createActivity("103", ["2","3","4","5","31","32","33","34","45","46"], "2019-07-20", "23:00:00", "Talk")
controller_activity.createActivity("104", ["9","21","22","23","24","1","3"], "2019-08-20", "23:00:00", "Communication")
controller_activity.createActivity("105", ["10","11","12","13","14","15","16","17","18","19","20","21"], "2019-09-20", "23:00:00", "Football")
controller_activity.createActivity("106", ["1","3","5","7","9"], "2019-10-20", "23:00:00", "Games")
controller_activity.createActivity("107", ["2","4","6","8","10","12","14","16"], "2019-11-20", "23:00:00", "Aaaa")
controller_activity.createActivity("108", ["1","2"], "2019-12-20", "23:00:00", "Ajjsjs")
controller_activity.createActivity("109", ["9"], "2019-04-20", "23:00:00", "Descr 109")
controller_activity.createActivity("110", ["10"], "2019-03-20", "23:00:00", "Descr 110")
controller_activity.createActivity("111", ["11"], "2019-02-20", "23:00:00", "Descr 111")
controller_activity.createActivity("112", ["12"], "2019-01-20", "23:00:00", "Descr 112")
controller_activity.createActivity("113", ["13"], "2019-05-21", "23:00:00", "Descr 113")
controller_activity.createActivity("114", ["14"], "2019-05-22", "23:00:00", "Descr 114")
controller_activity.createActivity("115", ["15"], "2019-05-23", "23:00:00", "Description 115")
controller_activity.createActivity("116", ["16"], "2019-05-24", "23:00:00", "Description 116")
controller_activity.createActivity("117", ["17"], "2019-05-25", "23:00:00", "Description 117")
controller_activity.createActivity("118", ["18"], "2019-05-26", "23:00:00", "Description 118")
controller_activity.createActivity("119", ["19"], "2019-05-27", "23:00:00", "Description 119")
controller_activity.createActivity("120", ["20"], "2019-05-28", "23:00:00", "Description 120")
controller_activity.createActivity("121", ["21"], "2019-05-29", "23:00:00", "Desc 121")
controller_activity.createActivity("122", ["22"], "2019-05-30", "23:00:00", "Desc 122")
controller_activity.createActivity("123", ["23"], "2019-05-01", "23:00:00", "Desc 123")
controller_activity.createActivity("124", ["24"], "2019-05-02", "23:00:00", "Desc 124")
controller_activity.createActivity("125", ["30"], "2019-05-03", "23:00:00", "Desc 125")
controller_activity.createActivity("126", ["31"], "2019-05-04", "23:00:00", "Desc 126")
controller_activity.createActivity("127", ["32"], "2019-05-05", "23:00:00", "Dscr 127")
controller_activity.createActivity("128", ["33"], "2019-05-05", "05:00:00", "Dscr 128")
controller_activity.createActivity("129", ["34"], "2019-05-05", "06:00:00", "Dscr 129")
controller_activity.createActivity("130", ["35"], "2019-05-05", "07:00:00", "Dscr 130")
controller_activity.createActivity("131", ["36"], "2019-05-05", "08:00:00", "Dscr 131")
controller_activity.createActivity("132", ["37"], "2019-05-05", "09:00:00", "Dscr 132")
controller_activity.createActivity("133", ["38"], "2019-05-05", "10:00:00", "Dscr 133")
'''


def readSettings():
    '''
    Reads the program's settings file
    Output: A dictionary containing the program settings
    '''
    f = open("settings_text.txt", "r")
    lines = f.read().split("\n")
    settings = {}
    
    for line in lines:
        setting = line.split("=")
        if len(setting) > 1:
            settings[setting[0]] = setting[1]
    f.close()
    return settings

settings = readSettings()

activitiesDict = None
personsDict = None

if settings['repository'] == "inmemory":
    personsDict = PersonRepository()
    activitiesDict = ActivityRepository()
    initializePersonList(personsDict)
    initializeActivityList(activitiesDict)
elif settings["repository"] == "CSV":   #CSV = comma separated values => reading from file
    personsDict = PersonFileRepository()  
    activitiesDict = ActivityFileRepository()
elif settings["repository"] == "binaryfiles":
    personsDict = picklePersonFileRepository()
    activitiesDict = pickleActivityFileRepository()


controller_undo = undoController()
controller_person = personController(personsDict, activitiesDict, controller_undo)
controller_activity = activityController(activitiesDict, personsDict, controller_undo)


ui = Menu(controller_person, controller_activity, controller_undo)

ui.show()
