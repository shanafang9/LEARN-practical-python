

# Exercise 1.26: File Preliminaries
import os 

print(os.getcwd())

file_path = 'F:\\vscode_pj\\_practical_py36\\practical-python\\Work\_self\\1\\portfolio.csv'

"""
with open(file_path, 'rt') as f:
    data = f.read()
    print('data.__repr__() :')
    print(data.__repr__())
    print('data.__str__() :')
    print(data.__str__())
    print('data :')
    print(data)
"""

"""
with open(file_path, 'rt') as f:
    for line in f:
        print(line, end='')

"""

"""
f = open(file_path, 'rt')
headers = next(f)
print(headers)
for line in f:
    print(line, end='')

f.close()
"""






