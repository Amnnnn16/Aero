class planes:
    def __init__(self,fno,mod,cap,route,ticket):
        self.fno=fno
        self.mod=mod
        self.cap=cap
        self.route=route
        self.ticket=ticket
        with open("aero.txt","w") as t:
            t.write(f"Route of flight {self.route}") #route at 1st line

        with open("aero.txt","a") as t:
            t.write(f"\n flight no is {self.fno} model is {self.mod} moving {self.route}")
    def viewroute(self):
        with open("aero.txt") as t:
            f=t.readline()
            print(f)

    def getinfo(self):
         with open("aero.txt") as t:
            f=t.readline()
            print(f)
            f=t.readline()
            print(f)

a=planes(123,12,12,"dehli to lucknow",2)
a.viewroute()