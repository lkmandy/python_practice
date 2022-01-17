"""
- The LinkedList code from before is provided below. Add three functions to the LinkedList.
- "get_position" returns the element at a certain position.
- The "insert" function will add an element to a particular spot in the list.
- "delete" will delete the first element with that particular value.
- Then, use "Test Run" and "Submit" to run the test cases at the bottom.
"""

class Element(object):
    def __init__(self, data):
        self.data = data
        self.next = None
        
class LinkedList(object):
    def __init__(self, head=None):
        self.head = head
        
    def append(self, new_element):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element
            
    def get_position(self, position):
        """Get an element from a particular position.
        Assume the first position is "1".
        Return "None" if position is not in the list."""
        counter = 1
        current_node = self.head

        if position < 1:
            return None
        
        while current_node and counter <= position:
            if counter == position:
                return current_node
            current_node = current_node.next
            counter += 1
        return None
    
    def insert(self, new_element, position):
        """Insert a new node at the given position.
        Assume the first position is "1".
        Inserting at position 3 means between
        the 2nd and 3rd elements."""
        counter = 1
        current = self.head
        if position > 1:
            while current and counter < position:
                if counter == position - 1:
                    new_element.next = current.next
                    current.next = new_element
                current = current.next
                counter += 1
        # If we are inserting at the start of the linked list
        elif position == 1:
            new_element.next = self.head
            self.head = new_element

    def delete(self, value):

        cur_node = self.head
        prev = None 

        # deleting the head of a linked list
        if cur_node and cur_node.data == value:
            self.head = cur_node.next
            cur_node = None
            return

        while cur_node and cur_node.data != value:
            prev = cur_node
            cur_node = cur_node.next

        if cur_node is None:
            return 

        prev.next = cur_node.next
        cur_node = None

# Test cases
# Set up some Elements
e1 = Element(1)
e2 = Element(2)
e3 = Element(3)
e4 = Element(4)

# Start setting up a LinkedList
ll = LinkedList(e1)
ll.append(e2)
ll.append(e3)

print(ll.head.data)

# Test get_position
# Should print 3
print(ll.head.next.next.data)

# Should also print 3
print(ll.get_position(3).data)

# Test insert
ll.insert(e4,3)

# Should print 4 now
print(ll.get_position(3).data)

# Test delete
ll.delete(1)

# Should print 2 now
print(ll.get_position(1).data)

# Should print 4 now
print(ll.get_position(2).data)

# Should print 3 now
print(ll.get_position(3).data)