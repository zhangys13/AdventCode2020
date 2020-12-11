from pathlib import Path
from IPython import embed

def solver(inputs, target=2020):
    tmp = set()
    for x in inputs:
        if x in tmp:
            return (x * (target - x))
        else:
            tmp.add(target - x)

    return None

def solver2(inputs):
    # O(n ** 2)
    for x in inputs:
        new_ins = inputs.copy()
        new_ins.remove(x)
        ret = solver(new_ins, target=2020 - x)
        if ret is not None:
            return ret * x
    return None


fn = Path('input.txt')
inputs = [ int(x) for x in fn.read_text().split('\n') if len(x) > 0]
# print(solver(inputs))
print(solver2(inputs))
