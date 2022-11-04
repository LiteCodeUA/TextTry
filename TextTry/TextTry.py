from tkinter import *
from tkinter.filedialog import *
from tkinter.messagebox import *
import fileinput
 
class Window_blank:
  def __init__(self):
    main_menu = Menu(root)
    root.config(menu=main_menu)
    first_menu = Menu(main_menu)
    main_menu.add_cascade(label="File", menu=first_menu)
    first_menu.add_command(label="open",     command=self.open_file)
    first_menu.add_command(label="save as", command=self.save_file)
    first_menu.add_command(label="about us", command=self.about)
    self.txt = Text(root, width=75, height=25)
    self.txt.pack()
 
  def open_file(self):
    op = askopenfilename()
    try:
      self.txt.delete(1.0, END)
      for i in fileinput.input(op):
        self.txt.insert(END, i)
    except:
      pass
 
  def save_file(self):
    save_as = asksaveasfilename()
    try:
      letter = self.txt.get(1.0, END)
      f = open(save_as, "w")
      f.write(letter)
      f.close()
    except:
      pass
 
  def close_win(self):
    if askyesno("Saving file", "save file?"):
      self.save_file()
      root.destroy()
    else:
      root.destroy()
 
  def about(self):
    showinfo("TextTry", "TextTry | created by Evgeniy Tryhub")
 
root = Tk()
root.title("TextTry")
 
obj_menu = Window_blank()
root.mainloop()
