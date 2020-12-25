#!/usr/bin/env python
"""
### What is CBT_Trainer? 
CBT_Trainer is a program that offers a Graphic User Interface environment for a Computer Base Test in the form
of multiple choice questions. It is written in Python3 using the Tkinter GUI
Library.

### Dependence
Python 3

### How to use

#### Preparation
Download the app folder and access it.

#### Trial
For a trial, execute the file "cbt_trainer.py". Do File>New and enter an
integer between 1 and 6. The test will start. To check your answers, 
do Tools>Check. Missed questions will be in the file "missed.txt".

#### Customization
To customize with your own questions:

1. put in the folder "unsolved" multiple choice questions
( one .gif file for each question). For instance, files
could be denoted 1.gif, 2.gif, ...

2. Modify the file "solution/sol.txt" to reflect the correct answer 
(one answer per line, the line number corresponds to the question number).

3. Enjoy!
"""
# max number of questions
NBRQUESTIONS=6
# minutes per questions
MNPERQESTION=5

# import tkinter and all
from tkinter import *
from tkinter import scrolledtext
from tkinter import filedialog
from tkinter import messagebox
from tkinter import font

# other imports
import datetime
import time
import os

 
# pour pouvoir utiliser les functions sample() et range()
from random import *

seed() #random.



class atop:
    
    '''
A top level to choose the number of questions. It takes a master
(root from App) and a masterclass App that has root.
    '''
    def center(self,topLevel):
      topLevel.update_idletasks()
      width = topLevel.winfo_screenwidth()
      heigth = topLevel.winfo_screenheight()
      size = tuple(int(_) for _ in topLevel.geometry().split('+')[0].split('x'))
      x = width/2 - size[0]/2
      y = heigth/2 - size[1]/2
      topLevel.geometry("%dx%d+%d+%d" % (size + (x, y)))
    
    def __init__(self,masterclass,master):
        
        def gett(self):
            "The validate command function. Check if the input is correct"
            tampon=self.entr.get()
            try:
                tampon=int(tampon)
                if tampon>0 and tampon<=NBRQUESTIONS:
                        self.masterclass.number_questions=tampon
                        self.top.quit() # quit this window
                        self.top.destroy()
                else:
                    messagebox.showerror('Bad format',\
                                           "Must be an integer\n"
                                           +"from 1 to "+str(NBRQUESTIONS))
                    pass
                pass
            except:
                messagebox.showerror('Bad format',\
                                       "Must be an integer\nfrom 1 to "
                                       +str(NBRQUESTIONS))
                
                   
                    
        self.masterclass=masterclass
        self.top=Toplevel(master)
        self.lab=Label(self.top,text="Enter the number of\n"\
                  +"questions")
        self.lab.grid(row=0)
        self.entr=Entry(self.top)
        self.entr.grid(row=1)
        self.entr.focus()
        self.butt=Button(self.top,text="Validate",command= lambda:gett(self))
        self.butt.grid(row=2)        
        self.center(self.top)
        self.top.mainloop()


class data_class:
    def __init__(self):
        self.welcome_message="Hi"

data=data_class()

class App:

    def welcome(self):
        messagebox.showinfo('Firt time usage', data.welcome_message)


    def doNew(self):
        self.begin()
        pass


    def doSaveAs(self):
        pass


    def doOpen(self):
        pass


    def check(self):
        answertext0=open('solution/sol.txt','r').readlines()
        answertext=[answertext0,[]]
        temp=['A','B','C','D','E','0']
        self.score=0
        temp_sol=[]
        missed=[]
        sel0=[elem  for elem in self.selection if elem[0]<200]
        sel1=[elem  for elem in self.selection if elem[0]>=200]
        sel=[sel0,sel1]
        for k in range(2):
          for elem in sel[k]:
            if answertext[k][-k*1000+ elem[0]-1].strip()==temp[elem[1]]:
                self.score+=1
                pass
            else:
                missed.append([elem[0],answertext[k][-k*1000+ elem[0]-1].strip(),temp[elem[1]]])
            temp_sol.append([elem[0],answertext[k][-k*1000+ elem[0]-1].strip()])

        messagebox.showinfo('SELECTIONS',
         "selected= "+str(self.selection)+'\n'+\
        "sol= "+str(temp_sol)+'\n'+\
        "score="+ str(self.score))
        messagebox.showinfo('MISSED',
         "You missed "+str(missed))
        afile=open('missed.txt','a')
        for elem in missed:
            afile.write(str(elem[0])+'\n')
            pass
        afile.close()
        self.Intercepte()


    pass

    def show_missed(self):
        pass




    def move_attended(self):
        try:

            for elem in self.q_lists:
                os.system('mv unsolved/'+elem+' solved')
                pass
        except:
            pass
    def statistics(self):
        pass


    def updateGui(self):
        self.labels[3]['text']=str(self.current_number+1)
        self.labels[5]['text']=str(self.number_questions)
        for i in range(0,8):
            if i!=2+self.selection[self.current_number][1]:
                self.b_choices[i].config(bg=self.root.cget('bg'))
            else:
                self.b_choices[i].config(bg='blue')
                pass
        pass



    def action(self,a):
        """"""
        if a=="<== Back":
            self.current_number-=1
            if self.current_number in range(self.number_questions):
                self.gif1 = PhotoImage(file = 'unsolved/'+
                         self.q_lists[self.current_number])
                self.image_label['image']=self.gif1
                self.updateGui()
            else:
                self.current_number+=1
            pass

        elif a=="Foward ==>":
            self.current_number+=1
            if self.current_number in range(self.number_questions):
                self.gif1 = PhotoImage(file = 'unsolved/'+self.q_lists[self.current_number])
                self.image_label['image']=self.gif1
                self.updateGui()
            else:
                self.current_number-=1
            pass
        elif a=="A":
            self.selection[self.current_number][1]=0
            self.updateGui()
            pass
        elif a=="B":
            self.selection[self.current_number][1]=1
            self.updateGui()
            pass
        elif a=="C":
            self.selection[self.current_number][1]=2
            self.updateGui()
            pass
        elif a=="D":
            self.selection[self.current_number][1]=3
            self.updateGui()
            pass
        elif a=="E":
            self.selection[self.current_number][1]=4
            self.updateGui()
            pass
        elif a=="Unanswered":
            self.selection[self.current_number][1]=5
            self.updateGui()
            pass

        pass


    def Intercepte(self):
        "execute this before exiting"
        #uncomment the following line if you want to move solved questions
        #self.move_attended()
        self.root.destroy()


    def setup_root(self):
        """# Set up the screen, the title, and the size."""
        self.root = Tk()
        self.root.title("Exam")
        #self.root.minsize(width=800,height=600)
        self.root['bg']='white'
        # redirect exit
        self.root.protocol("WM_DELETE_WINDOW", self.Intercepte)




    def obtain_time(self):
        left=int(-time.time()+self.end_time)
        if left<0:
            self.check()
            self.Intercepte()
            pass
        else:
            ss=left%60; left-=ss; mm=(left//60)%60; hh=left//3600
            self.labels[1]['text']=(str(hh)+":"+str(mm)+":"+str(ss))
            self.labels[1].after(200,self.obtain_time)
            pass





    def setup_menu(self):
        """ Set up basic Menu"""
        self.menuBar = Menu(self.root)

        # File
        fileMenu = Menu(self.menuBar,tearoff=0)
        self.menuBar.add_cascade(label="File", menu=fileMenu)
        
        # File >New File
        fileMenu.add_command(label="New File", command=self.doNew,
                             accelerator="Ctrl+N")

        # File>Open
        fileMenu.add_command(label="Open", command=self.doOpen,
                             accelerator="Ctrl+O")

        # File> Save
        fileMenu.add_command(label="Save", command=self.doSaveAs,
                             accelerator="Ctrl+Shift+S")

        # File> Quit
        fileMenu.add_command(label="Quit", command=self.Intercepte,
                             accelerator="Ctrl+Shift+Q")

        

        # Tools
        toolsMenu = Menu(self.menuBar,tearoff=0)
        self.menuBar.add_cascade(label="Tools", menu=toolsMenu)

        # Tools>Check
        toolsMenu.add_command(label="Check", command=self.check,
                              accelerator="Ctrl+K")

        # Tools>Statistics
        toolsMenu.add_command(label="Statistics", command=self.statistics,
                              accelerator="Ctrl+T")

        
        # Help
        helpMenu = Menu(self.menuBar,tearoff=0)
        self.menuBar.add_cascade(label="Help", menu=helpMenu)

        # Help>Help
        helpMenu.add_command(label="Help", command=self.welcome,
                             accelerator="Ctrl+H")

        #Help>About
        helpMenu.add_command(label="About", command=self.welcome,
                             accelerator="Ctrl+B")
         
        

        """   add menu to root"""

        self.root.config(menu=self.menuBar)


    def setup_image_label(self):
         
        self.gif1 = PhotoImage(file = 'welcome.gif')
        self.image_label=Label(self.root,bg="white",height=420,width=1150,
                               image=self.gif1)
        self.image_label.grid(column=0,row=0,columnspan=1,
                              rowspan=15, sticky="EWNS")

         


    def setup_buttons(self):
        """definir les boutons pour choisirs"""
        self.texts_button=["<== Back", "Foward ==>","A"]+[
                      "B","C",\
                      "D","E","Unanswered"]
        self.b_choices=[]
        self.separation_label1=Label(self.root,text="___ Your Choice ___ ")
        self.separation_label1.grid(row=8,column=2,sticky="EWNS")

        for bbl in self.texts_button:
            self.b_choices.append(Button(self.root,text="",
                                         command=lambda bbl=bbl:self.action(str(bbl))))

        #Placer les boutons

        for j in range(2):
            self.b_choices[j].grid(column=2,row=j+6,columnspan=1,rowspan=1,\
                              sticky="WENS")
            pass
        for j in range(2,8):
            self.b_choices[j].grid(column=2,row=j+7,columnspan=1,rowspan=1,\
                              sticky="WENS")
            pass
        for index,b in enumerate(self.b_choices):
            b["text"]=self.texts_button[index]

            pass

    def setup_labels(self):
        self.labels_text=["Time left"," ","Question #:","","of",
                          "",]
        self.labels=[Label(self.root,relief=RIDGE,text=self.labels_text[0]),\
                     Label(self.root,  relief=SUNKEN,text=self.labels_text[1]),\
                     Label(self.root,relief=RIDGE,text=self.labels_text[2]),\
                     Label(self.root,relief=RIDGE,text=self.labels_text[3]),\
                     Label(self.root,relief=SUNKEN,text=self.labels_text[4]   ),\
                     Label(self.root,relief=RIDGE,text=self.labels_text[5]),]
        for index,lb in enumerate(self.labels):
            lb.grid(column=2,row=index,sticky="EWNS",)



    def build_list_questions(self):
        questions_files=[]
        for f in os.listdir("unsolved/"):
            if f.endswith(".gif"):
                questions_files.append(f)
        
        dummy=atop(self,self.root)
        if not questions_files or not self.number_questions:
            messagebox.showinfo("Warning",
                                  "Oups! Something went wrong!\nSomething is rotten in Danemark")
            self.q_lists=[]
            self.Intercepte()
            return
        self.q_lists=sample(questions_files,min(len(questions_files),
                                                self.number_questions))
        self.current_number=-1


    def __init__(self):
        self.setup_root()
        self.setup_menu()
        self.setup_image_label()
        self.setup_buttons()
        self.setup_labels()
        pass

    
    def begin(self):
        self.build_list_questions()
        self.begin_time=time.time()
        self.end_time=self.begin_time+60*MNPERQESTION*int(self.number_questions)
        self.root.after(0, self.obtain_time())
        self.selection=[]
        for e in self.q_lists:
            ee=int(e[:-4])
            self.selection.append([ee,5])
            

        self.action('Foward ==>')



if __name__=="__main__":
    app = App()
    app.root.mainloop()
    pass

        
