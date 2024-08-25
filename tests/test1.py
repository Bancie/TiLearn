import tilearn

x = [[1, 2, 3],
     [2, 4, 8], 
     [1, 2, 3],
     [2, 4, 6]]

time = tilearn.show_mytime(x, 30)
for row in time:
    print(row)