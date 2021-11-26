class hero_make():
    def __init__(self, name):
        self.name = name
        self.level = 1
        self.attack = 10
        self.defend = 2
        self.max_hp = 50
        self.max_mp = 20
        self.hp = self.max_hp
        self.mp = self.max_mp
        self.exp = 0
        self.atk_equip = None
        self.def_equip = None
    def gain_exp(self, n):
        self.exp+=n
        if self.exp>=self.level*10:
            self.exp = self.exp - self.level*10
            self.level+=1
            self.max_hp+=10
            self.max_mp+=5
            self.attack+=5
            self.defend+=2
            print("레벨업")
    


