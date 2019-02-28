import time
import random
from DB import con
x = 0
y = 0
z = 0
con = con(database="datrotprueba")
con.est_con()
while(True):
    con.ex_ins("INSERT INTO rot(x, y, z) VALUES (" +
               str(x) + "," + str(y) + "," + str(z) + ")")
    x = round(random.uniform(-140, 140), 3)
    y = round(random.uniform(-140, 140), 3)
    z = round(random.uniform(-140, 140), 3)
    print("INSERT INTO rot(x, y, z) VALUES (" +
          str(x) + "," + str(y) + "," + str(z) + ")")
    time.sleep(1)
