# insert(0,0,matrix_point,resolved1_grid,list("SPAN"))
# format_board(matrix_point)

import json
import requests
import pdb

def format_row(row):
    return '|' + '|'.join('{0:^4}'.format(x) for x in row) + '|'


def format_board(board):
    return '\n----------------------------------------------------------------------------\n'.join(format_row(row) for row in board)


def printing_crossword(matrix, rows, cols):
    # for i in range(rows):
    #   print('|' + '|'.join('{0:^2}'.format(x) for x in gridnums[i:i+cols]) + '|')
     #   print("---"*cols)
    for i in range(rows):
        print("\n")
        for j in range(cols):
            print(matrix_point[i][j], end="\t")

    return


def printing_clues(clues):
    print("ACROSS")
    for i in clues[0]:
        print(i)
    print("DOWN:")
    for i in clues[1]:
        print(i)
    return


def create_matrix_square(rows, cols, point_gr):
    grid = [[" " for i in range(rows)]for j in range(cols)]
    pc = 0
    for i in range(15):
        for j in range(15):
            if(point_gr[pc] == "."):
                grid[i][j] = "█"
            pc = pc + 1
    return grid


def create_matrix_number(rows, cols, grid, gridnums):
    count = 0
    for i in range(15):
        for j in range(15):
            if(gridnums[count] != 0):
                grid[i][j] = str(gridnums[count])
            count = count+1
    return grid


def insert(i, j, matrix, resolved_matrix, lista, code=False):
    
    
    if not lista:
        return True
    if not code :
        if (lista[0] == resolved_matrix[i][j]):
            tmp = matrix[i][j]
            matrix[i][j] += " "+lista[0]
        else:return False    
        if insert(i, j+1, matrix, resolved_matrix, lista[1:]):
            return True
        matrix[i][j] = tmp
        return False
    else:
        if (lista[0] == resolved_matrix[i][j]):
            tmp = matrix[i][j]
            matrix[i][j] += " "+lista[0]
        else:return False
        if insert(i+1, j, matrix, resolved_matrix, lista[1:], True):
            return  True
        matrix[i][j] = tmp
        return False
        
def help_(i, j, matrix, resolved_matrix, lista, code=False):
    
    
    if not lista:
        return True
    if not code :
        if (lista[0] == resolved_matrix[i][j]):
            tmp = matrix[i][j]
            matrix[i][j] += " "+lista[0]
        else:return False    
        if insert(i, j+1, matrix, resolved_matrix, lista[1:]):
            return True
        matrix[i][j] = tmp
        return False
    else:
        if (lista[0] == resolved_matrix[i][j]):
            tmp = matrix[i][j]
            matrix[i][j] += " "+lista[0]
        else:return False
        if insert(i+1, j, matrix, resolved_matrix, lista[1:], True):
            return  True
        matrix[i][j] = tmp
        return False

def index(rows, cols,number,matrix_gridnums):
    
    for i in range(cols):
        for j in range(rows):
            if matrix_gridnums[i][j] == number:
                return i, j
    return -1,-1
if __name__ == "__main__":
    #url = "https://www.xwordinfo.com/JSON/Data.aspx?format=text"
    #url = "https://raw.githubusercontent.com/doshea/nyt_crosswords/master/2000/01/01.json"
    #r = requests.get(url).json()
    #data = r.json()
    
    with open('crossword.json') as f:
        data = json.load(f)

    cols = data["size"]["cols"]
    rows = data["size"]["rows"]
    clues = [data["clues"]["across"], data["clues"]["down"]]
    resolved_grid = data["grid"]
    gridnums = data["gridnums"]
    matrix_gridnums =[gridnums[i:i+cols]
                  for i in range(0, len(gridnums), rows)]
    resolved1_grid = [resolved_grid[i:i+cols]
                  for i in range(0, len(resolved_grid), rows)]
    print(format_board(resolved1_grid))
    matrix_point = create_matrix_square(rows, cols, resolved_grid)
    matrix_point = create_matrix_number(rows, cols, matrix_point, gridnums)
    print(index(15, 15,10,matrix_gridnums))
    while True:
        i=0
        j=0
        print("1 inserisci parola")
        print("2 help parola")
        print("3 stampa")
        a = int(input())
        if(a == 1):
            num = int(input("1 inserisci numero "))
            i,j=index(rows, cols,num,matrix_gridnums)
            print(i,j)
            scelta = int(input("1=orizzontale  2=verticale: "))
            word = list(input("inserisci parola: "))
            if(scelta == 1):
                var = insert(i, j, matrix_point, resolved1_grid, word)
                print("ESATTO!!")
            else:
                var = insert(i, j, matrix_point, resolved1_grid, word, True)
            if(not var):
                print("Sbagliata")
        if(a == 3):
            print(format_board(matrix_point))
            printing_clues(clues)
        if(a == 2):
            num = int(input("1 inserisci numero "))
            i,j=index(rows, cols,num,matrix_gridnums)
            print(i,j)
            scelta = int(input("1=orizzontale  2=verticale: "))
            word = list(input("inserisci parola: "))
            if(scelta == 1):
                var = help_(i, j, matrix_point, resolved1_grid, word)
            else:
                var = help_(i, j, matrix_point, resolved1_grid, word, True)
            