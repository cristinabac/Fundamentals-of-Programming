'''
Created on Dec 1, 2018

@author: hp840
'''
import pickle

from domain.person import person
from domain.activity import activity

def writeToBinaryFile(fileName, obj_list):
    f = open(fileName, "wb")
    pickle.dump(obj_list,f)
    f.close()

def readBinaryFile(fileName):
    result = []
    try:
        f = open(fileName, "rb")
        return pickle.load(f)
    except EOFError:
        return []
    except IOError as e:
        print("An error occured - "+str(e))
        raise e
    return result
'''
persons = [person("1", "Ana", "0742123456", "Address 1 ; Romania"),person("11", "Gigi", "0742775699", "Romania; Cluj"),person("2", "Marry Judy", "0742777966", "Romania, Brasov")]
writeToBinaryFile("persons.pickle", persons)

activities = [activity("1", ["1","2"], "2019-11-11", "08:00:00", "Description 1 lala"),activity("2", ["11"], "2019-11-06", "09:00:00", "Description 2 aa"),activity("3", ["2","11"], "2017-11-11", "18:00:00", "Description bbb cc ")]
writeToBinaryFile("activities.pickle", activities)
'''