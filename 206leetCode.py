# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        prev, curr = None, head

        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        return prev


    def print(self, head):
        curr = head
        while curr :
            print(curr.val, end = "--->")
            curr = curr.next
        print("\n")
# # listNode

l1 = ListNode()
head = l1
l2 = ListNode()
l3 = ListNode()
l4 = ListNode()
l5 = ListNode()

l1.next = l2
l2.next = l3
l3.next = l4
l4.next = l5
l5.next = None

l1.val = 1
l2.val = 2
l3.val = 3
l4.val = 4
l5.val = 5




class anith(object):

    # creatin LInkedLIst using loops


    def createLL(self, n):
        
        i = 0
        h = None

        while i <= n:
            temp = ListNode()
            temp.val = i
            temp.next = h
            h = temp

            i += 1

        return h

    # print LinkedList

    def print(self,head):

        while head:
            print(head.val)
            head = head.next



LL = anith()

head = LL.createLL(10)

# LL.print(head)

obj = Solution()

# # head = [1,2,3,4,5]

ans = obj.reverseList(head)

LL.print(ans)
# ans = obj.print(ans)

# print(ans)

