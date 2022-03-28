class Control:
    
    def __init__(self):
        self._tv=""
        
    def enlazar(self, tv):
        self._tv=tv
        tv.setControl(self)
    
    def setTv(self, tv):
        self._tv=tv
        
    def getTv(self):
        return self._tv
    
    def turnOn(self):
        self._tv.turnOn()
    def turnOff(self):
        self._tv.turnOff()
        
    # def getEstado(self):
    #     return self._tv._estado
    
    def canalUp(self):
        if self._tv.getCanal() == 120 or self._tv.getEstado() == False:
            return
        else:
            self._tv.canalUp()
            
    def canalDown(self):
        if self._tv.getCanal() == 1 or self._tv.getEstado() == False:
            return
        else:
            self._tv.canalDown()
            
    def volumenUp(self):
        if self._tv.getVolumen() == 7 or self._tv.getEstado() == False:
            return
        else:
            self._tv.volumenUp()
            
    def volumenDown(self):
        if self._tv.getVolumen() == 0 or self._tv.getEstado() == False:
            return
        else:
            self._tv.volumenDown()
            
    def setCanal(self, num):
        if num<=120 and num>=1 and self._tv.getEstado() == True:
            self._tv.setCanal(num)
        else:
            return