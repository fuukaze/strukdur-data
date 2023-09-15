from queue import LifoQueue

panjang = int(input("banyak data = "))
stack = LifoQueue(maxsize=panjang)
data1 = []

while panjang > 0:
    if panjang != 0:
        data = input("NIM = ")
        stack.put(data)
        data1.append(data)
    panjang -= 1

print(data1)
print("Data Penuh?  ", stack.full())
