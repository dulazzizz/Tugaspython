import tkinter as tk
from tkinter import messagebox

def simpan_data():
    nim = entry_nim.get()
    nama = entry_nama.get()
    prodi = entry_prodi.get()
    semester = entry_semester.get()
    ipk1 = entry_ipk1.get()
    ipk2 = entry_ipk2.get()

    if not all([nim, nama, prodi, semester, ipk1, ipk2]):
        messagebox.showwarning("Peringatan", "Semua data harus diisi!")
        return

    try:
        ipk1 = float(ipk1)
        ipk2 = float(ipk2)
    except ValueError:
        messagebox.showerror("Kesalahan", "IPK harus berupa angka!")
        return

    messagebox.showinfo("Data Disimpan", f"Data Mahasiswa:\nNIM: {nim}\nNama: {nama}\nProdi: {prodi}\nSemester: {semester}\nIPK Semester 1: {ipk1}\nIPK Semester 2: {ipk2}")

# Membuat jendela utama
window = tk.Tk()
window.title("Data Mahasiswa")

# Membuat grid layout
label_title = tk.Label(window, text="Data Mahasiswa", font=("Arial", 14))
label_title.grid(row=0, column=0, columnspan=2, pady=10)

label_nim = tk.Label(window, text="NIM")
label_nim.grid(row=1, column=0, sticky="w", padx=10, pady=5)
entry_nim = tk.Entry(window)
entry_nim.grid(row=1, column=1, padx=10, pady=5)

label_nama = tk.Label(window, text="Nama")
label_nama.grid(row=2, column=0, sticky="w", padx=10, pady=5)
entry_nama = tk.Entry(window)
entry_nama.grid(row=2, column=1, padx=10, pady=5)

label_prodi = tk.Label(window, text="Prodi")
label_prodi.grid(row=3, column=0, sticky="w", padx=10, pady=5)
entry_prodi = tk.Entry(window)
entry_prodi.grid(row=3, column=1, padx=10, pady=5)

label_semester = tk.Label(window, text="Semester")
label_semester.grid(row=4, column=0, sticky="w", padx=10, pady=5)
entry_semester = tk.Entry(window)
entry_semester.grid(row=4, column=1, padx=10, pady=5)

label_ipk1 = tk.Label(window, text="IPK Semester 1")
label_ipk1.grid(row=5, column=0, sticky="w", padx=10, pady=5)
entry_ipk1 = tk.Entry(window)
entry_ipk1.grid(row=5, column=1, padx=10, pady=5)

label_ipk2 = tk.Label(window, text="IPK Semester 2")
label_ipk2.grid(row=6, column=0, sticky="w", padx=10, pady=5)
entry_ipk2 = tk.Entry(window)
entry_ipk2.grid(row=6, column=1, padx=10, pady=5)

# Tombol Simpan
button_simpan = tk.Button(window, text="SIMPAN", command=simpan_data)
button_simpan.grid(row=7, column=0, columnspan=2, pady=10)

# Menjalankan aplikasi
window.mainloop()