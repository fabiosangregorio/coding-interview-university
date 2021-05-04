class ListNode:
    def __init__(self, data, next_node=None, prev_node=None):
        self.data = data
        self.next_node = next_node
        self.prev_node = prev_node


class LinkedList:
    def __init__(self):
        self._head = None
        self._tail = None

    def empty(self):
        return self._head is None

    def size(self):
        list_size = 0
        node = self._head
        while node:
            list_size += 1
            node = node.next_node
        return list_size

    def front(self):
        return self._head.data if self._head else None

    def back(self):
        return self._tail.data if self._tail else None

    def push_front(self, value):
        next_node = self._head
        new_node = ListNode(value, next_node=next_node)
        self._head = new_node
        if next_node:
            next_node.prev_node = new_node
        else:
            self._tail = new_node

    def push_back(self, value):
        prev_node = self._tail
        new_node = ListNode(value, prev_node=prev_node)
        self._tail = new_node
        if prev_node:
            prev_node.next_node = new_node
        else:
            self._head = new_node

    def pop_front(self):
        if self.empty():
            raise ReferenceError("Cannot pop an empty list")

        popped_node = self._head
        next_node = popped_node.next_node
        self._head = next_node
        if next_node:
            next_node.prev_node = None
        else:
            self._tail = None
        return popped_node.data

    def pop_back(self):
        if self.empty():
            raise ReferenceError("Cannot pop an empty list")

        popped_node = self._tail
        prev_node = popped_node.prev_node
        self._tail = prev_node
        if prev_node:
            prev_node.next_node = None
        else:
            self._head = None

    # ------ Builtins functions ------

    def __str__(self):
        result = ""
        node = self._head
        while node:
            result += f"{node.data} "
            node = node.next_node
        return result


if __name__ == "__main__":
    lst = LinkedList()
    assert lst.empty()
    assert lst.size() == 0

    lst.push_front(1)
    lst.push_front(2)
    print(lst)
    assert lst.size() == 2

    lst.pop_front()
    assert lst.size() == 1
    lst.pop_front()
    assert lst.empty()
    assert lst._tail == None
    print(lst)
    try:
        lst.pop_front()
    except:
        assert lst.empty()

    lst.push_back(1)
    assert lst.front() == 1
    assert lst.back() == 1
    lst.push_back(2)
    assert lst.front() == 1
    assert lst.back() == 2
    lst.push_back(3)
    print(lst)
    assert lst.size() == 3

    lst.pop_back()
    assert lst.size() == 2
    lst.pop_back()
    lst.pop_back()
    assert lst.size() == 0


# value_at(index) - returns the value of the nth item (starting at 0 for first)
# insert(index, value) - insert value at index, so current item at that index is pointed to by new item at index
# erase(index) - removes node at given index
# value_n_from_end(n) - returns the value of the node at nth position from the end of the list
# reverse() - reverses the list
# remove_value(value) - removes the first item in the list with this value
