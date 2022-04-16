from predicate import *
from action import *
from TheBlockWorld import *

A = 'A'
B = 'B'
C = 'C'
D = 'D'
E = 'E'
F = 'F'
G = 'G'

start = [[A, B], [C]]

goal = [[A], [C], [B]]

s = TheBlockWorld(start, goal)

print(repr(s))

print('------------------------------------------------------------------')

s.solve()

print(repr(s))