# untuk memanggin extensions
from flask import Flask, render_template, request, session, url_for, redirect, flash
from app import my_class, data #untuk products
import os

app = Flask(__name__)
app.secret_key = "-0987654321~"

products = my_class.create_list()
# menyimpan data email dan assword

txt_email_filepath = os.path.join(os.getcwd(), 'documents/projek toko web/app/txt/email.txt')
users = data.load_data_email(txt_email_filepath)

txt_barang_filepath = os.path.join(os.getcwd(), 'documents/projek toko web/app/txt/barang.txt')
barang = data.load_data_barang(txt_barang_filepath)

def cari_huruf(dalam_list, huruf):
    hasil = []
    huruf = huruf.lower()  # Mengubah huruf yang dicari menjadi huruf kecil
    for item in dalam_list:
        if huruf in item["name"].lower():  # Mengubah item menjadi huruf kecil untuk perbandingan
            hasil.append(item)
    return hasil

@app.route('/')
def index():
    return render_template('login/login.html')

@app.route('/home')
def home():
    return render_template('index.html', name=session['nama'], products=products)

@app.route('/admin-?admin-@admin-ac-id-&-Password?!')
def admin():
    return render_template('admin.html',users=users,product=barang)

@app.route('/login', methods=['POST'])
def login():
    data=[]
    email = request.form['email']
    password = request.form['password']
    for item in users:
        if email in item["email"] and password in item["password"]:
            data.append(item)
            session['username']=email
            session['nama']=item['username']
            return redirect(url_for('dashboard'))
        if email == "admin@gmail.com" and password == "admin123":
            return redirect(url_for('admin', users=users))
    return 'Login failed, please check your email and password'

@app.route('/sigin', methods=['POST'])
def signup():
    username = request.form['username']
    email = request.form['email']
    password = request.form['password']
    
    if username not in users:
        id_baru = len(users) + 1
        with open(txt_email_filepath,'a') as file:
            file.write(f"id: {id_baru}, email: {email}, password: {password}, username: {username}\n")
        # session['nama']=username
        return redirect(url_for('index'))
    return 'Signup failed, username already exists'

@app.route('/dashboard')
def dashboard():
    if 'username' in session:
        username = session['username']
        flash('login succes','succes')
        return redirect(url_for('home',username=username))
    return redirect(url_for('index'))

@app.route("/logout")
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))

@app.route('/src', methods=['GET', 'POST'])
def src():
    search_ditemukan = []
    if request.method =='POST':
        searching = request.form['src']
        search_ditemukan = cari_huruf(products, searching)
        if not search_ditemukan:
            return 'Mohon maaf, produk yang anda cari tidak ditemukan. Coba masukkan kata kunci yang lain.'
    return render_template('pencarian/src.html',products=products, name=session['nama'], search_ditemukan=search_ditemukan)

@app.route('/product/<int:product_id>/')
def product(product_id):
    product = next((p for p in products if p['id'] == product_id), None)
    return render_template('product.html', product=product, products=products)

@app.route('/product/checkout/<int:product_id>/')
def checkout(product_id):
    nama = session['nama']
    product = next((p for p in products if p['id'] == product_id), None)
    return render_template('quitansi/checkout.html', product=product, nama=nama)

@app.route('/process_checkout/', methods=['GET','POST'])
def process_checkout():
    if request.method == 'POST':
        nama = session['nama']
        alamat = request.form['alamat']
        jumlah = int(request.form['jumlah'])
        tanggal = request.form['tanggal']
        keterangan = request.form['keterangan']
        pembayaran = request.form['pembayaran']
        product = request.form['product']
        harga = request.form['harga']
        produk = next((p for p in my_class.my_list() if p['name'] == request.form['product']), None)
        hitung = (float(produk["price"])*int(jumlah))
        total = str(my_class.format_uang(hitung))

        data = {
            "nama": nama,
            "alamat": alamat, 
            "jumlah": jumlah,
            "harga": harga,
            "tanggal": tanggal,
            "keterangan": keterangan, 
            "pembayaran": pembayaran, 
            "produk":product, 
            "total":total,
        }
        id_barang=len(barang)+1
        with open(txt_barang_filepath,'a') as file:
            file.write(f"id: {id_barang}, nama: {nama}, alamat: {alamat.replace(',','~')}, jumlah: {jumlah}, harga: {harga}, tanggal: {tanggal}, keterangan: {keterangan.replace(',','~')}, pembayaran: {pembayaran}, produk: {product.replace(',','~')}, total: {total}\n")
        return render_template('quitansi/quitansi.html', products=products, data=data)
    return render_template('quitansi/checkout.html')

# untuk menjalankan server lokal
if __name__ == '__main__':
    app.run(debug=True)