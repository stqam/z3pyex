from z3 import *

def pprove(e):
    print e
    sys.stdin.readline()
    prove(e)
    print ""
    sys.stdin.readline()

def psolve(e):
    print e
    sys.stdin.readline()
    solve(e)
    print ""
    sys.stdin.readline()


x      = BitVec('x', 32)
powers = [ 2**i for i in range(32) ]
fast   = And(x != 0, x & (x - 1) == 0)
slow   = Or([ x == p for p in powers ])

print """
x      = BitVec('x', 32)
powers = [ 2**i for i in range(32) ]
fast   = And(x != 0, x & (x - 1) == 0)
slow   = Or([ x == p for p in powers ])
"""
sys.stdin.readline()

print "prove(fast == slow)"
sys.stdin.readline()

pprove(fast == slow)

print """buggy version...
fast   = x & (x - 1) == 0"""

fast   = x & (x - 1) == 0

sys.stdin.readline()
print "prove(fast == slow)"

sys.stdin.readline()

pprove(fast == slow)


