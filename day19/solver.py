import re
import sys
from pathlib import Path
from IPython import embed

sys.setrecursionlimit(10000)

def solver(inputs):
    ret = 0
    rule = {}  # idx: [ ... [idx] ... ] or str
    msgs = []
    for line in inputs:
        sp = re.split(':|\|', line)
        if len(sp) == 1:  # msg
            msgs.append(line)
        else:  # rule
            idx = int(sp[0])
            rule[idx] = []
            for text in sp[1:]:
                match = re.search(r'\s*\"(\w*)\"\s*', text)
                if match is None:
                    sub = [ int(x) for x in text.split() if len(x) > 0]
                    rule[idx].append(sub)
                else:
                    rule[idx] = match.group(1)

    def is_valid(msg, msg_idx, rule_idx):
        # leaf rule
        if isinstance(rule[rule_idx], str):
            if msg[msg_idx] == rule[rule_idx]:
                return True, msg_idx + 1
            else:
                return False, msg_idx

        for subs in rule[rule_idx]:  #  遍历 | 两边
            new_m_id = msg_idx
            subs_tf = True
            for sub in subs:  # 在 | 的一边
                tf, new_m_id = is_valid(msg, new_m_id, sub)
                if not tf:
                    subs_tf = False
                    break   # 没通过，是 | 的另一边
            if subs_tf:  # 在 | 的某一边通过了
                return True, new_m_id
        return False, msg_idx  # 都没通过




    for msg in msgs:
        tf, end_id =  is_valid(msg, msg_idx=0, rule_idx=0)
        if tf and end_id == len(msg):
            ret += 1
    return ret

def solver2(inputs):
    ret = 0
    rule = {}  # idx: [ ... [idx] ... ] or str
    msgs = []
    for line in inputs:
        sp = re.split(':|\|', line)
        if len(sp) == 1:  # msg
            msgs.append(line)
        else:  # rule
            idx = int(sp[0])
            rule[idx] = []
            for text in sp[1:]:
                match = re.search(r'\s*\"(\w*)\"\s*', text)
                if match is None:
                    sub = [ int(x) for x in text.split() if len(x) > 0]
                    rule[idx].append(sub)
                else:
                    rule[idx] = match.group(1)

    # part2 change
    rule[8].append([42, 8])
    rule[11].append([42, 11, 31])

    def is_valid(msg, msg_idx, rule_idx):
        if msg_idx >= len(msg):
            return False, msg_idx + 1  # +1 为了最后 msg 的 while 能停来
        # leaf rule
        if isinstance(rule[rule_idx], str):
            if msg[msg_idx] == rule[rule_idx]:
                return True, msg_idx + 1
            else:
                return False, msg_idx

        for subs in rule[rule_idx]:  #  遍历 | 两边
            new_m_id = msg_idx
            subs_tf = True
            loop_frontier = msg_idx
            for sub in subs:  # 在 | 的一边
                tf, new_m_id = is_valid(msg, new_m_id, sub)
                if tf:
                    loop_frontier = new_m_id
                if not tf:
                    subs_tf = False
                    #if sub == rule_idx:  # loop 节点前，已经通过的sub 可以重复计算，算通过
                        #return False, loop_frontier
                    break   # 没通过，是 | 的另一边
            if subs_tf:  # 在 | 的某一边通过了
                return True, new_m_id
        return False, msg_idx  # 都没通过




    for msg in msgs:
        tf, end_id =  is_valid(msg, msg_idx=0, rule_idx=0)
        if tf and end_id == len(msg):
            ret += 1
    return ret


fn = Path('input.txt')
inputs = [ x for x in fn.read_text().split('\n') if len(x) > 0]
#print(solver(inputs))
print(solver2(inputs))
