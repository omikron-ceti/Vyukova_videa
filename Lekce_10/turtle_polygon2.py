# Napište funkci, která vedle sebe nakreslí rovnostranný trojúhelník, čtverec, pravidelný pětiúhelník a pravidelný šestiúhelník.
import turtle
from turtle_polygon import polygon # Půjčuji si funkci z jiného souboru v téhle složce. Pokud to nefunguje, funkci si sem překopírujte


def polygons(radius):
    turtle.penup()
    turtle.goto(-400, 0)            # OPTIONAL: posunu želvu ndoleva, abych měla místo na všechny tvary
    turtle.pendown()
    for n in range(3, 7):           # iteruji přes počty stran n-úhelníku - pozor, range končí jeden krok před poslední hodnotou!!!
        polygon(n, radius)          # volám funkci polygon s aktuálním počtem stran a zadaným poloměrem
        turtle.penup()              # zvednu pero, abych mohl přesunout želvu bez kreslení
        turtle.forward(radius * 2)  # posunu želvu doprava o dvojnásobek poloměru, aby se další tvar nepřekrýval s předchozím
        turtle.pendown()            # spustím pero zpět dolů pro kreslení dalšího tvaru

    

if __name__ == "__main__":
    polygons(100)
    turtle.mainloop()               # nechám otevřené okno s nakreslenými tvary