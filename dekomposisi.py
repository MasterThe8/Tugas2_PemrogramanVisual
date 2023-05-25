import numpy as np

def apply_wavelet(image, wavelet_filter):
    rows, cols = image.shape
    transformed_image = np.zeros((rows, cols))
    
    # Iterasi per baris citra
    for i in range(rows):
        # Operasi konvolusi pada baris citra dengan filter wavelet
        transformed_image[i, :] = np.convolve(image[i, :], wavelet_filter, mode='same')
    
    # Iterasi per kolom citra
    for j in range(cols):
        # Operasi konvolusi pada kolom citra dengan filter wavelet
        transformed_image[:, j] = np.convolve(transformed_image[:, j], wavelet_filter, mode='same')
    
    return transformed_image

def decompose_wavelet(image, levels):
    wavelet_filter = np.array([0.5, 0.5])  # Filter Haar untuk wavelet sederhana
    
    # Inisialisasi citra hasil dekomposisi
    decomposed_image = [image]
    
    # Iterasi sesuai jumlah level
    for _ in range(levels):
        # Aplikasikan wavelet transform pada citra level sebelumnya
        transformed_image = apply_wavelet(decomposed_image[-1], wavelet_filter)
        
        # Ambil bagian LL (Low-Low) hasil transform sebagai citra level berikutnya
        next_level_image = transformed_image[:image.shape[0]//2, :image.shape[1]//2]
        
        # Simpan citra level berikutnya dalam hasil dekomposisi
        decomposed_image.append(next_level_image)
    
    return decomposed_image

# Contoh penggunaan
image = np.array([[1, 2, 3, 4],
                  [5, 6, 7, 8],
                  [9, 10, 11, 12],
                  [13, 14, 15, 16]])

decomposed = decompose_wavelet(image, levels=2)

# Tampilkan hasil dekomposisi
for level, image_level in enumerate(decomposed):
    print(f"Level {level}:")
    print(image_level)
    print()
