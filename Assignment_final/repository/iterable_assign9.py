'''
Created on Dec 10, 2018

@author: hp840
'''
import unittest
from domain.person import person

class iterableList:
    
    def __init__(self):
        self._data = []
        self._index = 0
    
    def __setitem__(self, pos, val):
        '''
        Sets the element at the position pos with the value val
        '''
        self._data[pos] = val
    
    def __delitem__(self, pos):
        '''
        Removes the element at the given position pos
        '''
        del self._data[pos]
        
    
    def __iter__(self):
        #Get an iterator from an object.  In the first form, the argument must supply its own iterator, or be a sequence.
        return iter(self._data)
        
    '''
    def __iter__(self):
        return self
    '''
    
    def __next__(self):
        if self._index >= len(self._data):
            raise StopIteration
        self._index +=1
        return self._data[self._index-1]    
    
    def __len__(self):
        return len(self._data)
    
    def append(self, obj):
        self._data.append(obj)
    
    def __getitem__(self, pos):
        '''
        Returns the element at the given position pos
        '''
        return self._data[pos]
    
    def sort(self, cmp):
        '''
        Sorts the list, using gnome sort
        '''
        gnomeSort(self._data, cmp)
    
    def __filter__(self, acceptance):
        '''
        Returns a list of objects that passes the filter (the acceptance)
        '''
        return filterList(self._data, acceptance)

'''
class ListIterator:
    def __init__ (self, lst):
        self.lst = lst
        self.idx = 0

    def __iter__ (self):
        return self

    def __next__ (self):
        try:
            item = self.lst[self.idx]
        except IndexError:
            raise StopIteration()
        self.idx += 1
        return item
'''
   
   
def twoForSort(data, cmp):
    l = len(data)
    for i in range(0,l-1):
        for j in range(i+1,l):
            if cmp(data[i], data[j]) == False:
                aux = data[i]
                data[i]= data[j]
                data[j] = aux

def cmpMethod(a,b):
    '''
    Returns True if a<b and False otherwise
    '''
    return a<b

def cmpMethod_gnome(a,b):
    '''
    Returns True if a>b and False otherwise
    '''
    return a<b

def cmpMethod_name(a,b):
    return a.getName() < b.getName()

def gnomeSort(data, cmp):
    '''
    2 parameters: data - the list of objects to sort
                  cmp - a functon that returns true if its parameters (a and b) are in the right order
    '''
    i = 0
    n = len(data)
    while i < n:
        if i and cmp(data[i], data[i-1]) == True:
            data[i], data[i-1] = data[i-1], data[i]
            i = i - 1
        else:
            i = i + 1
    return


def filterList(lst, acceptance):
    '''
    2 parameters: lst - the list of objects to be filtered
                  acceptance -  acceptance function that decide whether a given value passes the filter
                                returns True if it passes the filter, and False otherwise
    Output : result - a list of obj containing the objects that passes the filter
    '''
    result = []
    for i in lst:
        if acceptance(i):
            result.append(i)
    return result

def exampleAcceptance(a):
    '''
    Returns True if the last digit of the number is seven, and returns False otherwise
    '''
    return a%10 == 7

def exampleAcceptance2(a):
    return a.getName() != "Ana"

class testIterable(unittest.TestCase):
    
    def setUp(self):
        
        self._data= iterableList()
        lst = [54,26,93,17,77,31,44,55,20]
        for i in lst:
            self._data.append(i)
    
    def testIterableList(self):
        self.assertEqual(self._data[0], 54)
        self._data[0] = 11
        self.assertEqual(self._data.__next__(), 11)
        self.assertEqual(self._data.__next__(), 26)
        self.assertEqual(self._data.__next__(), 93)
        self.assertEqual(self._data.__next__(), 17)
        self.assertEqual(self._data[0], 11)
        
        self.assertEqual(len(self._data), 9)
        self._data.append(22)
        self.assertEqual(len(self._data), 10)
        
        self._data.append(56)
        lastpos = len(self._data) -1
        self.assertEqual(self._data[lastpos], 56)
        

        
    def testSort(self):
        '''
        Test sorting methods on a list of numbers
        '''
        
        sortedlist= [17,20,26,31,44,54,55,77,93]
        
        # check sorting a normal list - two fors sorting method
        lst = [54,26,93,17,77,31,44,55,20]
        twoForSort(lst,cmpMethod)
        self.assertEqual(lst, sortedlist)
        
        # check sorting a normal list - gnome sorting method
        lst = [54,26,93,17,77,31,44,55,20]
        gnomeSort(lst,cmpMethod_gnome)
        self.assertEqual(lst, sortedlist)
        
        # check sorting an iterable class - two fors
        twoForSort(self._data, cmpMethod)
        lstcheck= []
        for i in self._data:
            lstcheck.append(i)
        self.assertEqual(lstcheck, sortedlist)
        
        # check sorting an iterable class - gnome
        #gnomeSort(self._data, cmpMethod_gnome)
        self._data.sort(cmpMethod_gnome)
        lstcheck= []
        for i in self._data:
            lstcheck.append(i)
        self.assertEqual(lstcheck, sortedlist)
        
        
    def testFilter(self):
        filtered = [17,77]
        result = self._data.__filter__(exampleAcceptance)
        #result = filterList(self._data, exampleAcceptance)
        # keep only numbers ending in 7
        self.assertEqual(filtered, result)
    
    
    
class testIterable2(unittest.TestCase):
    def setUp(self):
        
        self._data= iterableList()
        lst = [person("1", "Ana", "0742123456", "Address 1 , Romania"), person("2", "Maria", "0742123123", "Address 2 , Romania"), person("3", "Baciu Ana", "0743111111", "Address 3 , Romania")]
        for i in lst:
            self._data.append(i)
            
    def testFilter(self):
        #filtered = [person("2", "Maria", "0742123123", "Address 2 , Romania"), person("3", "Baciu Ana", "0743111111", "Address 3 , Romania")]
        filtered = self._data[1::]
        result = self._data.__filter__(exampleAcceptance2)
        self.assertEqual(filtered, result)
    
    def testSort(self):
        sortedList = [self._data[0], self._data[2], self._data[1]]
        self._data.sort(cmpMethod_name)
        lstcheck = []
        for i in self._data:
            lstcheck.append(i)
        self.assertEqual(sortedList, lstcheck)
        