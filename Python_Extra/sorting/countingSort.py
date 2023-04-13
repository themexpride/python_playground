li = [2, 1, 2, 0, 1]

def countingSort(lp):
    max_val = max(lp) + 1
    count = [0] * max_val 
    for i in lp:
        count[i] = count[i] + 1
    st = count[0]
    p1 = 1
    while p1 < len(count):
        count[p1] = count[p1] + st
        st = count[p1]
        p1 += 1
    output = [0] * len(lp)
    for v in lp[::-1]:
        c = count[v] - 1
        output[c] = v
        count[v] -= 1
    return output

print(countingSort(li))
