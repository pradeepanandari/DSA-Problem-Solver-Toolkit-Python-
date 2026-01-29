from searching import linear_search, binary_search
from arrays import *
from stack import Stack
from queue_ds import Queue
from linked_list import LinkedList


arr = [10, 20, 30, 40, 50]
stack = Stack()
queue = Queue()
ll = LinkedList()


while True:
    print("\n--- DSA PROBLEM SOLVER TOOLKIT ---")
    print("1. Linear Search")
    print("2. Binary Search")
    print("3. Reverse Array")
    print("4. Find Max & Min")
    print("5. Stack Push")
    print("6. Stack Pop")
    print("7. Exit")
    print("8. Queue Enqueue")
    print("9. Queue Dequeue")
    print("10. Linked List Insert")
    print("11. Linked List Delete")
    print("12. Display Linked List")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        key = int(input("Enter element: "))
        print("Index:", linear_search(arr, key))

    elif choice == 2:
        key = int(input("Enter element: "))
        print("Index:", binary_search(arr, key))

    elif choice == 3:
        print("Reversed Array:", reverse_array(arr))

    elif choice == 4:
        mx, mn = find_max_min(arr)
        print("Max:", mx, "Min:", mn)

    elif choice == 5:
        val = int(input("Enter value: "))
        stack.push(val)
        print("Stack:", stack.display())

    elif choice == 6:
        print("Popped:", stack.pop())

    elif choice == 7:
        print("Exiting Toolkit...")
        break
    
    elif choice == 8:
        val = int(input("Enter value: "))
        queue.enqueue(val)
        print("Queue:", queue.display())
    
    elif choice == 9:
        print("Dequeued:", queue.dequeue())
        
    elif choice == 10:
        val = int(input("Enter value: "))
        ll.insert_end(val)
        print("Linked List:", ll.display())
        
    elif choice == 11:
        val = int(input("Enter value to delete: "))
        ll.delete(val)
        print("Linked List:", ll.display())
    
    elif choice == 12:
        print("Linked List:", ll.display())

    else:
        print("Invalid choice")
    
