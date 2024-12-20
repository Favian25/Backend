from flask import Flask, render_template, request, redirect, url_for, jsonify
import pymysql
import pymysql.cursors, os

app = Flask(__name__)

conn = cursor = None

# Fungsi koneksi database
def openDb():
    global conn, cursor
    conn = pymysql.connect(host="localhost", user="root", passwd="", database="perpus")
    cursor = conn.cursor(pymysql.cursors.DictCursor)

# Fungsi untuk menutup koneksi
def closeDb():
    global conn, cursor
    cursor.close()
    conn.close()

# Route untuk halaman utama
@app.route('/')
def index():
    openDb()
    container = []
    sql = "SELECT * FROM buku_nim"
    cursor.execute(sql)
    results = cursor.fetchall()
    for data in results:
        container.append(data)
    closeDb()
    return render_template('index_nim.html', books=container)

# Route untuk menampilkan form tambah buku
@app.route('/tambah', methods=['GET', 'POST'])
def tambah():
    if request.method == 'POST':
        openDb()
        kode_buku = request.form['kode_buku']
        nama_buku = request.form['nama_buku']
        penerbit = request.form['penerbit']
        pengarang = request.form['pengarang']
        jumlah = request.form['jumlah']
        
        sql = "INSERT INTO buku_nim (kode_buku, nama_buku, penerbit, pengarang, jumlah) VALUES (%s, %s, %s, %s, %s)"
        val = (kode_buku, nama_buku, penerbit, pengarang, jumlah)
        cursor.execute(sql, val)
        conn.commit()
        closeDb()
        return redirect(url_for('index'))
    else:
        return render_template('tambah_nim.html')

# Route untuk menampilkan form edit dan mengubah data
@app.route('/edit/<kode_buku>', methods=['GET', 'POST'])
def edit(kode_buku):
    openDb()
    cursor.execute('SELECT * FROM buku_nim WHERE kode_buku=%s', (kode_buku,))
    data = cursor.fetchone()
    if request.method == 'POST':
        nama_buku = request.form['nama_buku']
        penerbit = request.form['penerbit']
        pengarang = request.form['pengarang']
        jumlah = request.form['jumlah']
        
        sql = "UPDATE buku_nim SET nama_buku=%s, penerbit=%s, pengarang=%s, jumlah=%s WHERE kode_buku=%s"
        val = (nama_buku, penerbit, pengarang, jumlah, kode_buku)
        cursor.execute(sql, val)
        conn.commit()
        closeDb()
        return redirect(url_for('index'))
    else:
        closeDb()
        return render_template('edit_nim.html', book=data)

# Route untuk menghapus data
@app.route('/delete/<kode_buku>', methods=['GET'])
def delete(kode_buku):
    openDb()
    sql = "DELETE FROM buku_nim WHERE kode_buku = %s"
    cursor.execute(sql, (kode_buku,))
    conn.commit()
    closeDb()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)