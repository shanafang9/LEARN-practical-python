
# a = 1,2,3
# s = (1,2,3)

# print(type(a))
# print(type(s))



import csv

file_path = 'F:\\vscode_pj\\_practical_py36\\practical-python\\Work\_self\\1\\portfolio.csv'

f = open(file_path)
rows = csv.reader(f)
print(next(rows))



# Exercise 2.1: Tuples

row = next(rows)
# t = (row[0], int(row[1]), float(row[2]))
# cost  = t[1] * t[2]
# print(cost)
# print(f'{cost:0.2f}')



# Exercise 2.2: Dictionaries as a data structure
"""
d = {
    'name' : row[0],
    'shares' : int(row[1]),
    'price'  : float(row[2])
}

cost = d['shares'] * d['price']
print(cost)

d['date'] = (6, 11, 2007)
d['account'] = 12345
print(d)
"""


# Exercise 2.3: Some additional dictionary operations








