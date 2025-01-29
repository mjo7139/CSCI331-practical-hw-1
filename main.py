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
    # differ by one letter and are the same length
    if len(str1) != len(str2):
        return False
    count = 0
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            count += 1
            if count > 1:
                return False
            
    return True

def initializeList(filename):
    # open the file and read all of the words into a list
    words = []
    with open(filename, "r") as file:
        lines = file.readlines()
        for line in lines:
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
    rows, cols = (len(list), len(list))
    parent = [[0 for i in range(cols)] for j in range(rows)]
    # keep track of every word that we check so we dont double check, and get the index of the start word
    checked = []
    index = list.index(start)
    checked.append(index)
    # for each word, if it is connected...
    for word in matrix[index]:
        if word == 1:
            #check if it is the target
            if list(word) == target:



def main():
    args = sys.argv[1:]
    filename = args[0]
    start = args[1]
    target = args[2]

    # open the file and read all of the words into a list
    list = initializeList(filename)
    # read through the list and create an adjacency matrix for the words
    matrix = createMatrix(list)
    # given the list and the adjacency matrix lets make our spanning tree
    # we will make a tuple dictionary 
    # (index1, index2) = distfrom(index -> index2)
    BFS(list, matrix, start, target)
    

if __name__ == '__main__':
    main()
