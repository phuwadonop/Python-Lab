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

s = Stack()

inp = input('Enter Input : ').split(',')

for ele in inp :
    if ele[0] == 'A' : 
        if s.isEmpty() : s.push(int(ele[2:]))
        else : 
            storange = s.items();
            e_del = [e for e in storange if e < int(ele[2:])]
            for e in e_del : s.delete(e)
            s.push(int(ele[2:]))
    else : print(s.size())