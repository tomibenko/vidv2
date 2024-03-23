import cv2 as cv
import numpy as np



def konvolucija(slika, jedro):
    # Dobimo dimenzije slike in jedra
    visina_slike, sirina_slike, _ = slika.shape
    velikost_jedra = jedro.shape[0]
    prekrivanje = velikost_jedra // 2
    
    # Nastavimo novo sliko, ki bo rezultat konvolucije
    nova_slika = np.zeros_like(slika)
    
    # Ustvarimo novo sliko z dodatnim robom
    slika_z_robom = np.pad(slika, ((prekrivanje, prekrivanje), (prekrivanje, prekrivanje), (0, 0)), mode='constant', constant_values=0)
    
    # Opravimo konvolucijo za vsak kanal posebej
    for kanal in range(3):
        for i in range(prekrivanje, visina_slike + prekrivanje):
            for j in range(prekrivanje, sirina_slike + prekrivanje):
                # Izračunamo konvolucijo za trenutno pikslo in kanal
                rezultat = 0
                for m in range(-prekrivanje, prekrivanje + 1):
                    for n in range(-prekrivanje, prekrivanje + 1):
                        # Izračunamo konvolucijski element
                        rezultat += slika_z_robom[i + m, j + n, kanal] * jedro[m + prekrivanje, n + prekrivanje]
                # Shrani rezultat v novo sliko
                nova_slika[i - prekrivanje, j - prekrivanje, kanal] = rezultat
    
    return nova_slika
    

def filtriraj_z_gaussovim_jedrom(slika,sigma):
      # Izračun velikosti jedra
    velikost_jedra = int((2 * sigma) * 2 + 1)
    
    # Izračun posameznih vrednosti znotraj jedra
    k = velikost_jedra // 2 - 0.5
    jedro = np.zeros((velikost_jedra, velikost_jedra))
    for i in range(velikost_jedra):
        for j in range(velikost_jedra):
            H = 1 / (2 * np.pi * sigma ** 2) * np.exp(-((i - k) ** 2 + (j - k) ** 2) / (2 * sigma ** 2))
            jedro[i, j] = H
    
    # Normalizacija jedra
    jedro /= np.sum(jedro)
    
    # Uporaba konvolucije za filtriranje slike
    filtrirana_slika = konvolucija(slika, jedro)
    
    return filtrirana_slika

def filtriraj_sobel_horizontalno(slika):
    # Definiramo jedro za Sobel filter v horizontalni smeri
    jedro_horizontalno = np.array([[-1, -2, -1],
                                   [0, 0, 0],
                                   [1, 2, 1]])
    
    # Uporabimo konvolucijo za zaznavanje robov v horizontalni smeri
    robovi_horizontalno = konvolucija(slika, jedro_horizontalno)
    
    return robovi_horizontalno

def filtriraj_sobel_smer(slika):
    # Definiramo jedro za Sobel filter v vertikalni smeri
    jedro_vertikalno = np.array([[-1, 0, 1],
                                 [-2, 0, 2],
                                 [-1, 0, 1]])
    
    # Uporabimo konvolucijo za zaznavanje robov v vertikalni smeri
    robovi_vertikalno = konvolucija(slika, jedro_vertikalno)
    
    return robovi_vertikalno

def filtriraj_sobel_horizontalno_in_smer(slika):
    # Filtriramo sliko z Sobel filtrom v horizontalni smeri
    robovi_horizontalno = filtriraj_sobel_horizontalno(slika)
    
    # Filtriramo sliko z Sobel filtrom v vertikalni smeri
    robovi_vertikalno = filtriraj_sobel_smer(slika)
    
    # Izračunamo gradient magnitude
    gradient_magnitude = np.sqrt(robovi_horizontalno**2 + robovi_vertikalno**2)
    
    # Najdemo močne robove (gradient > 100)
    močni_robovi_indeksi = np.where(gradient_magnitude > 13)
    
    # Spremenimo barvo močnih robov na rdečo
    filtrirana_slika = slika.copy()
    for y, x in zip(močni_robovi_indeksi[0], močni_robovi_indeksi[1]):
        filtrirana_slika[y, x] = [0, 0, 255]  # Rdeča barva
    
    return filtrirana_slika
  
if __name__ == '__main__':    
    jedro = np.array([  [1, 2, 1],
                        [2, 4, 2],
                        [1, 2, 1]])
    slika = cv.imread('lenna.png')
    
    slike_nov=filtriraj_sobel_horizontalno_in_smer(slika)
    #cv.imshow("neke",slike_nov)
    
    cv.imshow("neke",slike_nov)
    cv.waitKey(0)
    
        

    print("neke")
   
    pass