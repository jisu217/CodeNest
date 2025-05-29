class Human( ):
    '''인간'''
    def create( name, weight ):
        person = Human()
        person.name = name
        person.weight = weight
        return person

    def eat( self ):
        self.weight += 0.1
        print("{}가 먹어서 {}kg이 되었습니다".format(self.name, self.weight))