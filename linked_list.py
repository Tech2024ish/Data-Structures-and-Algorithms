class Node:
    def __init__(self, data):
        self.data = data
        self.next_node = None

    def __repr__(self):
        return "node data: %s" % self.data


class LinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head == None

    def size(self):
        current = self.head
        count = 0

        while current:
            count += 1
            current = current.next_node
        return count

    def add(self, data):
        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node

    def insert(self, data, index):
        if index < 0 or index > self.size():
            raise IndexError("Index out of bound error.")
        if index == 0:
            self.add(data)
            return
        new_node = Node(data)
        position = 0
        current = self.head

        while position < index-1:
            current = current.next_node
            position += 1
        new_node.next_node = current.next_node
        current.next_node = new_node

    def remove(self, key):
        current = self.head
        previous = None
        found = False

        while current and not found:
            if current.data is key and current is self.head:
                found = True
                self.head = current.next_node
            elif current.data is key:
                found = True
                previous.next_node = current.next_node
            else:
                previous = current
                current = current.next_node

    def search(self, key):
        current = self.head
        while current:
            if current.data == key:
                return current
            else:
                current = current.next_node
        return current

    def node_at_index(self, index):
        if index == 0:
            return self.head

        current = self.head
        position = 0

        while position < index:
            current = current.next_node
            position += 1
        return current

    def __repr__(self):
        current = self.head
        nodes = []

        while current:
            if current is self.head:
                nodes.append("[Head: %s]" % current.data)
            elif current.next_node is None:
                nodes.append("[Tail: %s]" % current.data)
            else:
                nodes.append("[%s]" % current.data)
            current = current.next_node
        return "->".join(nodes)
