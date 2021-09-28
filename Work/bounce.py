# bounce.py
#
# Exercise 1.5

hight = 100 # meters
data = 3/5
num = 1

while num <= 10:
    hight = data * hight
    # print(num, hight)
    print(num, round(hight, 4))
    num += 1

# print()
