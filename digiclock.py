from tkinter import *
from tkinter import Label
from time import strftime
import time

class StopWatch(Frame):  

    def __init__(self, parent= None, **kw):        
        Frame.__init__(self, parent, kw)
        self._start = 0.0        
        self._elapsedtime = 0.0
        self._running = 0
        self.timestr = StringVar()
        self.lapstr = StringVar()
        self.e = 0
        self.m = 0
        self.makeWidgets()
        self.laps = []
        self.lapmod2 = 0
        self.today = time.strftime("%d %b %Y %H-%M-%S", time.localtime())
        
    def makeWidgets(self):                         
        
        l = Label(self, text='PROCRAMMERS STOPWATCH',font=("Minecraft 15 bold"),fg="white", bg="#383275")
        l.pack(fill=Y, expand=NO, pady=5, padx=2)

        l = Label(self, text=
        '''The stopwatch offers a START, STOP, LAP, RESET functions. 
        The time elapsed can also be saved to your devices 
        by using the SAVE function. ''',font=("calibri 10"), fg="#383366")
        l.pack(fill=Y, expand=NO, pady=0, padx=2)

        l1 = Label(self, text='ENTER FILE NAME',font=("Minecraft 9 bold"), fg= "MediumPurple4")
        l1.pack(fill=X, expand=NO, pady=5, padx=2)

        self.e = Entry(self)
        self.e.pack(pady=2, padx=2)
    
        l = Label(self, textvariable=self.timestr)
        self._setTime(self._elapsedtime)
        l.pack(fill=X, expand=NO, pady=3, padx=2)

        l2 = Label(self, text='LAPS',font=("Minecraft 12 bold"), fg ="MediumPurple4")
        l2.pack(fill=X, expand=NO, pady=4, padx=2)

        scrollbar = Scrollbar(self, orient=VERTICAL)
        self.m = Listbox(self,selectmode=EXTENDED, height = 5,
                         yscrollcommand=scrollbar.set, bg='lavender blush')
        self.m.pack(side=LEFT, fill=BOTH, expand=1, pady=5, padx=2)
        scrollbar.config(command=self.m.yview)
        scrollbar.pack(side=RIGHT, fill=Y)

    def _update(self): 
        
        self._elapsedtime = time.time() - self._start
        self._setTime(self._elapsedtime)
        self._timer = self.after(50, self._update)
    
    def _setTime(self, elap):
        
        minutes = int(elap/60)
        seconds = int(elap - minutes*60.0)
        hseconds = int((elap - minutes*60.0 - seconds)*100)                
        self.timestr.set('%02d:%02d:%02d' % (minutes, seconds, hseconds),)

    def _setLapTime(self, elap):
        
        minutes = int(elap/60)
        seconds = int(elap - minutes*60.0)
        hseconds = int((elap - minutes*60.0 - seconds)*100)            
        return '%02d:%02d:%02d' % (minutes, seconds, hseconds)
        
    def Start(self):                                                     
        
        if not self._running:            
            self._start = time.time() - self._elapsedtime
            self._update()
            self._running = 1        
    
    def Stop(self):                                    
        
        if self._running:
            self.after_cancel(self._timer)            
            self._elapsedtime = time.time() - self._start    
            self._setTime(self._elapsedtime)
            self._running = 0
    
    def Reset(self):                                  
        
        self._start = time.time()         
        self._elapsedtime = 0.0
        self.laps = []   
        self._setTime(self._elapsedtime)

    def Lap(self):
        
        tempo = self._elapsedtime - self.lapmod2
        if self._running:
            self.laps.append(self._setLapTime(tempo))
            self.m.insert(END, self.laps[-1])
            self.m.yview_moveto(1)
            self.lapmod2 = self._elapsedtime
       
    def GravaCSV(self):
    
        file = str(self.e.get()) + ' - '
        with open(file + self.today + '.txt', 'wb') as lapfile:
            for lap in self.laps:
                lapfile.write((bytes(str(lap) + '\n', 'utf-8')))

def main():

    root = Tk()
    root.wm_attributes("-topmost", 1)
    root.title("PRO[CRAMMERS] STOPWATCH (っ＾▿＾)っ")
    root.geometry("500x450")
    root.configure(bg="#383366")

    l = Label(root, text='DIGITAL CLOCK',font=("Minecraft 10"),fg="white", bg="#383275")
    l.pack(fill=Y, expand=NO, pady=13, padx=0)

    def time():
        
        string = strftime('%H : %M : %S %p')
        mark.config(text = string)
        mark.after(1000, time)
    mark = Label(root,font = ('Minecraft 35'),pady=0, padx=0,foreground = 'white', bg="#383366")
    mark.pack(anchor = 'center')

    time()

    sw = StopWatch(root)
    sw.pack(side=TOP)

    Button(root, text='Lap', command=sw.Lap,font=("Minecraft 12 bold"),bg="#b5b1e0").place(x=65,y=410)
    Button(root, text='Start', command=sw.Start,font=("Minecraft 12 bold"),bg="#a09ad6").place(x=120,y=410)
    Button(root, text='Stop', command=sw.Stop,font=("Minecraft 12 bold"),bg="#746cc0").place(x=186,y=410)

    Button(root, text='Reset',fg = "white", command= sw.Reset, font=("Minecraft 12 bold"),bg="#5a548e").place(x=247,y=410)
    Button(root, text='Save',fg = "white", command=sw.GravaCSV,font=("Minecraft 12 bold"),bg="#383366").place(x=320,y=410)
    Button(root, text='Quit', command=root.destroy,font=("Minecraft 12 bold"),bg="#cdb7f2").place(x=387,y=410)

    root.mainloop()

if __name__ == '__main__':

    main()