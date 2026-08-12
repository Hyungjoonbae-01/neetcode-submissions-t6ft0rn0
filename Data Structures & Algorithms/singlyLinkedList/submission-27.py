class Linked_List():
    def __init__(self, current_node=None, next_node=None):
        self.current_node = current_node
        self.next_node = next_node
class LinkedList:
    
    def __init__(self):
        self.head = None
        
    def get(self, index: int) -> int:
        if (self.head== None) and (index == 0):
            return -1
        head = self.head
        for i in range(index):
            head = head.next_node
            if not head:
                return -1
        return head.current_node

    def insertHead(self, val: int) -> None:
        if self.head == None:
            self.head = Linked_List(val, None)
        else:
            node = Linked_List(self.head.current_node, self.head.next_node)
            self.head = Linked_List(val, node)

    def insertTail(self, val: int) -> None:
        if self.head == None:
            self.head = Linked_List(val, None)
        else:
            node = self.head
            while True:
                next_node = node.next_node
                if next_node:
                    node = node.next_node
                else:
                    break
            node.next_node = Linked_List(val, None)
            print(self.getValues())


    def remove(self, index: int) -> bool:
        if index == 0:
            if self.head== None:
                return False
            if self.head.next_node:
                self.head = self.head.next_node
            else:
                print("hi")
                self.head = None
        else:
            head = self.head
            for i in range(index-1):
                head = head.next_node
            if not head:
                return False
            node_removed = head.next_node
            if not node_removed:
                return False
            next_node = node_removed.next_node
            head.next_node = next_node
            node_removed =None
        return True

    def getValues(self) -> List[int]:
        node = self.head
        ans =[]
        if self.head == None:
            return []
        else:
            while True:
                ans.append(node.current_node)
                next_node = node.next_node
                if next_node:
                    node = node.next_node
                else:
                    break
        return ans
        
