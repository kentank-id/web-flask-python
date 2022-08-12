from flask import Flask, render_template
app = Flask(__name__)

konten = [
    {
    'penulis': 'Joko Fatih',
    'judul': 'Postingan Pertama',
    'sinopsis': 'Ini adalah postingan pertama',
    'isi': 'Ini adalah isi dari postingan pertama',
    'tanggal': '12 Desember 2022',
    'jam': '16.00'
    },
    {
    'penulis': 'Ahmad Cebes',
    'judul': 'Tutorial Flask',
    'sinopsis': 'Ini adalah tutorial flask',
    'isi': 'Ini adalah isi dari tutorial flask',
    'tanggal': '13 Desember 2022',
    'jam': '18.00'
    }
]

@app.route("/")
def home():
    nama = "Joko"
    return render_template('home.html', a=nama, konten=konten, judul="Beranda")

@app.route("/tentang/")
def tentang():
    return render_template('tentang.html', judul='Tentang')

@app.route("/masuk/")
def masuk():
    return render_template('masuk.html', judul='Masuk')

@app.route("/daftar/")
def daftar():
    return render_template('daftar.html', judul="Daftar")

@app.route("/profil")
def profil():
    return render_template('profil.html', judul="Profil")

if __name__ == '__main__':
    app.run(debug=True)