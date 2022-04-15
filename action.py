from predicate import *

class Action():
    """An action is an atomic step for state transitions."""
    def preconditions(self):
        """A set of constraints that must be met in order to execute the action."""
        pass
    def postconditions(self):
        """A set of constraints that will be removed or added after the execution of the action."""
        pass

class UNSTACK(Action):
    def __init__(self, block, other_block):
        self.block = block
        self.other_block = other_block
    
    def preconditions(self):
        return {Top(self.block), ArmEmpty(), OnTop(self.block, self.other_block)}
    
    def postconditions(self):
        remove = {OnTop(self.block, self.other_block), ArmEmpty()}
        add = {Holding(self.block), Top(self.other_block)}
        
        return remove, add


class STACK(Action):
    def __init__(self, block, other_block):
        self.block = block
        self.other_block = other_block
    
    def preconditions(self):
        return {Top(self.other_block), Holding(self.block)}

    def postconditions(self):
        remove = {Top(self.other_block), Holding(self.block)}
        add = {ArmEmpty(), OnTop(self.block, self.other_block)}

        return remove, add

class PICKUP(Action):
    def __init__(self, block):
        self.block = block

    def preconditions(self):
        return {Top(self.block), OnTable(self.block), ArmEmpty()}

    def postconditions(self):
        remove = {OnTable(self.block), ArmEmpty()}
        add = {Holding(self.block)}

        return remove, add
    



class PUTDOWN(Action):
    def __init__(self, block):
        self.block = block
    
    def preconditions(self):
        return {Holding(self.block)}

    def postconditions(self):
        remove = {Holding(self.block)}
        add = {OnTable(self.block), ArmEmpty()}