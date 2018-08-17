#Bilal Sayed 12/1/17

import tkinter

class JoesAutomotive:
    def __init__(self):
        #create main window
        self.main_window = tkinter.Tk()
        #create 10 frames for the labels, checkboxes, and buttons
        self.frame1 = tkinter.Frame(self.main_window)
        self.frame2 = tkinter.Frame(self.main_window)
        self.frame3 = tkinter.Frame(self.main_window)
        self.frame4 = tkinter.Frame(self.main_window)
        self.frame5 = tkinter.Frame(self.main_window)
        self.frame6 = tkinter.Frame(self.main_window)
        self.frame7 = tkinter.Frame(self.main_window)
        self.frame8 = tkinter.Frame(self.main_window)
        self.frame9 = tkinter.Frame(self.main_window)
        self.frame10 = tkinter.Frame(self.main_window)
        #create a label to instruct the usere on what to do
        self.header = tkinter.Label(self.frame1, text='Select the services that need to be performed:')
        #pack the header
        self.header.pack()
        #Create 7 variables for the 7 checkboxes
        self.cb_var1 = tkinter.IntVar()
        self.cb_var2 = tkinter.IntVar()
        self.cb_var3 = tkinter.IntVar()
        self.cb_var4 = tkinter.IntVar()
        self.cb_var5 = tkinter.IntVar()
        self.cb_var6 = tkinter.IntVar()
        self.cb_var7 = tkinter.IntVar()
        #initialize all them to 0
        self.cb_var1.set(0)
        self.cb_var2.set(0)
        self.cb_var3.set(0)
        self.cb_var4.set(0)
        self.cb_var5.set(0)
        self.cb_var6.set(0)
        self.cb_var7.set(0)
        #create the widgets
        self.cb1 = tkinter.Checkbutton(self.frame2, text='Oil Change', variable=self.cb_var1)
        self.cb2 = tkinter.Checkbutton(self.frame3, text='Lube Job', variable=self.cb_var2)
        self.cb3 = tkinter.Checkbutton(self.frame4, text='Radiator Flush', variable=self.cb_var3)
        self.cb4 = tkinter.Checkbutton(self.frame5, text='Transmission Flush', variable=self.cb_var4)
        self.cb5 = tkinter.Checkbutton(self.frame6, text='Inspection', variable=self.cb_var5)
        self.cb6 = tkinter.Checkbutton(self.frame7, text='Muffler Replacment', variable=self.cb_var6)
        self.cb7 = tkinter.Checkbutton(self.frame8, text='Tire Rotation', variable=self.cb_var7)
        #pack the widgets
        self.cb1.pack()
        self.cb2.pack()
        self.cb3.pack()
        self.cb4.pack()
        self.cb5.pack()
        self.cb6.pack()
        self.cb7.pack()
        #create a total label and a label to display the total
        self.descr_label = tkinter.Label(self.frame9, text='Total: $')
        self.value = tkinter.StringVar()
        self.total_label = tkinter.Label(self.frame9, textvariable=self.value)
        #pack the toatal labels
        self.descr_label.pack(side='left')
        self.total_label.pack(side='left')
        #create the total and the quit buttons
        self.total_button = tkinter.Button(self.frame10, text='Total', command=self.calculate_total)
        self.quit_button = tkinter.Button(self.frame10, text='Quit', command=self.main_window.destroy)
        #pack the buttons
        self.total_button.pack(side='left')
        self.quit_button.pack(side='left')
        #pack the frames all to the west
        self.frame1.pack(anchor=tkinter.W)
        self.frame2.pack(anchor=tkinter.W)
        self.frame3.pack(anchor=tkinter.W)
        self.frame4.pack(anchor=tkinter.W)
        self.frame5.pack(anchor=tkinter.W)
        self.frame6.pack(anchor=tkinter.W)
        self.frame7.pack(anchor=tkinter.W)
        self.frame8.pack(anchor=tkinter.W)
        self.frame9.pack(anchor=tkinter.W)
        self.frame10.pack(anchor=tkinter.W)

        tkinter.mainloop()
    #Ddefine claculate total
    def calculate_total(self):
        self.total = 0
        if self.cb_var1.get() == 1:
            self.total = self.total + 30.00
        if self.cb_var2.get() == 1:
            self.total = self.total + 20.00
        if self.cb_var3.get() == 1:
            self.total = self.total + 40.00
        if self.cb_var4.get() == 1:
            self.total = self.total + 100.00
        if self.cb_var5.get() == 1:
            self.total = self.total + 35.00
        if self.cb_var6.get() == 1:
            self.total = self.total + 200.00
        if self.cb_var7.get() == 1:
            self.total = self.total + 20.00
            
        (format(self.total), ',.0f')
        #set value to the total
        self.value.set("{:.2f}".format(float(self.total)))
        
#create and instance
joe = JoesAutomotive()
