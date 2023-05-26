import numpy as np

def custom_round(number):
    decimal = number - int(number)
    if decimal >= 0.5:
        return int(number) + 1
    else:
        return int(number)
    
def custom_sum(arr):
    result = 0
    for element in arr:
        result += element
    return result


def calculate_glcm(image, d, theta):
    # Mengambil dimensi gambar
    rows, cols = image.shape
    
    # Menginisialisasi matriks GLCM
    glcm = np.zeros((256, 256), dtype=np.uint8)
    
    # Menormalisasi gambar menjadi 256 level keabuan [custom_round]
    # normalized_image = np.round(image / 255.0 * 255)
    
    # Mengiterasi setiap piksel dalam gambar
    for i in range(rows):
        for j in range(cols):
            # Menentukan piksel referensi
            ref_pixel = normalized_image[i, j]
            
            # Menentukan piksel tetangga berdasarkan jarak dan sudut theta
            neighbor_pixel = get_neighbor_pixel(normalized_image, i, j, d, theta)
            
            # Menambahkan entri ke GLCM
            glcm[ref_pixel, neighbor_pixel] += 1
    
    # Menormalkan GLCM [custom_sum]
    # glcm /= np.sum(glcm)
    
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
    neighbor_i = i + offset[0]
    neighbor_j = j + offset[1]
    
    # Memastikan koordinat piksel tetangga berada dalam rentang gambar
    neighbor_i = 0 if neighbor_i < 0 else rows - 1 if neighbor_i >= rows else neighbor_i
    neighbor_j = 0 if neighbor_j < 0 else cols - 1 if neighbor_j >= cols else neighbor_j
    
    return image[neighbor_i, neighbor_j]

