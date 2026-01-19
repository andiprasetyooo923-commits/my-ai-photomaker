import streamlit as st
import google.generativeai as genai

# --- KONFIGURASI API ---
# Tempelkan API Key yang baru saja Anda dapatkan di sini
API_KEY = "AIzaSyBs_m8CVvIX8kqCuJ9jSKCfUq6dN4yz6LI"
genai.configure(api_key=API_KEY)

# --- TAMPILAN APLIKASI ---
st.set_page_config(page_title="10-Prompt Image Generator", layout="wide")

st.title("📸 Mega Image Generator (10 Prompts)")
st.write("Masukkan 10 deskripsi gambar di bawah ini untuk dibuat secara bersamaan.")

# Membuat form input otomatis untuk 10 prompt
prompts = []
col_input1, col_input2 = st.columns(2)

for i in range(1, 11):
    # Membagi input ke dua kolom agar tidak terlalu panjang ke bawah
    target_col = col_input1 if i <= 5 else col_input2
    with target_col:
        p = st.text_input(f"Prompt {i}:", placeholder=f"Deskripsi gambar ke-{i}...")
        prompts.append(p)

st.divider()

# Tombol Eksekusi
if st.button("Generate 10 Gambar Sekarang", type="primary"):
    # Cek apakah semua prompt sudah diisi
    if all(prompts):
        st.write("### 🚀 Hasil Generasi Gambar:")
        
        # Membuat grid tampilan hasil (2 gambar per baris)
        cols = st.columns(2)
        
        for index, p_text in enumerate(prompts):
            # Menentukan kolom mana (0 atau 1)
            col_idx = index % 2
            with cols[col_idx]:
                with st.spinner(f"Memproses Gambar {index+1}..."):
                    try:
                        # Memanggil model Image (Banana/Imagen)
                        model = genai.GenerativeModel('imagen-3.0-generate-001')
                        # Catatan: Pastikan API Key Anda memiliki akses ke model Imagen
                        response = model.generate_content(p_text)
                        
                        # Menampilkan hasil
                        st.subheader(f"Gambar {index+1}")
                        st.info(f"Prompt: {p_text}")
                        # st.image(response.images[0]) # Mengasumsikan response mengembalikan objek image
                    except Exception as e:
                        st.error(f"Gagal memproses gambar {index+1}: {e}")
    else:
        st.warning("Harap isi semua (10) kolom prompt sebelum menekan tombol!")

# --- FOOTER ---
st.caption("Aplikasi Multi-Prompt Power by Google Gemini Nano")
