import tilearn as tl
from tilearn import _data as data
import os

# ╔═══════════════════════════════╗
# ║          CLASS DATA           ║
# ╚═══════════════════════════════╝
class List:
    def __init__(self, backup_path, file_path, prec):
        self.backup = os.path.abspath(backup_path)
        self.path = data.path(os.path.abspath(file_path), self.backup)
        self.prec = prec
    
    def info(self):
        return data.read_file(self.path)
    
    def check(self):
        return self.prec
    
    def path(self):
        return self.path
    
    def run(self):
        if self.prec == 1:
            return tl.sum_factor(data.read_file(self.path))
        elif self.prec == 0:
            return tl.factor_data(data.read_file(self.path))
    
# ╔═══════════════════════════════╗
# ║         CRUCIAL DATA          ║
# ╚═══════════════════════════════╝
def count_file(folder_path):
    csv_count = len([file for file in os.listdir(folder_path) if file.endswith('.csv')])
    return csv_count

def ja_all(lists, path):
    sum = 0
    folder_path = path
    csv_count = len([file for file in os.listdir(folder_path) if file.endswith('.csv')])
    for i in range(csv_count):
        count = sum + tl.job_amount(lists[i].info())
        sum = count
    return count

def location(lists, type):
    """
    Returns
    -------
    List
        opt = [sublist, row]
    """
    opt = tl.list_gen(2, 1)
    max_value = 0
    init = 0
    for sublist in lists:
        for i in range(tl.job_amount(sublist.info())):
            if sublist.run()[i][5] > max_value:
                max_value = sublist.run()[i][5]
                opt[0] = init
                opt[1] = i
        init += 1
    if type == 'sub':
        return opt[0]
    elif type == 'row':
        return opt[1]