
class cnvrt:
    def __init__(self):
        self.arch = ""
    
    def mat2txt(self, mat, dir):
        file = open(dir, "w")
        
        for i in mat:
            line = ""
            for j in i:
                line = line + str(j) + ","
            file.write(line+"\n")
    
    def arr2txt(self, arr, dir):
        file = open(dir, "w")
        line = ""
        for j in arr:
            file.write(str(j)+"\n")
    
    