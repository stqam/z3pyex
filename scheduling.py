from z3 import *


print """
t11, t12, t21, t22, t31, t32 = Ints('t11 t12 t21 t22 t31 t32')
"""

sys.stdin.readline()

print """
s = Solver()

s.add(And([t11 >= 0, t12 >= t11 + 2, t12 + 1 <= 8]))
s.add(And([t21 >= 0, t22 >= t21 + 3, t22 + 1 <= 8]))
s.add(And([t31 >= 0, t32 >= t31 + 2, t32 + 3 <= 8]))"""

sys.stdin.readline()

print """
s.add(Or(t11 >= t21 + 3, t21 >= t11 + 2))
s.add(Or(t11 >= t31 + 2, t31 >= t11 + 2))
s.add(Or(t21 >= t31 + 2, t31 >= t21 + 3))
s.add(Or(t21 >= t22 + 1, t22 >= t12 + 1))
s.add(Or(t12 >= t32 + 3, t32 >= t12 + 1))
s.add(Or(t22 >= t32 + 3, t32 >= t22 + 1))"""

sys.stdin.readline()


t11, t12, t21, t22, t31, t32 = Ints('t11 t12 t21 t22 t31 t32')

s = Solver()

s.add(And([t11 >= 0, t12 >= t11 + 2, t12 + 1 <= 8]))
s.add(And([t21 >= 0, t22 >= t21 + 3, t22 + 1 <= 8]))
s.add(And([t31 >= 0, t32 >= t31 + 2, t32 + 3 <= 8]))

s.add(Or(t11 >= t21 + 3, t21 >= t11 + 2))
s.add(Or(t11 >= t31 + 2, t31 >= t11 + 2))
s.add(Or(t21 >= t31 + 2, t31 >= t21 + 3))
s.add(Or(t21 >= t22 + 1, t22 >= t12 + 1))
s.add(Or(t12 >= t32 + 3, t32 >= t12 + 1))
s.add(Or(t22 >= t32 + 3, t32 >= t22 + 1))

print """
print s.check()
"""
sys.stdin.readline()

print ">>", s.check()
sys.stdin.readline()

print """
print s.model()"""
sys.stdin.readline()

print ">>", s.model()

sys.stdin.readline()
