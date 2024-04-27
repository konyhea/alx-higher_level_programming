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
        if isinstance(value, int) is not int:
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        '''retrieve next node'''
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        ''''next node setter'''
        if isinstance(value, None) is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value

class SinglyLinkedList:
    def __init__(self):
        '''constructor'''
        self.__head = None

    def sorted_insert(self, value):
        '''insert Node'''
