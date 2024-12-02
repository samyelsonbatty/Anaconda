class Number():
    def __init__(self, value):
        self.value = value
        
    def eval(self):
        return int(self.value)
    
class BinaryOp():
    def __init__(self, right, left):
        self.right = right
        self.left = left
        
class Sum(BinaryOp):
    def eval(self):
        return self.left.eval() + self.right.eval()
    
class Sub(BinaryOp):
    def eval(self):
        return self.left - self.right.eval()
    
class Print():
    def __init_(self, value):
        self.value = value
        
    def eval(self):
        print(self.value.eval())