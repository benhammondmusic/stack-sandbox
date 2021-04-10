# Listed List Implementation of a Stack Data Structure
# Referenced the following resources:
# https://learnersbucket.com/tutorials/data-structures/implement-stack-using-linked-list/
# https://gist.github.com/dineshrajpurohit/0bb67d29a039f85f2f10
# https://openbookproject.net/thinkcs/python/english3e/classes_and_objects_I.html
# https://www.w3schools.com/python/python_classes.asp
# https://www.geeksforgeeks.org/implement-a-stack-using-singly-linked-list/


""" List of operations performed on stack
clear: Clears the stack. """


# Define the class for all nodes
class Node:
    # constructor: node starts with value from arg, and is last in line so no next value
    def __init__(self, value):
        self.value = value
        self.next = None
        print(f"New node - value: {value} next: {next}")


# Define the class for the stack
class Stack:
    # constructor: Stack starts empty
    def __init__(self):
        print("creating a stack")
        self.head = None    

    #
    def is_empty(self):

        print("checking if stack is empty")

        if self.head == None:
            return True
        else:
            return False
    

    # Adds the item in the stack at the top.
    def push(self, item):

        print(f"pushing {item}") 
        
        if self.head == None: # use is_empty()
            # if stack is empty, point head to new node with the item
            self.head = Node(item)
            print("stack was empty, item is new head")
        else:
            # otherwise, make a new node with the item
            new_node = Node(item)
            # point this new node next to the current head node
            new_node.next = self.head
            # and then change the stack head to be the new node
            self.head = new_node
            print("stack wasn't empty, item is new head")

    # Removes the top item from the stack and returns it.
    def pop(self):
        
        print("popping the last node off of the stack")

        if self.is_empty():
            # can't pop an empty stack
            return None
        else:
            # set current head node to a new variable popped_node
            popped_node = self.head
            # make head point to the next node in line form the current head
            self.head = self.head.next
            # remove the popped node from the chain
            popped_node.next = None
            # just return the innter value from the popped node
            return popped_node.value

    # view all items in stack
    def display(self):

        current_head = self.head

        if self.is_empty():
            print("Empty Stack!")
        else:
            # iterate each item and print it out 
            while(current_head != None):
                print(f"{current_head.value}\n")
                # move print head forward to next node
                current_head = current_head.next
            return

    # Peek: Shows the top item from the stack.
    def peek(self):
        if self.is_empty():
            print("Empty Stack!")
        else:
            print(f"Peeking - Top item on stack is: {self.head.value}")


    # size: Returns the size of the stack.
    def size(self):
        
        # initial value
        stack_size = 0

        if self.is_empty():
            print(f"Returning size of stack: {stack_size}")
            return stack_size
        else:
            # walk through the linkedlist
            current_head = self.head
            while (current_head != None):
                # increment the counter each step
                stack_size += 1
                # take a step thru the linked list
                current_head = current_head.next
            # finally return counter value once walked thru the whole list
            print(f"Returning size of stack: {stack_size}")
            return stack_size

    # to_list: Convert the stack to a python list.
    def to_list(self):

        # start with empty list
        stack_as_list = []

        # start at the top of the stack
        current_head = self.head

        # walk thru each node in the linked list
        while (current_head != None):
            # and stick each value into an list in order
            stack_as_list.append(current_head.value)
            # step thru the linked list
            current_head = current_head.next
        
        # reverse so that old HEAD = new item[0]
        stack_as_list.reverse()
        # finally return the array/list
        return stack_as_list #.reverse()

    # clear: Clears the stack
    def clear(self):
        print("Clearing the Stack")
        self.head = None
        return




######################
# (testing)
######################


# instantiate a stack 
New_Stack = Stack()

# add some items
New_Stack.push("a")
New_Stack.push("b")
New_Stack.push("c")

# print current size and stack
print(New_Stack.size())
New_Stack.display()
print(f"Create a list from the stack: {New_Stack.to_list()}")

# pop items one by one
New_Stack.pop()
print(New_Stack.size())
New_Stack.peek()
New_Stack.display()


New_Stack.pop()
print(New_Stack.size())
New_Stack.peek()
New_Stack.display()

New_Stack.pop()
New_Stack.peek()
New_Stack.display()

# should be empty now
New_Stack.peek()
print(New_Stack.size())

# add some new items
New_Stack.push(100)
New_Stack.push(200)
New_Stack.push(300)

New_Stack.display()

# clear the stack
New_Stack.clear()

# should be 0
print(New_Stack.size())
