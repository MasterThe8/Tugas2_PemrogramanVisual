import numpy as np

def opening_manual(citra, kernel):
    erosi = erosi_manual(citra, kernel)
    hasil_opening = dilasi_manual(erosi, kernel)
    return hasil_opening

def erosi_manual(citra, kernel):
    baris, kolom = citra.shape[:2]
    kernel_baris, kernel_kolom = kernel.shape[:2]

    hasil = np.zeros((baris, kolom), dtype=np.uint8)

    for i in range(baris):
        for j in range(kolom):
            erosi = True
            for m in range(kernel_baris):
                for n in range(kernel_kolom):
                    if kernel[m, n] > 0:
                        if i + m - (kernel_baris // 2) >= 0 and i + m - (kernel_baris // 2) < baris and j + n - (
                                kernel_kolom // 2) >= 0 and j + n - (kernel_kolom // 2) < kolom:
                            if citra[i + m - (kernel_baris // 2), j + n - (kernel_kolom // 2)] == 0:
                                erosi = False
                                break
                if not erosi:
                    break
            if erosi:
                hasil[i, j] = 255

    return hasil

def dilasi_manual(citra, kernel):
    baris, kolom = citra.shape[:2]
    kernel_baris, kernel_kolom = kernel.shape[:2]

    hasil = np.zeros((baris, kolom), dtype=np.uint8)

    for i in range(baris):
        for j in range(kolom):
            if citra[i, j] > 0:
                for m in range(kernel_baris):
                    for n in range(kernel_kolom):
                        if kernel[m, n] > 0:
                            if i + m - (kernel_baris // 2) >= 0 and i + m - (kernel_baris // 2) < baris and j + n - (
                                    kernel_kolom // 2) >= 0 and j + n - (kernel_kolom // 2) < kolom:
                                hasil[i + m - (kernel_baris // 2), j + n - (kernel_kolom // 2)] = 255

    return hasil

# Contoh penggunaan
citra = np.array([[0, 0, 0, 0, 0],
                  [0, 255, 255, 0, 0],
                  [0, 0, 255, 0, 0],
                  [0, 0, 0, 0, 0]], dtype=np.uint8)

kernel = np.array([[0, 1, 0],
                   [1, 1, 1],
                   [0, 1, 0]], dtype=np.uint8)

hasil_opening = opening_manual(citra, kernel)

print("Citra Asli:")
print(citra)
print("\nHasil Opening:")
print(hasil_opening)
