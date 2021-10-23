class inv_make():
    def __init__(self):
        self.item_list = []
    def gain_item(self, item):
        if len(self.item_list)>10:
            return False
        self.item_list.append(item)
        return True
    def use_itme(self, num):
        self.item_list[num].effect()
        del self.item_list[num]

class item_make():
    def __init__(self,name,effect):
        self.name = name
        self.effect = effect
i = item_make("i",sum)
inv = inv_make()
inv.gain_item(i)
