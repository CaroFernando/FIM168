import time

class data:
	def __init__(self, num):
		self.num = num
		self.arr = []
		for i in range(0, num): self.arr.append(0)

	def setdata(self, mat):
		self.arr = []
		for i in range(0, self.num): self.arr.append(None)
		for pt in mat:
			self.arr[pt[0]] = pt[1]

	def getarr(self):
		return self.arr

class interpolation:
	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.ind = 0
		self.data = []
		self.est = []
		self.times = []

		self.time1 = time.time()

		for i in range(0,y):
			self.data.append([])
			self.est.append([])
			self.times.append(0)

			for j in range(0,x):
				self.est[i].append(False)
				self.data[i].append(0)

	def val(self, d):
		res = []
		for i in range(0, len(d)):
			if(d[i] == None or d[i] == 0): res.append(i)
		#print("Miss: ", res)
		return res

	def corr(self, dat):
		ok = False
		ac = self.ind - 1
		res = 0
		op = []
		t = []
		while(ok == False):
			if(ac != self.ind):

				if(self.est[ac][dat]):
					op.append(self.data[ac][dat])
					t.append(self.times[ac])
					
				ac = ac - 1

				if(ac < 0):
					ac = self.y - 1
			else:
				ok = True
		return (t, op)

	def ins(self, arr):
		if self.ind < self.y:
			self.data[self.ind] = arr.getarr()

			res = []
			for i in range(0, self.x): res.append(True)
			val = self.val(arr.getarr())

			for i in val:
				ret = self.corr(i)
				(x, y) = ret
				if(len(y) < 2):
					if(self.ind - 1 < 0):
						self.data[self.ind][i] = self.data[self.y - 1][i]
					else:
						self.data[self.ind][i] = self.data[self.ind - 1][i]

					res[i] = False
				else:
					xsum = 0
					ysum = 0
					
					for j in range(0, len(x)):
						xsum = xsum + x[j]
						ysum = ysum + y[j]

					xprom = xsum/len(x)
					yprom = ysum/len(y)

					num = 0
					den = 0

					for j in range(0, len(x)):
						num = num + ((x[j] - xprom) * (y[j] - yprom))
						den = den + ((x[j] - xprom) * (x[j] - xprom))

					m = num / den

					#print(xprom, yprom)
					b = yprom - (m * xprom)

					file = open("lr.txt", "w")

					for j in ret:
						line = ""
						for k in j:
							line = line + str(k) + ","
						file.write(line+"\n")
					
					#print(m, b)

					self.data[self.ind][i] = m * (time.time() - self.time1) + b
					res[i] = False

			self.est[self.ind] = res
			self.times[self.ind] = time.time() - self.time1

			self.ind = self.ind + 1
		else:
			self.ind = 0
			self.ins(arr)
		file = open("index.txt", "w")
		file.write(str(self.ind))


	def getLReg(self):
		if(self.ind - 1 < 0): return self.data[self.y]
		else: return self.data[self.ind - 1]
	
	def getData(self):
		return (self.times, self.data, self.est)

	def getEst(self):
		print("-----------Estatement---------------")
		print("Index: " + str(self.ind))
		for i in range(len(self.data)):
			print(int(self.times[i]),self.data[i], self.est[i])
		print("------------------------------------")

def prueba():
	a = [[1,2],[0,3],[2,1]]
	A = data(3)
	A.setdata(a)

	b = [[1,2],[0,1],[2,1.5]]
	B = data(3)
	B.setdata(b)

	c = [[1,1],[0,2]]
	C = data(3)
	C.setdata(c)

	print(B.getarr())

	intrp = interpolation(3, 5)
	intrp.getEst()
	for i in range(0,4):intrp.ins(A)
	intrp.getEst()
	intrp.ins(B)
	intrp.getEst()
	intrp.ins(C)
	intrp.getEst()

	print(intrp.getDat())
