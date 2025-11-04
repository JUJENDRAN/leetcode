
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def modifiedList(self, nums: list[int], head: ListNode) -> ListNode:
        num_set = set(nums)

        dummy = ListNode(0)
        dummy.next = head

        curr = dummy

        while curr.next:
            if curr.next.val in num_set:
                curr.next = curr.next.next
            else:
                curr = curr.next

        return dummy.next