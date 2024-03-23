import cv2 as cv
import numpy as np



def konvolucija(slika, jedro):
    # Dobimo dimenzije slike in jedra
    visina_slike, sirina_slike, kanali = slika.shape
    visina_jedra, sirina_jedra = jedro.shape
    
    # Izračunamo velikost območja prekrivanja glede na velikost jedra
    prekrivanje_vrstice = (visina_jedra - 1) // 2
    prekrivanje_stolpci = (sirina_jedra - 1) // 2
    
    # Nastavimo novo sliko, ki bo rezultat konvolucije
    nova_slika = np.zeros_like(slika)
    
    # Ustvarimo novo sliko z dodatnim robom
    slika_z_robom = np.pad(slika, ((prekrivanje_vrstice, prekrivanje_vrstice), (prekrivanje_stolpci, prekrivanje_stolpci), (0, 0)), mode='constant', constant_values=0)
    
    # Opravimo konvolucijo za vsak kanal posebej
    for kanal in range(kanali):
        for i in range(prekrivanje_vrstice, visina_slike + prekrivanje_vrstice):
            for j in range(prekrivanje_stolpci, sirina_slike + prekrivanje_stolpci):
                # Izračunamo konvolucijo za trenutno pikslo in kanal
                rezultat = 0
                for m in range(-prekrivanje_vrstice, prekrivanje_vrstice + 1):
                    for n in range(-prekrivanje_stolpci, prekrivanje_stolpci + 1):
                        # Izračunamo konvolucijski element
                        rezultat += slika_z_robom[i + m, j + n, kanal] * jedro[prekrivanje_vrstice + m, prekrivanje_stolpci + n]
                # Shrani rezultat v novo sliko
                nova_slika[i - prekrivanje_vrstice, j - prekrivanje_stolpci, kanal] = rezultat / np.sum(jedro)  # Normalizacija rezultata
                
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

def filtriraj_sobel_smer(slika):
    '''Filtrira sliko z Sobelovim jedrom in označi gradiente v orignalni sliki glede na ustrezen pogoj.'''
    pass
  
if __name__ == '__main__':    
    jedro = np.array([  [1, 2, 1],
                        [2, 4, 2],
                        [1, 2, 1]])
    slika = cv.imread('lenna.png')
    
    slike_nov=filtriraj_z_gaussovim_jedrom(slika,3)
    #cv.imshow("neke",slike_nov)
    
    cv.imshow("neke",slike_nov)
    cv.waitKey(0)
    
        

    print("neke")
   
    pass