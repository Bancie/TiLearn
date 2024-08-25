import tilearn

x = [[1, 2, 3],
     [2, 4, 8], 
     [1, 2, 3],
     [2, 4, 6]]

# print(tilearn.job_amount(x))

rows = 3
cols = 4
two_d_list = []

for i in range(rows):
    row = []
    for j in range(cols):
        row.append(0)
    two_d_list.append(row)

for row in two_d_list:
    print(row)