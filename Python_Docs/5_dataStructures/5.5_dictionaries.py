"""
Data Structures - Dictionaries

Dictionary
    Set of key-value pairs

Keys
    immutable type
        typically strings and numbers

Keys and Tuples
    Can use Tuples as keys
        Tuples must ONLY contain strings, numbers, or tuples
        Tuples CANNOT contain mutable objects (directly or indirectly)

Empty Dictionary
    create using {}

Create pre-filled Dictionary
    create using comma-separated list of key-value pairs within {}
    can also use dict() constructor
        you can specify pairs with keyword arguments
            use it with mutuable sequences that store tuples

Dictionary operations
    Storing values
        Attach a key to it
            dict[key] = val
    Extracting values
        Use a key to get it
            dict[key]
    Delete key-value
        del dict[key]
    Replacing values
        Save using key to OVERWRITE value

Extracting using non-existent keys
    Results in error

Get list of keys of dict
    use list(dict)
    For sorted keys
        use sorted(dict)

Finding key
    use 'in' keyword

Dictionary comprehensions
    Create dictionaries from arbitrary key-value expressions

"""

tel = {'jack': 4098, 'sape': 4139}
tel['guido'] = 4127
print(tel)
print(tel['jack'])

del tel['sape']
tel['irv'] = 4127
print(tel)

print(list(tel))
print(sorted(tel))

print('guido' in tel)
print('mike' in tel)

print(dict([('sape', 4139), ('guido', 4127), ('jack', 4127)]))

print({x: x**2 for x in (2, 4, 6)})
