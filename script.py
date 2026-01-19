import google.generativeai as genai
import os
import time

# 1. Ambil API Key dari Environment GitHub
api_key = os.getenv("AIzaSyBs_m8CVvIX8kqCuJ9jSKCfUq6dN4yz6LI")

if not api_key:
    print("❌ ERROR: API Key tidak ditemukan di environment secret!")
else:
    genai.configure(api_key=api_key)

def run_generator():
    output_folder = "finalplay"
    
    # 2. Pastikan folder output ada
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
        print(f"📁 Folder '{output_folder}' berhasil dibuat.")

    # 3. Baca 10 Prompt dari file
    if not os.path.exists("prompts.txt"):
        print("❌ ERROR: File prompts.txt tidak ditemukan!")
        return

    with open("prompts.txt", "r") as f:
        # Mengambil 10 baris pertama yang tidak kosong
        prompts = [line.strip() for line in f.readlines() if line.strip()][:10]

    if not prompts:
        print("❌ ERROR: prompts.txt kosong!")
        return

    # 4. Inisialisasi Model (Banana/Imagen)
    # Gunakan model imagen-3.0-generate-001 (standar terbaru)
    try:
        model = genai.GenerativeModel('imagen-3.0-generate-001')
    except Exception as e:
        print(f"❌ Gagal memuat model: {e}")
        return

    print(f"🚀 Memulai proses generate {len(prompts)} gambar...\n")

    for i, p in enumerate(prompts):
        print(f"🔄 [{i+1}/{len(prompts)}] Memproses: {p}")
        
        try:
            # Proses Generate
            response = model.generate_content(p)
            
            # Cek apakah response sukses dan memiliki gambar
            if hasattr(response, 'images') and response.images:
                filename = f"{output_folder}/gambar_{i+1}.png"
                # Simpan gambar menggunakan library bawaan response
                response.images[0].save(filename)
                print(f"   ✅ BERHASIL: {filename}")
            else:
                # Jika diblokir sensor Google
                print(f"   ⚠️ GAGAL: Tidak ada gambar yang dihasilkan. (Cek Safety Filter/Prompt)")
                if hasattr(response, 'prompt_feedback'):
                    print(f"   📝 Feedback: {response.prompt_feedback}")
            
            # Jeda singkat agar tidak terkena Rate Limit API
            time.sleep(2)
            
        except Exception as e:
            print(f"   ❌ ERROR pada prompt {i+1}: {str(e)}")

    print("\n✨ Semua proses selesai!")

if __name__ == "__main__":
    run_generator()
        
