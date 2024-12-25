from flask import Flask, redirect, url_for, request, render_template

# Membuat instance aplikasi Flask
app = Flask(__name__)

# Halaman Utama (Root URL)
@app.route("/")  # Rute untuk halaman utama
def home():
    # Menampilkan halaman home.html yang ada di folder templates
    return render_template('home.html')  # Pastikan file home.html ada di dalam folder templates

# Halaman Login
@app.route('/login', methods=['POST', 'GET'])  # Rute untuk halaman login, menerima dua metode: POST dan GET
def login():
    # Jika metode yang digunakan adalah POST (data form dikirimkan oleh pengguna)
    if request.method == 'POST':  
        # Mengambil data dari form dengan nama 'nm' (misalnya input untuk username)
        user = request.form['nm']  
        # Menampilkan halaman login.html dan mengirimkan nama pengguna untuk ditampilkan di halaman
        return render_template('login.html', name=user)  
    else:
        # Jika metode GET (halaman login pertama kali dimuat), hanya menampilkan form login
        return render_template('login.html')  # Render halaman login.html tanpa data tambahan

# Menjalankan aplikasi Flask
if __name__ == '__main__':  
    # Mengaktifkan server dengan mode debug, sehingga aplikasi akan reload otomatis saat ada perubahan
    app.run(debug=True)