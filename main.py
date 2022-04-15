from TheBlockWorld import State

A = 'A'
B = 'B'
C = 'C'
D = 'D'
E = 'E'
F = 'F'
G = 'G'

start = [[A, B], [C, D, E], [F], [G]]
goal = [[B, A]]

s = State(start)

print(repr(s))