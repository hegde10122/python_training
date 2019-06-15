'''
Queue is a collection of objects that are inserted and removed according to First-in,first-out (FIFO) principle.
That is elements,can be inserted at any time, but only the element that has been in the queue the longest can be removed next.
The elements enter a queue at the back and are removed from the front.

Queue ADT
--------
The queue ADT defines a collection that keeps objects in a sequence, where element access and deletion are restricted to the first element in the 
queue.The element insertion is restricted to the back of the sequence. This restriction enforces the rule that items are inserted and deleted
in a queue according to the first-in,first-out principle.The queue abstract data type (ADT) supports the following two 
fundamental methods for a queue Q:
Q.enqueue(e): Add element to the back of queue Q
Q.dequeue(): Remove and return the first element from queue Q; an error occurs if the queue is empty
Q.first(): return a reference to the element at the front of queue Q, without removing it;an error occurs if the queue is empty.
Q.is_empty(): return True if queue Q does not contain any elements.
len(Q): Return the number of elements in queue Q; in python, we implement using this using the special method __len__

We assume that a newly created queue is empty, and that there is no limit to the number of elements that can be added. Elements added to 
the queue can be of any arbitrary type.

Array based Queue and its Pitfalls
---------------------------------

Let us use a Python list to model our Queue ADT. We can enqueue element x by calling append(x) to add it to the end of the list.
To follow the FIFO principle, we will have to call pop(0) for dequeue operation. But here is the problem. When we call pop(0) method 
on a list, Python will execute a loop to shift all elements from right to the left and fill the "hole" at index 0. See diagram.
This leads to worst-case behaviour of Big Theta(n) time.

To overcome the limitation, we will use the idea of dereferencing. As soon as an element is dequeued, we can reference it to None and 
use an explicit variable "head" that stores the index of the element that is currently at the front of the queue. The algorithm for dequeue
would then run in O(1) time. See diagram after we have performed 10 enqueue operations followed by 5 dequeue operations.

The second method we discussed above also suffers from a limitation. Suppose we enqueue 100 elements. Then we have a queue of 100 elements.
No we repeatedly dequeue one element followed by enqueue of one element alternately. No the length of the list after 100 such operations is 
150. This hapens because the dequeue happens from left to right and we would reference the first 50 elements to None. But the enqueue 
operation happens at the end of the queue which would swell from the size of 100 to 150 after 50 enqueue operations. Thus the size of the 
queue is O(z) where z is the number of enqueue operations since the creation of the queue. But the current number of elements in the queue
is actually 100. Thus we have 50 wasted "slots" in the queue leading to a poor design.

Using a circular array
----------------------

We now overcome the "wasteful" memory implementation discussed previously and allow the front of the queue to drift rightward and the queue
to "wrap around" the end of the array. We have an array size of N greater than the actual number of elements in the queue.The elements are 
enqueued from front to index N-1 and continuing at index 0,1,2 and so on. When we dequeue an element and want to advance the front index,
we use the modulo arithmetic head = (head + 1) % N. Modulo operator return the remainder after integer division. Assume we have N = 10.
Our current front index is 9. When we dequeue element at index 9 and want to advance the front index we compute the new head = (9 + 1) % 10
or head = 0. Thus we can use circular array to solve our problem.

A python implementation of Queue in the code below
--------------------------------
'''



class QueueArray:
    """ FIFO queue implementation using a Python list"""
    INITIAL_CAPACITY = 5 # restricting to just five

    class EmptyError(Exception):

        """ Error generated while trying to access an element from an empty container"""
        pass

    def __init__(self):
        """ Create an empty queue
        
        _queue is a reference to the list instance of some initial capacity 
        _size is an integer that tells us the current number of elements stored in the queue.
        _head = integer that represents the index of the first element in the queue.
        
        """
        self._queue = [None] * QueueArray.INITIAL_CAPACITY
        self._size = 0
        self._head = 0

    def __len__(self):
        """ Return number of elements in the Queue"""    
        return self._size

    def is_empty(self):
        """ Return True if the queue is empty"""    
        return self.__len__() == 0

    def first(self):
        """ Return the element at the front of the queue without actually removing it
            Raise empty exception if the queue is empty
        """
        if self.is_empty():
            raise self.EmptyError('Queue empty')
        return self._queue[self._head]        

    def dequeue(self):
        """ Remove and return the first element of the queue FIFO
            Raise Empty exception if the queue is empty
        """    
        if self.is_empty():
            raise self.EmptyError('Queue empty')
        elem = self._queue[self._head] # element to be returned
        self._queue[self._head] = None # garbage collection
        self._head = (self._head + 1) % len(self._queue) # advance head index
        self._size -= 1
        return elem

    def enqueue(self,elem):
        """ Adds an element to the back of the queue"""
        if self._size == len(self._queue):
            self._resize(2*len(self._queue)) # double the array size
            

    def _resize(self,capacity):




qeue = QueueArray()
print(qeue.first)
