# untuk mengambil data dari file.txt
def load_data_email(email):
    data = []
    try:
        with open(email,'r') as file:
            for line in file:
                email, password, username = line.strip().split(': ')
                
                data.append({"email": email, email: password, "username": username})
    except FileNotFoundError:
        print(f"file {email} tidak ditemukan!!")
    return data

def load_data_barang(barang):
    data = []
    try:
        with open(barang,'r') as file:
            for line in file:
                values = line.strip().split(', ')
                id, nama, alamat, jumlah, harga, tanggal, keterangan, pembayaran, produk, total = values
                id = id.split(': ')[1]
                nama = nama.split(': ')[1]
                alamat = alamat.split(': ')[1]
                jumlah = jumlah.split(': ')[1]
                harga = harga.split(': ')[1]
                tanggal = tanggal.split(': ')[1]
                keterangan = keterangan.split(': ')[1]
                pembayaran = pembayaran.split(': ')[1]
                produk = produk.split(': ')[1]
                total = total.split(': ')[1]
                data.append({'id': id, 'nama': nama, 'alamat': alamat.replace('~',','), 'jumlah': jumlah, 'harga': harga, 'tanggal': tanggal, 'keterangan': keterangan.replace('~',','), 'pembayaran': pembayaran, 'produk': produk.replace('~',','), 'total': total})
    except FileNotFoundError:
        print(f"file {barang} tidak ditemukan!!")
    return data