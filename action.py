from predicate import *

class Action():
    """An action is an atomic step for state transitions."""
    def preconditions(self) -> set[Predicate]:
        """A set of constraints that must be met in order to execute the action."""
        pass
    def postconditions(self) -> tuple[set[Predicate], set[Predicate]]:
        """A set of constraints that will be removed or added after the execution of the action."""
        pass

class UNSTACK(Action):
    """UNSTACK(X, Y) means taking block X away from block Y."""
    def __init__(self, block: int, other_block: int):
        self.block = block
        self.other_block = other_block
    
    def preconditions(self) -> set[Predicate]:
        return {Top(self.block), ArmEmpty(), OnTop(self.block, self.other_block)}
    
    def postconditions(self) -> tuple[set[Predicate], set[Predicate]]:
        remove = {OnTop(self.block, self.other_block), ArmEmpty()}
        add = {Holding(self.block), Top(self.other_block)}
        
        return remove, add


class STACK(Action):
    """STACK(X, Y) means putting block X on block Y."""
    def __init__(self, block: int, other_block: int):
        self.block = block
        self.other_block = other_block
    
    def preconditions(self) -> set[Predicate]:
        return {Top(self.other_block), Holding(self.block)}

    def postconditions(self) -> tuple[set[Predicate], set[Predicate]]:
        remove = {Top(self.other_block), Holding(self.block)}
        add = {ArmEmpty(), OnTop(self.block, self.other_block)}

        return remove, add

class PICKUP(Action):
    """PICKUP(X) means taking block X from a stack with only block X (height of 1)."""
    def __init__(self, block):
        self.block = block

    def preconditions(self) -> set[Predicate]:
        return {Top(self.block), OnTable(self.block), ArmEmpty()}

    def postconditions(self) -> tuple[set[Predicate], set[Predicate]]:
        remove = {OnTable(self.block), ArmEmpty()}
        add = {Holding(self.block)}

        return remove, add
    



class PUTDOWN(Action):
    """PUTDOWN(X) means putting block X onto the table (result in a new stack with height of 1)."""
    def __init__(self, block):
        self.block = block
    
    def preconditions(self) -> set[Predicate]:
        return {Holding(self.block)}

    def postconditions(self) -> tuple[set[Predicate], set[Predicate]]:
        remove = {Holding(self.block)}
        add = {OnTable(self.block), ArmEmpty()}