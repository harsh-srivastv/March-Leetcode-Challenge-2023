# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        # Base condition
        if lists is None or len(lists) == 0:
            return None
        return self.mergeLists(lists, 0, len(lists) - 1)

    def mergeLists(self, lists, start, end):
        # Base condition
        if start == end:
            return lists[start]
        # Mid of lists of lists
        mid = start + (end - start) // 2
        # Recursive calls for left sublist
        left = self.mergeLists(lists, start, mid)
        # Recursive call for right sublist
        right = self.mergeLists(lists, mid + 1, end)
        # Merge these sorted lists
        return self.merge(left, right)

    @staticmethod
    def merge(left, right):
        # Dummy node
        head = ListNode(-1)
        # Temp node
        temp = head
        # Loop until any of the lists becomes null
        while left is not None and right is not None:
            # Choose the smaller value from left and right lists
            if left.val < right.val:
                temp.next = left
                left = left.next
            else:
                temp.next = right
                right = right.next
            temp = temp.next
        # Take all nodes from left list if remaining
        while left is not None:
            temp.next = left
            left = left.next
            temp = temp.next
        # Take all nodes from right list if remaining
        while right is not None:
            temp.next = right
            right = right.next
            temp = temp.next
        return head.next
        