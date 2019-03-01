
from DB import con
from Interpolation import data
from Interpolation import interpolation
from Interpolation import prueba
from Serial import ser
from out.CreateD import cnvrt
import os

#sudo chmod a+rw /dev/ttyACM0
os.system("sudo chmod a+rw /dev/ttyUSB0")
d = data(16)
intrp = interpolation(16, 60)
outTxt = cnvrt()
db = con(host = "192.168.0.101",database = "Satelite", user = "fernando", password = "1234")
db.est_con()

ser = ser("/dev/ttyUSB0", 9600, 16)
while(True):
    a = ser.readline()
    #print(a)
    if(a != 0):
        d.setdata(a)
        intrp.ins(d)
        #intrp.getEst()
        (times,data,est) = intrp.getData()
        outTxt.mat2txt(data, "data.txt")
        outTxt.mat2txt(est, "est.txt")
        outTxt.arr2txt(times, "times.txt")
        res = intrp.getLReg()
        #query = ("INSERT INTO val(p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,p11,p12,p13,p14,p15,p16,p17) VALUES ('"+str(res[0])+"','"+str(res[1])+"','"+str(res[2])+"','"+str(res[3])+"','"+str(res[4])+"','"+str(res[5])+"','"+str(res[6])+"','"+str(res[7])+"','"+str(res[8])+"','"+str(res[9])+"','"+str(res[10])+"','"+str(res[11])+"','"+str(res[12])+"','"+str(res[13])+"','"+str(res[14])+"','"+str(res[15])+"')")
        queryV2 = ("CALL Insert_date('"+str(res[0])+"','"+str(res[1])+"','"+str(res[2])+"','"+str(res[3])+"','"+str(res[4])+"','"+str(res[5])+"','"+str(res[6])+"','"+str(res[7])+"','"+str(res[8])+"','"+str(res[9])+"','"+str(res[10])+"','"+str(res[11])+"','"+str(res[12])+"','"+str(res[13])+"','"+str(res[14])+"','"+str(res[15])+"')")
        #print(query)
        db.ex_ins(queryV2)
