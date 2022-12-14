#!/usr/bin/python3
"""Define classes for a Singly linked list"""


class Node:
    """Represent a node in a singly linked list"""
    def __init__(self, data, next_node=None):
        """initialize a new node
        Args:
            data (int): the data of the new node
            next_node (Node): the next node of the new node
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        return (self.__data)

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        return (self.__next_node)

    @next_node.setter
    def next_node(self, value):
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Represent a Singly linked list"""
    def __init__(self):
        """initialize a new singly linked list"""
        self.__head = None

    def sorted_insert(self, value):
        """insert a node at new singly linked list
        in order
        Args:
            value (Node): the new Node to insert
        """
        new = Node(value)
        if self.__head is None:
            new.next_node = None
            self.__head = new
        elif self.__head.data > value:
            new.next_node = self.__head
            self.__head = new
        else:
            tmp = self.__head
            while (tmp.next_node is not None and
                    tmp.next_node.data < value):
                tmp = tmp.next_node
            new.next_node = tmp.next_node
            tmp.next_node = new

    def __str__(self):
        """define the print() rep of a singly linked list"""
        values = []
        tmp = self.__head
        while tmp is not None:
            values.append(str(tmp.data))
            tmp = tmp.next_node
        return ('\n'.join(values))
