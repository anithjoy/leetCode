class KthLargest(object):

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.nums = sorted(nums,reverse= True)
        self.k = k
        
        

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        #consider 3 element [3,4,5,5]
        #insert 7 <= 3, 7<= 4, 7 <= 5,
        
        self.insert(val) # O(n)
        if len(self.nums) < self.k:
            return None
        return self.nums[((self.k)-1)]
       
    def insert(self,val):
        for i in range(len(self.nums)):
            if val >= self.nums[i]:
                self.nums.insert(i,val)
                return
        self.nums.insert(len(self.nums),val)
        return

        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)