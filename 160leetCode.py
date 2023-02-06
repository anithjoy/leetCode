# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Input given
# list1 = [4,1,8,4,5]
# list2 = [5,6,1,8,4,5]

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """

        copyHeadA = headA
        copyHeadB = headB

        countA = 0
        countB = 0

        while copyHeadA or copyHeadB:

            if copyHeadA:
                countA += 1
                copyHeadA = copyHeadA.next
            
            if copyHeadB:
                countB += 1
                copyHeadB = copyHeadB.next

        increment = abs(countA - countB)
        count = 0

        while headA or headB:

            if countA > countB and count < increment:
                count += 1
                headA = headA.next
                continue
            elif countB>countA and count < increment:
                count += 1
                headB = headB.next
                continue

            if headA.val == headB.val:
                return headA
            headA = headA.next
            headB = headB.next

        return headA



# Code from neetCode
# below code is very good thant he above one. 
# learned something new concept


    def getIntersectionNode_NeetCode(self, headA, headB):

        l1 = headA
        l2 = headB

        while l1 != l2:
            l1 = l1.next if l1 else headB
            l2 = l2.next if l2 else headA

        return l1
            

        



"""
     def getIntersectionNode(self, headA, headB):
      
        copyHeadA = headA
        copyHeadB = headB

        countA = 0
        countB = 0

        while copyHeadA or copyHeadB:

            if copyHeadA:
                countA += 1
                copyHeadA = copyHeadA.next
            
            if copyHeadB:
                countB += 1
                copyHeadB = copyHeadB.next

        

        increment = abs(countA - countB)
        print(countA,countB,increment)
        count = 0

        while headA or headB:

            if countA > countB and count < increment:
                count += 1
                headA = headA.next
                print("run headA")
                continue
            elif countB>countA and count < increment:
                count += 1
                headB = headB.next
                print("run headB", headB.val)
                continue
            print("comparison",headA.val,headB.val)
            if headA.val == headB.val:
                return headA
            headA = headA.next
            headB = headB.next

        return headA"""