from node import Node

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def add_node(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.length += 1

    def remove_node(self, data):
        if self.head is None:
            print("The playlist is empty.")
            return
        if self.head.data.title == data.title:
            self.head = self.head.next
            self.length -= 1
            return True
        current = self.head
        while current.next is not None:
            if current.next.data.title == data.title:
                current.next = current.next.next
                self.length -= 1
                if current.next is None:
                    self.tail = current
                return True
            current = current.next
        return False

    def __len__(self):
        return self.length

    def __iter__(self):
        current = self.head
        while current:
            yield current.data
            current = current.next