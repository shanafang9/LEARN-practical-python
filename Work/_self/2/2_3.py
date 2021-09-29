
file_path = 'F:\\vscode_pj\\_practical_py36\\practical-python\\Work\_self\\1\\portfolio.csv'
"""
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
            # print(line, end='')
            tmp = line.strip().split(',')

            try:
                _shares = int(tmp[1])
                _price = float(tmp[2])
            except ValueError as e:
                _shares = int(tmp[1]) if tmp[1] else 0
                _price = float(tmp[2]) if tmp[2] else 0

            data_dict[tmp[0]] = {column[1]:int(_shares), column[2]:float(_price)}

            print(f'{tmp[0]:>10s} {_shares:>10d} {_price:>10.2f}')

            data_list.append(data_dict)
            total_cost += int(_shares) * float(_price)

    return total_cost

cost = portfolio_cost(file_path)
print('Total cost:', cost)
"""


# Exercise 2.8: How to format numbers
"""
value = 42863.1
print(f'{value:0.4f}')      #42863.1000
print(f'{value:>16.2f}')    #        42863.10
print(f'{value:<16.2f}')    #42863.10
print(f'{value:*>16,.2f}')  #*******42,863.10

print('%0.4f' % value)
print('%16.2f' % value)
"""

# Exercise 2.9: Collecting Data

def read_portfolio(filename):
    total_cost = 0
    data_list = []

    with open(filename, 'rt') as f:
        headers = next(f)
        column = headers.strip().split(',')
        print(f'{column[0]:>10s} {column[1]:>10s} {column[2]:>10s}')
        s1 = '_'
        print(' '.join([f"{'':_^10}"]*3))
        # for line in f:
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

    # return total_cost
    return data_list

def read_prices(filename):
    with open(filename, 'rt') as f:
        data_dict = {}
        for line in f:
            tmp = line.strip().split(',')
            try:
                _price = float(tmp[1])
            except ValueError as e:
                _price = float(tmp[1]) if tmp[1] else 0
            except IndexError as e:
                print(line.__repr__())
                pass
            data_dict[tmp[0]] = _price
    return data_dict

def make_report(portfolio, prices):
    for data_dict in portfolio:
        _name = data_dict['name']
        if _name in prices:
            data_dict['change'] = prices[_name] -data_dict['price']
    return portfolio


portfolio_file = 'F:\\vscode_pj\\_practical_py36\\practical-python\\Work\\Data\\portfolio.csv'
prices_file = 'F:\\vscode_pj\\_practical_py36\\practical-python\\Work\\Data\\prices.csv'

portfolio = read_portfolio(portfolio_file)
print('portfolio: ', portfolio)
prices = read_prices(prices_file)
print('prices: ', prices)
report = make_report(portfolio, prices)
print('report: ', report)


def _print(lst):
    for index, i in enumerate(lst):
        if index == 0:
            column = list(i.keys())
            for j in column:
                print(f'{j.capitalize():>10s} ', end='')
            print()
            # print(f'{column[0]:>10s} {column[1]:>10s} {column[2]:>10s}')
        for _, v in i.items():
            if isinstance(v, str):
                print(f'{v:>10s} ', end='')
            elif isinstance(v, int):
                print(f'{v:>10d} ', end='')
            elif isinstance(v, float):
                print(f'{v:>10.2f} ', end='')
        print('')


_print(report)