__all__ = ['context', 'get_context', 'uarray', 'add']

current_device = 'cpu'

class context(object):
    def __init__(self, device):
        self.device = device
    def __enter__(self):
        global current_device
        print(f'Switching context from {current_device} to {self.device}')
        self.previous_device = current_device
        current_device = self.device
    def __exit__(self, *args):
        global current_device
        print(f'Switching context from {current_device} to {self.previous_device}')
        current_device = self.previous_device

def get_context():
    return current_device

class uarray(object):
    def __init__(self, array=None, device='cpu'):
        self.array = array
        self.device = device

def add(x1, x2, out):
    dx1 = x1
    if x1.device != current_device:
        print(f'Moving "x1" from {x1.device} to {current_device}')
        dx1 = uarray(array=x1.array, device=current_device)
    dx2 = x2
    if x2.device != current_device:
        print(f'Moving "x2" from {x2.device} to {current_device}')
        dx2 = uarray(array=x2.array, device=current_device)
    dout = out
    if out.device != current_device:
        print(f'Allocating memory for "out" on {current_device}')
        dout = uarray(array=out.array, device=current_device)
    print(f'Adding arrays in {current_device}')
    for i in range(len(dx1.array)):
        dout.array[i] = dx1.array[i] + dx2.array[i]
    if out.device != dout.device:
        print(f'Moving "out" from {current_device} to {out.device}')
        out.array = dout.array
