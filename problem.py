


##Practice trees and linkedlists 

#check if the value is the value of the head 
#check if the value is the value of the tail 
#double linked lists


class LinkedLists():
    """One way linked list."""

    def __init__(self, head):
        """Initializing."""

        self.head = head
    
    def print_linked_list(self):
        """Printing each value in a linked list."""

        current_node = self.head

        while current_node is not None:
            print(current_node.value)

            current_node = current_node.next_node



class Node():
    """Node class."""

    def __init__(self, value, next_node=None):
        """Initializing."""

        self.value = value 
        self.next_node = next_node
    

head = Node('apple')
node_two = Node('berry')
node_three = Node('cherry')
node_four = Node('banana')
node_five = Node('mango')
head.next_node = node_two
node_two.next_node = node_three
node_three.next_node = node_four
node_four.next_node = node_five

l = LinkedLists(head)

l.print_linked_list()

# LinkedLists.print_linked_list()
