def garis():
    print("----------")

#fungsi bubble sort ascending (dari kecil ke besar)
def sort_asc(array):
    array = sorted(array)
    return(array)

#fungsi bubble sort descending (dari besar ke kecil)
def sort_desc(array):
    array = sorted(array, reverse = True)
    return(array)

#fungsi rata rata
def rata_rata(angka):
    return sum(angka)/len(angka)

#input nilai
garis()
print("masukkan tiga buah nilai")
#masukan tipe data integer
nilai_a = int(input("nilai a : "))
nilai_b = int(input("nilai b : "))
nilai_c = int(input("nilai c : "))
#masukan tipe data array
angka = [nilai_a, nilai_b, nilai_c]
garis()
print()

#nilai akhir
print("hasil akhir----")
print("urutan angka ascending : ", (sort_asc(angka)))
print("urutan angka descending : ", (sort_desc(angka)))
garis()
print()

#angka terbesar
print("angka terbesar : ",max(angka))

#angka terkecil
print("angka terkecil : ",min(angka))

#rata rata
print("rata rata : ",round(rata_rata(angka),2))

#jumlah angka
print("jumlah angka : ",sum(angka))



