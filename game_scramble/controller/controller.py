import random


class game:
    def __init__(self,repo):
        self._repo  = repo
        self._sen = self._repo.chooseRandom()
        self._bad_sen = ''
        self.setBadSen()

    def setBadSen(self):
        lst = self.wordsList(self._sen)
        lst2 = []
        for word in lst:
            for j in word:
                lst2.append(j)
        random.shuffle(lst2)
        poz = 0
        for word in lst:
            for i in word:
                self._bad_sen = self._bad_sen + lst2[poz]
                poz += 1
            self._bad_sen = self._bad_sen + ' '


    def wordsList(self, str):
        lst = str.split(' ')
        return lst


    def swap(self,w1,l1,w2,l2):
        '''

        :param w1: word1
        :param l1: letter1
        :param w2: word2
        :param l2: letter2
        '''
        new_sen = ""
        lst = self.wordsList(self._bad_sen)
        lst2 = []
        for word in lst:
            l = []
            for i in word:
                l.append(i)
            lst2.append(l)

        lst2[w1][l1],lst2[w2][l2]=lst2[w2][l2],lst2[w1][l1]

        for word in lst2:
            s = ''
            for i in word:
                s = s + i
            new_sen = new_sen +s +' '
        self._bad_sen = new_sen


