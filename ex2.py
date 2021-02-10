import sys

from z3 import Const, DeclareSort, Function, Solver

print("""
S = DeclareSort('S')       # Declare an uninterpreted sort S
f = Function('f', S, S)    # Declare function f : S -> S
x = Const('x', S)          # Declare constant x : S
""")
sys.stdin.readline()

S = DeclareSort('S')
f = Function('f', S, S)
x = Const('x', S)

print("""
s = Solver()               # Create a solver context
s.add(x == f(f(x)))        # Assert fact 1
s.add(x == f(f(f(x))))     # Assert fact 2
""")
sys.stdin.readline()

s = Solver()
s.add(x == f(f(x)))
s.add(x == f(f(f(x))))

print("""
print s                   # Print solver's state
""")
sys.stdin.readline()
print(">>", s)
sys.stdin.readline()

print("""
print s.check()           # Check satisfiability
""")
sys.stdin.readline()
print(">>", s.check())
sys.stdin.readline()

print("""
s.add(x != f(x))
print s
""")

s.add(x != f(x))
sys.stdin.readline()

print(">>", s)
sys.stdin.readline()

print("""print s.check()""")
sys.stdin.readline()

print(">>", s.check())
sys.stdin.readline()
