import csv

# ==========================
# LINKED LIST BARANG
# ==========================

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def tambah(self, data):
        node_baru = Node(data)

        if self.head is None:
            self.head = node_baru
            return

        sekarang = self.head

        while sekarang.next:
            sekarang = sekarang.next

        sekarang.next = node_baru

    def tampilkan(self):
        sekarang = self.head

        while sekarang:
            print(sekarang.data)
            sekarang = sekarang.next

    def cari(self, id_barang):
        sekarang = self.head

        while sekarang:
            if sekarang.data["id"] == id_barang:
                return sekarang

            sekarang = sekarang.next

        return None

    def hapus(self, id_barang):

        sekarang = self.head

        if sekarang and sekarang.data["id"] == id_barang:
            self.head = sekarang.next
            return True

        sebelumnya = None

        while sekarang:
            if sekarang.data["id"] == id_barang:
                sebelumnya.next = sekarang.next
                return True

            sebelumnya = sekarang
            sekarang = sekarang.next

        return False


barang_list = LinkedList()

# ==========================
# HASH MAP BAHAN
# ==========================

bahan = {}

# ==========================
# CSV BARANG
# ==========================

def load_barang():
    try:
        with open("barang.csv", "r", newline="") as file:
            reader = csv.DictReader(file)

            for row in reader:
                barang_list.tambah(row)

    except FileNotFoundError:
        pass


def simpan_barang():
    with open("barang.csv", "w", newline="") as file:

        fieldnames = ["id", "nama", "harga", "stok"]

        writer = csv.DictWriter(
            file,
            fieldnames=fieldnames
        )

        writer.writeheader()

        sekarang = barang_list.head

        while sekarang:
            writer.writerow(sekarang.data)
            sekarang = sekarang.next

# ==========================
# CSV BAHAN
# ==========================

def load_bahan():
    try:
        with open("bahan.csv", "r", newline="") as file:
            reader = csv.DictReader(file)

            for row in reader:
                bahan[row["id"]] = row

    except FileNotFoundError:
        pass


def simpan_bahan():
    with open("bahan.csv", "w", newline="") as file:

        fieldnames = ["id", "nama", "stok"]

        writer = csv.DictWriter(
            file,
            fieldnames=fieldnames
        )

        writer.writeheader()

        for data in bahan.values():
            writer.writerow(data)

# ==========================
# CRUD BARANG
# ==========================

def tambah_barang():

    id_barang = input("ID Barang : ")
    nama = input("Nama Barang : ")
    harga = input("Harga : ")
    stok = input("Stok : ")

    barang_list.tambah({
        "id": id_barang,
        "nama": nama,
        "harga": harga,
        "stok": stok
    })

    simpan_barang()

    print("Barang berhasil ditambahkan")


def lihat_barang():

    print("\n=== DATA BARANG ===")
    barang_list.tampilkan()


def update_barang():

    id_barang = input("ID Barang : ")

    node = barang_list.cari(id_barang)

    if node:
        node.data["nama"] = input("Nama Baru : ")
        node.data["harga"] = input("Harga Baru : ")
        node.data["stok"] = input("Stok Baru : ")

        simpan_barang()

        print("Data berhasil diupdate")

    else:
        print("Barang tidak ditemukan")


def hapus_barang():

    id_barang = input("ID Barang : ")

    if barang_list.hapus(id_barang):

        simpan_barang()

        print("Barang berhasil dihapus")

    else:
        print("Barang tidak ditemukan")

# ==========================
# SEARCHING
# ==========================

def cari_barang():

    id_barang = input("Masukkan ID Barang : ")

    node = barang_list.cari(id_barang)

    if node:
        print(node.data)

    else:
        print("Barang tidak ditemukan")

# ==========================
# SORTING
# ==========================

def urutkan_barang():

    data = []

    sekarang = barang_list.head

    while sekarang:
        data.append(sekarang.data)
        sekarang = sekarang.next

    data.sort(key=lambda x: x["nama"])

    print("\n=== DATA TERURUT ===")

    for item in data:
        print(item)

# ==========================
# CRUD BAHAN
# ==========================

def tambah_bahan():

    id_bahan = input("ID Bahan : ")
    nama = input("Nama Bahan : ")
    stok = input("Stok : ")

    bahan[id_bahan] = {
        "id": id_bahan,
        "nama": nama,
        "stok": stok
    }

    simpan_bahan()

    print("Bahan berhasil ditambahkan")


def lihat_bahan():

    print("\n=== DATA BAHAN ===")

    for data in bahan.values():
        print(data)

# ==========================
# KEUANGAN
# ==========================

def tambah_transaksi():

    tanggal = input("Tanggal : ")
    jenis = input("Jenis (pemasukan/pengeluaran) : ")
    jumlah = input("Jumlah : ")
    ket = input("Keterangan : ")

    with open("keuangan.csv", "a", newline="") as file:

        writer = csv.writer(file)

        writer.writerow([
            tanggal,
            jenis,
            jumlah,
            ket
        ])

    print("Transaksi berhasil disimpan")


def lihat_saldo():

    saldo = 0

    try:

        with open("keuangan.csv", "r") as file:

            reader = csv.reader(file)

            for row in reader:

                if len(row) < 4:
                    continue

                if row[1] == "pemasukan":
                    saldo += int(row[2])

                elif row[1] == "pengeluaran":
                    saldo -= int(row[2])

        print("Saldo Saat Ini :", saldo)

    except FileNotFoundError:
        print("Belum ada data transaksi")

# ==========================
# PROGRAM UTAMA
# ==========================

load_barang()
load_bahan()

while True:

    print("""
===== SISTEM MANAJEMEN BUTIK =====

1. Tambah Barang
2. Lihat Barang
3. Update Barang
4. Hapus Barang
5. Cari Barang
6. Urutkan Barang
7. Tambah Bahan
8. Lihat Bahan
9. Tambah Transaksi
10. Lihat Saldo
0. Keluar
""")

    pilih = input("Pilih Menu : ")

    if pilih == "1":
        tambah_barang()

    elif pilih == "2":
        lihat_barang()

    elif pilih == "3":
        update_barang()

    elif pilih == "4":
        hapus_barang()

    elif pilih == "5":
        cari_barang()

    elif pilih == "6":
        urutkan_barang()

    elif pilih == "7":
        tambah_bahan()

    elif pilih == "8":
        lihat_bahan()

    elif pilih == "9":
        tambah_transaksi()

    elif pilih == "10":
        lihat_saldo()

    elif pilih == "0":
        print("Program selesai")
        break

    else:
        print("Menu tidak tersedia")