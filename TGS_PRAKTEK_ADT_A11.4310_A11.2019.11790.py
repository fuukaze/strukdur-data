import os
# membuat class node
class Node(object):
  def __init__(self, data=None, next_node=None):
    self.data = data
    self.next_node = next_node
  
  # mengambil data dari node
  def get_data(self):
    return self.data 
  
  # mengambil node berikutnya
  def get_next(self):
    return self.next_node

  # menentukan node berikutnya
  def set_next(self, urut_baru):
    self.next_node = urut_baru

# membuat class linkedlist 
class linkedlist(object):
  def __init__(self, head=None, tail=None):
    self.head = head
    self.tail = tail

  # menambah node baru
  def tambahdepan(self, data):
    # inisialisasi node baru
    new_node = Node(data)
    # jika head masi kosong
    if (self.head is None):
      self.head = new_node
      self.tail = new_node
    else:
      new_node.set_next(self.head)
      self.head = new_node

  def tambahbelakang(self, data):
    # inisialisasi node baru
    new_node = Node(data)
    # jika head masi kosong
    if (self.head is None):
      self.head = new_node
      self.tail = new_node
    else:
      self.tail.next_node = new_node
      self.tail = new_node

  def lihatdata(self):
    print("data pada list : ")
    current_node = self.head
    if (self.head is None):
      print("data masih kosong")
    else:
      while current_node is not None:
        print(current_node.data)
        print(">")
        current_node = current_node.next_node

  def menuutama(self):
    perintah = 'y'
    while(perintah == 'y'):
      print("Daftar Perintah yang bisa digunakan")
      print("1. Tambah Data")
      print("2. Lihat Data yang ada")
      pilih = int(input("Pilihan : "))
      if (pilih == 1):
        angka = int(input("angka yang akan dimasukkan : "))
        if angka % 2 == 1:
          self.tambahbelakang(angka)
        else:
          self.tambahdepan(angka)
      elif (pilih == 2):
        self.lihatdata()
        x = input("")
      else:
        perintah = 'n'
if __name__ == "__main__":
    l = linkedlist()
    l.menuutama()
