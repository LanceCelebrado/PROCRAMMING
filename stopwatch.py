from tkinter import *
import time

class StopWatch(Frame):
    
    def __init__(self, parent=None, **kw):
        Frame.__init__(self, parent, kw)
        self._start = 0.0
        self._elapsedtime = 0.0
        self._running = 0
        self.timestr = StringVar()
        self.e = 0
        self.m = 0
        self.makeWidgets()
        self.laps = []
        self.lapmod2 = 0
        self.today = time.strftime("%d %b %Y %H-%M-%S", time.localtime())
        
    def makeWidgets(self):
        l1 = label(self, text='(っ＾▿＾)💨 FILE NAME ')
        l1.pack(fill=X, expand=NO, pady=1, padx=2)
        self.e = Entry(self)
        self.e.pack(pady=2, padx=2)
        l = Label(self, textvariable=self.timestr)
        self._setTime(self._elapsedtime)
        l.pack(fill=X, expand=NO, pady=3, padx=2)
        l2 = Label(self, text='=Laps=')
        l2.pack(fill=X, expand=NO, pady=4, padx=2)
        scrollbar = Scrollbar(self, orient=VERTICAL)
        self.m = Listbox(self,selectmode=EXTENDED, height = 5,
                         yscrollcommand=scrollbar.set)
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
        hseconds = int ((elap - minutes*60.0 - seconds)*100)
        self.timestr.set('%02d:%02d:%02d' % (minutes, seconds, hseconds))
                         
    def _setLapTime(self, elap):
        minutes = int(elap/60)
        seconds = int(elap - minutes*60.0)
        hseconds = int ((elap - minutes*60.0 - seconds)*100)
        return '%02d:%02d:%02d' % (minutes, seconds, hseconds)
                       
    def Lap(self):
        '''Makes a lap, only if started'''
        tempo = self._elapsedtime - self.lapmod2
        if self.running:
            self.laps.append(self._setLapTime(tempo))
            self.m.insert(END, self.laps[-1])
            self.m.yview_moveto(1)
            self.lapmod2 = self._elapsedtime
            
    def GravaCSV(self):
        '''Get the name of the stopwatch and create a file to store the laps'''
        file = str(self.e.get()) + '-'
        with open(file + self.today + '.txt', 'wb') as lapfile:
            for lap in self.lalps
                lapfile.write((bytes(str(lap) + '\n', 'utf-8')))
    def main():
        root = Tk()
        root.wm_attributes("-topmost", 1)
        sw = StopWatch(root)
        sw.pack(side = TOP)
        Button(root, text = "Lap", command = sw.Lap).pack(sie = LEFT)
        Button(root, text = "Start", command = sw.Start).pack(sie = LEFT)
        Button(root, text = "Stop", command = sw.Stop).pack(sie = LEFT)
        Button(root, text = "Save", command = sw.Save).pack(sie = LEFT)
        Button(root, text = "Quit", command = sw.Quit).pack(sie = LEFT)
        root.mainloop()
        
    if __name__ == "__main__":
        main()
