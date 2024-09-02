import tilearn as tl

x = [[1, 2, 3, 5, 7],
     [2, 4, 8, 6, 6], 
     [1, 2, 3, 2, 3],
     [2, 4, 6, 7, 4],
     [2, 4, 8, 6, 6], 
     [1, 2, 3, 2, 3]]

time = tl.show_mytime(x, 30)
for row in time:
    print(row)