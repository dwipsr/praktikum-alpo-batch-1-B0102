# Program Pengolahan Data Nilai Mahasiswa Sederhana

def hitung_rata_rata(daftar_nilai):
    """Fungsi untuk menghitung rata-rata dari list nilai"""
    if not daftar_nilai:
        return 0
    return sum(daftar_nilai) / len(daftar_nilai)

def tentukan_grade(rata):
    """Menentukan huruf mutu berdasarkan nilai rata-rata"""
    if rata >= 85:
        return "A (Sangat Baik)"
    elif rata >= 75:
        return "B (Baik)"
    elif rata >= 65:
        return "C (Cukup)"
    else:
        return "D (Kurang)"

# Data mahasiswa menggunakan Dictionary dan List
mahasiswa = {
    "nama": "Ahmad Rian",
    "nim": "23010199",
    "mata_kuliah": {
        "Algoritma & Pemrograman": 85.5,
        "Basis Data": 78.0,
        "Pemrograman Web": 90.2
    }
}

print("=" * 45)
print(f"  LAPORAN AKADEMIK: {mahasiswa['nama'].upper()}")
print(f"  NIM: {mahasiswa['nim']}")
print("=" * 45)

print("\nNilai Per Mata Kuliah:")
kumpulan_nilai = []
for matkul, nilai in mahasiswa["mata_kuliah"].items():
    print(f"- {matkul}: {nilai}")
    kumpulan_nilai.append(nilai)

# Kalkulasi akhir
rata_rata_akhir = hitung_rata_rata(kumpulan_nilai)
status_lulus = rata_rata_akhir >= 75.0

print("-" * 45)
print(f"Rata-rata Nilai : {rata_rata_akhir:.2f}")
print(f"Grade Mutu      : {tentukan_grade(rata_rata_akhir)}")
print(f"Status Kelulusan: {'LULUS' if status_lulus else 'TIDAK LULUS'}")
print("=" * 45)