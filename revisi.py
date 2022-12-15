import csv
import os 
import pandas as pd
try:
    nama_csv = 'tugas akhir.csv'

    def clear_screen():
        os.system('cls' if os.name == 'nt' else 'clear')

    def menu():
        clear_screen()
        print("="*30, "BitCount", "="*30)
        print("Selamat Datang di aplikasi BitCount,\nkelola dan maksimalkan lahan anda\ndengan bantuan kami")
        print("=="*35)
        print("")
        print("="*70)
        print("[1] Tampilkan Data")
        print("[2] Buat Data Baru")
        print("[3] Edit Data")
        print("[4] Hapus Data")
        print("[0] Exit")
        print("------------------------")
        selected_menu = input("Pilih menu > ")
        if (selected_menu == "1"):
            tampilan()
        elif(selected_menu == "2"):
            inputan()
        elif(selected_menu == "3"):
            Edit()
        elif(selected_menu == "4"):
            Hapus()
        elif(selected_menu == "0"):
            exit()
        else:
            print("Kamu memilih menu yang salah!")
            back_to_menu()

    def back_to_menu():
        print("\n")
        input("Tekan Enter untuk kembali...")
        menu()

        
    def inputan_salah():
        print("\n")
        print("Maaf ada kesalahan pada input data")
        input("Tekan Enter Untuk Kembali...")
        inputan()
        
    def edit_salah():
        print("\n")
        print("Maaf ada kesalahan pada input data")
        input("Tekan Enter Untuk Kembali...")
        Edit()
    
    def tampilan():
        clear_screen()
        print("-"*100)
        df = pd.read_csv(nama_csv)
        print(df.to_string(index = False)) 
        back_to_menu()
    def inputan():
        clear_screen()
        contacts = []
        listnomor = []
        with open(nama_csv, mode="r") as data_csv:
            csv_reader = csv.DictReader(data_csv)
            for row in csv_reader:
                contacts.append(row)
                listnomor.append(row['NO'])
        
        if len(listnomor) == 0:
            ketnomor = 0
            ketnomor = int(ketnomor)
        else:
            ketnomor = listnomor[-1:][0]
            ketnomor = int(ketnomor)
        
        nomor = ketnomor+1

        nama = input("masukkan nama anda : ")
        
        try:
            luas = int(input("masukkan luas lahan anda (m^2): "))
        except ValueError:
            inputan_salah()
        jenis_tanaman = input("masukkan jenis tanaman yang ingin ditanam : ")
        try:
            jarak_antar_tanaman = int(input("masukkan jarak lebar antar tanaman(cm) : "))
            jarak_antar_tanaman1 = int(input("masukkan jarak panjang antar tanaman(cm) : "))
        except ValueError:
            inputan_salah() 
        jarak_antar_tanaman = jarak_antar_tanaman / 100
        jarak_antar_tanaman1 = jarak_antar_tanaman1 / 100
        jarak_antar_tanaman = jarak_antar_tanaman*jarak_antar_tanaman1
        jumlah_maksimal = luas/jarak_antar_tanaman
        
        with open(nama_csv, mode='a') as data_csv:
            fieldnames = ['NO', 'NAMA', 'LUAS' , 'JENIS TANAMAN' , 'BIBIT TANAMAN YANG DIBUTUHKAN']
            writer = csv.DictWriter(data_csv, fieldnames=fieldnames)
            jumlah_maksimal = int(jumlah_maksimal)
            writer.writerow({'NO': nomor, 'NAMA': nama, 'LUAS': luas , 'JENIS TANAMAN' : jenis_tanaman , 'BIBIT TANAMAN YANG DIBUTUHKAN' : jumlah_maksimal})    
        tampilan()
        
    def Hapus():
        clear_screen()
        contacts = []
        with open(nama_csv, mode="r") as data_csv:
            csv_reader = csv.DictReader(data_csv)
            for row in csv_reader:
                contacts.append(row) 
        print("-"*100)
        df = pd.read_csv(nama_csv)
        print(df.to_string(index = False)) 
        print("-"*100)
        
        nomor = input("Hapus nomer> ")
        indeks = 0
        for data in contacts:
            if nomor == data['NO']:
                contacts.remove(contacts[indeks])
            indeks = indeks + 1
        with open(nama_csv, mode="w") as data_csv:
            fieldnames = ['NO', 'NAMA', 'LUAS' , 'JENIS TANAMAN' , 'BIBIT TANAMAN YANG DIBUTUHKAN']
            writer = csv.DictWriter(data_csv, fieldnames=fieldnames)
            writer.writeheader()
            for new_data in contacts:
                writer.writerow({'NO': new_data['NO'], 'NAMA': new_data['NAMA'], 'LUAS': new_data['LUAS'] , 'JENIS TANAMAN':new_data['JENIS TANAMAN'] , 'BIBIT TANAMAN YANG DIBUTUHKAN':new_data['BIBIT TANAMAN YANG DIBUTUHKAN']}) 

        
        tampilan()
        
    def Edit():
        clear_screen()
        contacts = []
        with open(nama_csv, mode="r") as data_csv:
            csv_reader = csv.DictReader(data_csv)
            for row in csv_reader:
                contacts.append(row) 
        print("-"*100)
        df = pd.read_csv(nama_csv)
        print(df.to_string(index = False)) 
        print("-"*100)
        
        nomor = input("masukkan nomor urutan = ")   
        for data in contacts:
            
            if nomor == data['NO']:
                nama = input("masukkan nama anda : ")
                try:
                    luas = int(input("masukkan luas lahan anda (m^2): "))
                except ValueError:
                    edit_salah()
                    
                jenis_tanaman = input("masukkan jenis tanaman yang ingin ditanam : ")
                try:
                    jarak_antar_tanaman = int(input("masukkan jarak lebar antar tanaman(cm) : "))
                    jarak_antar_tanaman1 = int(input("masukkan jarak panjang antar tanaman(cm) : "))
                except ValueError:
                    edit_salah()
                jarak_antar_tanaman = jarak_antar_tanaman / 100
                jarak_antar_tanaman1 = jarak_antar_tanaman1 / 100
                jarak_antar_tanaman = jarak_antar_tanaman*jarak_antar_tanaman1
                jumlah_maksimal = luas/jarak_antar_tanaman 
                jumlah_maksimal = int(jumlah_maksimal)    
                indeks = 0
                for data in contacts:
                    if (data['NO'] == nomor):
                        contacts[indeks]['NAMA'] = nama
                        contacts[indeks]['LUAS'] = luas 
                        contacts[indeks]['JENIS TANAMAN'] = jenis_tanaman
                        contacts[indeks]['BIBIT TANAMAN YANG DIBUTUHKAN'] = jumlah_maksimal
                    indeks = indeks + 1
                with open(nama_csv, mode="w") as data_csv:
                    fieldnames = ['NO', 'NAMA', 'LUAS' , 'JENIS TANAMAN' , 'BIBIT TANAMAN YANG DIBUTUHKAN']
                    writer = csv.DictWriter(data_csv, fieldnames=fieldnames)
                    writer.writeheader()
                    for new_data in contacts:
                        writer.writerow({'NO': new_data['NO'], 'NAMA': new_data['NAMA'], 'LUAS': new_data['LUAS'] , 'JENIS TANAMAN':new_data['JENIS TANAMAN'] , 'BIBIT TANAMAN YANG DIBUTUHKAN':new_data['BIBIT TANAMAN YANG DIBUTUHKAN']}) 
                tampilan()
        print("maaf nomor anda tidak ada di database kita")
        back_to_menu()
        
    menu()
    
except ValueError:
    print("maaf ada kesalahan pada saat menginputkan data")
    back_to_menu()
    
