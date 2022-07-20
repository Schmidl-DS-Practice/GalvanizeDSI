from node import Node, TypedNode
import numpy as np

class LinkedList():
    '''
    A Linked List Class
    '''
    def __init__(self, l_in, line_break=5):
        '''
        Takes a python list and transforms to a linked list, should have a head attribute that is the first node in the linked list

        Input: python list
              (optional) number of nodes before line break in str
        Output: None
        '''

        self.line_break = line_break
        self.len = len(l_in)
        if self.len == 0:
            self.head, self.tail = None, None
            return

        last = Node(l_in[-1])
        self.tail = last
        for val in l_in[-2::-1]:
            this_node = Node(val, next_node=last)
            last = this_node
        self.head = last

    def __str__(self):
        if self.len == 0:
            return "empty"
        str_ret, nodes = "", 1
        for node in self:
            str_ret = str_ret + str(node.value()) + "->"
            nodes += 1
            if nodes == self.line_break:
                str_ret += "\n  "
                nodes = 0
        return str_ret

    def __iter__(self):
        self.current = self.head
        return self
    
    def __next__(self):
        if self.current is not None:
            ret = self.current
            self.current = self.current.next()
            return ret
        else:
            raise StopIteration
        

    def append(self, val):
        '''
        Takes a value and adds it in a new Node to the end of the list

        Input: value
        Output: None
        '''
        last = Node(val)
        if self.len == 0:
            self.head=last
        else:
            self.tail.set_next(last)
        self.tail = last
        self.len += 1

    def copy(self):
        '''
        Returns a copy of the link list

        Think about mutability and what you are trying to do
        '''
        ret_ll = LinkedList([])
        for node in self:
            ret_ll.append(node.value())
        return ret_ll
    
    def count(self):
        '''
        Returns the number of items in the list

        Think about the time complexity
        '''
        return self.len

    def extend(self, ll2):
        '''
        Extend the linked list

        Input: Linked List
        Output: None
        '''
        self.len += ll2.len
        self.tail.set_next(ll2.head)
        self.tail = ll2.tail

    def index(self, search_val):
        '''
        Find the index at which a passed value exist

        Input: value to find
        Return: node number of first existance

        ex:
        >>> ll = LinkedList([2, 4, 7, 4])
        >>> ll.index(4)
        1
        '''
        idx = 0
        for node in self:
            if node.value() == search_val:
                return idx
            idx += 1
        return -1
        

    def insert(self, val, index):
        '''
        Insert a new Node object into the list at the given index

        Input:  Value to add
                Index to add value
        Output: None
        '''
        if index > self.len:
            raise ValueError("Chosen index larger than linked list length")

        self.len += 1
        # Define special cases for inserting at head and tail first
        if index == 0:
            new_node = Node(val, next_node=self.head)
            self.head = new_node
            return

        # now the tail
        if index == self.len:
            new_node = Node(val)
            self.tail.set_next(new_node)
            self.tail = new_node

        # all other cases
        ind, node = 0, self.head
        while ind < index - 1:
            ind += 1
            node = node.next()
        temp = node.next()
        node.set_next(Node(val, next_node=temp))

    def pop(self):
        '''
        Remove and return last value in the linked list

        Input: None
        Output: Value of node
        '''
        if self.len == 0:
            raise ValueError("Link List is empty")
        
        current = self.head
        prev = None
        while current.next():
            prev = current
            current = current.next()
        # if only one item in list list will be empty 
        if prev is None:
            self.head = None   
        else:
            prev.set_next(None)
            
        self.tail = prev
        self.len -= 1

        return current.value()

    def reverse(self):
        '''
        Return a copy of this linked list in reverse order

        Input: None
        Output: Linked List
        '''
        ret_ll = LinkedList([])
        for node in self:
            ret_ll.insert(node.value(), 0)
        return ret_ll

    def sort(self):
        '''
        Sort the linked list

        Input: None
        Output: returns a sorted copy of the linked list
        '''
        if self.len < 2:
            return self.copy
        
        # Ready for some inception Linked lists :-P
        stack_list = LinkedList([])
        for node in self:
            stack_list.append(LinkedList([node.value()]))

        while stack_list.len > 1:
            temp_stack = LinkedList([])
            this_l = stack_list.head
            this_r = this_l.next()
            while (this_l is not None) and (this_r is not None):
                temp_stack.append(self.merge_sorted_ll(this_l.value(), this_r.value()))
                this_l = this_r.next()
                if this_l is not None:
                    this_r = this_l.next()
                    if this_r is None:
                        temp_stack.append(this_l.value())
            stack_list = temp_stack
        return stack_list.head.value()

    @staticmethod
    def merge_sorted_ll(ll_left, ll_right):
        ret_ll = LinkedList([])
        this_l, this_r = ll_left.head, ll_right.head
        while (this_l is not None) and (this_r is not None):
            if this_l.value() < this_r.value():
                ret_ll.append(this_l.value())
                this_l = this_l.next()
            else:
                ret_ll.append(this_r.value())
                this_r = this_r.next()

        if this_l is None:
            while this_r is not None:
                ret_ll.append(this_r.value())
                this_r = this_r.next()
        else:
            while this_l is not None:
                ret_ll.append(this_l.value())
                this_l = this_l.next()
        
        return ret_ll

class TypedLinkedList(LinkedList):
    '''
    Implements a typed linked list class
    '''
    def __init__(self, l_in, line_break=5):
        '''
        Takes a python list and transforms to a linked list with type restriction, 
        should have a head attribute that is the first node in the linked list

        Input: python list
              (optional) number of nodes before line break in str
        Output: None
        '''
        self.line_break = line_break
        self.len = len(l_in)
        self.type = None
        if self.len == 0:
            self.head, self.tail = None, None
            return

        last = TypedNode(l_in[-1])
        self.tail = last
        self.type = last.val_type
        for val in l_in[-2::-1]:
            if type(val) != self.type:
                raise ValueError("List is not of uniform type")
            this_node = TypedNode(val, next_node=last)
            last = this_node
        self.head = last

    def extend(self, ll2):
        '''
        Extend the linked list

        Input: Linked List
        Output: None
        '''
        if ll2.type != self.type:
            raise TypeError("Typed Linked Lists must contain objects of the same type")
        
        super(TypedLinkedList, self).extend(ll2)

    def append(self, val):
        '''
        Takes a value and adds it in a new Node to the end of the list

        Input: value
        Output: None
        '''
        if type(val) != self.type:
            raise TypeError("New value is of type {} and must be of type {}".format(type(val), self.type))
        super(TypedLinkedList, self).append(val)

    def insert(self, val, index):
        '''
        Insert a new Node object into the list at the given index

        Input:  Value to add
                Index to add value
        Output: None
        '''
        if type(val) != self.type:
            raise TypeError("New value is of type {} and must be of type {}".format(type(val), self.type))
        super(TypedLinkedList, self).insert(val, index)

if __name__ == "__main__":
    l1, l2 = [x**2 for x in range(2, 7)], [x for x in range(8, 14)]
    ll = LinkedList(l1)
    ll.insert(2, 4)
    ll.insert(1, 2)
    ll_sorted = ll.sort()
    print(ll)
    print(ll_sorted)
    ll2 = LinkedList(l2)
    
    ll.extend(ll2)
    print(ll)
    
    ll3 = ll.reverse()
    print(ll3)
