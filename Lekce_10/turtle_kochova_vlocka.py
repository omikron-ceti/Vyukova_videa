# Napište funkci, která nakreslí Kochovu vločku (https://en.wikipedia.org/wiki/Koch_snowflake).

import turtle

def kochova_vlocka(radius, depth):
    if depth == 0:
        turtle.forward(radius)
    else:
        kochova_vlocka(radius / 3, depth - 1)   # jo, je to rekurze :(
        turtle.left(60)
        kochova_vlocka(radius / 3, depth - 1)
        turtle.right(120)
        kochova_vlocka(radius / 3, depth - 1)
        turtle.left(60)
        kochova_vlocka(radius / 3, depth - 1)


if __name__ == "__main__":
    turtle.speed(0)
    kochova_vlocka(300, 4)
    turtle.mainloop()