import math


class IntVector:
    _DEFAULT_VALUE = 0
    _CAPACITY_MULTIPLIER = 2
    _SHRINK_TRESHOLD = 0.25

    def __init__(self, initial_capacity):
        self._capacity = initial_capacity
        self._size = 0
        self._array = [self._DEFAULT_VALUE] * self._capacity

    def size(self):
        return self._size

    def capacity(self):
        return self._capacity

    def is_empty(self):
        return self._size == 0

    def at(self, index):
        self._check_bounds(index)
        return self._array[index]

    def find(self, item):
        for i in range(self._size):
            if self.at(i) == item:
                return i
        return -1

    def push(self, item):
        if self._is_full():
            self._expand()

        self._array[self._size] = item
        self._size += 1

    def insert(self, index, item):
        self._check_bounds(index)

        if self._is_full():
            self._expand()

        for i in reversed(range(index, self._size)):
            self._array[i + 1] = self._array[i]
        self._array[index] = item

        self._size += 1

    def prepend(self, item):
        # TODO:
        pass

    def pop(self):
        if self.is_empty():
            raise IndexError("Attempted popping an empty array")

        popped_item = self._array[self._size - 1]
        self._array[self._size] = self._DEFAULT_VALUE
        self._size -= 1

        if self._size <= self._min_size():
            self._shrink()

        return popped_item

    def delete(self, index):
        # TODO:
        pass

    def remove(self, item):
        # TODO:
        pass

    # ------ Private functions ------

    def _check_bounds(self, index):
        if index < 0 or index >= self._size:
            raise IndexError("Index out of bounds")

    def _min_size(self):
        return self._SHRINK_TRESHOLD * self._capacity

    def _is_full(self):
        return self._size == self._capacity

    def _expand(self):
        new_capacity = self._capacity * self._CAPACITY_MULTIPLIER
        self._resize(new_capacity)

    def _shrink(self):
        new_capacity = math.ceil(self._capacity / self._CAPACITY_MULTIPLIER)
        self._resize(new_capacity)

    def _resize(self, new_capacity):
        new_array = [self._DEFAULT_VALUE] * new_capacity

        for index in range(self._size):
            new_array[index] = self._array[index]

        self._array = new_array
        self._capacity = new_capacity

    # ------ Builtins functions ------

    def __str__(self):
        result = ""

        for index in range(self._size):
            result += f" {self.at(index)}"
        result += "|"
        for index in range(self._capacity - self._size):
            result += f"{self._DEFAULT_VALUE} "

        return result


if __name__ == "__main__":
    vec = IntVector(3)

    print(vec)
    assert vec.size() == 0
    assert vec.is_empty()
    assert vec.capacity() == 3

    vec.push(1)
    print(vec)
    assert vec.size() == 1
    assert not vec.is_empty()
    assert vec.capacity() == 3

    vec.push(2)
    vec.push(3)
    print(vec)
    assert vec.at(0) == 1
    assert vec.at(1) == 2
    assert vec.at(2) == 3

    vec.push(4)
    print(vec)
    assert vec.size() == 4
    assert vec.capacity() == 6
    assert vec.at(3) == 4

    vec.push(5)
    vec.push(6)
    vec.push(7)
    print(vec)
    assert vec.capacity() == 12

    assert vec.find(9) == -1

    vec.insert(3, 9)
    print(vec)
    assert vec.at(3) == 9
    assert vec.find(9) == 3

    vec.delete(3)
    assert vec.at(3) == 4

    vec.pop()
    vec.pop()
    vec.pop()
    print(vec)
    assert vec.capacity() == 12

    vec.pop()
    print(vec)
    assert vec.capacity() == 6

    vec.pop()
    print(vec)
    assert vec.capacity() == 6

    vec.pop()
    print(vec)
    assert vec.capacity() == 3

    vec.pop()
    print(vec)