class Stack :
    def __init__(self):
        self.ls = []

    def __str__(self):
        s = 'stack of '+ str(self.size())+' items : '
        for ele in self.ls:
            s += str(ele)+' '
        return s
    def items(self):
        return str(self.ls)

    def push(self,i) :
        self.ls.append(i)

    def isEmpty(self) :
        return self.ls == []
    
    def size(self) :
        return len(self.ls)

    def pop(self) :
        if self.ls == [] :
            print("Don't have item in stack.")
        else : return self.ls.pop()


print(" *** Stack implement by Python list***")

ls = [e for e in input("Enter data to stack : ").split()]

s = Stack()

for e in ls:

    s.push(e)

print(s.size(),"Data in stack : ",s.items())

while not s.isEmpty():

    s.pop()

print(s.size(),"Data in stack : ",s.items())

    
