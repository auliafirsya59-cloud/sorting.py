import streamlit as st 
import time

st.title("visualisasi sorting")

#1. Kontrol UI imput data dan algoritma
col1, col2 = st.colums(2)
algo = col1.selection ("Pilih algoriitma", ["bubble sort", "selection sort", "insertion sort"])
user_input = col2.text_input("input data (pisahkan koma)", "85, 60, 92, 75, 88")

#2. keterangan algoritma
if algo == "bubble sort.":
    st.info(" **bubble sort**:, membandingkan elemen bersebelahan dan menukarnya jika salah urutan. Elemen terbesar 'menggelembung' ke akhir.")
elif algo == "selection sort":
    st.info(" **selection sort**: memilih elemen terkecil dari bagian yang belum terurut, lalu menukarnya ke posisi paling depan.")
elif algo == "insertion sort":
    st.info("**insertion sort**: bekerja seperti mengurutkan kartu: menyisipkan elemen satu per satu ke posisi yang tepat di bagian yang sudah terurut.")
    
    
#3. keamanan input (porsing teks ke angka)    
try:
    data = [int(x.strip()) for x in user_input.split(",")if x.strip()]
except ValueError:
    st.eror("gagal! pastikan anda hanya memasukaan angka.")
    st.stop()
    
#4. tombol 4 area gambar grafik
chart = st.empty()
chart.bar_chart(data)

#5. tombol dan logika sorting utama
if st.button("mulai urutan", type = "primary"):
    n = len(data)

    
    if algo == "bubble sort.":
        for i in range(n):
            for j in range(0, n - i - 1):
                if data[j] > data[j + 1]:
                    data[j], data[j + 1] = data[j + 1], data[j]
                    #tukar posisi
                    chart.bar_chart(data)
                    time.slepp(0.2)
                
    elif algo == "selection sort":
        for i in range(n):
            min_idx = i
            for j in range(i + 1, n):
                if data[j] < data[min_idx]:
                    min_idx = j
            data[i], data[min_idx] = data[min_idx], data[i]
            #tukar ke depan
            chart.bar_chart(data)
            time.sleep(0.2)
            
    elif algo == "insertion sort":
        for i in range(1, n):
            key = data[i]
            j = i - 1
            while j >= 0 and data[j] > key:
                data[j + i] = data[j] #geser ke kanan
                j -= 1
                chart.bar_chart(data)
                time.sleep(0.2)
            data[j + 1] = key
            chart.bar_chart(data)
            time.sleep(0.2)
    
    st.success(f"sorting selesai! hasil: {data}")
            
    
