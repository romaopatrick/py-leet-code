# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        lst = [head]

        cur = head.next

        while cur:
            lst.append(cur)
            cur = cur.next
            
        first_v = lst[k-1].val
        last_v = lst[-(k)].val
        
        lst[k-1].val = last_v
        lst[-(k)].val = first_v

        return head