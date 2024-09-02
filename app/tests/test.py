import tilearn

data = [['bt task 1', 4, 0, 10, 0],
        ['luyen speaking', 9, 0, 10, 3],
        ['task 2', 6, 0, 10, 2],
        ['reading b1', 7, 0, 10, 3],
        ['listening b4', 4, 0, 10, 2],
        ['doc sach', 5, 0, 10, 100],
        ['lam viec nha', 8, 0, 10, 3],
        ['writing', 3, 0, 10, 1],
        ['luyen de', 2, 0, 10, 1],
        ['final', 6, 0, 10, 2]]

schedule = tilearn.wspt(data, 10)

for row in schedule:
    print(row)