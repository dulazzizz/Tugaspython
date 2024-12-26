from abc import ABC, abstractmethod

# Abstract class BangunDatar
class BangunDatar(ABC):
    @abstractmethod
    def luas(self):
        pass

    @abstractmethod
    def keliling(self):
        pass

# Class Turunan PersegiPanjang
class PersegiPanjang(BangunDatar):
    def __init__(self, panjang, lebar):
        self.panjang = panjang
        self.lebar = lebar

    def luas(self):
        return self.panjang * self.lebar

    def keliling(self):
        return 2 * (self.panjang + self.lebar)

# Implementasi program
def main():
    panjang = float(input("Masukkan panjang persegi panjang: "))
    lebar = float(input("Masukkan lebar persegi panjang: "))

    persegi_panjang = PersegiPanjang(panjang, lebar)

    print("\nHasil Perhitungan:")
    print(f"Luas Persegi Panjang: {persegi_panjang.luas()}")
    print(f"Keliling Persegi Panjang: {persegi_panjang.keliling()}")

if __name__ == "__main__":
    main()
