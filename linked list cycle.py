# buscando un ciclo en una linked list

class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head

        while fast and fast.next:  # mientras que no haya un null en un nodo.next
            slow = slow.next
            fast = fast.next.next  # avanza 2 espacios

            if slow == fast:  # si ambos punteros se encuentran hay un ciclo
                return True

        return False  # no hay ciclo
    