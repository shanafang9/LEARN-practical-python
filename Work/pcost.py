# pcost.py
#
# Exercise 1.27: Reading a data file

file_path = 'F:\\vscode_pj\\_practical_py36\\practical-python\\Work\_self\\1\\portfolio.csv'

"""
total_cost = 0
data_list = []

with open(file_path, 'rt') as f:
    headers = next(f)
    column = headers.strip().split(',')
    for line in f:
        data_dict = {}
        print(line, end='')
        tmp = line.strip().split(',')
        data_dict[tmp[0]] = {column[1]:int(tmp[1]), column[2]:float(tmp[2])}
        data_list.append(data_dict)
        total_cost += int(tmp[1]) * float(tmp[2])
    

print(data_list)
print(total_cost)

"""


# Exercise 1.28: Other kinds of "files"

zip_file = 'F:\\vscode_pj\\_practical_py36\\practical-python\\Work\\Data\\portfolio.csv.gz'

import gzip

"""
# with gzip.open(zip_file, 'rt') as f:
#     for line in f:
#         print(line, end='')

with gzip.open(zip_file, 'r') as f:
    for line in f:
        print(line, end='')
"""


# Exercise 1.29: Defining a function
"""
def greeting(name):
    'Issues a greting'
    print('Hello', name)

greeting('Guido')
print(help(greeting))
"""



# Exercise 1.30: Turning a script into a function

def portfolio_cost(filename):
    '''
    This function takes a filename as input, reads the portfolio data in that file, and returns the total cost of the portfolio as a float.
    '''
    total_cost = 0
    data_list = []

    with open(filename, 'rt') as f:
        headers = next(f)
        column = headers.strip().split(',')
        for line in f:
            data_dict = {}
            print(line, end='')
            tmp = line.strip().split(',')

            try:
                _shares = int(tmp[1])
                _price = float(tmp[2])
            except ValueError as e:
                _shares = int(tmp[1]) if tmp[1] else 0
                _price = float(tmp[2]) if tmp[2] else 0

            data_dict[tmp[0]] = {column[1]:int(_shares), column[2]:float(_price)}
            data_list.append(data_dict)
            total_cost += int(_shares) * float(_price)

    return total_cost
"""
cost = portfolio_cost(file_path)
print('Total cost:', cost)
"""



# Exercise 1.31: Error handling

"""
error_file = 'F:\\vscode_pj\\_practical_py36\\practical-python\\Work\\Data\\missing.csv'

cost = portfolio_cost(error_file)
print('Total cost:', cost)
"""



# Exercise 1.32: Using a library function
"""
import csv
f = open(file_path)
rows = csv.reader(f)
headers = next(rows)
print(headers)

for row in rows:
    print(row)

f.close()
"""



# Exercise 1.33: Reading from the command line

"""
'''python pcost.py .\Data\missing.csv'''
import sys

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = file_path

cost = portfolio_cost(filename)
print('Total cost:', cost)
"""










