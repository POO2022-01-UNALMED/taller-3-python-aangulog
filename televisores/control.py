class Control:
    
    def __init__(self):
        self._tv=""
        
    def enlazar(self, tv):
        self._tv=tv
        tv.control = self
    
    def setTv(self, tv):
        self._tv=tv
        
    def getTv(self):
        return self._tv
    
    def turnOn(self):
        self._tv._estado = True
    def turnOff(self):
        self._tv._estado = False
        
    def getEstado(self):
        return self._tv._estado
    
    def canalUp(self):
        if self._tv._canal == 120 or self._tv._estado == False:
            return
        else:
            self._tv._canal += 1
            
    def canalDown(self):
        if self._tv._canal == 1 or self._tv._estado == False:
            return
        else:
            self._tv._canal-=1
            
    def volumenUp(self):
        if self._tv._volumen == 7 or self._tv._estado == False:
            return
        else:
            self._tv._volumen+=1
            
    def volumenDown(self):
        if self._tv._volumen == 0 or self._tv._estado == False:
            return
        else:
            self._tv._volumen-=1
            
    def setCanal(self, num):
        if num<=120 and num>=1 and self._tv._estado == True:
            self._tv._canal = num
        else:
            return