
class Test:

    def __init__(self,num):
      self.num = num

    # private helper function which cannot be accessed out side the class
    def __helperFunction (self,num):
        return num**2
    
    # public function which can be accessed out side the class
    def square(self):
       return self.__helperFunction(self.num)
    


obj1 = Test(2)
res = obj1.square()



print(res)