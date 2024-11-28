class QueueUsingStacks:
    def __init__(self):
        self.stack1 = []  # Stack for enqueueing
        self.stack2 = []  # Stack for dequeueing

    def enqueue(self, item):
        # Push the item onto stack1
        self.stack1.append(item)

    def dequeue(self):
        # If stack2 is empty, transfer elements from stack1 to stack2
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        
        # If stack2 is still empty, the queue is empty
        if not self.stack2:
            raise IndexError("Dequeue from an empty queue")
        
        # Pop the top element from stack2
        return self.stack2.pop()

    def is_empty(self):
        # The queue is empty if both stacks are empty
        return not self.stack1 and not self.stack2

    def size(self):
        # Return the total number of elements in the queue
        return len(self.stack1) + len(self.stack2)

# Example usage
queue = QueueUsingStacks()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

print("Dequeued:", queue.dequeue())  # Output: Dequeued: 1
print("Dequeued:", queue.dequeue())  # Output: Dequeued: 2

queue.enqueue(4)
print("Dequeued:", queue.dequeue())  # Output: Dequeued: 3

print("Queue empty:", queue.is_empty())  # Output: Queue empty: False
print("Queue size:", queue.size())  # Output: Queue size: 1