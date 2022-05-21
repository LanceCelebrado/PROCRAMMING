from tkinter import *
import time

class StopWatch(Frame):
    
     
        
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
