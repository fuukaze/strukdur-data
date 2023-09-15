from collections import deque
# buat list Q
# set list Q kosong
myqueue = deque()
# tambah elemen (enqueue)
myqueue.append('a')
myqueue.append('b')
myqueue.append('c')
myqueue.insert(1, 'ayam')
print(myqueue)
# hapus elemen (dequeue)
out = myqueue.popleft()
print("data terhapus: ", out)
print(myqueue)


def is_empty():
    return myqueue == deque()
print(is_empty())
