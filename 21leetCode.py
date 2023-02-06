# Definition for singly-linked list.
# this is working

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        merged = ListNode(None)
        status = True
        firstNode = None

        while list1 and list2:

            if list1.val <= list2.val:
                if status == True:
                    firstNode = list1
                    status = False
                
                merged.next = list1
                merged = list1
                list1 = list1.next

            else:
                if status == True:
                    firstNode = list2
                    status = False

                merged.next = list2
                merged = list2
                list2 = list2.next


        if list1:
            merged.next = list1
        elif list2:
            merged.next = list2

        return firstNode


l1 = ListNode(1)
l2 = ListNode(3,l1)
l3 = ListNode(5,l2)
l4 = ListNode(7,l3)
l5 = ListNode(9,l4)


c1 = ListNode(2)
c2 = ListNode(4,c1)
c3 = ListNode(6,c2)
c4 = ListNode(8,c3)
c5 = ListNode(10,c4)


obj = Solution()

ans = obj.mergeTwoLists(l5,c5)

print(ans)