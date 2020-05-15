class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.oldest_index = 0
        self.storage = []

    def append(self, item):
        # list is empty
        if len(self.storage) == 0:
            self.storage.append(item)

        else:

            # if capacity is full
            if len(self.storage) == self.capacity:
                # if full, increment oldest index and use it to replace items in list

                if self.oldest_index == self.capacity:
                    # once full, reset
                    self.oldest_index -= self.capacity
                    # replace item at index 0
                    self.storage[self.oldest_index] = item
                    # increment so next iteration will replace the next item
                    self.oldest_index += 1

                else:

                    self.storage[self.oldest_index] = item
                    self.oldest_index += 1

            else:
                self.storage.append(item)

    def get(self):
        return self.storage

