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

def prec(file_path, opt_row):
    with open(file_path, 'r') as infile:
        reader = csv.reader(infile)
        rows = [row for index, row in enumerate(reader) if index < 0 or index > opt_row]
    return rows

def none(file_path, opt_row):
    with open(file_path, 'r') as infile:
        reader = csv.reader(infile)
        rows = [row for index, row in enumerate(reader) if index != opt_row]
    return rows

def updated(file_path, prec, opt_row):
    if prec == 1:
        # rows = prec(file_path, opt_row)
        with open(file_path, 'r') as infile:
            reader = csv.reader(infile)
            rows = [row for index, row in enumerate(reader) if index < 0 or index > opt_row]
    elif prec == 0:
        # rows = none(file_path, opt_row)
        with open(file_path, 'r') as infile:
            reader = csv.reader(infile)
            rows = [row for index, row in enumerate(reader) if index != opt_row]
    with open(file_path, 'w', newline='') as outfile:
        writer = csv.writer(outfile)
        writer.writerows(rows)
            
def clear(folder_path):
    csv_files = glob.glob(os.path.join(folder_path, '*.csv'))
    for file in csv_files:
        os.remove(file)