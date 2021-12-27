#test #1 for micro concious computers



#GUI GUI GUI

from tkinter import *


root = Tk()
root.title("MCC_test#1")
#root.geometry("390x400")
root.configure(background = "#557755")


frame = LabelFrame(root, padx = 100, pady = 100)
frame.grid(row = 0, column = 10)



chat = ""

message_box = Label(root, text = chat, padx = 250, pady = 100)
message_box.grid(row = 0, column = 0, columnspan = 3)

text_bar = Entry(root,width = 75)
text_bar.grid(row = 5,column = 0, columnspan = 2)
text_bar.insert(0,"hello")


def message_linker(text):
    global chat
    chat +="\n"+text
    text = Label(root,text = chat).grid(row = 0, column = 0)

def speech(text):
    print(text)
    if text == "hello":
        output = "Computer : Hi"
    else :
        output = "Computer : Oh!, great! what else?\n"+text
    
    message_linker(output)   
        
def talk():
    #global chat
    message_linker(text_bar.get())
    speech(text_bar.get())
    text_bar.delete(0,END)
    
    

send = Button(root,text = 'send', command = talk, padx = 7)
send.grid(row = 5,column = 2, columnspan = 1)




root.mainloop()