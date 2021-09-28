# mortgage.py
#
# Exercise 1.7

# principal = 500000
# rate = 0.05
# payment = 2684.11
# total_paid = 0.0
# count = 1

# while principal > 0:
#     principal = principal * (1+rate/12) - payment
#     count += 1
#     total_paid = total_paid + payment

# print('Total paid', total_paid)
# print('Month ', count)


# Exercise 1.8

# principal = 500000
# rate = 0.05
# payment = 2684.11
# total_paid = 0.0
# count = 0

# while principal > 0:
#     count += 1
#     if count <= 12:
#         all_payment = payment + 1000
#     else:
#         all_payment = payment
#     principal = principal * (1+rate/12) - all_payment
#     total_paid = total_paid + all_payment

# print('Total paid', total_paid)
# print('Month ', count)






# Exercise 1.9

principal = 500000
rate = 0.05
payment = 2684.11
total_paid = 0.0
count = 0
extra_payment_start_month = 12 * 5 + 1 # 61
extra_payment_end_month = 12 * 5 + 12 * 4 # 108
extra_payment = 1000

while principal > 0:
    count += 1
    if extra_payment_start_month <= count <= extra_payment_end_month:
        all_payment = payment + extra_payment
    else:
        all_payment = payment
    principal = principal * (1+rate/12) - all_payment
    total_paid = total_paid + all_payment
    # print(count, payment, total_paid)
    print(f'{count:3} {payment} {total_paid:10.2f}')

print('Total paid', total_paid)
print('Month ', count)


# Exercise 1.17
"""
print(f'{count:3} {payment} {total_paid:10.2f}')
"""
