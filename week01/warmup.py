def f(x,lst=[]):
    lst.append(x)
    return lst
print(f(1))
print(f(2))
nums=[1,2,3,4,5,6]
evens_sq=[x**2 for x in nums if x%2==0]
print(evens_sq)
words=["gan","transformer","ai"]
lengths={n:len(n) for n in words}
print(lengths)
class Animal:
    def __init__(self,name):
        self.name=name
class Dog(Animal):
    def __init__(self,name,breed):
        super().__init__(name)
        self.breed=breed
d=Dog("旺财","柴犬")
print(d.name)