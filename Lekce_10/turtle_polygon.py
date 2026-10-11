# Napište funkci polygon(n, radius), která pomocí želví grafiky nakreslí pravidelný n-úhelník o poloměru radius (vzdálenost od středu k jednomu vrcholu n-úhelníku)
import turtle

def polygon(n, radius):
    a = 360/n                   # vydělím 360 počtem stran m-úhelníku - dostanu velikost vnitřního úhlu
    for i in range(n):          # iteruji přes počet stran n-úhelníku
        turtle.forward(radius)  # nakreslím jednu stranu
        turtle.left(a)         # a otočím se o velikost vnitřního úhlu

if __name__ == "__main__":
    polygon(5, 100)
    turtle.mainloop()           # nechám otevřené okno s nakresleným n-úhelníkem
