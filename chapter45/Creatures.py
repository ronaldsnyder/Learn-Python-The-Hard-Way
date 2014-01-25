from Hero import Hero

class Monster(Hero):
    """Base Monster Class"""
    def __init__(self):
        super(Monster,self).__init__()
        self.name = 'Monster'
    