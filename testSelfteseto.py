from televisores.tv import TV
from televisores.control import Control
from televisores.marca import Marca


def testEnlazar():
    marca = Marca("Semsung")

    tv = TV(marca, True)
    control = Control()
    control.enlazar(tv)
    print(tv.getControl() != None)
    
testEnlazar()


def testEnlazarControl():
    marca = Marca("Semsung")

    tv = TV(marca, True)
    control = Control()

    control.enlazar(tv)

    print(control.getTv() != None)

testEnlazarControl()
