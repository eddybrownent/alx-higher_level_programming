#!/usr/bin/python3
"""node of a singly linked list"""


class Node:
    """
    class representing a node of a singly linked list
    """

    def __init__(self, data, next_node=None):
        """
        initializes a new instance of the Node class

        Args:
            data: the data value to store in the node
            next_node: the next node in the linked list
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """
        get the data value of the node

        Returns:
            int: the data value of the node
        """
        return self.__data

    @data.setter
    def data(self, value):
        """
        set the data of the node

        Args:
            value: the data value to set

        Raises:
            TypeError: if the value is not an integer
        """
        if type(value) is not int:
            raise TypeError('data must be an integer')
        self.__data = value

    @property
    def next_node(self):
        """
        get the next node in the linked list

        Returns:
            Node: the noext node in the linked list
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """
        set the next node in the linked list

        Args:
            value: the next node to set

        Raises:
            TypeError: if the value is not None or a Node object
        """
        if value is not None and type(value) is not Node:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """
    class represents a singly linked list
    """

    def __init__(self):
        """
        initializes a new instance of the singlyliknedlist class
        """
        self.head = None

    def __str__(self):
        """
        Returns a string representation of the linked list

        Returns:
            str: string representation of the linked list
        """
        current = self.head
        nodes = []
        while current:
            nodes.append(str(current.data))
            current = current.next_node
        return '\n'.join(nodes)

    def sorted_insert(self, value):
        """
        inserts a new node into the sorted position in the linked list

        Args:
            value: the value to inser into the linked list

        Raises:
            TypeError: if the value is not an integer
        """
        if type(value) is not int:
            raise TypeError("value must be an integer")
        new_node = Node(value)

        if self.head is None:
            # If the linked list is empty, the new node becomes the head
            self.head = new_node
        elif value <= self.head.data:
            # If the value is less than or equal to the head data,
            # the new node becomes the new head
            new_node.next_node = self.head
            self.head = new_node
        else:
            # find the correct postion to insert the new node
            current = self.head
            while current.next_node and value > current.next_node.data:
                current = current.next_node

                # insert the new node between current and current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node
