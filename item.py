class inv_make():
    def __init__(self):
        self.item_list = []
    def gain_item(self, item):
        if len(self.item_list)>10:
            print("인벤토리가 가득 찼다.")
            return False
        self.item_list.append(item)
        print("{} 을(를) 얻었다.".format(item.name))
        return True
    def start_item(self, item):
        self.item_list.append(item)
    def use_item(self, num):
        self.item_list[num].effect()
        del self.item_list[num]

class item_make():
    def __init__(self,name,effect, price):
        self.name = name
        self.effect = effect
        self.price = price 
