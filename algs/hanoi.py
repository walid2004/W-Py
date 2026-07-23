from functools import lru_cache  
from ctypes import py_object
@lru_cache
def towerhanoi(n, src='A', tar='C', aux='B'):
    if n == 1: 
        print('Move disk 1 from {0} to {1}'.format(src, tar)) 
        return
    towerhanoi(n-1, src, aux, tar) 
    print('Move disk {0} from {1} to {2}'.format(n, src, tar)) 
    towerhanoi(n-1, aux, tar, src)

towerhanoi(5,'A','B','C')

print('ff')