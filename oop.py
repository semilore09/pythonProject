class Person:
     def _init_(self,name,age):
         self.name=name
         self.age=age
student1= Person()
student1.name="sola"
student1.age=12
print("my name is",student1.name)
print("I am",student1.age,"years old")
student2= Person()
student2.name="Ade"
student2.age = 13
print(student2.name,student2.age)






class Food:
    def _init_(self,classes,categories):
        self.classes= classes
        self.categories= categories
carbonhydrates= Food()
carbonhydrates.classes= ["rice","yam","cassava"]
carbonhydrates.categories= "Energy giving food"
print("Examples of carbonhydrates includes",carbonhydrates.classes)
print("They are known to be",carbonhydrates.categories)
a=["garri", "amala","fufu"]
carbonhydrates.classes.insert(0,"fufu")
carbonhydrates.classes.extend(a)
carbonhydrates.classes.count("fufu")
print(carbonhydrates.classes)


class Tempoconversion:
    def _init_(self, celcius,fahrenheit):
        self.celcius=celcius
        self.fahrenheit=fahrenheit
concel= Tempoconversion()
concel.celcius=(100)
concel.fahrenheit=(212)
result=(concel.celcius*9/5)+32
print("The value of celcius to fahrenheit is",result)
confah=Tempoconversion()
result=(concel.fahrenheit-32)*5/9
print("The value of fahrenheit to celcius is",result)








