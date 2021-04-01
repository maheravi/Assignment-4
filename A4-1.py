import random
import time
import termcolor
import colorama
colorama.init()

Run_Time = time.time()


def show():
    for i in range(3):
        for j in range(3):
            if game[i][j] == 'X':
                print(termcolor.colored('X', color='blue'), end=" ")
            elif game[i][j] == 'O':
                print(termcolor.colored('O', color='red'), end=" ")
            else:
                print(game[i][j], end=" ")
        print()


def check():
    for i in range(3):
        if game[i][0] == 'X' and game[i][1] == 'X' and game[i][2] == 'X':
            print('player1 wins')
            print("--- %s seconds ---" % (time.time() - Run_Time))
            exit()
        elif game[0][i] == 'X' and game[1][i] == 'X' and game[2][i] == 'X':
            print('player1 wins')
            print("--- %s seconds ---" % (time.time() - Run_Time))
            exit()
        elif game[0][0] == 'X' and game[1][1] == 'X' and game[2][2] == 'X':
            print('player1 wins')
            print("--- %s seconds ---" % (time.time() - Run_Time))
            exit()
        elif game[0][2] == 'X' and game[1][1] == 'X' and game[2][0] == 'X':
            print('player1 wins')
            print("--- %s seconds ---" % (time.time() - Run_Time))
            exit()

        if game[i][0] == 'O' and game[i][1] == 'O' and game[i][2] == 'O':
            print('player2 wins')
            print("--- %s seconds ---" % (time.time() - Run_Time))
            exit()
        elif game[0][i] == 'O' and game[1][i] == 'O' and game[2][i] == 'O':
            print('player2 wins')
            print("--- %s seconds ---" % (time.time() - Run_Time))
            exit()
        elif game[0][0] == 'O' and game[1][1] == 'O' and game[2][2] == 'O':
            print('player2 wins')
            print("--- %s seconds ---" % (time.time() - Run_Time))
            exit()
        elif game[0][2] == 'O' and game[1][1] == 'O' and game[2][0] == 'O':
            print('player2 wins')
            print("--- %s seconds ---" % (time.time() - Run_Time))
            exit()


def counter():
    if count >= 5:
        print('Tie!')
        exit()


game = [['_', '_', '_'],
        ['_', '_', '_'],
        ['_', '_', '_']]

show()
print('1- one player')
print('2- two player')
CP = (input('one or two player?: '))
count = 0

while True:
    # playe 1
    print('Player 1')
    while True:
        count += 1
        row = int(input('Enter row: '))
        col = int(input('Enter column: '))

        if 0 <= row <= 2 and 0 <= col <= 2:
            if game[row][col] == '_':
                game[row][col] = 'X'
                break
            else:
                print('error! this cell is not empty')
        else:
            print('error! index is out of range. try again.')
    check()
    show()

    if CP == '2':
        counter()
        # player 2
        print('Player 2')
        while True:
            row = int(input('Enter row: '))
            col = int(input('Enter column: '))

            if 0 <= row <= 2 and 0 <= col <= 2:
                if game[row][col] == '_':
                    game[row][col] = 'O'
                    break
                else:
                    print('error! this cell is not empty')
            else:
                print('error! index is out of range. try again.')
    else:
        counter()
        # cpu player
        print('cpu player')

        while True:
            row = random.randint(0, 2)
            col = random.randint(0, 2)

            if 0 <= row <= 2 and 0 <= col <= 2:
                if game[row][col] == '_':
                    game[row][col] = 'O'
                    break
                else:
                    print('error! this cell is not empty')
            else:
                print('error! index is out of range. try again.')
    check()
    show()

