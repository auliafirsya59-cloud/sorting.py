import streamlit as st
import time

st.title("Visualisasi Sorting")

# 1. Kontrol UI input data dan algoritma
col1, col2 = st.columns(2)

algo = col1.selectbox(
    "Pilih algoritma",
    ["Bubble Sort", "Selection Sort", "Insertion Sort"]
)
user_input = col2.text_input(
    "Input data (pisahkan koma)",
    "85, 60, 92, 75, 88"
)

# 2. Keterangan algoritma dinamis
if algo == "Bubble Sort":
    st.info(
        "**Bubble Sort**: Membandingkan elemen yang bersebelahan dan menukarnya jika salah urutan. "
        "Elemen terbesar akan 'menggelembung' ke akhir daftar."
    )
elif algo == "Selection Sort":
    st.info(
        "**Selection Sort**: Mencari elemen terkecil dari bagian yang belum terurut, "
        "lalu menukarnya ke posisi paling depan."
    )
elif algo == "Insertion Sort":
    st.info(
        "**Insertion Sort**: Bekerja seperti mengurutkan kartu; "
        "menyisipkan elemen satu per satu ke posisi paling tepat di bagian yang sudah terurut"
    )

# 3. Keamanan Input (Parsing teks ke angka)
try:
    data = [int(x.strip()) for x in user_input.split(",") if x.strip()]
except ValueError:
    st.error("Gagal ! pastikan anda hanya memasukan angka.")
    st.stop()

# 4. tombol 4 area gambar grafika
chart = st.empty()
chart.bar_chart(data)

# 5. Area Gambar Grafik
if st.button("Mulai urutkan", type="primary"):

    n = len(data)

    if algo == "Bubble Sort":
        for i in range(n):
            for j in range(0, n - i - 1):
                if data[j] > data[j + 1]:
                    data[j], data[j + 1] = data[j + 1], data[j]
                    # tukar posisi
                    chart.bar_chart(data)
                    time.sleep(0.2)

    elif algo == "Selection Sort":
        for i in range(n):
            min_idx = i
            for j in range(i + 1, n):
                if data[j] < data[min_idx]:
                    min_idx = j
            data[i], data[min_idx] = data[min_idx], data[i]
            # tukar ke depan
            chart.bar_chart(data)
            time.sleep(0.2)

    elif algo == "Insertion Sort":
        for i in range(1, n):
            key = data[i]
            j = i - 1
            while j >= 0 and data[j] > key:
                data[j + 1] = data[j] 
                #geser ke kanan
                j -= 1
                chart.bar_chart(data)
                time.sleep(0.2)
            data[j + 1] = key

            chart.bar_chart(data)
            time.sleep(0.2)

    st.success(f"Sorting selesai! Hasil: {data}")
