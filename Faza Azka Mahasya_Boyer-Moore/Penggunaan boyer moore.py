# Fungsi untuk membangun tabel bad character heuristic
def buat_tabel_karakter_buruk(pola):
    ukuran = len(pola)
    tabel = {char: ukuran for char in set(pola)}
    for i in range(ukuran - 1):
        tabel[pola[i]] = ukuran - 1 - i
    return tabel

# Fungsi utama Boyer-Moore
def boyer_moore(teks, pola):
    n, m = len(teks), len(pola)
    tabel_buruk = buat_tabel_karakter_buruk(pola)
    geser = 0
    
    while geser <= n - m:
        j = m - 1
        while j >= 0 and pola[j] == teks[geser + j]:
            j -= 1
        if j < 0:
            return geser
        else:
            geser += tabel_buruk.get(teks[geser + m - 1], m)
    return -1

# Contoh Penggunaan
teks = "ABAAABCD"
pola = "ABC"
print("Pola ditemukan pada indeks:", boyer_moore(teks, pola))