import queue

q = queue.Queue()
q.put("Python")
q.put("Django")

print(q.queue) 
print(q.qsize())

while not q.empty():
  print(q.get())

#
'''
var1, var2 = input("enter something: ").split(",")

print(var1, var2)
'''

#
var= 5.58
print(f"This is a number {var}")