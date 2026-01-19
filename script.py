import google.generativeai as genai
import os
from PIL import Image

# Konfigurasi API
api_key = os.getenv("AIzaSyBs_m8CVvIX8kqCuJ9jSKCfUq6dN4yz6LI")
genai.configure(api_key=api_key)

def run_workflow():
    if not os.path.exists("prompts.txt"):
        print("❌ File prompts.txt tidak ditemukan!")
        return

    output_folder = "finalplay"
    os.makedirs(output_folder, exist_ok=True)

    with open("prompts.txt", "r") as f:
        prompts = [line.strip() for line in f.readlines() if line.strip()]

    # Menggunakan model Imagen 3 (Pastikan API Key Anda punya akses)
    model = genai.GenerativeModel('imagen-3.0-generate-001')

    for i, p in enumerate(prompts[:10]):
        print(f"🔄 Memproses Gambar {i+1}: {p}")
        try:
            response = model.generate_content(p)
            
            # Cek apakah response mengandung gambar
            if hasattr(response, 'images') and response.images:
                for j, image_data in enumerate(response.images):
                    filename = f"{output_folder}/gambar_{i+1}.png"
                    image_data.save(filename)
                    print(f"✅ Berhasil: {filename}")
            else:
                # Jika tidak ada gambar, cetak alasan (mungkin diblokir filter keamanan)
                print(f"⚠️ Prompt {i+1} tidak menghasilkan gambar. Cek feedback: {response.prompt_feedback}")
                
        except Exception as e:
            print(f"❌ Error pada prompt {i+1}: {str(e)}")

if __name__ == "__main__":
    run_workflow()
            
                
