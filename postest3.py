from prettytable import PrettyTable



class Bansos:
    def __init__(self, id_cart, nama, kelamin):
        self.id_cart = id_cart
        self.nama = nama
        self.kelamin = kelamin
        self.next = None


class BansosLinkedList:
    def __init__(self):
        self.head = None

    def tambah_bansos(self, id_cart, nama, kelamin):
        new_bansos = Bansos(id_cart, nama, kelamin)

        if not self.head:
            self.head = new_bansos
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_bansos


    def tampilkan_bansos(self):
        if not self.head:
            print("Tidak ada Bansos yang terdaftar.")
        else:
            current = self.head
            table = PrettyTable(["KTP", "Nama", "Kelamin"])
            while current:
                table.add_row([current.id_cart, current.nama, current.kelamin])
                current = current.next
            print(table)

    def cari_bansos(self, id_cart):
        current = self.head
        while current is not None:
            if current.id_cart == id_cart:
                return current
            current = current.next
        return None



    def update_bansos(self, id_cart, nama, kelamin):
        mahasiswa = list_bansos.cari_bansos(id_cart)
        if mahasiswa:
            mahasiswa.id_cart = id_cart
            mahasiswa.nama = nama
            mahasiswa.kelamin = kelamin
            print("Data Bansos berhasil diupdate!")
        else:
            print("Bansos dengan KTP tersebut tidak ditemukan.")

    def hapus_bansos(self, id_cart):
        current = self.head
        if current and current.id_cart == id_cart:
            self.head = current.next
            current = None
            print("Bansos berhasil dihapus")
            return
        prev = None
        while current and current.id_cart != id_cart:
            prev = current
            current = current.next
        if current is None:
            print("Bansos dengan KTP tersebut tidak ditemukan.")
            return
        prev.next = current.next
        current = None
        print("Bansos berhasil dihapus!")



def tampilan_menu():
    print("""
    =========================================
    ==========Menu user Bansos===============
    _________________________________________
    1. Tambah Data Bansos                   
    2. Tampilkan Data Bansos                
    3. Cari Data Basos                      
    4. Update Data Bansos                   
    5. Hapus Data Bansos                    
    6. Keluar                               
    _________________________________________""")


tampilan_menu()
list_bansos = BansosLinkedList()

while True:
    pilih = input("Masukan pilihan anda: ")

    if pilih == "1":
        id_cart = input("Masukan KTP          : ")
        nama = input("Masukan Nama         : ")
        kelamin = input("Masukan Jenis kelamin : ")
        list_bansos.tambah_bansos(id_cart, nama, kelamin)
        print("Data bansos berhasil ditambahkan!")
        tampilan_menu()
    
    elif pilih == "2":
        list_bansos.tampilkan_bansos()
        tampilan_menu()

    elif pilih == "3":
        list_bansos.tampilkan_bansos()
        id_cart = input("Masukan KTP yang ingin dicari: ")
        bansos1 = list_bansos.cari_bansos(id_cart)
        if bansos1:
            
            print(f"mahasiswa dengan KTP {id_cart} ditemukan")
            print(f"KTP : {bansos1.id_cart}")
            print(f"Nama : {bansos1.nama}")
            print(f"Kelamin : {bansos1.kelamin}")
            tampilan_menu()
        else:
            print(f"Bansos dengan KTP {id_cart} tidak ditemukan.")
            

    elif pilih == "4":
        list_bansos.tampilkan_bansos()
        id_cart = input("Masukan KTP mahasiswa yang ingin diupdate: ")
        bansos1 = list_bansos.cari_bansos(id_cart)
        if bansos1:
            id_cart_baru = input("Masukan KTP baru: ")
            nama_baru = input("Masukan Nama baru: ")
            Kelamin_baru = input("Masukan Kelamin baru: ")
            bansos1.id_cart = id_cart_baru
            bansos1.nama = nama_baru
            bansos1.kelamin = Kelamin_baru
            list_bansos.update_bansos(id_cart_baru, nama_baru, Kelamin_baru)
        else:
            print(f"Bansos dengan KTP {id_cart} tidak ditemukan.")
            tampilan_menu()



    elif pilih == "5":
        list_bansos.tampilkan_bansos()
        id_cart = input("Masukan KTP mahasiswa yang ingin dihapus: ")
        bansos1 = list_bansos.cari_bansos(id_cart)
        if bansos1:
            list_bansos.hapus_bansos(id_cart)
        else:
            print(f"Bansos dengan KTP {id_cart} tidak ditemukan.")
            tampilan_menu()

    elif pilih == "6":
        exit()