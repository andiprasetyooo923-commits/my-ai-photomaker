import google.generativeai as genai
import os
from PIL import Image

api_key = os.getenv("AIzaSyBs_m8CVvIX8kqCuJ9jSKCfUq6dN4yz6LI")
genai.configure(api_key=api_key)

def run_workflow():
    output_folder = "finalplay"
    os.makedirs(output_folder, exist_ok=True)
    
    # Buat file dummy agar folder tidak dianggap kosong oleh Git
    with open(f"{output_folder}/info.txt", "w") as f:
        f.write("Folder hasil generate gambar.")

    if not os.path.exists("prompts.txt"):
        print("❌ File prompts.txt tidak ada!")
        return

    with open("prompts.txt", "r") as f:
        prompts = [line.strip() for line in f.readlines() if line.strip()]

    # Pastikan modelnya benar
    model = genai.GenerativeModel('imagen-3.0-generate-001')

    for i, p in enumerate(prompts[:10]):
        print(f"🔄 Mencoba prompt {i+1}: {p}")
        try:
            response = model.generate_content(p)
            
            # Cek jika ada gambar yang dihasilkan
            if hasattr(response, 'images') and response.images:
                filename = f"{output_folder}/gambar_{i+1}.png"
                response.images[0].save(filename)
                print(f"✅ Tersimpan: {filename}")
            else:
                print(f"⚠️ Google tidak memberikan gambar untuk prompt {i+1}. Mungkin kena filter sensor.")
        except Exception as e:
            print(f"❌ Error: {str(e)}")

if __name__ == "__main__":
    run_workflow()
            
