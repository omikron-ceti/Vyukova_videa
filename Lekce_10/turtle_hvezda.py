# Napište funkci, která nakreslí pravidelnou pěticípou hvězdu (https://en.wikipedia.org/wiki/File:Pentagram.svg). Zkuste zobecnit i pro více cípů.

import turtle

def hvezda(n, radius):
    if n%2:                         # jedním tahem (podobně jako pentagram) lze nakreslit jen hvězdu s lichým počtem cípů)
        a = 180 - (180/n)           # vypočítám velikost vnitřního úhlu hvězdy
        for i in range(n):          # iteruji přes počet cípů hvězdy
            turtle.forward(radius)  # nakreslím jednu stranu
            turtle.right(a)         # a otočím se o velikost vnitřního úhlu
    else:
        print("Hvězda musí mít lichý počet cípů!")

if __name__ == "__main__":
    hvezda(7, 100)
    turtle.mainloop()           # nechám otevřené okno s nakreslenou hvězdou