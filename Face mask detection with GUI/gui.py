from tkinter import *
from PIL import ImageTk,Image  
window=Tk()
#btn=Button(window, text="This is Button widget", fg='blue')
#btn.place(x=80, y=100)

#txtfld=Entry(window, text="This is Entry Widget", bd=5)
#txtfld.place(x=80, y=150)

#canvas = Canvas(window, width = 300, height = 300)  
#canvas.pack()  
img = ImageTk.PhotoImage(Image.open("familymask.jpg"))  
#canvas.create_image(20, 20, anchor=NW, image=img)  


#bg = PhotoImage(file = "familymask.jpg")
  
# Create Canvas
canvas1 = Canvas(window, width = 400,
                 height = 400)
  
canvas1.pack(fill = "both", expand = True)
  
# Display image
canvas1.create_image( 0, 0, image = img, 
                     anchor = "nw")
  
lbl=Label(window, text="Covid - 19 Mask detection is starting.......", fg='red', font=("Helvetica", 16))
lbl.place(x=60, y=50)



window.title('Face mask Detection')
window.geometry("500x286+10+10")
window.mainloop()

