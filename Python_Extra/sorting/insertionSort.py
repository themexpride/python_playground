li = [38, 43, 3, 9, 82, 10]

def insertionSort(l):
    for i in range(1, len(l)):
        current = l[i]
        j = i - 1
        while j >= 0 and current < l[j]:
            l[j + 1] = l[j]
            j -= 1
        l[j + 1] = current
    return l

print(insertionSort(li))
