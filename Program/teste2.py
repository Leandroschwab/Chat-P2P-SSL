from Tkinter import *

class GUI:
    def __init__(self):
        self.root      = Tk()
        self.labelVariable = StringVar()
        self.root.title('Projet informatique')
        self.initialize()
        self.root.mainloop()

    def initialize(self):
        #You don't need to let your class be an instance of Tkinter class.
        #Therefore you doesn't need self.grid() call.
        #Just create a main frame from "self.root" (Tk instance) and put widgets
        #inside the frame. You could also need to create several frame,
        #for more complex layouts, but this doesn't seems the case...
        #Main frame(used to contain widgets):
        self.main = Frame(self.root)
        #In this window i used "pack" manager just to show you a quicker way to
        #accomplish your task, but it's just an example.
        self.main.pack()

        label = Label(self.main, textvariable=self.labelVariable, font=('courier',10,'bold'), anchor="w", fg="red", bg="white")
        label.pack()

        self.labelVariable.set(u"xx")

        v=Listbox(self.main)
        v.insert("end","modelo SIR")
        v.insert("end", "modelo de Witowski")
        v.insert("end", "modelo de Munz")
        v.insert("end", "modelo avec infection latente")
        v.insert("end", "modelo avec traitement")
        v.bind("<Double-Button-1>", self.Double) #your method call must match. In this case i drop "On" and it works.
        #v.grid(row=2,column=0) #your old code to layout widget
        v.pack(expand=1,fill=BOTH) #another way to layout widgets

        #self.grid_columnconfigure(0,weight=1)

    def Double(self,event):
        widget    = event.widget
        selection = widget.curselection()
        value     = widget.get(selection[0])
        self.newWindow(value)
        #Your function doesn't need to return anything (if i understood what you meant!)
        #return(selection)

    def ModifyTextarea(self,elem,msg,clear=None):
        """This function let you modify a text widget easier. It's just an helper function"""
        elem.config(state=NORMAL)
        if clear:
            elem.delete(1.0, END)
        else:
            elem.insert(END,msg)
        elem.config(state=DISABLED)

    def newWindow(self,msg):
        """This is the function you asked for. It creates a new window clicking on main window items. I layout it with grid layout as you can see"""
        top = Toplevel(self.root)
        q1 = Frame(top)
        q1.pack()
        top.grab_set()

        scrollbar = Scrollbar(q1)
        scrollbar.grid(row=0,column=3,sticky=NS)
        text = Text(q1,relief=FLAT,yscrollcommand=scrollbar.set,state=DISABLED,exportselection=True)
        text.grid(row=0,column=0,columnspan=3)

        lbl = Label(q1,text="")
        lbl.grid(row=1,column=0,columnspan=3)

        self.ModifyTextarea(text,msg)

        scrollbar.configure(command=text.yview)

        btnquit = Button(q1,borderwidth = 1,text = "Ok",command = lambda: top.destroy())
        btnquit.grid(row=2,column=1,sticky=W+E)

if __name__ == "__main__":
    """I put all tkinter logic inside GUI class in this way you only need to instantiate it, but if you prefer, you can add an additional method "show", it's up to you. This is just an example"""
    app = GUI()