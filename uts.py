#Fikri Alfadani (20552021026)
#Menu Pilihan Jurusan di UNIVERSITAS ISLAM RADEN RAHMAT MALANG

import os
print("==PROGRAM PEMILIHAN JURUSAN UNIRA MALANG==")
print("1. Sains dan Teknologi")
print("2. Fakultas Ilmu Sosial dan Politik")
print("3. Fakultas Ilmu Pendidikan ")
print("4. Fakultas Ilmu Keislaman")
print("5. Fakultas Ekonomi dan Bisnis\n")
fakultas = input("Pilih Fakultas : ")

os.system('cls')
if(int(fakultas)==1):
    print("PROGRAM STUDI FAKULTAS SAINTEK")
    print("1. Teknik Informatika")
    print("2. Sistem Informasi")
    print("3. Teknik Mesin")
    print("4. Teknik Elektro")
    print("5. Agroteknologi\n")
    prodi = input("Pilih Prodi : ")
    os.system('cls')
    if(int(prodi)==1):
        print("Mahasiswa Prodi Teknik Informatika Fakultas Saintek\n\n")
    elif(int(prodi)==2):
        print("Mahasiswa Prodi Sistem Informasi Fakultas Saintek\n\n")
    elif(int(prodi)==3):
        print("Mahasiswa Prodi Teknik Mesin Fakultas Saintek\n\n")
    elif(int(prodi)==4):
        print("Mahasiswa Prodi Teknik Elektro Fakultas Saintek\n\n")
    elif(int(prodi)==5):
        print("Mahasiswa Prodi Agroteknologi Fakultas Saintek\n\n")
    else:
        print("Tidak ada Pilihan Prodi!\n\n")

elif(int(fakultas)==2):
    print("PROGRAM STUDI FISIP")
    print("1. Psikologi")
    print("2. Ilmu Pemerintahan\n")
    prodi = input("Pilih Prodi : ")
    os.system('cls')
    if(int(prodi)==1):
        print("Mahasiswa Prodi Psikologi Fakultas Ilmu Sosial dan Politik\n\n")
    elif(int(prodi)==2):
        print("Mahasiswa Prodi Ilmu Pemerintahan Fakultas Ilmu Sosial dan Politik\n\n")
    else:
        print("Tidak ada Pilihan Prodi!\n\n")

elif(int(fakultas)==3):
    print("PROGRAM STUDI FIP")
    print("1. Pendidikan IPS")
    print("2. PGSD\n")
    prodi = input("Pilih Prodi : ")
    os.system('cls')
    if(int(prodi)==1):
        print("Mahasiswa Prodi Pendidikan IPS Fakultas Ilmu Pendidikan\n\n")
    elif(int(prodi)==2):
        print("Mahasiswa Prodi PGSD Fakultas Ilmu Pendidikan\n\n")
    else:
        print("Tidak ada Pilihan Prodi!\n\n")

elif(int(fakultas)==4):
    print("PROGRAM STUDI FIK")
    print("1. PAI")
    print("2. PGMI\n")
    prodi = input("Pilih Prodi : ")
    os.system('cls')
    if(int(prodi)==1):
        print("Mahasiswa Prodi PAI Fakultas Ilmu Keislaman\n\n")
    elif(int(prodi)==2):
        print("Mahasiswa Prodi PGMI Fakultas Ilmu Keislaman\n\n")
    else:
        print("Tidak ada Pilihan Prodi!\n\n")

elif(int(fakultas)==5):
    print("PROGRAM STUDI FEB")
    print("1. HES")
    print("2. Manajemen")
    print("3. Perbankan Syari'ah\n")
    prodi = input("Pilih Prodi : ")
    os.system('cls')
    if(int(prodi)==1):
        print("Mahasiswa Prodi HES Fakultas Ekonomi dan Bisnis\n\n")
    elif(int(prodi)==2):
        print("Mahasiswa Prodi Manajemen Fakultas Ekonomi dan Bisnis\n\n")
    elif(int(prodi)==3):
        print("Mahasiswa Prodi Perbankan Syari'ah Fakultas Ekonomi dan Bisnis\n\n")
    else:
        print("Tidak ada Pilihan Prodi!\n\n")

else:
    print("Pilihan Tidak Ada!!!!\n\n")