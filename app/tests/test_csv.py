import tilearn as tl
from tilearn import data

schedule = tl.wspt(data.read_file('app/tests/data.csv'))

for row in schedule:
    print(row)