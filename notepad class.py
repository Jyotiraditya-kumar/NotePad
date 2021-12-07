from tkinter import *
from tkinter import scrolledtext,filedialog,messagebox

class notepad:
    
    def __init__(self,root):
        self.text=scrolledtext.ScrolledText(root)
        self.text.place(relwidth=1,relheight=1)
        self.text.focus()
        self.opt=StringVar()
        self.var=IntVar()
        menubar=Menu(root)
        self.file=None
        self.font=Toplevel(root)
        self.font.geometry("480x480")
        self.font.title("Font")
        options=("2","4","6","10","14","16","20","22","26")
        opm=OptionMenu(self.font,self.opt,*options).pack()
        cb=Checkbutton(self.font,text="Bold",variable=self.var).pack()
        self.bold={"1":" bold","0":""}
        self.it={"1":" italic","0":""}
        b=Button(self.font,text="OK",command=self.ok)
        b.pack()
        self.font.withdraw()
        filemenu=Menu(menubar,tearoff=0)
        menubar.add_cascade(label="File",menu=filemenu)
        filemenu.add_command(label="New",command=self.new)
        filemenu.add_command(label="Open",command=self.Open)
        filemenu.add_command(label="Save",command=self.save)
        filemenu.add_command(label="Save as",command=self.saveas)
        filemenu.add_separator()
        filemenu.add_command(label="Exit",command=lambda:root.destroy())
        
        editmenu=Menu(menubar,tearoff=0)
        menubar.add_cascade(label="Edit",menu=editmenu)
        editmenu.add_command(label="Undo",command=lambda:self.Edit("Undo"))
        editmenu.add_command(label="Redo",command=lambda:self.Edit("Redo"))
        editmenu.add_command(label="Cut",command=lambda:self.Edit("Cut"))
        editmenu.add_command(label="Copy",command=lambda:self.Edit("Copy"))
        editmenu.add_command(label="Paste",command=lambda:self.Edit("Paste"))
        editmenu.add_command(label="Find",command=self.find)

        fontmenu=Menu(menubar,tearoff=0)
        menubar.add_cascade(label="Font",menu=fontmenu)
        fontmenu.add_command(label="font",command=lambda:self.font.deiconify())
        """fontmenu.add_command(label="12",command=lambda:self.font("12"))
        fontmenu.add_command(label="15",command=lambda:self.font("15"))
        fontmenu.add_command(label="20",command=lambda:self.font("20"))
        fontmenu.add_command(label="24",command=lambda:self.font("24"))"""
        root.config(menu=menubar)

        
        
    def new(self):
        self.file=None
        self.text.delete("1.0",END)
        root.title("Untitled notepad")
        self.text.focus()
    def Open(self):
        try:
            filename=filedialog.askopenfilename(defaultextension=".txt",initialdir="/",filetype=(("text file","*.txt"),("all files","*.*")))
            f=open(filename)
            root.title(filename)
            self.text.delete("1.0",END)
            self.file=filename
            self.text.insert(INSERT,f.read())
            f.close()
        except:
            pass
    def save(self):
        try:
            if self.file==None:
                filename=filedialog.asksaveasfilename(title="",defaultextension=".txt",
                                                      initialdir="/",filetype=(("text file","*.txt"),("all files","*.*")))
                self.file=filename
            else:
                filename=self.file
            f=open(filename,"w")
            f.write(self.text.get("1.0",END))
            f.close()
            messagebox.showinfo("Success","file saved successfully")
        except:
            pass
    def saveas(self):
        try:
            filename=filedialog.asksaveasfilename(title="",defaultextension=".txt",
                                                      initialdir="/",filetype=(("text file","*.txt"),("all files","*.*")))
            f=open(filename,"w")
            f.write(self.text.get("1.0",END))
            f.close()
            messagebox.showinfo("Success","file saved successfully")
        except:
            pass
        
    def Edit(self,st):
        self.text.event_generate("<<"+st+">>")
        
        
    def find(self):
        #s=self.text.get("1.0",END)
        self.text.config(fg="red")
    def ok(self):
        self.text.config(font="arial "+self.opt.get()+self.bold[str(self.var.get())])
        self.font.withdraw()
root=Tk()
root.geometry("1920x1080")
root.title("Notepad")
a=notepad(root)
root.mainloop()
