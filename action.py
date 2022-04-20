from predicate import *

class Action():
    """An action is an atomic step for state transitions."""
    def preconditions(self) -> set[Predicate]:
        """A set of constraints that must be met in order to execute the action."""
        return set()
    def postconditions(self) -> tuple[set[Predicate], set[Predicate]]:
        """A set of constraints that will be removed or added after the execution of the action."""
        return set(), set()
    
    def repr(self) -> str:
        return ''

class UNSTACK(Action):
    """UNSTACK(X, Y) means taking block X away from block Y."""
    def __init__(self, block: str, other_block: str):
        self.block = block
        self.other_block = other_block
    
    def preconditions(self) -> set[Predicate]:
        return {Top(self.block), ArmEmpty(), OnTop(self.block, self.other_block)}
    
    def postconditions(self) -> tuple[set[Predicate], set[Predicate]]:
        remove = {OnTop(self.block, self.other_block), ArmEmpty()}
        add = {Holding(self.block), Top(self.other_block)}
        
        return remove, add
    
    def __repr__(self) -> str:
        return 'UNSTACK({}, {})'.format(self.block, self.other_block)


class STACK(Action):
    """STACK(X, Y) means putting block X on block Y."""
    def __init__(self, block: str, other_block: str):
        self.block = block
        self.other_block = other_block
    
    def preconditions(self) -> set[Predicate]:
        return {Top(self.other_block), Holding(self.block)}

    def postconditions(self) -> tuple[set[Predicate], set[Predicate]]:
        remove = {Top(self.other_block), Holding(self.block)}
        add = {ArmEmpty(), OnTop(self.block, self.other_block)}

        return remove, add
    
    def __repr__(self) -> str:
        return 'STACK({}, {})'.format(self.block, self.other_block)

class PICKUP(Action):
    """PICKUP(X) means taking block X from a stack with only block X (height of 1)."""
    def __init__(self, block: str):
        self.block = block

    def preconditions(self) -> set[Predicate]:
        return {Top(self.block), OnTable(self.block), ArmEmpty()}

    def postconditions(self) -> tuple[set[Predicate], set[Predicate]]:
        remove = {OnTable(self.block), ArmEmpty()}

        return remove, {Holding(self.block)}
    
    def __repr__(self) -> str:
        return 'PICKUP({})'.format(self.block)
    



class PUTDOWN(Action):
    """PUTDOWN(X) means putting block X onto the table (result in a new stack with height of 1)."""
    def __init__(self, block: str):
        self.block = block
    
    def preconditions(self) -> set[Predicate]:
        return {Holding(self.block)}

    def postconditions(self) -> tuple[set[Predicate], set[Predicate]]:
        add = {OnTable(self.block), ArmEmpty()}
        
        return {Holding(self.block)}, add
    
    def __repr__(self) -> str:
        return 'PUTDOWN({})'.format(self.block)