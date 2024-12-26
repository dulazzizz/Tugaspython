# Class 
class Mobil:
    # Instance
    def __init__(self, pd):
        self.pd = pd
        self.Merk = ""
        self.Warna = ""
        self.Kecepatan = ""

    # Method 1
    def printMbl(self):
        print("Merk Mobil : ", self.Merk)
        print("Warna Mobil : ", self.Warna)
        print("Kecepatan Mobil : ", self.Kecepatan)
        print("Model Mobil : ", self.pd)
    
    # Method 2
    def Her(self, kondisi):
        print("Telah Melakukan Pembayaran")
        print(kondisi)

# Objek
mbl1 = Mobil("Sports")
mbl2 = Mobil("Classic")

# Value
mbl1.Merk = "Porsche 911"
mbl1.Warna = "Kuning"
mbl1.Kecepatan = "308km/jam"
mbl2.Merk = "Volkswagen Beetle 1961"
mbl2.Warna = "Putih"
mbl2.Kecepatan = "100km/jam"

# Pemanggilan Method
mbl1.printMbl()
mbl1.Her("Mobil Siap dijalankan")
mbl2.printMbl()
mbl2.Her("Mobil Siap dijalankan")
