list_1 = [1,2,3,4,5]


class replace:
    def __init__(self,olditem,newitem):
        self.olditem = olditem
        self.newitem = newitem
    def runn(self):
        list_1[list_1.index(self.olditem)] = self.newitem


hey = replace(1,"hi")
hey.runn()
print(list_1)