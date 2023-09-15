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

  # mencari data pada list
  def cari(self, data):
    # membuat pointer baru menunjuk ke NODE yang ditunjuk head
    current = self.head
    found = False
    idx = 0
    # perulangan mencari NODE yang dicari
    while current and found is False:
      idx=+1
      if current.get_data() == data:
        found = True
        print("ketemu pada urutan ke-",idx)
        x = input()
      else:
        current = current.get_next()
      return found

  # menambah data ditengah pada list
  def tambahtengah(self, data):
    # membuat pointer baru menunjuk ke NODE yang ditunjuk head
    current = self.head
    found = False
    # perulangan mencari NODE yang dicari
    while current and found is False:
      if current.get_data() == data:
        found = True
        angkal = int(input("angka yang akan dimasukkan : "))
        new_node = Node(angkal)
        new_node.next_node = current.next_node
        current.next_node = new_node
      else:
        current = current.get_next()
    return found

  # menampilkan isi dari list
  def showdata(self):
    print("data pada list : ")
    current_node = self.head
    if (self.head is None):
      print("data masih kosong")
    else:
      while current_node is not None:
        print(current_node.data)
        print(">")
        current_node = current_node.next_node

  # menghapus data dari depan
  def deletedepan(self):
    if (self.head is None):
      print("Data tidak ada")
    else:
      print(self.head.get_data(), "telah dihapus")
      self.head = self.head.next_node
      x = input()

  # menghapus data dari belakang
  def deletebelakang(self):
    current_node = self.head
    if (self.head is None):
      print("data masih kosong")
    else:
      while current_node.next_node.next_node is not None:
        current_node = current_node.next_node
      print(self.tail.get_data, "telah dihapus")
      current_node.next_node = self.tail.next_node
      self.tail = current_node
      x = input()

  # mengecek data apakah kosong atau tidak
  def cekkosong(self):
    if (self.head is None):
      return True
    else:
      return False

  # mengisi data baru ataupun pilihan lain
  def menuutama(self):
    perintah = 'y'
    while (perintah == 'y'):
      os.system("cls")
      print("Daftar Perintah yang bisa digunakan")
      print("1. Tambah Data")
      print("2. Tambah Data dari tengah")
      print("3. Cari Data")
      print("4. Delete dari Depan")
      print("5. Delete dari Belakang")
      print("6. Lihat Data yang ada")
      pilih = int(input("Pilihan : "))
      if (pilih == 1):
        os.system("cls")
        angka = int(input("angka yang akan dimasukkan : "))
        if angka % 2 == 1:
          self.tambahbelakang(angka)
        else:
          angka = int(input("angka yang akan dimasukkan : "))
          self.tambahdepan(angka)
      elif (pilih == 2):
        os.system("cls")
        self.showdata()
        angka = int(input("angka yang akan dicari : "))
        self.tambahtengah(angka)
      elif (pilih == 3):
        os.system("cls")
        if self.cekkosong() == False:
          self.showdata()
          angka = int(input("angka yang akan dicari : "))
          self.cari(angka)
        else:
          self.showdata()
          x = input()
      elif (pilih == 4):
        os.system("cls")
        if self.cekkosong() == False:
          self.deletedepan()
        else:
          print("data masih kosong, gagal menghapus")
          x = input()
      elif (pilih == 5):
        os.system("cls")
        self.showdata()
        if self.cekkosong() == False:
          self.deletebelakang()
        else:
          print("data masih kosong, gagal menghapus")
          x = input()
      elif (pilih == 6):
        os.system("cls")
        self.showdata()
        x = input("")
      else:
        perintah = 'n'
if __name__ == "__main__":
    l = linkedlist()
    l.menuutama()
