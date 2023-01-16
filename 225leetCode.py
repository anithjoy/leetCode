class MyStack(object):
    

    def __init__(self):
        self.stack = []
        

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.stack.append(x)
        

    def pop(self):
        """
        :rtype: int
        """
        return self.stack.pop()
        

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]
        

    def empty(self):
        """
        :rtype: bool
        """
        if self.stack:
            return False
        return True
        


# Your MyStack object will be instantiated and called as such:
obj = MyStack()
obj.push(1)
obj.push(2)

param_3 = obj.top()
param_2 = obj.pop()
param_4 = obj.empty()

print(param_3, param_2,  param_4)
