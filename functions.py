class Tempoconversion():
    def __init__(self, celval, fahval):
        self.celval = celval
        self.fahval = fahval
    def cel2fahwx(self):
        celsius = (self.celval*9/5)+32
        print("The value of celsius to fahrenheit is", celsius)
    def fah2cel(self):
        fahrenheit = (self.fahval-32)*5/9
        print("The value of fahrenheit to celsius is", fahrenheit)
temperature= Tempoconversion(60,140)
temperature.cel2fah()
temperature.fah2cel()


