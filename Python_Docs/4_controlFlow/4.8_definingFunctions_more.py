"""
More Control Flow Tools - More on Defining Functions

Function Definitions
    can define functions with a variable number of arguments
        three forms to follow
        can combine forms

Default Argument Values
    specify default value for one or more arguments
        function can be called with fewer arguments than defined to allow
    function can be called in several ways
        mandatory argument
        mand.. + optional argument
        all arguments

in keyword
    test whether or not a sequence contains a certain value

default values - evaluation
    evaluated at the point of function definition
        in the defining scope

default values - mutable objects
    default value evaluated once only
    useful on mutable objects
        list, dictionary, instances...
    can accumulate arguments on subsequent calls
        to stop this, default value should be None

keyword arguments
    arguments of the form kwarg=value used in calls
        name of the argument is explicitly specified
            parrot(voltage=1000)

function call - arg order
    order doesn't matter if keyword arguments are used
        otherwise, it matters
    if using keyword arguments, all arguments must be keyword except required
    required arguments must be filled in always
    optional arguments can remain optional
    non-keyword arguments cannot be included after a keyword argument
    no duplicate values for same argument

**name formal parameter
    receive a dictionary with all keyword arguments
        except those corresponding to formal parameter
    combine with *name formal parameter
        receives a tuple with positional argumebnts beyond formal parameter list
    *name occurs before **name

functional call - keyword arguments and positional arguments
    keyword arguments must follow positional arguments
        all keyword args passed must match one of the args accepted by the function
            also includes non-optional argumens
    no args can receive a value more than once

special parameters
    arguments may be passed either by position or explicitly by keywrod
        restrictions to argument passing due to readability and performance
    can determine between passing by position, position or keyword, or keyword
    you can use symbols to indicate parameter type
        /, *
        def f(pos1, pos2, /, pos_or_kwd, *, kwd1, kwd2)

positional-or-keyword arguments
    when / and * are not present, arguments are passed by position or keyword

positional-only parameters
    place args before /

keyword-only arguments
    place * before the first keyword-only parameter

"""

def ask_ok(prompt, retries=4, reminder='Try Again'):
    while True:
        ok = input(prompt)
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('invalid user response')
        print(reminder)

i = 5
def f(arg=i):
    print(arg)

i = 6
f()

def f2(a, L=[]):
    L.append(a)
    return L

print(f2(1))
print(f2(2))
print(f2(3))

def f3(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L

print(f3(1))
print(f3(2))
print(f3(3))

def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.")
    print("-- Lovely plumage, the", type)
    print("-- It's", state, "!")

parrot(1000)
parrot(voltage=1000)
parrot(voltage=1000000, action='VOOOOM')
parrot(action='VOOOOM', voltage=1000000)
parrot('a million', 'bereft of life', 'jump')
parrot('a thousand', state='pushing up the daisies')

"""These calls wouldn't work
parrot() -> required argument missing
parrot(voltage=5.0, 'dead') -> non-keyword arg after keyword arg
parrot(110, voltage=220) -> multiple values for same argument
parrot(actor='Ok') -> unknown keyword argument
"""



"""
