class Node():
    '''
    Node Class for Linked Lists
    '''
    def __init__(self, val, next_node=None):
        '''
        Instantiate the value and next node attribute of the class
        '''
        self.val = val
        self.next_node = next_node

    def set_value(self, val):
        '''
        Method to set the value of the node
        '''
        self.val = val

    def set_next(self, next_node):
        '''
        Method to set the pointer to the next value
        '''
        self.next_node = next_node

    def value(self):
        '''
        Return the value stored in the node
        '''
        return self.val

    def next(self):
        '''
        Return the next Node in the list
        '''
        return self.next_node

class TypedNode(Node):
    '''
    Typed Node Class for Linked Lists
    '''
    def __init__(self, val, next_node=None):
        '''
        Instantiate the value, and set the node type
        '''
        self.type = type(val)
        if (next_node is not None) and (type(next_node.value())!=self.type):
            raise TypeError("Cannot link a typed node to a node of a different type")
        super(TypedNode, self).__init__(val, next_node=next_node)

    def set_value(self, val):
        '''
        Method to set the value of the node
        '''
        if type(val) != self.type:
            raise TypeError("New value type does not match established value type for node")

        super(TypedNode, self).set_value(val)

    def set_next(self, next_node):
        '''
        Method to set the pointer to the next value
        '''
        if type(next_node.value()) != self.type:
            raise TypeError("New node type does not match established type for node")
        super(TypedNode, self).set_next(next_node)
