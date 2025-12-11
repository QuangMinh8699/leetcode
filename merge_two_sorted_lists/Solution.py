from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:
            return list2
        if list2 is None:
            return list1
        if list1.val < list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2

# Hàm tạo list từ mảng (ngoài class)
def build_list(arr):
    dummy = ListNode()
    current = dummy
    for x in arr:
        current.next = ListNode(x)
        current = current.next
    return dummy.next

# Hàm in LinkedList (ngoài class)
def print_list(node):
    while node:
        print(node.val, end=" -> ")
        node = node.next
    print("None")

if __name__ == "__main__":
    s = Solution()
    l1 = build_list([1,2,4])
    l2 = build_list([1,3,4])
    result = s.mergeTwoLists(l1, l2)
    print_list(result)
