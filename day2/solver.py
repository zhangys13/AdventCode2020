import re
from pathlib import Path
from IPython import embed

def solver(inputs):
    ret = 0
    for line in inputs:
        match = re.search(r'(\d*)-(\d*)\s*(\w):\s*(\w*)', line)
        cnt_low, cnt_up = int(match.group(1)), int(match.group(2))
        aim_char = match.group(3)
        cnt = match.group(4).count(aim_char)
        if cnt_low <= cnt <= cnt_up:
            ret += 1

    return ret

def solver2(inputs):
    ret = 0
    for line in inputs:
        match = re.search(r'(\d*)-(\d*)\s*(\w):\s*(\w*)', line)
        pos0, pos1 = int(match.group(1)), int(match.group(2))
        aim_char = match.group(3)
        text = match.group(4)
        cnt = int(text[pos0 - 1] == aim_char) + int(text[pos1 - 1] == aim_char)
        if cnt == 1:
            ret += 1

    return ret

fn = Path('input.txt')
inputs = [ x for x in fn.read_text().split('\n') if len(x) > 0]
# print(solver(inputs))
print(solver2(inputs))
