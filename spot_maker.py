class spot():
    def __init__(self, name):
        self.name = name
        self.east = None
        self.west = None
        self.south = None
        self.north = None
        self.mpc = []
        self.explain = ""
        self.regen = 0
        self.monster = []
    def set_east(self, east):
        self.east = east
        east.west = self
    def set_north(self, north):
        self.north = north
        north.south = self
    def set_explain(self, explain):
        for nnn in self.mpc:
            explain+=("\n"+nnn.name+" 이(가) 있다")
        if self.east != None:
            explain += "\n동쪽으로 갈수 있다"
        if self.west != None:
            explain += "\n서쪽으로 갈수 있다"
        if self.south != None:
            explain += "\n남쪽으로 갈수 있다"
        if self.north != None:
            explain += "\n북쪽으로 갈수 있다"
        self.explain = explain
    def regen_change(self, n):
        self.regen = n
    def monster_append(self, n):
        self.monster.append(n)


class monster():
    def __init__(self, name, atk, hp, exp, item):
        self.name = name
        self.atk = atk
        self.hp = hp
        self.exp = exp
        self.item = item
