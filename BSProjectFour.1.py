#Bilal Sayed 12/3/17

import tkinter
import tkinter.messagebox

class BMI:
    def __init__(self):
        #create main window
        self.main_window = tkinter.Tk()
        #create 6 frames for the labels, entries, and buttons
        self.frame1 = tkinter.Frame(self.main_window)
        self.frame2 = tkinter.Frame(self.main_window)
        self.frame3 = tkinter.Frame(self.main_window)
        self.frame4 = tkinter.Frame(self.main_window)
        self.frame5 = tkinter.Frame(self.main_window)
        self.frame6 = tkinter.Frame(self.main_window)
        #title in frame 1
        self.header = tkinter.Label(self.frame1, text='BMI Calculator')
        #pack the label
        self.header.pack()
        #label and entry for weight
        self.label_weight = tkinter.Label(self.frame2, text='Weight:       ')
        self.entry_weight = tkinter.Entry(self.frame2, width =10)
        #pack the label and entry
        self.label_weight.pack(side='left')
        self.entry_weight.pack(side='left')
        #label and entry for height
        self.label_height = tkinter.Label(self.frame3, text='Height:(in) ')
        self.entry_height = tkinter.Entry(self.frame3, width =10)
        #pack the label and entry
        self.label_height.pack(side='left')
        self.entry_height.pack(side='left')
        #label and display for bmi value
        self.desc_label1 = tkinter.Label(self.frame4, text='BMI:')
        self.bmivalue = tkinter.StringVar()
        self.bmivalue_label = tkinter.Label(self.frame4, textvariable=self.bmivalue)
        #pack the lable and display
        self.desc_label1.pack(side='left')
        self.bmivalue_label.pack(side='left')
        #label and display for the descriptive value
        self.desc_label2 = tkinter.Label(self.frame5, text='Description:')
        self.bmidesc = tkinter.StringVar()
        self.bmidesc_label = tkinter.Label(self.frame5, textvariable=self.bmidesc)
        #pack the label and display
        self.desc_label2.pack(side='left')
        self.bmidesc_label.pack(side='left')
        #create the calculate and quit buttons
        self.calculate_button = tkinter.Button(self.frame6, text='Calculate BMI', command=self.calculate_bmi)
        self.quit_button = tkinter.Button(self.frame6, text='Quit', command=self.main_window.destroy)
        #pack the buttons
        self.calculate_button.pack(side='left')
        self.quit_button.pack(side='left')
        #pack the frames
        self.frame1.pack(anchor=tkinter.W)
        self.frame2.pack(anchor=tkinter.W)
        self.frame3.pack(anchor=tkinter.W)
        self.frame4.pack(anchor=tkinter.W)
        self.frame5.pack(anchor=tkinter.W)
        self.frame6.pack(anchor=tkinter.W)
    #define calculate_bmi
    def calculate_bmi(self):
        #claculate the bmi
        self.bmi_total = (float(self.entry_weight.get()) * 703) / (float(self.entry_height.get()) * float(self.entry_height.get()))
        #set bmivalue to the bmi that was calculated
        self.bmivalue.set("{:.2f}".format(self.bmi_total))
        #if staments to find the descriptive word
        self.bmi_desc_value = 0
        if self.bmi_total < 18.5:
            self.bmi_desc_value = 'Underweight'
        elif self.bmi_total >= 18.5 and self.bmi_total < 25:
            self.bmi_desc_value = 'Normal'
        elif self.bmi_total >= 25 and self.bmi_total < 30:
            self.bmi_desc_value = 'Overweight'
        else:
            self.bmi_desc_value = 'Obese'
        #set the descriptive word
        self.bmidesc.set(self.bmi_desc_value)
#create instance        
bmi = BMI()

