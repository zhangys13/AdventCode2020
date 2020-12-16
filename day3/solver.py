import re
from pathlib import Path
from IPython import embed

def solver(inputs, slope=[3, 1]):
    pos = 0
    width = len(inputs[0])
    ret = 0
    for i in range(0, len(inputs), slope[1]):
        if inputs[i][pos] == '#':
            ret += 1
        pos = (pos + slope[0]) % width
    return ret

def solver2(inputs):
    ret = 1
    for slope in [[1, 1], [3, 1], [5, 1], [7,1], [1,2]]:
        ret *= solver(inputs, slope=slope)

    return ret

fn = Path('input.txt')
inputs = [ x for x in fn.read_text().split('\n') if len(x) > 0]
# print(solver(inputs))
print(solver2(inputs))
