#!/usr/bin/python3
'''Node for a singly linked list'''


class Node:
    def __init__(self, data, next_node=None):
        '''constructor'''
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        '''retrieve data'''
        return self.__data

    @data.setter
    def data(self, value):
        '''data setter'''
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        '''retrieve next node'''
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        '''next node setter'''
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    '''represent singly linked list'''
    def __init__(self):
        '''constructor'''
        self.__head = None

    def sorted_insert(self, value):
        '''insert Node'''
        new = Node(value)
        if self.__head is None:
            new.next_node = None
            self.__head = new
        elif self.__head.data > value:
            new.next_node = self.__head
            self.__head = new
        else:
            tmp = self.__head
            while tmp.next_node is not None and tmp.next_node.data < value:
                tmp = tmp.next_node
            new.next_node = tmp.next_node
            tmp.next_node = new

    def __str__(self):
        '''print singly linked list'''
        data = []
        tmp = self.__head
        while tmp is not None:
            data.append(str(tmp.data))
            tmp = tmp.next_node
        return '\n'.join(data)
