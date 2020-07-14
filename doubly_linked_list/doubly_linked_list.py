"""
Each ListNode holds a reference to its previous node
as well as its next node in the List. 
"""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next
    
    def __del__(self):
        # if both self.prev and self.next are none
            # nothing should happen and instead will be handled in the DLL to adjust head & Tail
        if (self.next == None) and (self.prev == None):
            pass
        # if self.prev == None 
            # set next.prev to none
            # set self.next to none
        elif (self.next) and (self.prev == None):
                self.next.prev = None
                self.next = None
        # if self.next == None 
            # set prev.next to none
            # set self.prev to None
        elif (self.previous) and (self.next == None):
            self.prev.next = None
            self.prev = None
        # if self.prev & self.next
            # set prev.next to next
            # set next.prev to prev
            # set the self.prev and next to none
        else:
            self.prev.next = self.next
            self.next.prev = self.prev
            self.prev = None
            self.next = None
            
"""
Our doubly-linked list class. It holds references to 
the list's head and tail nodes.
"""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length
    
    """
    Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly.
    """
    def add_to_head(self, value):
        # Create instance of ListNode with Value
        # Increment the DLL length attribute

        # if DLL is empty
            # set head and tail to the new node instance

        # if DLL is not empty
            # Set new node's next to current head
            # set head's prev to new node
            # set head to the new node
        pass
        
    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):
        # store the value of the head
        # decrement the length of the DLL
        # delete the head
            # if head.next is not None
                # set head.next's prev to None
                # set gead to head.next
            # else (if head.next is None)
                # set head to None
                # set tail to None
        #return the value

        pass
            
    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):
        # Create instance of ListNode with Value
        # Increment the DLL length attribute

        # if DLL is empty
            # set head and tail to the new node instance

        # if DLL is not empty
            # Set new node's prev to current tail
            # set tail's next to new node
            # set tail to the new node
        pass
            
    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
        # store the value of the tail
        # decrement the length of the DLL
        # delete the tail
            # if tail.prev is not None
                # set tail.prev's next to None
                # set tail to tail.prev
            # else (if tail.prev is None)
                # set head to None
                # set tail to None
        #return the value
        pass
            
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        # set variable for current node
        # set variable for prev node
        # set variable for next node
        # set variable for head

        # change prev node's Next to next node
        # change next nodes's Prev to prev Node
        # change curent node's prev to None
        # change curent node's next to head
        # change head's prev to current node
        # change head to current node
        pass
        
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        # set variable for current node
        # set variable for prev node
        # set variable for next node
        # set variable for tail

        # change prev node's Next to next node
        # change next nodes's Prev to prev Node
        # change curent node's next to None
        # change curent node's prev to tail
        # change tail's next to current node
        # change tail to current node
        pass

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node):
        # need current node
        # need next node
        # need prev node
        # need tail
        # need head
        pass

    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    def get_max(self):
        pass