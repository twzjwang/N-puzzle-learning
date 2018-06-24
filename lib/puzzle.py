import numpy as np
import random
import math

def createPuzzle(size):
    frame = []
    for i in range(0, size * size):
        frame.append(i)
    random.shuffle(frame)
    while(notSolvable(frame, size) or isSolved(frame)):
        random.shuffle(frame)
    return frame

def printPuzzle(frame):
    size = int(math.sqrt(len(frame)))
    print('')
    for i in range(0, size):
        for j in range(0, size):
            print("%2d" % (frame[size * i + j]), end=" ")
        print('')
    print('')

def isSolved(frame):
    for i in range(0, len(frame)-1):
        if frame[i] != i + 1:
            return False
    if frame[len(frame)-1] != 0:
            return False
    return True

def notSolvable(frame, size): 
    space = frame.index(0)
    invCount = 0
    for i in range(0, len(frame)):
        for j in range(i + 1, len(frame)):
            if frame[i] and frame[j] and frame[i] > frame[j]:
                invCount = invCount + 1
    if size % 2 and invCount % 2 == 0:
        return False
    elif size % 2 == 0:
        if (size - int(space / size)) % 2 == 0 and invCount % 2:
            return False
        elif (size - int(space / size)) % 2 and invCount % 2 == 0:
            return False 
        else:
            return True
    else:
        return True

def movePuzzle(frame, move):   
    space = frame.index(0)
    size = int(math.sqrt(len(frame)))

    #0 : up 
    #1 : down
    #2 : left
    #3 : right
    if move == 0 and int(space / size) > 0:
        temp = frame[space]
        frame[space] = frame[space - size]
        frame[space - size] = temp
    elif move == 1 and int(space / size) < size - 1:
        temp = frame[space]
        frame[space] = frame[space + size]
        frame[space + size] = temp
    elif move == 2 and (space % size) - 1 >= 0:
        temp = frame[space]
        frame[space] = frame[space - 1]
        frame[space - 1] = temp
    elif move == 3 and (space % size) + 1 < size:
        temp = frame[space]
        frame[space] = frame[space + 1]
        frame[space + 1] = temp
    else:
        print("Error moving")

    return frame









        
    

