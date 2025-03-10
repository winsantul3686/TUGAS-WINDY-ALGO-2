#LATIHAN 1
import os
# Fungsi untuk mencetak menu menggunakan titik sebagai jarak
def print_menu(menu_list, parent_id=0, level=0):
    for menu in menu_list:
        if menu[1] == parent_id:
            print("." * (level * 2) + f"{menu[2]}")  # Titik sesuai level
            print_menu(menu_list, menu[0], level + 1)

# Meminta input jumlah menu
n = int(input("Masukkan jumlah menu: "))
menu_list = []

# Meminta input untuk setiap menu
for _ in range(n):
    menu_id = int(input("Masukkan ID menu: "))
    parent_id = int(input("Masukkan ID parent menu (0 jika tidak memiliki parent): "))
    label = input("Masukkan label menu: ")
    menu_list.append((menu_id, parent_id, label))

# Mencetak menu dengan struktur hierarki
print("\nStruktur Menu:")
print_menu(menu_list)

input("Selesai, klik Enter...")
os.system('cls')

#2. rekursif palindrom
def palindrom(s):
    # Filter agar tidak memperdulikan tanda baca dan huruf kapital
    s = ''.join(char.lower() for char in s if char.isalpha())  
    if len(s) <= 1:  # base code,dimana jika string 0 atau karakter hanya 1 dibalik pun tetap palindrom
        return True
    if s[0] == s[-1]:  # mengecek apakah huruf pertama dan terakhir sama
        return palindrom(s[1:-1])  # rekursif mengambil huruf selain huruf pertama dan terakhir
    else:
        return False

# Input data
string = input("Enter string: ")

# Mengecek apakah string adalah palindrom
if palindrom(string):
    print("User menggunakan palindrom")
else:
    print("Bukan palindrom")



