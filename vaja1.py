import cv2 as cv
import numpy as np

def konvolucija(slika, jedro):
    visina_jedra, _ = jedro.shape
    prekrivanje = (visina_jedra - 1) // 2
    nova_slika = np.zeros_like(slika)
    if len(slika.shape) == 2: 
        slika_z_robom = np.pad(slika, prekrivanje, mode='edge')
    else:  
        slika_z_robom = np.pad(slika, ((prekrivanje, prekrivanje), (prekrivanje, prekrivanje), (0, 0)), mode='edge')
    if len(slika.shape) == 2:  
        visina_slike, sirina_slike = slika.shape
        for i in range(prekrivanje, visina_slike + prekrivanje):
            for j in range(prekrivanje, sirina_slike + prekrivanje):
                rezultat = 0
                for m in range(-prekrivanje, prekrivanje + 1):
                    for n in range(-prekrivanje, prekrivanje + 1):
                        rezultat += slika_z_robom[i + m, j + n] * jedro[prekrivanje + m, prekrivanje + n]
                nova_slika[i - prekrivanje, j - prekrivanje] = rezultat
    else:  
        visina_slike, sirina_slike, kanali = slika.shape
        for kanal in range(3): 
            for i in range(prekrivanje, visina_slike + prekrivanje):
                for j in range(prekrivanje, sirina_slike + prekrivanje):
                    rezultat = 0
                    for m in range(-prekrivanje, prekrivanje + 1):
                        for n in range(-prekrivanje, prekrivanje + 1):
                            rezultat += slika_z_robom[i + m, j + n, kanal] * jedro[prekrivanje + m, prekrivanje + n]
                    nova_slika[i - prekrivanje, j - prekrivanje, kanal] = rezultat

    return nova_slika





def filtriraj_z_gaussovim_jedrom(slika, sigma):

    velikost_jedra = int((2 * sigma) * 2 + 1)


    k = velikost_jedra // 2 - 0.5
    jedro = np.zeros((velikost_jedra, velikost_jedra))
    for i in range(velikost_jedra):
        for j in range(velikost_jedra):
            H = (
                1
                / (2 * np.pi * sigma**2)
                * np.exp(-((i - k) ** 2 + (j - k) ** 2) / (2 * sigma**2))
            )
            jedro[i, j] = H

    jedro /= np.sum(jedro)
    print(jedro)
    filtrirana_slika = konvolucija(slika, jedro)
    return filtrirana_slika


def filtriraj_sobel_horizontalno(slika):
    
    sobel_x = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
    zamegljena = filtriraj_z_gaussovim_jedrom(slika, 4)
    gradient_x = konvolucija(zamegljena, sobel_x)
    močni_gradienti = gradient_x > 100
    maska_indices = np.argwhere(močni_gradienti)
    for idx in maska_indices:
        slika[idx[0], idx[1]] = [0, 0, 255] 

    return slika





if __name__ == "__main__":
    jedro = np.array([
    [1/9, 1/9, 1/9],
    [1/9, 1/9, 1/9],
    [1/9, 1/9, 1/9]
])
    slika = cv.imread("lenna.png")
    slika = np.uint8(slika)
    #slike_nov = filtriraj_sobel_horizontalno(slika)
    slike_nov=filtriraj_z_gaussovim_jedrom(slika,1)
    #slike_nov=konvolucija(slika,jedro)
    # cv.imshow("neke",slike_nov)

    cv.imshow("neke", slike_nov)
    cv.waitKey(0)

    print("neke")

    pass
