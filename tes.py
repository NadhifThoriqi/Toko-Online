from fuzzywuzzy import process

# Daftar barang dalam bentuk list of dictionaries
barang = [
    {"nama": "Laptop", "kategori": "Elektronik"},
    {"nama": "Smartphone", "kategori": "Elektronik"},
    {"nama": "Tablet", "kategori": "Elektronik"},
    {"nama": "Kamera", "kategori": "Elektronik"},
    {"nama": "Headphone", "kategori": "Aksesoris"},
    {"nama": "Smartwatch", "kategori": "Elektronik"},
    {"nama": "Printer", "kategori": "Perangkat Keras"},
    {"nama": "Monitor", "kategori": "Perangkat Keras"},
    {"nama": "Keyboard", "kategori": "Perangkat Keras"},
    {"nama": "Mouse", "kategori": "Perangkat Keras"},
    {"nama": "Televisi", "kategori": "Elektronik"},
    {"nama": "Kulkas", "kategori": "Peralatan Rumah Tangga"},
    {"nama": "Mesin Cuci", "kategori": "Peralatan Rumah Tangga"},
    {"nama": "Oven", "kategori": "Peralatan Dapur"},
    {"nama": "Blender", "kategori": "Peralatan Dapur"},
    {"nama": "Microwave", "kategori": "Peralatan Dapur"},
    {"nama": "Proyektor", "kategori": "Elektronik"},
    {"nama": "Speaker", "kategori": "Aksesoris"},
    {"nama": "Drone", "kategori": "Elektronik"},
    {"nama": "Action Camera", "kategori": "Elektronik"},
    {"nama": "Smart TV", "kategori": "Elektronik"},
    {"nama": "Game Console", "kategori": "Elektronik"},
    {"nama": "E-reader", "kategori": "Elektronik"},
    {"nama": "Fitness Tracker", "kategori": "Aksesoris"},
    {"nama": "Virtual Reality Headset", "kategori": "Elektronik"},
    {"nama": "Webcam", "kategori": "Perangkat Keras"},
    {"nama": "Router", "kategori": "Perangkat Keras"},
    {"nama": "Modem", "kategori": "Perangkat Keras"},
    {"nama": "Power Bank", "kategori": "Aksesoris"},
    {"nama": "Charger", "kategori": "Aksesoris"},
    {"nama": "USB Flash Drive", "kategori": "Aksesoris"},
    {"nama": "External Hard Drive", "kategori": "Aksesoris"},
    {"nama": "SSD", "kategori": "Aksesoris"},
    {"nama": "HDD", "kategori": "Aksesoris"},
    # Tambahkan lebih banyak barang sesuai kebutuhan
]

# Fungsi untuk mencari barang
def cari_barang(input_barang):
    # Ambil hanya nama barang untuk pencarian
    nama_barang = [item["nama"] for item in barang]
    hasil = process.extract(input_barang, nama_barang, limit=5)
    
    # Mengambil detail barang dari hasil pencarian
    hasil_detail = []
    for item in hasil:
        # Mencari barang yang sesuai dengan nama
        barang_ditemukan = next((b for b in barang if b["nama"] == item[0]), None)
        if barang_ditemukan:
            hasil_detail.append(barang_ditemukan)
    return hasil_detail

# Contoh penggunaan
input_user = input("Masukkan nama barang yang dicari: ")
hasil_cari = cari_barang(input_user)

print("Hasil pencarian:")
for item in hasil_cari:
    print(f"- {item['nama']} (Kategori: {item['kategori']})")