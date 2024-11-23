from tkinter import *
from pygame.math import Vector2
vec2 = Vector2

W = 800
H = 500
PlayerSize = 100
Pos = vec2(50, 50)
PlayerColor = "red"
XFinish = W - Pos.x

def KeyHander(event):
    Canva.move(PlayerId, 10, 0)

s = Tk()
s.title("Догони меня если сможешь")
Canva = Canvas(s, width=W, height=H, bg="white")
Canva.pack()
PlayerId = Canva.create_rectangle(*Pos, Pos.x + PlayerSize, Pos.y + PlayerSize, fill=PlayerColor)
FinishId = Canva.create_rectangle(XFinish, 0, XFinish + 10, H, fill="black")
s.bind("<KeyRelease>", KeyHander)
s.mainloop()