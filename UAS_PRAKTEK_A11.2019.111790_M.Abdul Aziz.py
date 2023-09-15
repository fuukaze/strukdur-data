from queue import LifoQueue

a = int(input("banyak data = "))
stack = LifoQueue(maxsize=a)
data1 = []

while a > 0:
    if a != 0:
        data = input("NIM = ")
        stack.put(data)
        data1.append(data)
    a -= 1

print(data1)
print("Data Penuh?  ", stack.full())
