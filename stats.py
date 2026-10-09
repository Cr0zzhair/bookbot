# stats.py
def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    text = text.lower()
    char_count = {}
    for char in text:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

def sort_characters(char_count):
    sorted_list = []
    for char in char_count:
        sorted_list.append({"char": char, "num": char_count[char]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

def sort_on(item):
    return item["num"]

#Spam no corelation  HKEY_USERS HKEY_CURRENT_CONFIG
# DEFAULT (mounted on `HKEY_USERS\DEFAULT`)
#
## **Struktur data dari sistem file FAT:**

## Sistem file FAT mendukung struktur Data berikut:

### Cluster:

## Cluster adalah unit penyimpanan dasar dari sistem file FAT. Setiap file yang disimpan pada perangkat penyimpanan dapat dianggap sebagai sekelompok cluster yang berisi bit informasi.

### Direktori:
#Direktori berisi informasi tentang identifikasi file, seperti nama file, cluster awal, dan panjang nama file.

### Tabel Alokasi File:

#Tabel Alokasi File adalah daftar tertaut dari semua cluster. Ini berisi status cluster dan penunjuk ke cluster berikutnya dalam rantai.
#it should be added

