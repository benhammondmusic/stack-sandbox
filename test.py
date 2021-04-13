import linked_list_stack


######################
# (testing)
######################


# instantiate a stack 
New_Stack = linked_list_stack.Stack()

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

print(New_Stack)

# clear the stack
New_Stack.clear()

# should be 0
print(New_Stack.size())

# add some new items
New_Stack.push("aaa")
New_Stack.push("bbb")
New_Stack.push("ccc")
New_Stack.push("ddd")

# reverse the linked list
New_Stack.reverse()


print(New_Stack)

