class Stack :
    def __init__(self,ls = None):
        if ls == None :
            self.ls = []
        else : self.ls = ls

    def __str__(self):
        s = 'stack of '+ str(self.size())+' items : '
        for ele in self.ls:
            s += str(ele)+' '
        return s
    
    def delete(self,i) :
        return self.ls.remove(i)

    def items(self):
        return self.ls

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

def isOp(string) :
    if string in "+-*/" :return True
    else : return False

def postFixeval(st):
    s = Stack()
    for ele in st : 
        if not isOp(ele) : s.push(ele)
        else :
            y = str(s.pop())
            x = str(s.pop())
            s.push(eval(x + ele + y))
    return s.pop()

# /////////////////////////////////////////////
print(" ***Postfix expression calcuation***")

token = list(input("Enter Postfix expression : ").split())



print("Answer : ",'{:.2f}'.format(postFixeval(token)))