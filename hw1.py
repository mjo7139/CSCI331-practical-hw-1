import sys
from collections import deque

# Write a program to solve the following search problem: You are given two
#  words of equal length and a dictionary of legal English words. At each step,
#  you can change any single letter in the word to any other letter, provided 
# that the result is a word in the dictionary; you cannot add or remove
#  letters. Your program should print the shortest list of words that connects
#  the two given words in this way, if there are multiple such paths, any one 
# is sufficient.    
# 
# done    

def isEdge(str1, str2):
    # function to check if two strings are edges in the problem. I.e they 
    # differ by one letter
    count = 0
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            count += 1
            if count > 1:
                return False
            
    return True

def initializeList(filename, wordLen):
    # open the file and read all of the words into a list
    words = []
    with open(filename, "r") as file:
        lines = file.readlines()
        for line in lines:
            line = line.rstrip('\n')
            # exclude everything that is not the same length as the start/end word
            if len(line) == wordLen:
                words.append(line)
    return words

def createMatrix(list):
    # read through the list and create an adjacency matrix for the words
    rows, cols = (len(list), len(list))
    matrix = [[0 for i in range(cols)] for j in range(rows)]
    # create a 2d list initialized with zeros for sizeof(words) x sizeof(words)
    # Here we are going to track the index of the word and the compared word using 2 counters
    indexOfWord = 0
    indexOfCompare = 0
    for word in list:
        for compareWord in list:
            if isEdge(word, compareWord):
                matrix[indexOfWord][indexOfCompare] = 1
            indexOfCompare += 1
        indexOfCompare = 0
        indexOfWord += 1

    return matrix

def BFS(list, matrix, start, target):
    # keep track of every word that we check so we dont double check, 
    # and get the index of the start word
    index = list.index(start)
    checked = set()
    checked.add(index)

    # so i think i need a 2d matrix in order to keep track of each path. 
    # every time there is a new path, add a new row to the matrix
    # array [branch # | 20] [step # along the branch | 20]
    # pathTracker = [[0 for i in range(100)] for j in range(20)]
    #print(pathTracker)

    # a queue of indexs to be checked starting with our start word
    queue = deque([index])

    # keep a list and add every word checked along with that words parent
    # this way we can retrace at the end
    parentList = [(index, None)]

    # While our queue is not empty
    while len(queue) > 0:
        # use count to keep track of the current potential neighbor index
        count = 0
        # for every other word accociated
        for potNeighbor in matrix[index]:
            # if the word differs by one letter...
            if potNeighbor == 1 and (count not in checked):
                # it is a neighbor and is not in the checked list, add it to the queue
                queue.append(count)

                # add this word to the parent list along with its parent
                parentList.append((count, index))

                #check if it is the target
                if list[count] == target:
                    retrace(parentList, count, list)
                    return
            count += 1
                    
            
        # We checked and added all of index's neighbors so we can add index to checked
        checked.add(index)
        # We can remove this from the queue to be checked. This queue structure should insure first in first out BFS
        queue.popleft()
        # Next up
        if len(queue) == 0:
            print("no solution")
            return
        index = queue[0]
        
    print("no solution")


def retrace(parentList, targetIndex, list):
    # given the final value "target"
    # go through the list grabbing each parent and adding it to its own list
    # then print the reverse of that list to get the path we took to get to target

    #parentList = list of (indexOfWord, IndexOfParent) on path
    give = []
    # sets index to the index at which (target, parentOfTarget) is
    index = next((i for i, v in enumerate(parentList) if v[0] == targetIndex), None)
    # sets parentIndex to the index at which parent is in list
    parentIndex = parentList[index][1]
    # adds the target as the first of the "give" list
    give.append(list[targetIndex])

    while parentIndex is not None:
        index = next((i for i, v in enumerate(parentList) if v[0] == parentIndex), None)
        give.append(list[parentIndex])
        parentIndex = parentList[index][1]
        
    give.reverse()
    for i in range(len(give)):
        print(give[i])


def main():
    args = sys.argv[1:]
    filename = args[0]
    start = args[1]
    target = args[2]
    wordLen = len(start)

    # open the file and read all of the words into a list
    list = initializeList(filename, wordLen)
    # read through the list and create an adjacency matrix for the words
    matrix = createMatrix(list)
    # given the list and the adjacency matrix lets make our spanning tree
    BFS(list, matrix, start, target)
    
    

if __name__ == '__main__':
    main()
