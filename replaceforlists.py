list_1 = [1,2,3,4,5]


class replace:
    def __init__(self,index1,item):
        self.index1 = int(index1)
        self.item = item
    def runn(self):
        list_1[self.index1] = self.item


hey = replace(1,"hi")
hey.runn()
print(list_1)