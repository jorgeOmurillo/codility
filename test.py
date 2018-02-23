class BinT():
    def __init__(self, value):
        self.value = value
        self.left_node = None
        self.right_node = None
    
    def insert_left(self, value):
        if self.left_node:
            self.left_node.value = value
        else:
            temp = BinT(value)
            temp.left_node = self.left_node
            self.left_node = temp

    def insert_right(self, value):
        if self.right_node:
            self.right_node.value = value
        else:
            temp = BinT(value)
            temp.right_node = self.right_node
            self.right_node = temp

    def pre_order(self):
        print(self.value)

        if self.left_node:
            self.left_node.pre_order()
        if self.right_node:
            self.right_node.pre_order()

hello = BinT(6)
hello.insert_right(1)
hello.insert_left(2)

hello.pre_order()
