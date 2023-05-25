import numpy as np

def apply_inverse_wavelet(image, wavelet_filter):
    rows, cols = image.shape
    reconstructed_image = np.zeros((rows, cols))
    
    # Iterasi per kolom citra
    for j in range(cols):
        # Operasi konvolusi pada kolom citra dengan filter wavelet
        reconstructed_image[:, j] = np.convolve(image[:, j], wavelet_filter, mode='same')
    
    # Iterasi per baris citra
    for i in range(rows):
        # Operasi konvolusi pada baris citra dengan filter wavelet
        reconstructed_image[i, :] = np.convolve(reconstructed_image[i, :], wavelet_filter, mode='same')
    
    return reconstructed_image

def reconstruct_wavelet(decomposed_image, wavelet_filter):
    reconstructed_image = decomposed_image[-1].copy()
    levels = len(decomposed_image) - 1
    
    # Iterasi dari level terakhir hingga level pertama
    for level in range(levels, 0, -1):
        # Perbesar citra level berikutnya menjadi ukuran citra level sekarang
        next_level_image = np.zeros_like(reconstructed_image)
        next_level_image[:decomposed_image[level-1].shape[0], :decomposed_image[level-1].shape[1]] = decomposed_image[level]
        
        # Rekonstruksi citra level sekarang dengan citra level berikutnya
        reconstructed_image = apply_inverse_wavelet(reconstructed_image, wavelet_filter) + next_level_image
    
    return reconstructed_image

# Contoh penggunaan
decomposed_image = [np.array([[1.5, 3.5],
                              [9.5, 11.5]]),
                    np.array([[2.5]])]

wavelet_filter = np.array([0.5, 0.5])  # Filter Haar untuk wavelet sederhana

reconstructed = reconstruct_wavelet(decomposed_image, wavelet_filter)

# Tampilkan citra hasil rekonstruksi
print(reconstructed)
