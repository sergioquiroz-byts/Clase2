from tkinter import Frame, Tk
from tkinter.messagebox import askyesno

principal = Tk()
principal.title("Prueba de enventos")

def digitar_letra(event):
    print("digitaste la letra", event.char)

def click_izquierdo(event):
    frame.focus_set()
    print("clickeado en: ", event.x, event.y)

def el_usuario_quiere_salir():
    if askyesno("salir de la aplicacion", "¿Seguro que quieres salir de la aplicacion?"):
        principal.destroy()

frame = Frame(principal, width=500, height=500)
frame.bind("<Key>", digitar_letra)
frame.bind("<Button-1>", click_izquierdo)
frame.pack()
frame.focus_set()


principal.protocol("WM_DELETE_WINDOW", el_usuario_quiere_salir)
principal.mainloop()
