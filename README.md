# uarray

```python
from uarray import *

x1 = uarray([0, 1, 2], 'cpu')
x2 = uarray([3, 4, 5], 'gpu')
out = uarray([0, 0, 0], 'cpu')

with context('gpu'):
    add(x1, x2, out)

print(f'out = {out.array}')
```

```
Switching context from cpu to gpu
Moving "x1" from cpu to gpu
Allocating memory for "out" on gpu
Adding arrays in gpu
Moving "out" from gpu to cpu
Switching context from gpu to cpu
out = [3, 5, 7]
```
