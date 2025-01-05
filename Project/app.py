from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3 as sql
import sqlite3

app = Flask(__name__)

@app.route("/")
@app.route("/index")
def index():
    sqliteConnection = sqlite3.connect('database_penginapan.db')
    cursor = sqliteConnection.cursor()
    cursor.row_factory = sql.Row
    sqlite_select_query = "SELECT data_tamu.id, data_tamu.nama_tamu, tipe_kamar.nama_kamar, tipe_kamar.harga FROM data_tamu JOIN tipe_kamar ON data_tamu.tipe_kamar_id = tipe_kamar.id"
    cursor.execute(sqlite_select_query)
    data = cursor.fetchall()
    return render_template("index.html", datas=data)

@app.route("/tambah_data", methods=['POST', 'GET'])
def tambah_data():
    if request.method == 'POST':
        nama = request.form['nama_tamu']
        tipe_kamar_id = request.form['tipe_kamar_id']  # Ambil tipe kamar ID dari form
        sqliteConnection = sqlite3.connect('database_penginapan.db')
        cursor = sqliteConnection.cursor()
        cursor.execute("INSERT INTO data_tamu(tipe_kamar_id, nama_tamu) VALUES (?, ?)", (tipe_kamar_id, nama))
        sqliteConnection.commit()
        flash('Data Sudah Masuk', 'success')
        return redirect(url_for("index"))
    
    # Ambil data tipe kamar untuk dropdown
    sqliteConnection = sqlite3.connect('database_penginapan.db')
    cursor = sqliteConnection.cursor()
    cursor.row_factory = sql.Row
    cursor.execute("SELECT * FROM tipe_kamar")
    kamar_data = cursor.fetchall()
    return render_template("tambah_data.html", kamar_data=kamar_data)

@app.route("/edit_data/<string:id>", methods=['POST', 'GET'])
def edit_data(id):
    if request.method == 'POST':
        nama = request.form['nama_tamu']
        tipe_kamar_id = request.form['tipe_kamar_id']  # Ambil tipe kamar ID dari form
        sqliteConnection = sqlite3.connect('database_penginapan.db')
        cursor = sqliteConnection.cursor()
        cursor.execute("UPDATE data_tamu SET nama_tamu=?, tipe_kamar_id=? WHERE id=?", (nama, tipe_kamar_id, id))
        sqliteConnection.commit()
        flash('Data Sudah Di Update', 'success')
        return redirect(url_for("index"))

    sqliteConnection = sqlite3.connect('database_penginapan.db')
    cursor = sqliteConnection.cursor()
    cursor.row_factory = sql.Row
    cursor.execute("SELECT * FROM data_tamu WHERE id=?", (id,))
    data = cursor.fetchone()

    # Ambil data tipe kamar untuk dropdown
    cursor.execute("SELECT * FROM tipe_kamar")
    kamar_data = cursor.fetchall()
    return render_template("edit_data.html", datas=data, kamar_data=kamar_data)

@app.route("/hapus_data/<string:id>", methods=['GET'])
def hapus_data(id):
    sqliteConnection = sqlite3.connect('database_penginapan.db')
    cursor = sqliteConnection.cursor()
    cursor.execute("DELETE FROM data_tamu WHERE id=?", (id,))
    sqliteConnection.commit()
    flash('Data Sudah Terhapus', 'warning')
    return redirect(url_for("index"))

if __name__ == '__main__':
    app.secret_key='stikom123'
    app.run(debug=True)