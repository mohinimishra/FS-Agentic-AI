class Vehical:
    @staticmethod
    def showText(text):
        return [item.strip() for item in text.split(",")]
    
raw = "Hey this is me ,    i am learning, this static method usecase "

# static method directly you can be directly called wihtout initalization
res = Vehical.showText(raw)
print(res)
    
response = Vehical()

