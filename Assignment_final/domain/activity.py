'''
Created on Nov 10, 2018

@author: hp840
'''
import datetime
import unittest

class activity:
    '''
    parameter - !exception! - how is stored 
    
    activityId - !only digits! - INT
    personIds - !only digits and exists in the list of persons! - LIST OF STRINGS - THEY MUST BE INTEGER NUMBERS
    activityDate - !date format, YYYY-MM-DD! - DATE
    activityTime - !time format, H:M:S (ex:   12:25:00)! - TIME
    activityDescription - STRING
    
    Initially, all params are strings
    '''
    def __init__(self, activityId, personIds, activityDate, activityTime, activityDescription):
        
        self._id = int(activityId)
        self._personIds = []
        for i in personIds:
            self._personIds.append(i)
        self._date = datetime.datetime.strptime(activityDate, '%Y-%m-%d').date()
        self._time = datetime.datetime.strptime(activityTime, '%H:%M:%S').time()
        self._description = activityDescription
    
    def getId(self):
        return self._id
    
    def getPersonIds(self):
        return self._personIds
    
    def getDate(self):
        return self._date
    
    def getTime(self):
        return self._time
    
    def getDescription(self):
        return self._description
    
    def setId(self, newId):
        self._id = int(newId)
    
    def setPersonIds(self, newPersonIds):
        self._personIds = []
        for i in newPersonIds:
            self._personIds.append(i)
    
    def setDate(self, newDate):
        self._date = datetime.datetime.strptime(newDate, '%Y-%m-%d').date()
    
    def setTime(self, newTime):
        self._time =  datetime.datetime.strptime(newTime, '%H:%M:%S').time()
    
    def setDescription(self, newDescription):
        self._description = newDescription
    
    def __str__(self):
        return str(self._id) + '  -  ' + ",".join(self._personIds) + '  -  ' + str(self._date) + '  -  ' + str(self._time) + '  -  ' + self._description

def testActivity():
    
    activity1 = activity("1",["2","1"],"2001-12-06","04:57:00","Description 3")
    assert activity1.getDate() == datetime.datetime.strptime('2001-12-06','%Y-%m-%d').date() 
    assert activity1.getId() == 1
    assert activity1.getPersonIds() == ["2","1"]  
    assert activity1.getDescription() == "Description 3"
    activity2 = activity("23",["3"],"2001-12-08","05:30:00","Description 4")
    assert (activity2.getDate() - activity1.getDate()).days == 2
    
    activity3 = activity("66",["3333","1"],"2012-11-12","08:25:00","Description 6")
    assert activity3.getTime() == datetime.datetime.strptime('08:25:00', '%H:%M:%S').time()
    assert activity3.__str__() == "66  -  3333,1  -  2012-11-12  -  08:25:00  -  Description 6"
    
    activity4 = activity("77",["777"],"2013-10-4","13:30:00","Description lalala")
    activity4.setDate("2012-10-5")
    assert activity4.getDate() == datetime.datetime.strptime('2012-10-5','%Y-%m-%d').date()
    activity4.setId("100") 
    assert activity4.getId() == 100
    activity4.setId(200) 
    assert activity4.getId() == 200
    activity4.setPersonIds(["3","4","5"])
    assert activity4.getPersonIds() == ["3","4","5"]
    activity4.setTime("08:00:00")
    assert activity4.getTime()== datetime.datetime.strptime('08:00:00','%H:%M:%S').time()
    activity4.setDescription("newDescription")
    assert activity4.getDescription()=="newDescription"



testActivity()




class unittestActivity(unittest.TestCase):
    
    def testactivity(self):
        
        activity1 = activity("1",["2","1"],"2001-12-06","04:57:00","Description 3")
        self.assertEqual( activity1.getDate(), datetime.datetime.strptime('2001-12-06','%Y-%m-%d').date() )
        self.assertEqual(activity1.getId(), 1)
        self.assertEqual( activity1.getPersonIds(), ["2","1"]  )
        self.assertEqual( activity1.getDescription(), "Description 3")
        
        
        activity4 = activity("77",["777","2","100"],"2013-10-4","13:30:00","Description lalala")
        activity4.setDate("2012-10-5")
        self.assertEqual( activity4.getDate(), datetime.datetime.strptime('2012-10-5','%Y-%m-%d').date())
        activity4.setId("100") 
        self.assertEqual( activity4.getId(), 100)
        activity4.setId(200) 
        self.assertEqual(activity4.getId(), 200)
        activity4.setPersonIds(["1","2"])
        self.assertEqual( activity4.getPersonIds(), ['1','2'])
        activity4.setTime("08:00:00")
        self.assertEqual(activity4.getTime(),datetime.datetime.strptime('08:00:00','%H:%M:%S').time())
        activity4.setDescription("newDescription")
        self.assertEqual( activity4.getDescription(),"newDescription")