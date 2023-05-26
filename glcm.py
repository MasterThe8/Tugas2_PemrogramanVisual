import numpy as np

def calculate_glcm(image, d, theta):
    # Mengambil dimensi gambar
    rows, cols = image.shape
    
    # Menginisialisasi matriks GLCM
    glcm = np.zeros((256, 256), dtype=np.uint8)
    
    # Menormalisasi gambar menjadi 256 level keabuan
    normalized_image = np.round(image / 255.0 * 255)
    
    # Mengiterasi setiap piksel dalam gambar
    for i in range(rows):
        for j in range(cols):
            # Menentukan piksel referensi
            ref_pixel = normalized_image[i, j]
            
            # Menentukan piksel tetangga berdasarkan jarak dan sudut theta
            neighbor_pixel = get_neighbor_pixel(normalized_image, i, j, d, theta)
            
            # Menambahkan entri ke GLCM
            glcm[ref_pixel, neighbor_pixel] += 1
    
    # Menormalkan GLCM
    glcm /= np.sum(glcm)
    
    return glcm

def get_neighbor_pixel(image, i, j, d, theta):
    # Mengambil dimensi gambar
    rows, cols = image.shape
    
    # Menentukan offset piksel berdasarkan sudut theta
    if theta == 0:
        offset = (0, d)
    elif theta == 45:
        offset = (-d, d)
    elif theta == 90:
        offset = (-d, 0)
    elif theta == 135:
        offset = (-d, -d)
    
    # Menghitung koordinat piksel tetangga
    neighbor_i = max(0, min(i + offset[0], rows - 1))
    neighbor_j = max(0, min(j + offset[1], cols - 1))
    
    return image[neighbor_i, neighbor_j]
