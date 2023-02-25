from tkinter import *
import random
root = Tk()
 
w = 400
h = 400

def change():
    
    r = random.randint(1, 3)

    a = random.randint(0, 300)
    b = random.randint(0, 300)
    c = random.randint(0, 300)
    d = random.randint(0, 300)
    e = random.randint(0, 300)
    f = random.randint(0, 300)

    if r == 1:
        canvas.delete('all')
        canvas.create_polygon(a, b, c, d, e, f, fill='grey')

    elif r == 2:
        canvas.delete('all')
        canvas.create_oval(a, b, a+100, b+100, fill='grey')
    else:
        canvas.delete('all')
        canvas.create_rectangle(a, b, a+100, b+100, fill='grey')

canvas = Canvas(root, width=w, height=h, bg='white')
canvas.pack()

 
Button(text="Нажми на меня", command=change).pack()
 
root.mainloop()