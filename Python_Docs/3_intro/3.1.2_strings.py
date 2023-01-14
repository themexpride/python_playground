"""
Using Python as a Calculator - Strings

Enclosing Strings
    ""
    ''

Escape quotes
    \'
    mix of "" and ''

Special characters
    They always start with \
    \n - output new line

Output
    print() outputs a function or operation
        \n is added by default
        
Raw Strings
    Add r to a string OR Add \\ OR repr()
    Special characters won't be interpreted
        This may not end in an odd number of \
            Use \\ instead
    Only used to prevent backslash character and you don't have odd number of them

Span muleiple lines
    Use \"\"\"...\"\"\" or '''...''' (ignore backspaces)
    end-of-lines automatically included
        add \ right after the first three quote characters to remove end-of-line space at top

Concatenation
    + to concatenate
    * to concatenate copies specified number of times
    Two or more string literals '' '' automatically concatenate
        Not with variables or expressions -> Use + operator

Index
    Each character has a index
    No character types -> Only string of size 1
    Index can also be negative

Slicing
    Obtain individual characters = Obtain substring
    Specify range with :
        0:2 -> pos 0 to 1
        4:7 -> pos 4 to 6
    Defaults
        :2 -> beginning to pos 1
        4: -> pos 4 to end
        -2: -> pos second-last to end
    Include all
        Use either :i or i:

Out-of-range
    Accessing an out-of-bounds index
        returns error message
    Slicing with out-of-bounds index
        returns characters found within the range

Immutable - Strings
    Strings cannot be changed
    Make new strings instead

Length
    built-in function len() returns length of a string
        len("Two") -> 3
    
"""

print("One")
print('One')

print('Let\'s kick it')
print("Let\'s kick it")

print('\n')

print(r'C:\One\Fuck\Face')
print('C:\\One\\Fuck\\')

print("""
Fuck around and find out!
Fuck around and find out!
""")
print('''\
Big Baby Deal
Big Baby Deal
''')

print("One" + "Two")
print(3 * "Waaah")
print("Where" "Are" "You" "Yeezy")

one = "One"
print(one[1])
print(one[-1])

print(one[1:])
print(one[-1:])
print(one[32:])

print(len("Three"))
print(len(one))
