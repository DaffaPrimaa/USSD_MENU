import sys

def menu_transfer_pulsa():
    nomor_handphone = input("Silahkan masukan nomor tujuan Transfer Pulsa: ")
    
    if 10 <= len(nomor_handphone) <= 12:
        nominal_pulsa = int(input("Silahkan masukkan jumlah pulsa yang akan ditransfer: "))

        print(f"Anda akan Transfer Pulsa {nominal_pulsa} ke nomor {nomor_handphone}?")
        print("1. Ya")
        print("2. Back")

        konfirmasi = input("Masukkan: ")
            
        if konfirmasi == "1":
            print("Terima kasih permintaan anda sedang diproses.")
            sys.exit()
        elif konfirmasi == "2":
            menu_utama()


def menu_utama():
    print("Selamat datang di menu USSD")
    print("Ketik angka untuk mengakses menu")
    print("1. Transfer Pulsa")
    print("2. Keluar")
    
    opsi = input("Masukkan: ")
    
    if opsi == "1":
        menu_transfer_pulsa()
    elif opsi == "2":
        sys.exit()
    else:
        print("Angka tidak valid, mohon coba lagi")
        menu_utama()

def ussd():
    while True:
        ussd_code = input("Masukkan kode USSD: ")
        if ussd_code == "*858#":
            menu_utama()
        else:
            print("USSD tidak valid")
            sys.exit()

if __name__ == "__main__":
    ussd()
