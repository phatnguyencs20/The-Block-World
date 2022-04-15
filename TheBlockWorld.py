from predicate import *
from action import *

class State():
    
    def __init__(self, stacks):
        self.predicates = set()

        for stack in stacks:
            self.predicates.add(ArmEmpty())
            self.predicates.add(OnTable(stack[0]))
            self.predicates.add(Top(stack[len(stack) - 1]))

            for i in range(1, len(stack)):
                self.predicates.add(OnTop(stack[i], stack[i - 1]))


    def __repr__(self):
        s = ''
        first = True

        for item in self.predicates:
            if first is True:
                s += repr(item)
                first = False
            else:
                s += ' ∧ ' + repr(item)
        
        return s

    
    def applicable(self, action):
        for precondition in action.preconditions():
            if precondition not in self.predicates:
                return False
        return True

    
    def apply(self, action):
        if self.applicable(action):
            remove, add = action.postconditions()

            for predicate in remove:
                self.predicates.remove(predicate)
            
            for predicate in add:
                self.predicates.add(predicate)


    
    

class TheBlockWorld():

    def __init__(self, start, goal):
        self.start = start
        self.goal = goal
        self.solution = None
        self.holding = None
    
