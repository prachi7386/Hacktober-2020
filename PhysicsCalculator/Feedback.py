class feedback:
    def __init__(self):
        self.fb=""
        self.name=""
        self.rate=0
    def inp(self):
        self.name=raw_input("Enter your name:")
        self.fb=raw_input("Enter your feed back:")
        self.rate=input("Enter rating out of 5:")

Obj=feedback()
Obj.inp()
fw=open("Feedbacknames.txt","a")
fw.write(Obj.name+" ")
fw.write(Obj.fb+" ")
fw.write(str(Obj.rate)+"\n")
fw.close()






    
