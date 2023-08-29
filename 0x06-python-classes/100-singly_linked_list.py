#!/usr/bin/python3
"""Make single-linked list classes."""


class Node:
    """single-linked list node should be shown."""

    def __init__(self, data, next_node=None):
        """start a fresh Square.

        Args:
            data (int): Data from new Node.
            next_node (Node): New Node subsequent node.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """determine or alter square current size."""
        return (self.__data)

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be integer")
        self.__data = value

    @property
    def next_node(self):
        """determine alter square current size"""
        return (self.__next_node)

    @next_node.setter
    def next_node(self, value):
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """express a single-linked list node."""

    def __init__(self):
        """Launch a fresh SinglyLinkedList."""
        self.__head = None

    def sorted_insert(self, value):
        """new Node be added to SinglyLinkedList.

        The node is inserted into the list at the correct
        ordered numerical position.

        Args:
            value (Node): Inserting the new Node.
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
        """Describe SinglyLinkedList is represented by print()."""
        values = []
        tmp = self.__head
        while tmp is not None:
            values.append(str(tmp.data))
            tmp = tmp.next_node
        return ('\n'.join(values))
