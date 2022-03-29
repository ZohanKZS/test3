class doma():
    """описание домов"""


    def __init__(self,street,number):
        self.street=street
        self.number=number
        self.age=0
    def build(self):
        print("dom na street " + self.street + " pod nomerom " + self.number)
    def agehous(self,year):
        self.age+=year

class prosp(doma):
    def __init__(self,prospect,number):
        super().__init__(self,number)
        self.prospect = prospect


prDom=prosp("Lenina",5)
"""
dom1=doma("Moscowskaya1","20")
dom2=doma("Moscowskaya2","30")

dom1.agehous(2021)

print(dom1.age)
"""