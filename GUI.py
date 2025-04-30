from tkinter import * 
from PIL import Image, ImageTk
import action 
import speech_to_text
import text_to_speech
import weather

root = Tk()
root.title("AI Assistant")
root.geometry("550x675")
root.resizable(False, False) 
root.config(bg="#1E1E2F")

# ask fun 

def ask():
    user_val = speech_to_text.speech_to_text()
    bot_val = action.Action(user_val)
    text.insert(END, 'User---->' + user_val + '\n')
    if bot_val != None:
        text.insert(END, "BOT <----" + str(bot_val) + "\n")
    if bot_val == "ok sir":
        root.destroy()    


# ask send
def send():
    print("send")

# ask delete
def Delete():
    print("Delete")



# Frame for the chat history

frame = LabelFrame(root, padx = 100, pady = 7, borderwidth = 3, relief = "raised")
frame.config(bg = "#1E1E2F")
frame.grid(row = 0, column = 1, padx = 20, pady = 10)
# text label
text_label = Label(frame, text = "Ai Assistant", font = ("comic sans ms", 14, "bold"), bg = "#356696")
text_label.grid(row = 0, column = 0, padx = 20, pady = 10)

#Image
image = ImageTk.PhotoImage(Image.open("Image/Assistant.png"))
image_label = Label(frame, image = image)
image_label.grid(row = 1, column = 0, pady = 10)
# image_label.config(width=300, height=300)

# Adding some text widget
text = Text(root, font = ('courier 10 bold'), bg = "#356696")
text.grid(row = 2, column = 0,)
text.place(x = 100, y = 420, width = 375, height = 100)

# Entry Widget

entry = Entry(root, justify = CENTER)
entry.place(x = 109, y = 530, width = 350, height = 30)

# Button 

Button1 = Button(root, text = "ASK", bg = "#356699", pady = 16, padx = 40, borderwidth = 3, relief = SOLID, command = ask)
Button1.place(x = 70, y = 575)

# Button2 

Button2 = Button(root, text = "SEND", bg = "#356699", pady = 16, padx = 40, borderwidth = 3, relief = SOLID, command = send)
Button2.place(x = 200, y = 575)

# Button 3

Button3 = Button(root, text = "DELETE", bg = "#356699", pady = 16, padx = 40, borderwidth = 3, relief = SOLID, command = Delete)
Button3.place(x = 330, y = 575)



root.mainloop()
