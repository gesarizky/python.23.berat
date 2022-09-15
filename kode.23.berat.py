# Author  : Gesa Rizky Nugraha
# Email   : gesarizkynugraha@gmail.com
# Website : karenabelajar.blogspot.com

# Menginput Satuan Jarak
Gram = float(input("Tuliskan Berapa Gram: "))

# Mengkonversi
Kg  = Gram / 1000
Hg  = Gram / 100
Dag = Gram / 10
Dg  = Gram * 10
Cg  = Gram * 100
Mg  = Gram * 1000
 
# Menampilkan Hasil 
print('%0.2f  Gram sama dengan %0.2f Kilogram' %(Gram,Kg))
print('%0.2f  Gram sama dengan %0.2f Hektogram' %(Gram,Hg))
print('%0.2f  Gram sama dengan %0.2f Dekagram' %(Gram,Dag))
print('%0.2f  Gram sama dengan %0.2f Desigram' %(Gram,Dg))
print('%0.2f  Gram sama dengan %0.2f Centigram' %(Gram,Cg))
print('%0.2f  Gram sama dengan %0.2f Miligram' %(Gram,Mg))
