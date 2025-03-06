#import libraries
from tkinter import *
from gtts import gTTS
from playsound import playsound

#initializing window
import os
root = Tk()
root.title("TEXT TO SPEECH CONVERTER")

#frame creation
frame = Frame(root,
               bg = "black",
               height = "1000", 
               highlightbackground="white",
               highlightthickness="130"
               )
frame.pack(fill = X)

#define label
label = Label( text = "Text to Speech Converter",
              border =5,
              highlightbackground="skyblue",
              highlightthickness="5",
              font = "bold, 60",
              justify='center'
               
              ) 
label.place(x = 300, y = 250)
Msg = StringVar()
Label(root,text ="Enter Text:", font = 'arial 15 bold',bg='white').place(x=250,y=450)


#define input text field
entry = Entry(frame, width = 70,
             font = 150,
            textvariable = Msg,
             
              )
entry.place(x = 300, y = 320,height=30)
entry.insert(0, "")

#function to convert text to speech
def play():
    
        myobj = gTTS(text = entry.get(),
                lang="en",
                slow = False
                 )
        myobj.save("convert.wav")
        os.system("convert.wav")

#function to Reset    
def Reset():
   Msg.set("")

#function to exit   
def Exit():
   root.destroy()     

#define button
btn =Button(root, text = "PLAY", font = 'arial 15 bold' ,width = '10', bg = 'Lightgreen',command =play).place(x=450,y=550),
btn =Button(root, font = 'arial 15 bold',text = 'RESET', width = '10',bg = 'skyblue',command = Reset ).place(x=650 , y = 550)
btn =Button(root, font = 'arial 15 bold',text = 'EXIT', width = '10' , bg = 'red', command = Exit).place(x=850 , y = 550),

 
# give a title 
root.title("text_to_speech_convertor")
 
 
 
# window size
root.geometry("650x350")

   
# start the gui
root.mainloop()
