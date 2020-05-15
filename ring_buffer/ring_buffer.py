# class RingBuffer:
#     def __init__(self, capacity):
#         self.capacity = capacity
#         self.oldest_index = 0
#         self.storage = []

#     def append(self, item):
#         # list is empty
#         if len(self.storage) == 0:
#             self.storage.append(item)

#         else:

#             # if capacity is full
#             if len(self.storage) == self.capacity:
#                 # if full, increment oldest index and use it to replace items in list

#                 if self.oldest_index == self.capacity:
#                     # once full, reset
#                     self.oldest_index -= self.capacity
#                     # replace item at index 0
#                     self.storage[self.oldest_index] = item
#                     # increment so next iteration will replace the next item
#                     self.oldest_index += 1

#                 else:

#                     self.storage[self.oldest_index] = item
#                     self.oldest_index += 1

#             else:
#                 self.storage.append(item)

#     def get(self):
#         return self.storage


# IF USING LINKEDLISTS IS REQUIRED SHOW THIS

class Node:
    def __init__(self, value=None, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next


class Dll:
    def __init__(self, node=None):
        self.head = None
        self.tail = None
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    def add_to_tail(self, value):
        new_node = Node(value)
        self.length += 1
        # list is empty
        if not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node

        # only one item in list
        elif self.head == self.tail:
            self.head.next = new_node
            new_node.prev = self.head
            self.tail = new_node

        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def remove_from_head(self):
        self.length -= 1
        if self.head == self.tail:
            self.head == None
            self.tail == None

        else:
            self.head.next.prev = None
            self.head = self.head.next


class RingBuffer:
    def __init__(self, capacity=3):
        self.capacity = capacity
        self.order = Dll()
        self.storage = {}
        self.oldest_key = 0

    def append(self, item):
        # nothing on the list
        if self.order.length == 0:
            self.order.add_to_tail(item)
            self.oldest_key += 1
            self.storage[self.oldest_key] = self.order.tail
        else:

            if self.order.length >= self.capacity:

                if self.oldest_key == self.capacity:
                    self.oldest_key -= self.capacity
                    self.oldest_key += 1
                    self.storage[self.oldest_key] = Node(item)

                else:
                    self.order.add_to_tail(item)
                    self.oldest_key += 1
                    self.storage[self.oldest_key] = self.order.tail
            else:
                self.order.add_to_tail(item)
                self.oldest_key += 1
                self.storage[self.oldest_key] = self.order.tail

    def get(self):

        items = []

        for key in self.storage:
            items.append(self.storage[key].value)

        return items
