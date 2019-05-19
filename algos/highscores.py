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
        """ Return entry at index k. This is for convenience."""
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

'''
To maintain a sequence of high scores, we develop a class named Scoreboard. A scoreboard is limited to a certain number of high scores
that can be saved; once that limit is reached, a new score only qualifies for the scoreboard if it is strictly higher than the lowest 
"high score" on the board. The length of the desired scoreboard may depend on the game, perhaps 10,50 or 100.
Since that limit may vary depending on the game,we allow it to be specified as a parameter to our Scoreboard constructor.

Internally, we will use a python list named _board in order to manage the GameEntry instances that represent the high scores. Since we expect the scoreboard to 
eventually reach full capacity, we initialise the list to be large enough to hold the maximum number of scores, but we initially set all
entries to None. By allocating the list with maximum capacity initially, it never needs to be resized. 
As entries are added, we will maintain them from highest to lowest score,starting at index 0 of the list.

(Draw Diagram here)

The add method is responsible for considering the addition of a new entry to the scoreboard. Every entry will not necessarily qualify as 
a high score. If the board is not yet full, any new entry will be retained. Once the board is full, a new entry is only retained
if it is strictly better than one of the other scores, in particular, the last entry of the scoreboard,which is the lowest of the high scores.

When a new score is considered, we begin by determining whether it qualifies as a high score. If so, we increase the count of active 
scores,_n, unless the board is already at full capacity. In that case, adding a new high score causes some other entry to be dropped 
from the scoreboard, so the overall number of entries remains the same.

To correctly place a new entry within the list, the final task is to shift any inferior scores one spot lower 
(with the least score) being dropped entirely when the scoreboard is full). This process is quite similar to the 
implementation  of the insert method of the list class. In the context of our scoreboard, there is no need to shift any None references that 
remain near the end of the array.

(Insert diagram here)

To implement the final stage,we begin by considering index j = self._n - 1, which is the index at which the last GameEntry 
instance will reside,after completing the operation. Either j is the correct index for the newest entry, or one or more immediately 
before it will have leser scores. The while loop at line 55 checks the compound condition,shifting references rightward and decrementing j,
as long as there is another entry at index j-1 with a score less than the new score.


'''




