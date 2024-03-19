import cv2 as cv
import numpy as np


def konvolucija(slika, jedro):
        # Določite dimenzije vhodne slike in jedra
    if len(slika.shape) == 3:  # Če je slika večkanalna (npr. RGB), vzamemo samo prvi kanal
        image_height, image_width, num_channels = slika.shape
    else:
        image_height, image_width = slika.shape
        num_channels = 1
    
    # Določite dimenzije jedra
    kernel_height, kernel_width = jedro.shape
    
    # Nastavite padding, da se izognete izgubi robov pri konvoluciji
    padding_height = kernel_height // 2
    padding_width = kernel_width // 2
    
    # Ustvarite izhodno sliko
    output = np.zeros_like(slika)
    
    # Izvedite konvolucijo
    for i in range(padding_height, image_height - padding_height):
        for j in range(padding_width, image_width - padding_width):
            # Izračunajte vrednost konvolucije za trenutno pozicijo
            sum = 0
            for m in range(kernel_height):
                for n in range(kernel_width):
                    sum += jedro[m, n] * slika[i - padding_height + m, j - padding_width + n]
            output[i, j] = sum
    
    return output
    

def filtriraj_z_gaussovim_jedrom(slika,sigma):
    '''Filtrira sliko z Gaussovim jedrom..'''
    pass

def filtriraj_sobel_smer(slika):
    '''Filtrira sliko z Sobelovim jedrom in označi gradiente v orignalni sliki glede na ustrezen pogoj.'''
    pass
  
if __name__ == '__main__':    
    jedro = np.array([[1, 1, 1],
                     [1, 1, 1],
                     [1, 1, 1]])
    slika = cv.imread('lenna.png')
    slike=konvolucija(slika,jedro)
    cv.imshow("neke",slika)
    cv.waitKey(0)
   
    pass