class wow:
    def __init__(self,*arguments):
        if len(arguments) == 0:
            self.numbers = (0,0)
        else:
            self.numbers = arguments
    
    def __add__(self,other):
        print(other.numbers)
        numbers = tuple (x+y for x,y in zip(self.numbers,other.numbers))
        return wow(numbers)    

x = wow(1,3)
y = wow(2,5)
#w = wow(5,7)
z = x+y
#z=z+w
print(z.numbers[::1])
