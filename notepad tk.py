import tkinter
from PIL import Image,ImageTk
from tkinter import StringVar,IntVar,scrolledtext,END,messagebox,filedialog



#window configuration
root = tkinter.Tk()
root.title("Notepad")
root.geometry("600x600")
root.resizable(0,0)
root.iconbitmap('pad.ico')

#fonts & color's
text_color = "white"
menu_color = "#F7CB1A"
root_color = "white"
root.config(bg=root_color)

#define functions
def change_font(event):
    """Change the given font based off dropbox option"""
    if font_style.get() == 'none':
       my_font = (font_family.get(),font_size.get())

    else:
        my_font = (font_family.get(),font_size.get(),font_style.get())
    #Change Font style

    input_text.config(font=my_font)


def new_note():
    question = messagebox.askyesno("New Note","Are You Sure You Want A New Note?")
    if question==1:
       input_text.delete("1.0",END)

def close_note():
    question = messagebox.askyesno("Close","Are You Sure You Want To Close Notepad?")
    if question==1:
        root.destroy()

def save_note():
    save_name= filedialog.asksaveasfilename(initialdir="./",title="Save Note",filetypes=(("Text Files","*.txt"),("All Files","*.*")))
    with open(save_name,'w')as f:
        f.write(input_text.get("1.0",END))

def open_note():
    open_name = filedialog.askopenfilename(initialdir='./',title="Open Note",filetypes=(("Text Files","*.txt"),("All Files","*.*")))
    with open(open_name,'r') as f:
        input_text.delete("1.0",END)
        change_font(1)
        text = f.read()
        input_text.insert("1.0",text)

#define layout
#define frames
menu_frame = tkinter.Frame(root,bg=menu_color)
text_frame = tkinter.Frame(root,bg=text_color)
menu_frame.pack(padx=5 ,pady=5)
text_frame.pack(padx=5 ,pady=5)


#Layout for menu frame
#Create the menu : new,open,save,close,font family,font size,font style
new_image = ImageTk.PhotoImage(Image.open('new.png'))
new_button = tkinter.Button(menu_frame,image=new_image,command=new_note)
new_button.grid(row=0,column=0,padx=5,pady=5)

open_image = ImageTk.PhotoImage(Image.open('open.png'))
open_button = tkinter.Button(menu_frame,image=open_image,command=open_note)
open_button.grid(row=0,column=1,padx=5,pady=5)

save_image = ImageTk.PhotoImage(Image.open('save.png'))
save_button = tkinter.Button(menu_frame,image=save_image,command=save_note)
save_button.grid(row=0,column=2,padx=5,pady=5)

close_image = ImageTk.PhotoImage(Image.open('close.png'))
close_button = tkinter.Button(menu_frame,image=close_image,command=close_note)
close_button.grid(row=0,column=3,padx=5,pady=5)

#Create a list of fonts
families = ['Terminal','Calibri','Arial','Courier','Calibri','Cambria','Georgia','Times New Roman','Wingdings']
font_family = StringVar()
font_family_drop = tkinter.OptionMenu(menu_frame,font_family,*families,command=change_font)
font_family.set('Terminal')
font_family_drop.config(width=15)#to set the tab at max length
font_family_drop.grid(row=0,column=4,padx=5,pady=5)

#Create a list of font sizes
size = [8,10,12,14,16,18,20,22,24,26,28,30,32,44,72,84]
font_size = IntVar()
font_size_drop = tkinter.OptionMenu(menu_frame,font_size,*size,command=change_font)
font_size.set(12)
font_size_drop.config(width=12)
font_size_drop.grid(row=0,column=5,padx=5,pady=5)


#Create a list of font styling
style = ['none','bold','italic','underline']
font_style = StringVar()
font_style_drop = tkinter.OptionMenu(menu_frame,font_style,*style,command=change_font)
font_style.set('none')
font_style_drop.config(width=10)
font_style_drop.grid(row=0,column=6,padx=5,pady=5)

#layout for text frame
my_font = (font_family.get(),font_size.get())

input_text = tkinter.scrolledtext.ScrolledText(text_frame,width=1000,height=100,bg=text_color,font=my_font)
input_text.pack()



#window mainloop
root.mainloop()