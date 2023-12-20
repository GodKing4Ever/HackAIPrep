import customtkinter as ctk
import tkinter as tk
from ttkwidgets.autocomplete import AutocompleteEntry
# import ctk_scrollable_dropdown, ctk_scrollable_dropdown_frame
#window
window=ctk.CTk()
window.title("First Trial")
window.geometry("800x800")
window.resizable(False,False)
window.title("")
#Variables
count= 0
blank = ctk.StringVar(value = "")
outText = tk.StringVar("")
countries_list = [[*[str(f) for f in range(10)], "next..."], ["prev...",*[str(f) for f in range(10, 20)], "next..."], ["prev...",*[str(f) for f in range(20, 30)]] ]
# print(countries_list)
#function
def button_print():

    print("Button pressed")
    outText.set(in1.get())
    window.update_idletasks()
    # print(window.winfo_width())
    pass
def optionmenu_callback(choice):
    global count


    if choice == "prev...":
        if count!=0:
            count-=1
            textbox.configure(values=countries_list[count])
        textbox.set("")

    elif choice == "next...":
        if count!=len(countries_list)-1:
            count+=1
            textbox.configure(values=countries_list[count])
        textbox.set("")

    else:
        print("Selected choice: ", choice)

def combobox_callback(choice):
    print("combobox dropdown clicked:", choice)       



#widgets
button = ctk.CTkButton(window, text = "printStuff", command = button_print, width=200, height = 50, corner_radius=10, fg_color='#666666', hover_color='#333333', border_color='#999999', border_width=2)
button.place(x=300, y = 100)
in1 = ctk.CTkEntry(window, width=300, height =50, corner_radius=30, placeholder_text="Enter here", placeholder_text_color='#999999' )
in1.place(x=250, y= 40)
out1 = ctk.CTkLabel(window, textvariable = outText, width = 300, height=50)
out1.place(x=250, y= 150)

textbox= ctk.CTkOptionMenu(window, values=countries_list[count], width=300, height=60, variable = blank, command = optionmenu_callback)



textbox.place(x=300, y = 250)

combobox = ctk.CTkComboBox(window, values=countries_list[count], command=combobox_callback)
combobox.place(x=300, y=220)

frame = ctk.CTkFrame(window, width=400, height = 400)
frame.place(x=200, y=320)
sbar = ctk.CTkScrollbar(frame, width=40)
sbar.place(x=360)
textArea= ctk.CTkScrollableFrame(frame, width = 200, height =800, border_color='#888888', border_width=5, fg_color="#333366", orientation="vertical")
textArea.place(x=20, y = 20)





#run
window.mainloop()
print("Testing")