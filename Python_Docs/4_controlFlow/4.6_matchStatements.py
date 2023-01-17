"""
More Control Flow Tools - match statements

match statement
    takes an expression and compares value to successive patterns
        given as one or more case blocks
    like the paradigm of switch statement, but more similar to pattern matching
    only first match pattern gets executed
    can also extract components from the value into variables
        sequence elements or object attributes

underscore as a case
    acts as a wildcard
        never fails to match

no case matches
    no branches are executed

combine literals in single pattern
    when multiple case matches want to return same value
        use |
            case 401 | 403 | 404

unpacking assignments - bind variables
    we can unpack a value onto a variable
        case (x, y) -> (x,y) = point
    we can bind variables as a result
        case (0, y)

Classes
    Used to structure data
    Can use the class name following an argument list resembling a constrctor
        will capture attributes into variables
        a way to construct objects with match statement

Positional Parameters
    used to order attributes
    can also define specific position for attributes by setting __match_args__ special attribute in class
        ex. set it to ("x", "y")
            Point(1, var) = Point(1, y=var) = Point(x=1, y=var) = Point(y=var, x=1)

Nested Patterns
    arbitrary nesting

Guard
    patterns can also include an if clause
        case Point(x,y) if x==y):
    if guard is false, the match goes to the next case block

Match statement features
    tuple and list patterns
        they have the same meaning
        match arbitrary sequences
        don't match iterators or strings
    extended unpacking
        sequence patterns can have [x,y,*rest], (x,y,*rest)
            can replace rest wtih _
    mapping patterns
        {"b": b, "l": l} to capture "b" and "l" values from dictionary
            extra keys ignored
        can also support **rest
            **_ redudant so no
    subpatterns
        capture using as keyword
            case (Point(x1, y1), Point(x2, y2) as p2):
                capture second element of input as p2
    literals comparison
        most literals compared by equality
        exception is singletons
            compared by identity
    named constant patterns
        only dotted names allowed
            prevent them from being interpreted as capture variable
    
    
"""
def http_error(status):
    match status:
        case 400:
            return "Bad Request"
        case 402 | 403:
            return "Huh"
        case 404:
            return "Not found"
        case 418:
            return "I'm a teapot"
        case _:
            return "Somethings wrong"

def pointTuple(point):
    match point:
        case (0,0):
            print("Origin")
        case (0,y):
            print(f"Y={y}")
        case (x,0):
            print(f"X={x}")
        case (x,y):
            print(f"X={x}, Y={y}")
        case _:
            raise ValueError("Not a point")

class Point:
    x: int
    y: int

def where_is(point):
    match point:
        case Point(x=0, y=0):
            print("Origin")
        case Point(x=0, y=y):
            print(f"Y={y}")
        case Point(x=x, y=0):
            print(f"X={x}")
        case Point():
            print("Somewhere else")
        case _:
            print("Not a point")

def where_is_nest(points):
    match points:
        case []:
            print("No points")
        case [Point(0, 0)]:
            print("Origin")
        case [Point(x, y)]:
            print(f"Single point {x}, {y}")
        case [Point(0, y1), Point(0, y2) as p2]:
            print(f"Two on the Y axis at {y1}, {y2}")
            print(p2)
        case _:
            print("Something else")

def where_is_2(point):
    match point:
        case Point(x,y) if x == y:
            print(f"Y=X at {x}")
        case Point(x,y):
            print("Not on the diagonal")

from enum import Enum
class Color(Enum):
    RED = 'red'
    GREEN = 'green'
    BLUE = 'blue'

color = Color(input("Enter your choice of 'red', 'blue', or 'green' \n"))

match color:
    case Color.RED:
        print("I see red!")
    case Color.BLUE:
        print("The blues...")
    case Color.GREEN:
        print("Grass is green")

