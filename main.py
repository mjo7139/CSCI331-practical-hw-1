import sys

# Write a program to solve the following search problem: You are given two
#  words of equal length and a dictionary of legal English words. At each step,
#  you can change any single letter in the word to any other letter, provided 
# that the result is a word in the dictionary; you cannot add or remove
#  letters. Your program should print the shortest list of words that connects
#  the two given words in this way, if there are multiple such paths, any one 
# is sufficient.

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
    # keep track of the parent of every word we gotten. This way we can retrace once we find the target

    # keep track of every word that we check so we dont double check, and get the index of the start word
    checked = []
    index = list.index(start)
    # a queue of indexs to be checked starting with our start word
    queue = [index]
    checked.append(index)
    go = True
    
    # for each word, if it is connected...
    while len(queue) > 0:
        # use count to keep track of the current potential neighbor index
        count = 0
        for potNeighbor in matrix[index]:
            # if the word differs by one letter...
            
            if potNeighbor == 1 and (potNeighbor not in checked):
                print(count)
                # it is a neighbor and is not in the checked list, add it to the queue
                queue.append(count)
                
                #check if it is the target
                if list[count] == target:
                    return target
            count += 1
                    
            
        # We checked and added all of index's neighbors so we can add index to checked
        checked.append(index)
        # We can remove this from the queue to be checked. This queue structure should insure first in first out BFS
        queue.pop(0)
        # Next up
        if len(queue) == 0:
            return
        index = queue[0]




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
    #print(matrix)
    # given the list and the adjacency matrix lets make our spanning tree
    # we will make a tuple dictionary 
    # (index1, index2) = distfrom(index -> index2)
    got = BFS(list, matrix, start, target)
    print(got)
    

if __name__ == '__main__':
    main()
