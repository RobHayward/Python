theBoard = {'top-L': "", 'top-M': "", 'top-R': "", 'mid-L': "", 'mid-M': "", 'mid-R': "", 'low-L': "", 'low-M': "", 'low-R': ""}
#nice printing
import pprint
pprint.pprint(theBoard)
# add some vales
theBoard['top-L'] = 'X'
theBoard['top-R'] = 'X'
theBoard['mid-L'] = 'O'
theBoard['low-L'] = 'X'
theBoard['mid-M'] = 'O'
#create representation of board
def printBoard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('------')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('------')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])

printBoard(theBoard)
    
