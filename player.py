import lib.puzzle as game

size = int(input('size(2~9):  '))
frame = game.createPuzzle(size)
game.printPuzzle(frame)
while(not game.isSolved(frame)):
    k = input('move(up: w, down : s, left : a, right : d):  ')
    if k=='w':
            i = 0
    elif k=='s':
            i = 1
    elif k=='a':
            i = 2
    elif k=='d':
            i = 3
    frame = game.movePuzzle(frame, i)
    game.printPuzzle(frame)
print("solved")
