"""
Data Structures - Lists

append(item)
    Add item to end of list
    equivalent to a[len(a):] = [x]

extend(iter)
    add all items from iterable
    equivalent to a[len(a):] = iterable

insert(i, item)
    add item at a given position of list
    first argument - index
        index where to insert
            a.insert(0,item) inserts at front of list
            a.insert(len(a), item) = a.append(item)

remove(item)
    remove first item of list that's equal to item
    ValueError when item not found

pop(index)
    remove item at given position and return it
    pop() removes and returns last item
    
clear()
    remove all items from list
    equivalent to del a[:]

index(item, start, end)
    return zero-based index of first item found equal to item
        ValueError when not found
    start, end
        optional arguments
        slice notation used to limit the search to subsequence
        return index based on full list, not subsequence

count(item)
    return number of times item appears

sort(*, key=None, reverse=False)
    sort items alphabetically
    key, reverse
        optional arguments
        key used to extract a comparison key from each element
            key=str.lower
        reverse is a boolean value to sort the opposite direction
    NOTE - Not everything can be sorted
        Mixed data cannot sort well
        Some data cannot sort at all

reverse()
    reverse elements

copy()
    return shallow copy
    equivalent to a[:]

"""

fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
fc = fruits.count('apple')
print(fc)

fc = fruits.count('tangerine')
print(fc)

fi = fruits.index('banana')
print(fi)

fi = fruits.index('banana', 4)  # Find next banana starting at position 4
print(fi)

fruits.reverse()
print(fruits)

fruits.append('grape')
print(fruits)

fruits.sort()
print(fruits)

print(fruits.pop())
