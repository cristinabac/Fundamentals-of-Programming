from random import choice


class repo:

    def __init__(self):
        self._data = []
        self.loadFromFile()

    def loadFromFile(self):
        f = open("fisier.txt","r")
        line = f.readline().strip()
        while line != "":
            self._data.append(line)
            line = f.readline().strip()
        f.close()

    def chooseRandom(self):

        sentance = choice(self._data)
        return sentance