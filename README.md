# PROCRAMMING
# ECE115.2_116JK_ExamRepository



def _update(self):
  self._elapsedtime = time.time()-self._start
  self._setTime(self._elapsedtime)
  self._timer=self.after(50,self._update)
