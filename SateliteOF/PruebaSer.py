
from DB import con
from Interpolation import data
from Interpolation import interpolation
from Interpolation import prueba
from Serial import ser
from out.CreateD import cnvrt
import os

#sudo chmod a+rw /dev/ttyACM0
os.system("sudo chmod a+rw /dev/ttyUSB0")
d = data(17)

ser = ser("/dev/ttyUSB0", 9600, 17)
while(True):
    a = ser.readStr()
    print(a)
