#Python program to demonstrate queue implementation using list.
queue = []

#Adding elements to the queue
queue.append('k')
queue.append('a')
queue.append('i')

print('Initial queue')
print(queue)

#Removing elements from the queue
print('\nElements dequeued from queue:')
print(queue.pop(0))
print(queue.pop(0))
print(queue.pop(0))


print('\nQueue after removing elements:')
print(queue)