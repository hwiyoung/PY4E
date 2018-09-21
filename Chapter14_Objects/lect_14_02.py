class PartyAnimal:
    x = 0

    def __init__(self):
        print('I am constructed')

    def party(self) :
        self.x = self.x + 1
        print('So far',self.x)

    def __del__(self):
        print('I am destructed', self.x)

an = PartyAnimal() # I am constructed
an.party() # So far 1
an.party() # So far 2
an = 42
print('an contains', an) # an contains 42

# I am constructed
# So far 1
# So far 2
# I am destructed 2
# an contains 42