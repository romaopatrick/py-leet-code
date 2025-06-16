# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return
        
        if head.next is None:
            return head
        
        head.next 
        
        nn = ListNode(head.next.val, ListNode(head.val, self.swapPairs(head.next.next)))
        
        return nn