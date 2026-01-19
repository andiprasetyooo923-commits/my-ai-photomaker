import google.generativeai as genai
import os

# Konfigurasi API
api_key = os.getenv("AIzaSyBs_m8CVvIX8kqCuJ9jSKCfUq6dN4yz6LI")
genai.configure(api_key=api_key)

def run_workflow():
    if not os.path.exists("prompts.txt"):
        print("File prompts.txt tidak ditemukan!")
        return

    # Folder tujuan sesuai permintaan Anda
    output_folder = "finalplay"
    os.makedirs(output_folder, exist_ok=True)

    with open("prompts.txt", "r") as f:
        prompts = [line.strip() for line in f.readlines() if line.strip()]

    model = genai.GenerativeModel('imagen-3.0-generate-001')

    for i, p in enumerate(prompts[:10]):
        print(f"Generating image {i+1} untuk prompt: {p}")
        try:
            response = model.generate_content(p)
            
            # Mengambil bit data gambar dari response
            for j, image_data in enumerate(response.images):
                filename = f"{output_folder}/gambar_{i+1}.png"
                image_data.save(filename)
                print(f"Berhasil menyimpan: {filename}")
                
        except Exception as e:
            print(f"Gagal pada prompt {i+1}: {e}")

if __name__ == "__main__":
    run_workflow()
                
