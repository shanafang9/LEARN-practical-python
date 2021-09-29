

"""
s = [1, 2, 3, 4]
print('sum(s) ', sum(s))

print('min(s) ', min(s))

print('max(s) ', max(s))

t = ['Hello', 'World']
print('max(t) ', max(t))
"""


# Exercise 2.13: Counting
"""
for i in range(10):
    print(i, end=' ')
print()
for i in range(10, 0, -1):  # 半开区间
    print(i, end=' ')
print()
for i in range(0, 10, 2):
    print(i, end=' ')
print()
"""


# Exercise 2.14: More sequence operations
"""
data = [4, 9, 1, 25, 16, 100, 49]

print(min(data))

for index, x in enumerate(data):
    print(index, x)


for index in range(len(data)):
    print(data[index])
"""


# Exercise 2.15: A practical enumerate() example

error_file = 'F:\\vscode_pj\\_practical_py36\\practical-python\\Work\\Data\\missing.csv'
"""
def read_portfolio(filename):
    total_cost = 0
    data_list = []

    with open(filename, 'rt') as f:
        headers = next(f)
        column = headers.strip().split(',')
        # print(f'{column[0]:>10s} {column[1]:>10s} {column[2]:>10s}')
        for rowno, line in enumerate(f, start=1):
            data_dict = {}
            # print(line, end='')
            tmp = line.strip().split(',')

            try:
                _shares = int(tmp[1])
                _price = float(tmp[2])
            except ValueError as e:
                print(f'Row {rowno}: Bad row: {line}')
                _shares = int(tmp[1]) if tmp[1] else 0
                _price = float(tmp[2]) if tmp[2] else 0

            # data_dict[tmp[0]] = {column[1]:int(_shares), column[2]:float(_price)}
            # new 2.9
            for index, col_name in enumerate(column):
                if index == 1:
                    data_dict[str(col_name)] = _shares
                elif index == 2:
                    data_dict[str(col_name)] = _price
                else:
                    data_dict[str(col_name)] = tmp[index]
            # print(f'{tmp[0]:>10s} {_shares:>10d} {_price:>10.2f}')

            data_list.append(data_dict)
            total_cost += int(_shares) * float(_price)


read_portfolio(error_file)
"""


# Exercise 2.16: Using the zip() function
"""
def read_portfolio(filename):
    total_cost = 0
    data_list = []

    with open(filename, 'rt') as f:
        headers = next(f)
        column = headers.strip().split(',')
        # print(f'{column[0]:>10s} {column[1]:>10s} {column[2]:>10s}')
        for rowno, line in enumerate(f, start=1):
            data_dict = {}
            # print(line, end='')
            tmp = line.strip().split(',')



            # data_dict[tmp[0]] = {column[1]:int(_shares), column[2]:float(_price)}
            # new
            data_dict = dict(zip(column, tmp))
            try:
                tmp_1 = data_dict['shares']
                tmp_2 = data_dict['price']
                _shares = int(tmp_1) if tmp_1 else 0
                _price = float(tmp_2) if tmp_2 else 0
            except ValueError as e:
                print(f'Row {rowno}: Bad row: {line}')

            # print(f'{tmp[0]:>10s} {_shares:>10d} {_price:>10.2f}')

            data_list.append(data_dict)
            total_cost += int(_shares) * float(_price)
    
    return data_list


portfolio_file = 'F:\\vscode_pj\\_practical_py36\\practical-python\\Work\\Data\\portfolio.csv'
new_portfolio_file = 'F:\\vscode_pj\\_practical_py36\\practical-python\\Work\\Data\\portfoliodate.csv'

print(read_portfolio(error_file))

print(read_portfolio(portfolio_file))

print(read_portfolio(new_portfolio_file))
"""



# Exercise 2.17: Inverting a dictionary


prices = {
    'GOOG' : 490.1,
    'AA' : 23.45,
    'IBM' : 91.1,
    'MSFT' : 34.23
}

pricelist = list(zip(prices.values(),prices.keys()))

print('min(pricelist) ', min(pricelist))
print('max(pricelist) ', max(pricelist))



