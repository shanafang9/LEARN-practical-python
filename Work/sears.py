# sears.py

bill_thickness = 0.11 * 0.001    # Meters (0.11 mm)
sears_height   = 442             # Height (meters)
num_bills      = 1
day            = 1

while num_bills * bill_thickness < sears_height:
    print(day, num_bills, num_bills * bill_thickness)
    day = days + 1
    num_bills = num_bills * 2

print('Number of days', day)
print('Number of bills', num_bills)
print('Final height', num_bills * bill_thickness)


"""

[Running] set PYTHONIOENCODING=utf8 &&"D:\ProgramData\Anaconda3\envs\py37env\python.exe" -u "f:\vscode_pj\_practical_py36\practical-python\Work\sears.py"
1 1 0.00011
Traceback (most recent call last):
  File "f:\vscode_pj\_practical_py36\practical-python\Work\sears.py", line 10, in <module>
    day = days + 1
NameError: name 'days' is not defined

[Done] exited with code=1 in 0.185 seconds

"""

"""
1.哪一行是错误
    第 10 行
2.错误是什么
    变量 'days' 未定义
3.修复错误
    days 改为 day
4.成功运行程序
"""

