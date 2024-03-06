class QueueWithStack:
    def __init__(self):
        self.enqueue_stack = []
        self.dequeue_stack = []

    def enqueue(self, value):
        self.enqueue_stack.append(value)

    def dequeue(self):
        if len(self.dequeue_stack) == 0 and len(self.enqueue_stack) == 0:
            return None
        while len(self.enqueue_stack) != 0:
            self.dequeue_stack.append(self.enqueue_stack.pop())
        return self.dequeue_stack.pop()

    def print_queue(self):
        print(f"enqueue stack: {self.enqueue_stack}")
        print(f"dequeue stack: {self.dequeue_stack}")


queue = QueueWithStack()

queue.enqueue(5)
queue.enqueue(78)
queue.enqueue(90)

print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())

queue.print_queue()
