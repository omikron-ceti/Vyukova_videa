# Napište funkci, která nakreslí domeček jedním tahem.

import turtle

def domecek(radius):
    turtle.forward(radius)  # podlaha
    turtle.left(90)
    turtle.forward(radius)  # pravá stěna
    turtle.left(90)
    turtle.forward(radius)  # strop
    turtle.left(90)
    turtle.forward(radius)  # levá stěna
    turtle.left(90+45)
    turtle.forward(radius * (2 ** 0.5))  # diagonálně nahoru
    turtle.left(90)
    turtle.forward(radius * (2 ** 0.5)/2)  # levá strana střechy
    turtle.left(90)
    turtle.forward(radius * (2 ** 0.5)/2)  # pravá strana střechy
    turtle.left(90)
    turtle.forward(radius * (2 ** 0.5))  # diagonálně dolů


if __name__ == "__main__":
    domecek(100)
    turtle.mainloop()           # nechám otevřené okno s nakresleným domečkem