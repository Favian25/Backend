#import modul
import sqlite3
try:
    sqliteConnection = sqlite3.connect('database_penginapan.db')
    cursor = sqliteConnection.cursor()
    print("Database berhasil terkoneksi")

    # Membuat tabel tipe_kamar
    sqlite_create_table_kamar_query = '''CREATE TABLE tipe_kamar (
                                            id INTEGER PRIMARY KEY,
                                            nama_kamar TEXT NOT NULL UNIQUE,
                                            harga INTEGER NOT NULL,
                                            slot INTEGER NOT NULL);'''
    cursor.execute(sqlite_create_table_kamar_query)
    sqliteConnection.commit()
    print("Tabel tipe_kamar berhasil dibuat")

    # Menambahkan data tipe kamar
    kamar_data = [
        ('Private Standart', 500000, 4),
        ('Deluxe Room', 750000, 2),
        ('Family Room', 1000000, 3)
    ]
    
    cursor.executemany('''INSERT INTO tipe_kamar (nama_kamar, harga, slot) VALUES (?, ?, ?)''', kamar_data)
    sqliteConnection.commit()
    print("Data tipe kamar berhasil ditambahkan")

    # Membuat tabel data_tamu
    sqlite_create_table_tamu_query = '''CREATE TABLE data_tamu (
                                            id INTEGER PRIMARY KEY,
                                            nama_tamu TEXT NOT NULL,
                                            tipe_kamar_id INTEGER NOT NULL,
                                            FOREIGN KEY (tipe_kamar_id) REFERENCES tipe_kamar (id));'''
    cursor.execute(sqlite_create_table_tamu_query)
    sqliteConnection.commit()
    print("Tabel data_tamu berhasil dibuat")

    cursor.close()

except sqlite3.Error as error:
    print("Error Gagal terkoneksi ke Database", error)
finally:
    if (sqliteConnection):
        sqliteConnection.close()
        print("Koneksi Database Selesai")