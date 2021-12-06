class spot():
    def __init__(self, name):
        self.name = name
        self.east = None
        self.west = None
        self.south = None
        self.north = None
        self.npc = []
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
        for nnn in self.npc:
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
    def set_npc(self,npc):
        self.npc.append(npc)
        self.set_explain(npc.name + "이 있다.")


class monster():
    def __init__(self, name, atk, hp, exp, item):
        self.name = name
        self.atk = atk
        self.hp = hp
        self.exp = exp
        self.item = item

class npc():
    def __init__(self, name, start_talk):
        self.name = name
        self.start_talk = start_talk
        self.trade_list = []
        self.quest_list = []
    def trade_insert(self, item, price):
        self.trade_list.append((item, price))
    def talk(self):
        print(self.start_talk)
        t = False
        q = False
        if len(self.trade_list)!=0:
            print("1 : 거래하기")
            t = True
        if len(self.quest_list)!=0:
            print("2 : 퀘스트")
            q = True
        print("나가려면 아무키나 누르시오.")
        i = input()
        if i=="1" and t:
            self.trade()
        if i=="2" and q:
            self.quest()
        else:
            return;


        
