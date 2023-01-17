"""
More Control Flow Tools - defining functions

def keyword
    function definition
    must be followed by function name and parameters
    body of function
        must be indentented
        first line is the next line after fn name

docstrings
    first statement of function body
        typically a string literal
    can be used to produce docs or help browse to code
    good practice

execution
    new symbol table created
        used for local variables of function
            all variable assignments in the function store value in local symbol table

variable references
    first look
        local symbol table
    next look
        local symbol tables of enclosing functions
    next look
        global symbol table
    final look
        built-in name table

global variables and enclosing function variables
    cannot be directly assigned within a function
        must use global or nonlocal statement for direct assignment
        can also use references

parameters (arguments)
    introduced in local symbol table of called function
        call-by-value
            object reference
    function calls another function
        new local symbol table created for call

function definition and symbol table
    definition associates name with object in current symbol table
        interpreter recognizes object pointed to by the name as user-defined function
            just call the function name in the interpreter to see
    other names can point to same function object
        can also access object
            f = fib -> f(100)

functions without return statement
    in other languages, it's considered a procedure
    in this case, the default return value would be None

methods
    functions that belong to an object
    called using object name and method name with argument
    some are more efficient than using operators
"""

def fib(n):
    """Print a Fibonacci series up to n."""
    a, b  = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

print(fib(100))


a = 100
def something(n):
    a = 10
    print(a)
something(100)
print(a)
def something2(n):
    global a
    a = 10
    print(a)
something2(100)
print(a)

print(something2)
something3 = something
something3(100)
something3(0)

def fib2(n):
    """Return a list containing the Fibonacci series up to n."""
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result
f100 = fib2(100)
print(f100)
