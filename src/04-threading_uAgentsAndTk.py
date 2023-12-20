from uagents import Agent, Context
import customtkinter as ctk
import tkinter as tk
from ttkwidgets.autocomplete import AutocompleteEntry
import threading
# import ctk_scrollable_dropdown, ctk_scrollable_dropdown_frame
#window

alice = Agent(name="Alice")
def doTK():
    window=ctk.CTk()
    window.title("First Trial")
    window.geometry("800x800")
    window.resizable(False,False)
    window.title("")


    window.mainloop()



@alice.on_interval(period=5)
async def sendMsg(ctx: Context):
    ctx.logger.info("Message sent here")

if __name__=='__main__':
    # threading.Thread(target=alice.run).start()

    threading.Thread(target=doTK).start()
    alice.run()



