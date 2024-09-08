import csv
import shutil
import glob
import os

def backup(src, dist):
    csv_files = glob.glob(os.path.join(src, '*.csv'))
    for file in csv_files:
        shutil.copy(file, dist)

def path(original_path):
    directory = os.path.dirname(original_path)
    filename = os.path.basename(original_path)
    new_directory = os.path.join(directory, 'backup')
    os.makedirs(new_directory, exist_ok=True)
    new_path = os.path.join(new_directory, filename)
    return new_path

def read_file(file_path):
    data = []
    backup = path(file_path)
    with open(backup, 'r') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            for i in range(1, 5):
                if i == 0:
                    row[i] = str(row[i])
                elif i == 1:
                    row[i] = float(row[i])
                else:
                    row[i] = int(row[i])
            data.append(row)
    return data

def updated(file_path, prec, end_index):
    if prec == 1:
        start_index = 0
        with open(file_path, 'r') as infile:
            reader = csv.reader(infile)
            rows = [row for index, row in enumerate(reader) if index < start_index or index > end_index]
        with open(file_path, 'w', newline='') as outfile:
            writer = csv.writer(outfile)
            writer.writerow(["Name", "p", "r", "d", "w", "p-factor"])
            writer.writerows(rows)
            
def clear(folder_path):
    csv_files = glob.glob(os.path.join(folder_path, '*.csv'))
    for file in csv_files:
        os.remove(file)