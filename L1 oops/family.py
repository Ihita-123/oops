class family():
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
    def message(self):
        print("Happy family")

p1=family("Bob",15,"male")
p1.message()
print(p1.age)
    

p2=family("Emma",14,"female")
print(p2.gender)
