import serial

ser = serial.Serial("COM3", 57600)

#-------------------
can = 10
ac = -1
arr = []
data = []
#-------------------

for i in range(can):
    arr.append(0)

for i in range(5):
    data.append(arr)


def cnvdata(line):
    (num,pts) = line.split(";")
    print(num)
    print(pts)
    pts = pts.split(",")

    for i in range(len(pts)):
        pts[i] = pts[i].rstrip()
        pts[i] = pts[i].split(':')
        pts[i][0] = int(pts[i][0])
        pts[i][1] = float(pts[i][1])
        print(pts[i])

    return (num,pts)

cont = 0
numdat = 0

line = str(ser.readline(), 'utf-8')
(num,pts) = cnvdata(line)

while cont < 5:
    line = str(ser.readline(), 'utf-8')
    (num,pts) = cnvdata(line)
    val = True

    if ac != num:
        for i in range(len(arr)):
            arr[i] = 0
        ac = num
        val = False

    if ac == num:
        print("Paso")
        for i in range(len(pts)):
            if(arr[pts[i][0]] == 0):
                arr[pts[i][0]] = pts[i][1]
                numdat = numdat + 1
        if numdat == can:
            cont = cont + 1
            print("Registro " + str(cont) +   " terminado")
    else:
        for i in range(len(arr)):
            arr[i] = 0
        ac = num





#-----------------

print("--------------------------------------")

while(True):
    line = str(ser.readline(), 'utf-8')

    (num,pts) = line.split(";")
    print(num)
    print(pts)
    pts = pts.split(",")

    for i in range(len(pts)):
        pts[i] = pts[i].rstrip()
        pts[i] = pts[i].split(':')
        pts[i][0] = int(pts[i][0])
        pts[i][1] = float(pts[i][1])
        print(pts[i])
