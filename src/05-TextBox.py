import customtkinter as ctk

root = ctk.CTk()

textbox = ctk.CTkTextbox(root, height=80)

textbox.insert("0.0", "new txsxnnqkxsmx njkelms.,xm csndewjlsext to insertell\n\n\n\n\n\n\n\n\n H")  # insert at line 0 character 0
text = textbox.get("0.0", "end")  # get text from line 0 character 0 till the en
# textbox.delete("0.0", "end")  # delete all text
textbox.configure(text_color="#999999")  # configure textbox to be read-only\
textbox.pack()

root.mainloop()