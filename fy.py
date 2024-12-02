class ListNode():
    def __init__(self, head=None, next=None):
        self.head = head
        self.next = next

    def __str__(self):
        return str(self.head)

Node1 = ListNode(1, 3)
Node2 = ListNode(next=2)

print(Node1)
print(Node2.next)
print(Node2)





