class Budget:
    def __init__(self,budgeted,actual,differences):
        self.budgeted = budgeted
        self.actual = actual
        self.differences = differences
    def food(self):
        Rice = 10000
        Beans = 5000
        indomie = 3000
        Total = (Rice + Beans + indomie)
        print(Total)
    def clothing(self):
        Shoes = 150000
        Bags = 5000
        Wristwatch = 20000

