# s = 'hello world'
# # t = s.replace('l', 'a')
# t = s.replace('l', 'l')

# print(s is t)
# print(id(s))
# print(id(t))


# data = b'hello world'
# print(data)
# print(data[0])  # 104 ASCII code
# text = data.decode('utf-8')
# print(text)
# print(text[0])


# name = 'IBM'
# shares = 100
# price = 91.1
# a = f'{name:>10s}#{shares:10d}#{price:10.2f}'
# print(a)



# --------------------------------------------------------------

symbols = 'AAPL,IBM,MSFT,YHOO,SCO'
# Exercises 1.13
"""
symbols = 'AAPL,IBM,MSFT,YHOO,SCO'

print(symbols[0])   # A
print(symbols[1])   # A
print(symbols[2])   # P
print(symbols[-1])   # O
print(symbols[-2])   # C

# symbols[0] = 'a'    # TypeError: 'str' object does not support item assignment
"""



# Exercises 1.14
"""
symbols += ',GOOG'

print(symbols)

symbols = 'HPQ,' + symbols
symbols = symbols.replace(',', '、')
print(symbols)
"""



# Exercises 1.15
"""
print('IBM' in symbols) # True
print('AA' in symbols) # True
print('CAT' in symbols) # False
"""



# Exercises 1.16
"""
print(symbols.lower())      # 'aapl,ibm,msft,yhoo,sco'
print(symbols)              # 'AAPL,IBM,MSFT,YHOO,SCO'

print(symbols.find('MSFT')) # 9
print(symbols[13:17])   # ',YHO'
symbols = symbols.replace('SCO', 'DOA')
print(symbols)  # 'AAPL,IBM,MSFT,YHOO,DOA'

name = '   IBM   \n'
name = name.strip()    # Remove surrounding whitespace
print(name)     # 'IBM'
print(name.__repr__())

"""



# Exercises 1.17
"""
print(f'{count:3} {payment} {total_paid:10.2f}')
"""








