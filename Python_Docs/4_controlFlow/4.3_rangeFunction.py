"""
More Control Flow Tools - range() functions

range()
    iterate over sequence of numbers
        generated math progressions

specified endpoint
    argument passed in
    never part of generated sequence
        if range(10) -> 10 values -> 0-9

specified start and end points
    end point is never part of generated sequence
        start point is

increment ('step')
    second or third argument
    specify the increments of the generated sequence
        can be positive or negative

iterating over indices
    works for sequences (lists, strings...)
    combine range() and len()
        range(len(seq))

enumerating over index iteration for sequences
    python recommends using enumerate() fnction

what does range() return
    an object
        constructor to generate the successive items
"""

for i in range(5):
    print(i)

print(list(range(5, 10)))

print(list(range(0, 10, 3)))

print(list(range(-10, -100, -30)))

a = ['Mary', 'had', 'a', 'little', 'lamb']
for i in range(len(a)):
    print(i, a[i])

for i, val in enumerate(a):
    print(i, val)

print(sum(range(4)))
