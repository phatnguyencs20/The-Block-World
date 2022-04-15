from predicate import *
from action import *
from TheBlockWorld import State

A = 'A'
B = 'B'
C = 'C'
D = 'D'
E = 'E'
F = 'F'
G = 'G'

start = [[A, B], [C]]

s = State(start)

print(repr(s))

print('\n')

s.apply(UNSTACK(B, A))

s.apply(STACK(B, C))

print(repr(s))