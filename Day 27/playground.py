#####################  unlimited arguments / positional args #########################
""" def add(*args):
    #acess arg example:
    #args[1]
    sum = 0
    for x in args:
        sum += x
    print(sum)

add(1,2,3,4,5) 
"""

######################  unlimited keyword arguments #########################
""" def calculate(n,**kwargs):
    print(kwargs)
    # for key,value in kwargs:
    #     print(key)
    #     print(value)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)

calculate(2,add=3,multiply=5)

class Car:
    #classes - when using keyword arguments like "**kw"
    def __init__(self, **kw):
        # instead of kw["key"] use kw.gey("key") -> avoid crash
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.colour = kw.get("colour")
        self.seats = kw.get("seats") 

car = Car(model="GT")
print(car.make)
print(car.model)
"""