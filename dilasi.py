import cv2
import numpy as np

def dilasi(citra, kernel):
    baris, kolom = citra.shape[:2]
    kernel_baris, kernel_kolom = kernel.shape[:2]
    
    # Membuat gambar hasil dengan ukuran yang sama seperti citra
    hasil = np.zeros(citra.shape, dtype=np.uint8)
    
    # Melakukan operasi dilasi
    for i in range(baris):
        for j in range(kolom):
            if citra[i, j] > 0:  # Jika ada piksel putih (nilai > 0)
                for m in range(kernel_baris):
                    for n in range(kernel_kolom):
                        # Menggabungkan citra dengan kernel
                        if kernel[m, n] > 0:
                            if i+m-(kernel_baris//2) >= 0 and i+m-(kernel_baris//2) < baris and j+n-(kernel_kolom//2) >= 0 and j+n-(kernel_kolom//2) < kolom:
                                hasil[i+m-(kernel_baris//2), j+n-(kernel_kolom//2)] = 255
    
    return hasil

# Membaca citra
citra = cv2.imread('citra.png', 0)  # Ubah 0 ke 1 untuk membaca citra berwarna

# Membuat kernel
kernel = np.array([[0, 1, 0],
                   [1, 1, 1],
                   [0, 1, 0]], dtype=np.uint8)

# Melakukan operasi dilasi
hasil_dilasi = dilasi(citra, kernel)

# Menampilkan citra asli dan hasil dilasi
cv2.imshow('Citra Asli', citra)
cv2.imshow('Hasil Dilasi', hasil_dilasi)
cv2.waitKey(0)
cv2.destroyAllWindows()
