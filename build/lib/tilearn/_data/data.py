import csv
import tilearn as tl

def read_file(file_path):
    data = []
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            for i in range(1, 5):
                row[i] = int(row[i])
            data.append(row)
    return data