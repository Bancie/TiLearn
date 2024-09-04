import tilearn as tl

# data = [['bt task 1', '4', '0', '1', '0'],
#         ['luyen speaking', '9', '0', '4', '3'],
#         ['task 2', '6', '0', '3', '2'],
#         ['reading b1', '7', '0', '2', '3'],
#         ['listening b4', '4', '0', '9', '2'],
#         ['doc sach', '5', '0', '7', '1'],
#         ['lam viec nha', '8', '0', '8', '3'],
#         ['writing', '3', '0', '6', '1'],
#         ['luyen de', '2', '0', '7', '1'],
#         ['final', '6', '0', '2', '2']]

data = [['bt task 1', 4, 0, 1, 0],
        ['luyen speaking', 9, 0, 4, 3],
        ['task 2', 6, 0, 3, 2],
        ['reading b1', 7, 0, 2, 3],
        ['listening b4', 4, 0, 9, 2],
        ['doc sach', 5, 0, 7, 1],
        ['lam viec nha', 8, 0, 8, 3],
        ['writing', 3, 0, 6, 1],
        ['luyen de', 2, 0, 7, 1],
        ['final', 6, 0, 2, 2]]
# schedule = tl.wspt(data, 10)

schedule = tl.c_time(data)
# full_schedule = tl.lateness(data)

# schedule = tl.edd(data)

for row in schedule:
    print(row)