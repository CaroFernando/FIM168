import serial

class ser:

    def rstrt(self):
        self.dat = []
        self.val = []
        for i in range(0,self.ndat):
            self.val.append(False)

    def __init__(self, puer, rate, ndat):
        self.ser = serial.Serial(puer, rate)
        self.ndat = ndat
        self.dat = []
        self.val = []

        self.rstrt()
        self.file = open("reg.txt", "w")

    def cnvdata(self, line):
        #print(num)
        #print(pts)
        pts = line.split(",")

        for i in range(len(pts)):
            pts[i] = pts[i].rstrip()
            pts[i] = pts[i].split(';')
            pts[i][0] = int(pts[i][0])
            pts[i][1] = float(pts[i][1])

        return pts

    def readStr(self):
        line = str(self.ser.readline(), 'utf-8')
        return line

    def readline(self):
        try:
            #print("readline")
            line = str(self.ser.readline(), 'utf-8')
            print(line)
            self.file.write(line)

            pts = self.cnvdata(line)
            tem = 0
            for i in pts:
                if(self.val[i[0]] == True):
                    tem = self.dat
                    self.rstrt()
                    self.dat.append(i)
                    self.val[i[0]] = True
                else:
                    self.dat.append(i)
                    self.val[i[0]] = True

            return tem
        except Exception as e:
            print(e)
            return self.readline()
