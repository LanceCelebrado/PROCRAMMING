# PROCRAMMING
# ECE115.2_116JK_ExamRepository
from tkinter import *
import time

class Stopwatch(Frame):

   def __init__(self, parent=None, **kw):
      Frame.__init__(self, parent, kw)
      self._start = 0.0
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


   def _update(self):
      self._elapsedtime = time.time()-self._start
      self._setTime(self._elapsedtime)
      self._timer=self.after(50,self._update)

   def _setTime(self,elap):
      minutes = int(elap/60)
      seconds = int(elap-minutes*60.0)
      hseconds = ((elap-minutes*60.0- seconds)*100)
      self.timestr.set('%02d:%02d:%02d' % (minutes,seconds,hseconds))

   def _setLapTime(slef, elap):
      minutes = int(elap/60)
      seconds =int(elap -minutes*60.0)
      hseconds = int((elap-minutes*60.0-seconds)*100)
      return '%02d:%02d:%02d' % (minutes,seconds,hseconds)
