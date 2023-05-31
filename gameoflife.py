def display_grid(grid) :
    lst =[]
    
    for row in grid :
            for row1 in row:
                 if row1 == 1 :
                      lst.append('#')
                 else :
                       lst.append('.')     
            lst.append("\n")
    a = "".join(lst)
    return a

