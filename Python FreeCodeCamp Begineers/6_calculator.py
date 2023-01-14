"""
Basic Calculator program.
    Get user input
        two numbers to start
    Perform operation
        Math operations with two numbers
    Return result
        Keep result and get more input
        Quit program
"""
from math import *

calc = "Y"

res = 0

carry = 0


prompt1 = """
Please enter the following operation:
1. Add
2. Subtract
3. Multiply
4. Divide
5. Power
\n
"""
prompt2 = "Please enter the first number: \n"
prompt3 = "Please enter the next number: \n"
prompt_res = "Result: "
prompt_res2 = "Do you wish to perform another operation with your new result? Y/n \n"

def math_op(num1, num2, op):
    if op == 1:
        return num1 + num2
    elif op == 2:
        return num1 - num2
    elif op == 3:
        return num1 * num2
    elif op == 4:
        return num1 / num2
    elif op == 5:
        return num1 ** num2
    else:
        return None

while calc == "Y":
    if carry == 1:
        op = int(input(prompt1))
        n1 = float(input(prompt3))
        res = math_op(res, n1, op)
        print(prompt_res + str(res))
        calc = input(prompt_res2)
    else:
        op = int(input(prompt1))
        n1 = float(input(prompt2))
        n2 = float(input(prompt3))
        res = math_op(n1, n2, op)
        print(prompt_res + str(res))
        carry = 1
        calc = input(prompt_res2)
