import sys
sys.path.append('..')

from uarray import *

x1 = uarray([0, 1, 2], 'cpu')
x2 = uarray([3, 4, 5], 'gpu')
out = uarray([0, 0, 0], 'cpu')

with context('gpu'):
    add(x1, x2, out)

print(f'out = {out.array}')
