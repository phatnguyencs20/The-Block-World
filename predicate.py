class Predicate():
    """A predicate is a constraint that the state satisfies."""
    def __hash__(self):
        pass

    def __eq__(self, other):
        pass

    def __repr__(self):
        pass

class ArmEmpty(Predicate):
    """ArmEmpty() means that the robot hand is not holding anything."""
    def __init__(self):
        pass

    def __hash__(self):
        return 0

    def __eq__(self, other):
        return isinstance(other, self.__class__)

    def __repr__(self):
        return 'ArmEmpty()'


class Holding(Predicate):
    """Holding(X) means that the robot hand is holding block X."""
    def __init__(self, block):
        self.block = ord(block)

    def __hash__(self):
        return hash(self.block << 3)
    
    def __eq__(self, other):
        return(
            isinstance(other, self.__class__) and
            self.block == other.block
        )
    
    def __repr__(self):
        return 'Holding({})'.format(chr(self.block))


class OnTop(Predicate):
    """OnTop(X, Y) means that block X is right above block Y."""
    def __init__(self, block, other_block):
        self.block = ord(block)
        self.other_block = ord(other_block)

    def __hash__(self):
        return (hash(self.block) << 2) ^ (hash(self.other_block) >> 1)

    def __eq__(self, other):
        return(
            isinstance(other, self.__class__) and
            self.block == other.block and
            self.other_block == other.other_block
        )

    def __repr__(self):
        return 'OnTop({}, {})'.format(chr(self.block), chr(self.other_block))


class OnTable(Predicate):
    """OnTable(X) means that block X is the only block on a particular stack."""
    def __init__(self, block):
        self.block = ord(block)
    
    def __hash__(self):
        return hash(self.block) << 2
    
    def __eq__(self, other):
        return(
            isinstance(other, self.__class__) and
            self.block == other.block
        )
    
    def __repr__(self):
        return 'OnTable({})'.format(chr(self.block))


class Top(Predicate):
    """Top(X) means that block X is on top of all other blocks of its stack,
    or is being held by the robot hand."""
    def __init__(self, block):
        self.block = ord(block)

    def __hash__(self):
        return hash(self.block) << 5
    
    def __eq__(self, other):
        return(
            isinstance(other, self.__class__) and
            self.block == other.block
        )
    
    def __repr__(self):
        return 'Top({})'.format(chr(self.block))