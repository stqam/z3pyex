from z3 import (BoolSort, Const, Datatype, Exists, ForAll, Function, Implies,
                Not, Solver, unsat)

problem = """Someone who lived in Dreadbury Mansion killed Aunt Agatha. Agatha,
the Butler and Charles were the only people who lived in Dreadbury
Mansion. A killer always hates his victim, and is never richer than
his victim. Charles hates no one that aunt Agatha hates. Agatha hates
everyone except the butler. The butler hates everyone not richer than
Aunt Agatha. The butler also hates everyone Agatha hates. No one hates
everyone. Agatha is not the butler.  Who killed Aunt Agatha?
"""

print(problem)

# declare finite data type mansion
MansionDT = Datatype("Mansion")
MansionDT.declare("Agatha")
MansionDT.declare("Butler")
MansionDT.declare("Charles")

# create finite sort Mansion
Mansion = MansionDT.create()

# constants for ease of reference
a, b, c = Mansion.Agatha, Mansion.Butler, Mansion.Charles


# declare predicates
killed = Function("killed", Mansion, Mansion, BoolSort())
hates = Function("hates", Mansion, Mansion, BoolSort())
richer = Function("richer", Mansion, Mansion, BoolSort())

# quantified variables
x = Const("x", Mansion)
y = Const("y", Mansion)

e1 = Exists([x], killed(x, a))
e2a = ForAll([x, y], Implies(killed(x, y), hates(x, y)))
e2b = ForAll([x, y], Implies(killed(x, y), Not(richer(x, y))))
e3 = ForAll([x], Implies(hates(a, x), Not(hates(c, x))))
e4a = hates(a, a)
e4b = hates(a, c)
e5 = ForAll([x], Implies(Not(richer(x, a)), hates(b, x)))
e6 = ForAll([x], Implies(hates(a, x), hates(b, x)))
e7 = ForAll([x], Exists([y], Not(hates(x, y))))

s = Solver()
s.add(e1)
s.add(e2a)
s.add(e2b)
s.add(e3)
s.add(e4a)
s.add(e4b)
s.add(e5)
s.add(e6)
s.add(e7)

print(s.sexpr())

killer = None
for z in [c, b, a]:
    # checkpoint the solver
    s.push()
    # check whether asserted constraints imply (killed z a)
    s.add(Not(killed(z, a)))
    res = s.check()
    # restore the solve to the last checkpoint
    s.pop()
    if res == unsat:
        killer = z
        break

if killer is not None:
    print(killed(killer, a).sexpr())
