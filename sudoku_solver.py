board = [
    [0, 0, 2, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 5, 0, 0, 0],
    [9, 8, 6, 0, 0, 2, 0, 0, 0],
    [0, 3, 0, 9, 0, 0, 7, 0, 8],
    [0, 9, 5, 0, 1, 0, 6, 2, 0],
    [2, 0, 7, 0, 0, 3, 0, 9, 0],
    [0, 0, 0, 8, 0, 0, 9, 4, 1],
    [0, 0, 0, 2, 0, 0, 0, 0, 7],
    [0, 0, 0, 0, 0, 0, 2, 0, 0]
]

#Make the sudoku board

def print_board(board):
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("---------------------")

        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print("|", end = " ")

            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end = "")

#Search for empty squares

def empty_squares(board):
    for i in range(len(board)):  #rows
        for j in range(len(board[0])):  #columns
            if board[i][j] == 0:
                return (i, j)

    return None

#Check if the board is valid

def isValid(board, num, pos):
    #row
    for i in range(len(board[0])):  
        if board[pos[0]][i] == num and pos[1] != i:
            return False
    #column
    for i in range(len(board)):  
        if board[i][pos[1]] == num and pos[0] != i:
            return False

    #square
    square_x = pos[1] // 3  
    square_y = pos[0] // 3

    for i in range(square_y * 3, square_y * 3 + 3):
        for j in range(square_x * 3, square_x * 3 + 3):
            if board[i][j] == num and (i, j) != pos:
                return False

    return True

#Complete the Sudoku board

def solve(board):

    es = empty_squares(board) # es -> empty squares

    if not es:
        return True
    else:
        row, col = es

    for i in range(1, 10):
        if isValid(board, i, (row, col)):
            board[row][col] = i

            if solve(board):
                return True

            board[row][col] = 0  #reset element
    return False



solve(board)
print_board(board)











        


