### Linked List in C Class Test (30 Marks)

#### Multiple Choice Questions (3 Marks Each)

1. **What is a linked list?**
   - a) A linear data structure

2. **Which of the following is not a type of linked list?**
   - d) Binary linked list

3. **What is the purpose of a head pointer in a linked list?**
   - a) It points to the first node of the list

4. **In a singly linked list, how is the last node identified?**
   - a) By pointing to NULL

5. **Which operation is used to insert a new node at the beginning of a singly linked list?**
   - c) insertAtBeginning()

6. **What is the time complexity for searching an element in a singly linked list of length 'n'?**
   - a) O(n)

7. **How is memory allocated for a new node in C?**
   - a) Using malloc()

8. **Which operation is used to delete the last node of a singly linked list?**
   - a) deleteAtEnd()

9. **What is the main advantage of a circular linked list over a singly linked list?**
   - b) It allows backward traversal

---

### Linked List in C Class Test (20 Marks)

#### Short Answer Questions (2 Marks Each)

1. **What is a linked list? Briefly explain its structure.**
   - A linked list is a linear data structure where each element, called a node, contains a data part and a reference (or link) to the next node in the sequence. This allows for dynamic memory allocation and efficient insertions/deletions.

2. **What is the difference between a singly linked list and a doubly linked list?**
   - A singly linked list has nodes with a single link pointing to the next node, while a doubly linked list has nodes with two links, one pointing to the next node and the other pointing to the previous node.

3. **Why is a head pointer necessary in a linked list?**
   - The head pointer is necessary because it stores the address of the first node in the list, allowing access to the entire list. Without it, the list cannot be traversed or modified.

4. **How is memory allocated for a new node in C?**
   - Memory for a new node in C is allocated using the `malloc()` function, which allocates a specified number of bytes and returns a pointer to the allocated memory.

5. **Explain the concept of traversal in a linked list.**
   - Traversal in a linked list involves starting from the head node and moving from one node to the next using the links until the end of the list is reached, typically indicated by a NULL pointer in a singly linked list.

6. **How can you determine if a linked list is empty?**
   - A linked list is empty if the head pointer is NULL, indicating that there are no nodes in the list.

7. **Describe the process of inserting a new node at the beginning of a linked list.**
   - To insert a new node at the beginning, create the new node, set its next pointer to the current head node, and then update the head pointer to point to the new node.

8. **What is the significance of the "next" pointer in a linked list?**
   - The "next" pointer in a linked list holds the address of the next node in the sequence, enabling the linked list to maintain its order and allow traversal from one node to the next.

9. **How can you delete a node from a linked list?**
   - To delete a node, find the node to be deleted, adjust the previous node's next pointer to bypass the node to be deleted, and then free the memory of the node to be deleted.

10. **What is the time complexity for searching an element in a linked list?**
    - The time complexity for searching an element in a linked list is O(n), where n is the number of elements in the list.