from app import my_deskrip
# Nama produk untuk mempermudah dibaca manusia(opsional)
# books => buku, fashion => pakaian, Laptop ""name"" => laptop,  => 
def my_list():
    merek = [
        {"id": 1,  "judul": "Laptop Asus",         "name": "Laptop Asus", 'name-produk': "", "price": 5270600, "image": "/static/img/Assus.png"},
        {"id": 2,  "judul": "Laptop HP",           "name": "Super Ngebut- Laptop Hp Elitebook 830 G5 Core I7 Gen8 Ram 16gb Ssd 512 - I5 Gen 8 Touch, 32gb/512ssd",  "price": 4950000, "image": "/static/img/HP elite book.png"},
        {"id": 3,  "judul": "Laptop Gaming",       "name": "SHINON Laptop Gaming Layar Hd 156 Inci dengan Sidik Jari Intel J4125 12GB+512GB Win10 Garansi Satu Tahu...", "price": 4000000, "image": "/static/img/Laptop Gaming.png"},
        {"id": 4,  "judul": "Meja Laptop",         "name": "Meja Laptop Roda Meja Portable Meja Kerja Meja Lipat Laptop Multifungsi Furnibest", "price": 169000, "image": "/static/img/Meja Laptop Portable.png", "video": "/static/video/a3413716b9e8fe4e24bf9bc4250b7f1a.mp4"},
        {"id": 5,  "judul": "Indomie Soto",        "name": "Indomie Soto Indofood Dus isi 40" ,  "price": 153000, "image": "/static/img/Indomie Soto.png"},
        {"id": 6,  "judul": "Powerbank",           "name": "Powerbank 20000 mAh with 4 Kabel Data Fast Charging Mini Size", "price": 138000, "image": "/static/img/Powerbank 20000 mAh 1.png", "video": "/static/video/Powerbank 30000 mAh with 4 Kabel Data.mp4"},
        {"id": 7,  "judul": "Tas Sonya",           "name": "Tas bahu wanita / Tas Sonya / Terbaru 2020 / Kulit sintetik",  "price": 20000,   "image": "/static/img/Tas Sonya.png"},
        {"id": 8,  "judul": "Gerobak Jualan ",     "name": "Gerobak Jualan Aluminium Pempek - Serbaguna",  "price": 5000000,   "image": "/static/img/grobak jualan alumunium.png"},
        {"id": 9,  "judul": "Printer Smart HP",    "name": "Printer Smart Tank HP 500 Print Scan Copy Pengganti HP 315 all in one",  "price": 1600000,   "image": "/static/img/Printer Smart.png"},
        {"id": 10, "judul": "Printer Epson",       "name": "Printer Epson L3216 EcoTank Print Scan Copy All In One", "price": 2300000,   "image": "/static/img/Printer Epson.png"},
        ]
    return merek

# untuk menggabung 2 list atau lebih
def create_list():
    gabung = []
    for m, s in zip(list1, list2):
        gabung.append({**m, **s})
    return gabung

# memberi titik dan memberi nilai dibelakang koma (,.2f)
def format_uang(value):
    return "Rp. {:,.0f}".format(value).replace(".",",").replace(",",".")

# mengubah isi key price
def get_format_number():
    return [
        {**num, "price": format_uang(num["price"])} for num in my_list()
    ]

# menyimpan list dari satu file
list1 = get_format_number()
# menyimpan list dari file lain
list2 = my_deskrip.create_deskripsi()