data = []
def tambah():
    peg = int(input("jumlah pegawai = "))
    for i in range(peg):
        data1 = []
        for j in range(1):
            id_peg = i + 1
            nama_peg = str(input("nama pegawai = "))
            jenis = int(input("posisi(1,2,3) = "))
            if jenis == 1:
                jenisnya = "admin"
            elif jenis == 2:
                jenisnya = "operator"
            elif jenis == 3:
                jenisnya = "karyawan"
            data1.append(id_peg)
            data1.append(nama_peg)
            data1.append(jenisnya)
        data.append(data1)
    print()
def lihat():
    for i in range(len(data)):
        for j in range(len(data[i])):
            print(data[i][j], end=" | ")
        print()
    print()
# def hapus():
#     id_data = int(input("ID data yang ingin dihapus : "))       
def main():
    print("-----Main Menu-----")
    print("| Pilihan        |")
    print("| 1. Tambah data |")
    print("| 2. Lihat data  |")
    print("| exit           |")
    pilihan = input("pilihan saya = ")
    if pilihan == "1":
        tambah()
        main()
    elif pilihan == "2":
        lihat()
        main()
    elif pilihan == "exit":
        exit()
    else:
        print("ulangi bambank")
        main()
    print()
if __name__ == "__main__":
    main()
