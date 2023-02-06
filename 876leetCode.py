# Definition for singly-linked list.


import math 


# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        count = 0
        temp = head
        while temp:
            count += 1
            temp = temp.next

        # if count%2 == 0:
        #     count = math.ceil(count/2) + 1
        # else:
        #     count = math.ceil(count/2)

        count = math.floor(count/2) + 1

        numberOfLoop = 1

        while numberOfLoop < count:
            head = head.next
            numberOfLoop += 1

        return head