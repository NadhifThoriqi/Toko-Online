# untuk memanggin extensions
from flask import Flask, render_template, request, session, url_for, redirect, flash
from flask_session import Session
from fuzzywuzzy import process
from app import my_class, data #untuk products
import os, datetime

app = Flask(__name__)
app.secret_key = "~~tugas_kolompok_7_membuat_website_toko_online~~"
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)

products = my_class.create_list()
# menyimpan data email dan assword

txt_email_filepath = os.path.join(os.getcwd(), 'app/txt/email.txt')
users = data.load_data_email(txt_email_filepath)

txt_barang_filepath = os.path.join(os.getcwd(), 'app/txt/barang.txt')
barang = data.load_data_barang(txt_barang_filepath)

def cari_huruf(data, kata_kunci):
    nama_barang = [item["name"] for item in data]
    nama_barang_ditemukan = process.extract(kata_kunci, nama_barang, limit=len(data))
    
    hasil_detail = []
    for item in nama_barang_ditemukan:
        # Mencari barang yang sesuai dengan nama
        barang_ditemukan = next((b for b in data if b["name"] == item[0]), None)
        if barang_ditemukan:
            hasil_detail.append(barang_ditemukan)
    return hasil_detail

@app.route('/admin-?admin-@admin-ac-id-&-Password?!/')
def admin():
    for i, d in enumerate(users):
        i = i+1
    return render_template('halaman utama/admin.html',nomor=i,users=d,product=barang)

@app.route('/login/', methods=['POST'])
def login():
    data=[]
    email = request.form['email']
    password = request.form['password']
    for item in users:
        if email in item["email"] and password in item[f"{email}"]:
            data.append(item)
            session['email']=email
            session['nama']=item['username']
            return redirect(url_for('dashboard'))
        if email == "admin@gmail.com" and password == "admin123":
            return redirect(url_for('admin', users=users))
    flash('login succes','succes')
    flash(f'Login failed,<br> please check your email and password !!', 'danger')
    return redirect(url_for('dashboard'))

@app.route('/sigin/', methods=['POST'])
def signup():
    username = request.form['username']
    email = request.form['email']
    password = request.form['password']
    
    if email not in (item['email'] for item in users):
        with open(txt_email_filepath,'a') as file:
            file.write(f"{email}: {password}: {username}\n")
        return redirect(url_for('dashboard'))
    flash(f'Signup failed,<br> email: {email} already exists')
    return redirect(url_for('dashboard'))

@app.route('/')
def dashboard():
    dashboard = (render_template('halaman utama/home.html', name=session['nama'], products=products) if 'email' in session else render_template('login/login.html'))
    return dashboard
    
@app.route("/logout/")
def logout():
    session.pop('email', None)
    return redirect(url_for('dashboard'))

@app.route('/src/', methods=['GET', 'POST'])
def src():
    search_ditemukan = []
    if request.method =='POST':
        searching = request.form['src']
        search_ditemukan = cari_huruf(products, searching)
        if not search_ditemukan:
            flash('Sorry, the product you were looking for could not be found. Try entering another keyword.', 'danger')
    return render_template('pencarian/src.html',products=products, name=session['nama'], search_ditemukan=search_ditemukan, searching=searching)

@app.route('/product/<int:product_id>/')
def product(product_id):
    product = next((p for p in products if p['id'] == product_id), None)
    return render_template('transaksi/product.html', product=product, products=products)

@app.route('/product/checkout/<int:product_id>/')
def checkout(product_id):
    nama = session['nama']
    product = next((p for p in products if p['id'] == product_id), None)
    return render_template('transaksi/checkout.html', product=product, nama=nama)

@app.route('/process_checkout/', methods=['GET','POST'])
def process_checkout():
    if request.method == 'POST':
        # Mendapatkan tanggal dan waktu saat ini
        tanggal = datetime.datetime.now()
        nama = request.form['name']
        alamat = request.form['alamat']
        jumlah = int(request.form['jumlah'])
        keterangan = request.form['keterangan']
        pembayaran = request.form['pembayaran']
        product = request.form['product']
        harga = request.form['harga']
        produk = next((p for p in my_class.my_list() if p['name'] == request.form['product']), None)
        hitung = (float(produk["price"])*int(jumlah))
        total = str(my_class.format_uang(hitung))

        keterangan = (keterangan if keterangan else 'no description')
        
        data = {
            "nama": nama,
            "alamat": alamat, 
            "jumlah": jumlah,
            "harga": harga,
            "tanggal": tanggal.strftime("%Y-%m-%d"),
            "keterangan": keterangan, 
            "pembayaran": pembayaran, 
            "produk":product, 
            "total":total,
        }
        id_barang=len(barang)+1
        with open(txt_barang_filepath,'a') as file:
            file.write(f"id: {id_barang}, nama: {nama}, alamat: {alamat.replace(',','~')}, jumlah: {jumlah}, harga: {harga}, tanggal: {tanggal.strftime('%Y-%m-%d %H:%M:%S')}, keterangan: {keterangan.replace(',','~')}, pembayaran: {pembayaran}, produk: {product.replace(',','~')}, total: {total}\n")
        return render_template('transaksi/quitansi.html', products=products, data=data)
    return render_template('transaksi/checkout.html')

# profile
@app.route('/profile/')
def profile():
    return render_template('profile/profile.html')

# untuk menjalankan server lokal
if __name__ == '__main__':
    app.run(debug=True)