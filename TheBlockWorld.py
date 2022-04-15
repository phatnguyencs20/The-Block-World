class State():

    class ArmEmpty():
        def __init__(self):
            pass

        def __hash__(self):
            return 0

        def __eq__(self, other):
            return isinstance(other, self.__class__)

        def __repr__(self):
            return 'ArmEmpty()'

    
    class Holding():
        def __init__(self, block):
            self.block = block

        def __hash__(self):
            return hash(self.block << 3)
        
        def __eq__(self, other):
            return(
                isinstance(other, self.__class__) and
                self.block == other.block
            )
        
        def __repr__(self):
            return 'Holding({})'.format(self.block)


    class OnTop():
        def __init__(self, block, other_block):
            self.block = block
            self.other_block = other_block

        def __hash__(self):
            return (hash(self.block) << 2) ^ (hash(self.other_block) >> 1)

        def __eq__(self, other):
            return(
                isinstance(other, self.__class__) and
                self.block == other.block and
                self.other_block == other.other_block
            )

        def __repr__(self):
            return 'OnTop({}, {})'.format(self.block, self.other_block)


    class OnTable():
        def __init__(self, block):
            self.block = block
        
        def __hash__(self):
            return hash(self.block) << 2
        
        def __eq__(self, other):
            return(
                isinstance(other, self.__class__) and
                self.block == other.block
            )
        
        def __repr__(self):
            return 'OnTable({})'.format(self.block)


    class Clear():
        def __init__(self, block):
            self.block = block

        def __hash__(self):
            return hash(self.block) << 5
        
        def __eq__(self, other):
            return(
                isinstance(other, self.__class__) and
                self.block == other.block
            )
        
        def __repr__(self):
            return 'Clear({})'.format(self.block)


    def __init__(self, stacks):
        self.stacks = stacks
        self.holding = None
        self.predicate = set()

        for stack in self.stacks:
            self.predicate.add(State.ArmEmpty())
            self.predicate.add(State.OnTable(stack[0]))
            self.predicate.add(State.Clear(stack[len(stack) - 1]))

            for i in range(1, len(stack)):
                self.predicate.add(State.OnTop(stack[i], stack[i - 1]))


    def __repr__(self):
        s = ''
        first = True

        for item in self.predicate:
            if first is True:
                s += repr(item)
                first = False
            else:
                s += ' ∧ ' + repr(item)
        
        return s


    
    

class TheBlockWorld():

    def __init__(self, start, goal):
        self.start = start
        self.goal = goal
        self.solution = None
        self.holding = None
    
