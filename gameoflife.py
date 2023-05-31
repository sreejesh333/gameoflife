def display_grid(grid) :
    lst =[]
    
    for row in grid :
            for row1 in row:
                 lst.append('#')
            lst.append("\n")
    a = "".join(lst)
    return a

        