from node_two import Node_two


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append_node(self, data):
        node = Node_two(data)

        if self.head is None:
            self.head = node
            self.tail = node
            return

        else:
            self.tail.next = node
            self.tail = self.tail.next

    def append_node_to_beginning(self, new_data):
        new_node = Node_two(new_data)
        new_node.next = self.head
        self.head = new_node

    def append_data_after(self, prev_node, new_data):
        if prev_node is None:
            print('Previous node is in the Linked List.')
            return
        new_node = Node_two(new_data)
        new_node.next = prev_node.next
        prev_node.next = new_node



    def print_nodes(self):
        node = self.head
        while node:
            print(node.data)
            node = node.next


