# The two chains cannot both use the same gear from the extra gear group
# get all of the extra gear group pairs
# save these pairs to a set
# P * e1/p, Q * e2/ti -> (e1, e2) -> whether this exist in the set
# O(mn) for every query
from fractions import Fraction

def solve(P, Q, pedals, tires, extras_pairs):
    found = False
    # p/e1 * e2/ti = P/Q => e2/e1 * p/ti = P/Q => e2/e1 = P*ti / Q * p
    for p in pedals:
        for ti in tires:
            tmpval = Fraction(P*ti, Q*p)
            if tmpval in extras_pairs:
                found = True
                break
        if found:
            break
    return 'Yes' if found else 'No'
    
def solve_problem():
    T = int(input())
    for t in range(1, T+1):
        print("Case #" + str(t) + ":")
        l = input().strip()
        while not l:
            l = input().strip()
        Np, Ne, Nt = map(int, l.split())
        pedals = list(map(int, input().split()))
        extras = list(map(int, input().split()))
        tires = list(map(int, input().split()))

        # all the pairs of extra gears
        extras_pairs = set()
        for i in range(Ne):
            for j in range(i+1, Ne):
                # a ratio or fraction
                extras_pairs.add(Fraction(extras[i], extras[j]))
                extras_pairs.add(Fraction(extras[j], extras[i]))
        
        M = int(input())
        for _ in range(M):
            P, Q = map(int, input().split())
            result = solve(P, Q, pedals, tires, extras_pairs)
            print(result)

solve_problem()
