'''
Created on Nov 24, 2018

@author: hp840
'''
from repository.personRepository import PersonRepository,\
    PersonRepositoryException

class undoController:
    
    def __init__(self):
        self._operations = []
        self._index = -1
        self._duringUndo = False
    
    
    def addOperation(self, operation):
        if self._duringUndo == True:
            return
        
        self._index += 1
        self._operations = self._operations[:self._index + 1]
        
        self._operations.append(operation)
        
        #self._index = len(self._operations)-1
        
        
    def undo(self):
        if self._index == -1:
            return False
        
        self._duringUndo = True
        self._operations[self._index].undo()
        self._duringUndo = False
        self._index -= 1
        return True
    
    
    def redo(self):
        if self._index >= len(self._operations)-1:
            return False
        try:
            self._duringUndo = True
            self._index += 1
            self._operations[self._index].redo()
            self._duringUndo = False
        except Exception:
            return False
        
        return True


class cascadeOperation:
    def __init__(self):
        self._operations = []
    
    def add(self, oper):
        self._operations.append(oper)
    
    def undo(self):
        for o in self._operations:
            o.undo()
    
    def redo(self):
        for o in self._operations:
            o.redo()


class operation:
    def __init__(self, undoFunction, redoFunction):
        self._undoFunction = undoFunction
        self._redoFunction = redoFunction
    
    def undo(self):
        self._undoFunction.call()
        
    def redo(self):
        self._redoFunction.call()
        
        
class functionCall:
    def __init__(self, func, *params):
        self._func = func
        self._params = params
    
    def call(self):
        self._func(*self._params)