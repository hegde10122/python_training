class GameEntry:
    """ Represents one entry of a list of high scores"""

    def __init__(self,score,name):
        self._name = name;
        self._score = score

    def get_name(self):
        """ accessor method for name"""
        return self._name

    def get_score(self):
        """ getter method for score """
        return self._score

    def __str__(self):
        """ This method returns a string representatiom of the score entry"""
        return '({0}, {1})'.format(self._name,self._score) #example: '(hegde,102)     

'''
We have defined a class representing a high score entry. It includes two components - an integer represnting the score itself which we identify using the field
_score. The second field is called _name which stores the name of the player.
'''

class ScoreBoard:
    """ Fixed-length sequence of high scores in non-decreasing order"""

    def __init__(self,capacity = 10):
        """ initialise scoreboard with given maximum capacity with all initial entries None"""
        self._board = [None] * capacity #reserve space for future scores
        self._n = 0 #number of actual entries

    def __getitem__(self,k):
        """ Return entry at index k"""
        return self._board[k]

    def __str__(self):
        """ Return string representation of the high score list"""    
        return '\n'.join(str(self._board[j]) for j in range(self._n))

    def add(self, entry):
        """ Consider adding entry to high scores"""
        score = entry.get_score()

        #Does new score qualify as a high score ?
        #answer is yes if board not full or score is higher than last entry         
        good = self._n < len(self._board) or score > self._board[-1].get_score()

        if good:
            if self._n < len(self._board): #no score drops from list
                self._n +=1                #so overall number increases

            #shift lower scores rightward to make room for new entry
            j = self._n - 1
            while j > 0 and self._board[j - 1].get_score() < score:
                self._board[j] = self._board[j - 1]  # shift entry from j-1 to j
                j -= 1                               # and decrement j
            self._board[j] = entry                   #when done, add new entry      




