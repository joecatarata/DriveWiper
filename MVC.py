import tkinter as tk

class mainGui(tk.Tk): # Inherit from Tk, representing the main window of the application.

    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self) #The main frame

        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (HomePage, PageOne):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")


        self.show_frame(HomePage)


    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

        # This is because the pages are 'stacked' and
        # tkraise() puts the passed frame in the top
        # of the stack.


class HomePage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text="Home")
        label.pack(pady=10, padx=10)

        button1 = tk.Button(self, text="Visit Page 1",command=lambda: controller.show_frame(PageOne))
        button1.pack()

class PageOne(tk.Frame):

    def __init__(self,parent,controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Home")
        label.pack(pady=10, padx=10)
        button1 = tk.Button(self, text="Back to Home", command=lambda: controller.show_frame(HomePage))
        button1.pack()


app = mainGui()
app.mainloop()
