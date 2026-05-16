class Vehical:
    color="gray"
    power="450cc"
    
    def showDetail(self):
        return(f"The color of the bike is {self.color} and power is {self.power}")

veical_detail = Vehical()
print({veical_detail.showDetail()}) 

print(Vehical.showDetail(veical_detail))