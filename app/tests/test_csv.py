import csv
import tilearn as tl
from tilearn import data

data = data.read_file('app/tests/data.csv')

schedule = tl.wspt(data)

for row in schedule:
    print(row)