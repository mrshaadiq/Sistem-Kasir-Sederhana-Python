def tampilkan_barang(data):
    print("\n===Daftar Barang===")
    for b in data:
        print(b["kode"], "-", b["nama"], "Rp", b["harga"])
        print("====================")

def cari_barang(data, kode):
    for b in data:
        if b["kode"] == kode:
            return b
    return None

def tambah_ke_keranjang(barang, keranjang):
    kode = input("Masukkan kode barang yang ingin ditambahkan ke keranjang: ")
    item = cari_barang(barang, kode)

    if item is None:
        print("Barang dengan kode tersebut tidak ditemukan.")
        return
    
    try:
        qty = int(input("Masukkan jumlah barang yang ingin ditambahkan: "))
    except:
        print("Jumlah barang harus berupa angka.")
        return
    
    for k in keranjang:
        if k["kode"] == kode:
            k["qty"] += qty
            k["total_harga"] = k["qty"] * k["harga"]
            print("Qty barang berhasil diperbarui di keranjang.")
            return
        
        keranjang.append({
        "kode": item["kode"],
        "nama": item["nama"],
        "harga": item["harga"],
        "qty": qty,
        "total_harga": item["harga"] * qty
    })
    print("Barang berhasil ditambahkan ke keranjang.")

def tampilkan_keranjang(keranjang):
    if not keranjang:
        print("\nKeranjang belanja kosong.")
        return
    
    print("\n===Keranjang Belanja===")
    for k in keranjang:
        print(k["kode"], "-", k["nama"], "Rp", k["harga"], "x", k["qty"], "= Rp", k["total_harga"])
    print("=======================")