from predicate import *
from action import *
from queue import LifoQueue
from copy import deepcopy

class TheBlockWorld():
    
    def __init__(self, start_stacks, goal_stacks):
        self.predicates = set()
        self.goal = set()
        self.solution = None
        self.blocks = []

        for stack in start_stacks:
            for i in stack:
                self.blocks.append(i)

        for stack in start_stacks:
            self.predicates.add(ArmEmpty())
            self.predicates.add(OnTable(stack[0]))
            self.predicates.add(Top(stack[len(stack) - 1]))

            for i in range(1, len(stack)):
                self.predicates.add(OnTop(stack[i], stack[i - 1]))
        
        self.database = deepcopy(self.predicates)
        
        for stack in goal_stacks:
            self.goal.add(ArmEmpty())
            self.goal.add(OnTable(stack[0]))
            self.goal.add(Top(stack[len(stack) - 1]))

            for i in range(1, len(stack)):
                self.goal.add(OnTop(stack[i], stack[i - 1]))


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
            if precondition not in self.database:
                return False
        return True

    
    def actions(self):
        actions = []
        for block in self.blocks:
            for other in self.blocks:
                if block != other:
                    if self.applicable(UNSTACK(block, other)):
                        actions.append(UNSTACK(block, other))
                    if self.applicable(STACK(block, other)):
                        actions.append(STACK(block, other))
            if self.applicable(PICKUP(block)):
                actions.append(PICKUP(block))
            if self.applicable(PUTDOWN(block)):
                actions.append(PUTDOWN(block))
        return actions


    
    def apply(self, action):
        if self.applicable(action):
            remove, add = action.postconditions()

            for predicate in remove:
                self.database.remove(predicate)
            
            for predicate in add:
                self.database.add(predicate)

    def solve(self):

        Stack = LifoQueue()
        Stack.put(self.goal)
        self.solution = []

        while not Stack.empty():
            s = Stack.get()
            if isinstance(s, Predicate) and s in self.database:
                pass
            elif isinstance(s, Predicate) and s not in self.database:
                actions = self.actions()
                if actions is not None:
                    for action in actions:
                        if s in action.postconditions()[1]:
                            Stack.put(action)
                            for predicate in action.preconditions():
                                Stack.put(predicate)
                            break
                else:
                    self.solution = None
                    return

            elif isinstance(s, Action):
                self.solution.append(s)
                self.apply(s)
            elif isinstance(s, set):
                Stack.put(s)
                added_new = False
                for predicate in s:
                    if predicate not in self.database:
                        Stack.put(predicate)
                        added_new = True
                if not added_new:
                    Stack.get()
                    for predicate in s:
                        if predicate not in self.database:
                            self.solution = None
                            return
            else:
                raise Exception("Invalid element in Stack.")
        
        return
                
