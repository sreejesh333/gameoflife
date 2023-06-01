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

# def ply_game(grid) :
#       a = display_grid(grid)
#       for row in range(5) :
