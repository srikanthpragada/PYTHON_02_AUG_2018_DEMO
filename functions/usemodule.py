# import mymodule
# from mymodule import add,mul

import sys

sys.path.append(r"e:\classroom\python\aug2\demo\exercises")

import anothermodule

from mymodule import *

print(add(10, 20))
print(mul(10, 20))

print(sys.path)
