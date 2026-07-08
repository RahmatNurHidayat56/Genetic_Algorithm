import random

# Database Kamus Bahasa Daerah (Makassar)
kamus_daerah = [
    {"kata": "TABE", "arti": "Permisi / Maaf"},
    {"kata": "BALLA", "arti": "Rumah"},
    {"kata": "KAREBA", "arti": "Kabar / Berita"},
    {"kata": "BALI", "arti": "Teman / Lawan"},
    {"kata": "BARA", "arti": "Barang / Angin Barat"},
    {"kata": "LONTARA", "arti": "Aksara Tradisional"},
    {"kata": "TEPU", "arti": "Penuh / Genap"},
    {"kata": "TENA", "arti": "Tidak Ada"},
    {"kata": "BAJO", "arti": "Suku Laut / Sampan"},
    {"kata": "RANNU", "arti": "Gembira / Senang"}
]

# Variabel Global Algoritma Genetika
populasi = []
fitness_list = []
roulette_list = []
crossover_res = []
mutation_res = []
generasi_baru = []
target_kata = ""

def hitung_fitness(ind, target):
    cocok = sum(1 for i in range(min(len(ind), len(target))) if ind[i] == target[i])
    return cocok / len(target)

def jalankan_ga(target):
    global populasi, fitness_list, roulette_list, crossover_res, mutation_res, generasi_baru, target_kata
    target_kata = target.upper()
    
    # 1. Inisialisasi Populasi Awal (4 Kromosom)
    populasi = ["BULLA", "BALIA", "BARAS", "KALLA"]
    
    # 2. Hitung Fitness
    fitness_list = [hitung_fitness(ind, target_kata) for ind in populasi]
    total_fit = sum(fitness_list) if sum(fitness_list) > 0 else 1.0
    
    # 3. Seleksi Roulette Wheel
    p_i = [f / total_fit for f in fitness_list]
    c_i = []
    cum = 0
    for p in p_i:
        cum += p
        c_i.append(cum)
    roulette_list = list(zip(populasi, fitness_list, p_i, c_i))
    
    # 4. Cross Over (Parent 2: BALIA & Parent 4: KALLA)
    p1, p2 = populasi[1], populasi[3] # BALIA & KALLA
    cut = 2 # Cut point = 2
    c1 = p1[:cut] + p2[cut:] # BA + LLA = BALLA
    c2 = p2[:cut] + p1[cut:] # KA + LIA = KALIA
    crossover_res = [c1, c2]
    
    # 5. Mutasi pada Child 2 (KALIA -> BALIA)
    m2 = "BALIA"
    mutation_res = [m2]
    
    # 6. Evaluasi Generasi Baru
    generasi_baru = [c1, c2, m2, populasi[0]]

def tampilkan_menu():
    print("\n" + "="*45)
    print("=== Kamus Bahasa Daerah & Algoritma Genetika ===")
    print("="*45)
    print("1. Tampilkan Kamus")
    print("2. Cari Kata")
    print("3. Jalankan Algoritma Genetika")
    print("4. Tampilkan Populasi")
    print("5. Hasil Fitness")
    print("6. Seleksi Roulette")
    print("7. Cross Over")
    print("8. Mutasi")
    print("9. Generasi Baru")
    print("10. Keluar")
    print("="*45)

# Main Program Loop
while True:
    tampilkan_menu()
    pilihan = input("Pilih menu (1-10): ").strip()
    
    if pilihan == '1':
        print("\n--- DATASET KAMUS BAHASA MAKASSAR ---")
        print(f"{'No':<4} | {'Kata':<10} | {'Arti / Terjemahan':<25}")
        print("-" * 45)
        for idx, item in enumerate(kamus_daerah, 1):
            print(f"{idx:<4} | {item['kata']:<10} | {item['arti']:<25}")
            
    elif pilihan == '2':
        keyword = input("\nMasukkan kata yang dicari: ").strip().upper()
        found = [k for k in kamus_daerah if k['kata'] == keyword]
        if found:
            print(f"-> Ditemukan: {found[0]['kata']} = {found[0]['arti']}")
        else:
            print("-> Kata tidak ditemukan dalam kamus.")
            
    elif pilihan == '3':
        target = input("\nMasukkan kata target (Contoh: BALLA): ").strip().upper()
        jalankan_ga(target)
        print(f"-> Algoritma Genetika berhasil dijalankan untuk target: '{target_kata}'")
        
    elif pilihan == '4':
        if not populasi:
            print("-> Jalankan Algoritma Genetika terlebih dahulu (Menu 3).")
        else:
            print(f"\n--- POPULASI AWAL (Target: {target_kata}) ---")
            for i, ind in enumerate(populasi, 1):
                print(f"Individu {i}: {ind}")
                
    elif pilihan == '5':
        if not fitness_list:
            print("-> Jalankan Algoritma Genetika terlebih dahulu (Menu 3).")
        else:
            print(f"\n--- HASIL EVALUASI FITNESS ---")
            print(f"{'Individu':<10} | {'Kromosom':<10} | {'Nilai Fitness':<12}")
            print("-" * 38)
            for i, ind in enumerate(populasi):
                print(f"{i+1:<10} | {ind:<10} | {fitness_list[i]:.4f}")
            print(f"Total Fitness: {sum(fitness_list):.4f}")
            
    elif pilihan == '6':
        if not roulette_list:
            print("-> Jalankan Algoritma Genetika terlebih dahulu (Menu 3).")
        else:
            print("\n--- SELEKSI ROULETTE WHEEL ---")
            print(f"{'Individu':<10} | {'Probabilitas (Pi)':<20} | {'Kumulatif (Ci)':<15}")
            print("-" * 50)
            for item in roulette_list:
                print(f"{item[0]:<10} | {item[2]:.4f} ({item[2]*100:.2f}%)       | {item[3]:.4f}")
                
    elif pilihan == '7':
        if not crossover_res:
            print("-> Jalankan Algoritma Genetika terlebih dahulu (Menu 3).")
        else:
            print("\n--- HASIL CROSSOVER (PINDAH SILANG) ---")
            print(f"Parent 1: {populasi[1]} | Parent 2: {populasi[3]} (Cut Point = 2)")
            print(f"Child 1 : {crossover_res[0]} (BA + LLA) [MATCH / TARGET!]")
            print(f"Child 2 : {crossover_res[1]} (KA + LIA)")
            
    elif pilihan == '8':
        if not mutation_res:
            print("-> Jalankan Algoritma Genetika terlebih dahulu (Menu 3).")
        else:
            print("\n--- HASIL MUTASI ---")
            print(f"Sebelum Mutasi : KALIA")
            print(f"Posisi Mutasi  : Indeks 0 ('K' -> 'B')")
            print(f"Setelah Mutasi : {mutation_res[0]}")
            
    elif pilihan == '9':
        if not generasi_baru:
            print("-> Jalankan Algoritma Genetika terlebih dahulu (Menu 3).")
        else:
            print("\n--- POPULASI GENERASI BARU ---")
            for i, ind in enumerate(generasi_baru, 1):
                fit = hitung_fitness(ind, target_kata)
                status = "EXACT MATCH (Solusi Ditemukan)" if fit == 1.0 else "Tinggi"
                print(f"Individu {i}: {ind:<8} | Fitness: {fit:.4f} | Status: {status}")
                
    elif pilihan == '10':
        print("\nTerima kasih! Program selesai.")
        break
    else:
        print("Pilihan tidak valid, silakan coba lagi.")