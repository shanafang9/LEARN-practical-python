


# 1.1

"""

>>> ( 711.25 - 235.14 ) * 75
35708.25
>>> _ * 0.8
28566.600000000002
>>>

"""


# 1.2

"""

>>> help(round)
Help on built-in function round in module builtins:

round(...)
    round(number[, ndigits]) -> number

    Round a number to a given precision in decimal digits (default 0 digits).
    This returns an int when called with one argument, otherwise the
    same type as the number. ndigits may be negative.

>>>
>>> help(for)
  File "<stdin>", line 1
    help(for)
           ^
SyntaxError: invalid syntax
>>> help("for")
The "for" statement
*******************

The "for" statement is used to iterate over the elements of a sequence
(such as a string, tuple or list) or other iterable object:

   for_stmt ::= "for" target_list "in" expression_list ":" suite
                ["else" ":" suite]

The expression list is evaluated once; it should yield an iterable
object.  An iterator is created for the result of the
"expression_list".  The suite is then executed once for each item
provided by the iterator, in the order returned by the iterator.  Each
item in turn is assigned to the target list using the standard rules
for assignments (see Assignment statements), and then the suite is
executed.  When the items are exhausted (which is immediately when the
-- More --

"""




# 1.3

"""

>>> (3+4\
... +5+6)
18
>>>

"""



# 1.4

"""
请求与解析

import urllib.request
from xml.etree.ElementTree import parse


配置代理
import os
os.environ['HTTP_PROXY'] = 'http://yourproxy.server.com'
"""










