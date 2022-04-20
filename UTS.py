print("Muhammad Yusuf Ibrahim Putra")
print("191011401926")

print("Kalkulator Sederhana")
print("1. Pertambahan")
print("2. Pengurangan")
print("3. Perkalian")
print("4. Sisa bagi")
print("pilih menu (1-4)")
menu = input()

if menu == "1":
    print("Menu pertambahan")
    print("Masukan nilai pertama")
    a = int(input())
    print("Masukan nilai kedua")
    b = int(input())
    hasil = a + b
    print(f"{a} + {b} = {hasil}")
elif menu == "2":
    print("Menu pengurang")
    print("Masukan nilai pertama")
    a = int(input())
    print("Masukan nilai kedua")
    b = int(input())
    hasil = a - b
    print(f"{a} - {b} = {hasil}")
elif menu == "3":
    print("Menu perkalian")
    print("Masukan nilai pertama")
    a = int(input())
    print("Masukan nilai kedua")
    b = int(input())
    hasil = a * b
    print(f"{a} * {b} = {hasil}")
elif menu == "4":
    print("Menu sisa bagi")
    print("Masukan nilai pertama")
    a = int(input())
    print("Masukan nilai kedua")
    b = int(input())
    hasil = a % b
    print(f"{a} % {b} = {hasil}")
else:
    print("Menu yang anda pilih tidak ada")
