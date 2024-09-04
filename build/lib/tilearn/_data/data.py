import csv

def read_file(file_path):
    data = []
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            for i in range(1, 5):
                row[i] = int(row[i])
            data.append(row)
    return data