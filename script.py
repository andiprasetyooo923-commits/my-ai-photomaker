import google.generativeai as genai
import os

# Ambil API Key dari Secret GitHub (Lebih Aman)
api_key = os.getenv("AIzaSyBs_m8CVvIX8kqCuJ9jSKCfUq6dN4yz6LI")
genai.configure(api_key=api_key)

def run_workflow():
    # Membaca 10 prompt dari file
    if not os.path.exists("prompts.txt"):
        print("File prompts.txt tidak ditemukan!")
        return

    with open("prompts.txt", "r") as f:
        prompts = [line.strip() for line in f.readlines() if line.strip()]

    model = genai.GenerativeModel('imagen-3.0-generate-001')

    # Buat folder untuk hasil jika belum ada
    if not os.path.exists("results"):
        os.makedirs("results")

    for i, p in enumerate(prompts[:10]):
        print(f"Generating image {i+1}: {p}")
        try:
            response = model.generate_content(p)
            # Simpan hasil gambar (tergantung format return API)
            # Contoh: response.images[0].save(f"results/image_{i+1}.png")
        except Exception as e:
            print(f"Error pada prompt {i+1}: {e}")

if __name__ == "__main__":
    run_workflow()
    
