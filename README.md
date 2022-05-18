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
