import customtkinter as ctk 
import time
import threading

root = ctk.CTk()

butStat=0
funcStat = 0



def setterFunc():
    while not funcStat:
        time.sleep(1)
        textbox.delete("0.0", "end")
        textbox.insert("0.0", str(butStat))
        print("Hello")



def butClick():
    global butStat
    butStat+=1
    print(butStat)

def but2Click():
    global funcStat
    funcStat=1


textbox = ctk.CTkTextbox(root, height=80)
but1 = ctk.CTkButton(root, text="but1", command=butClick)
but2 = ctk.CTkButton(root, text="but2", command=but2Click)
textbox.pack()
but1.pack()
but2.pack()


textbox.insert("0.0", "")
textbox.insert("0.0", str(butStat))

textbox.pack()

t1= threading.Thread(target=setterFunc, daemon=True)

root.mainloop()