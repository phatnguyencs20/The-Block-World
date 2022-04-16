class Predicate():
    """A predicate is a constraint that the state satisfies."""
    def __hash__(self) -> int:
        pass

    def __eq__(self, other: any) -> bool:
        pass

    def __repr__(self) -> str:
        pass

class ArmEmpty(Predicate):
    """ArmEmpty() means that the robot hand is not holding anything."""
    def __init__(self):
        pass

    def __hash__(self) -> int:
        return 0

    def __eq__(self, other: any) -> bool:
        return isinstance(other, self.__class__)

    def __repr__(self) -> str:
        return 'ArmEmpty'


class Holding(Predicate):
    """Holding(X) means that the robot hand is holding block X."""
    def __init__(self, block: chr):
        self.block = block

    def __hash__(self) -> int:
        return hash(ord(self.block) << 3)
    
    def __eq__(self, other: any) -> bool:
        return(
            isinstance(other, self.__class__) and
            self.block == other.block
        )
    
    def __repr__(self) -> str:
        return 'Holding({})'.format(self.block)


class OnTop(Predicate):
    """OnTop(X, Y) means that block X is right above block Y."""
    def __init__(self, block: chr, other_block: chr):
        self.block = block
        self.other_block = other_block

    def __hash__(self) -> int:
        return (hash(ord(self.block)) << 2) ^ (hash(ord(self.other_block)) >> 1)

    def __eq__(self, other: any) -> bool:
        return(
            isinstance(other, self.__class__) and
            self.block == other.block and
            self.other_block == other.other_block
        )

    def __repr__(self) -> str:
        return 'OnTop({}, {})'.format(self.block, self.other_block)


class OnTable(Predicate):
    """OnTable(X) means that block X is at the bottom of a particular stack."""
    def __init__(self, block: chr):
        self.block = block
    
    def __hash__(self) -> int:
        return hash(ord(self.block)) << 2
    
    def __eq__(self, other: any) -> bool:
        return(
            isinstance(other, self.__class__) and
            self.block == other.block
        )
    
    def __repr__(self) -> str:
        return 'OnTable({})'.format(self.block)


class Top(Predicate):
    """Top(X) means that block X is on top of all other blocks of its stack,
    or is being held by the robot hand."""
    def __init__(self, block: chr):
        self.block = block

    def __hash__(self) -> int:
        return hash(ord(self.block)) << 5
    
    def __eq__(self, other: any) -> bool:
        return(
            isinstance(other, self.__class__) and
            self.block == other.block
        )
    
    def __repr__(self) -> str:
        return 'Top({})'.format(self.block)