def display_grid(grid) :
    lst =[]
    
    for row in grid :
            for row1 in row:
                 if row1 == 1 :
                      lst.append('1')
                 elif row1 == 0 :
                      lst.append('0')

            lst.append('\n')   
    lst.pop()       
    a = ''.join(lst)
    return a


def next_generation(board):
    rows = len(board)
    cols = len(board[0])
    updated_board = [[0] * cols for _ in range(rows)]

    for row in range(rows):
        for col in range(cols):
            live_neighbours = get_neighbors(board, row, col)

            if board[row][col] == 1:
                if live_neighbours < 2 or live_neighbours > 3:
                    updated_board[row][col] = 0
                else:
                    updated_board[row][col] = 1
            else:
                if live_neighbours == 3:
                    updated_board[row][col] = 1

    return updated_board


def get_neighbors(board, row, col):
    rows = len(board)
    cols = len(board[0])
    live_neighbors = 0
    for i in range(max(0, row-1), min(rows, row+2)):
        for j in range(max(0, col-1), min(cols, col+2)):
            if board[i][j] == 1 and (i != row or j != col):
                live_neighbors += 1
    return live_neighbors




# def count_live_neighbours(board, row, col):
#     rows = len(board)
#     cols = len(board[0])
#     live_neighbours = 0

#     for i in range(-1, 2):
#         for j in range(-1, 2):
#             if i == 0 and j == 0:
#                 continue
#             neighbor_row = (row + i + rows) % rows
#             neighbor_col = (col + j + cols) % cols

#             if board[neighbor_row][neighbor_col] == 1:
#                 live_neighbours += 1

#     return live_neighbours


