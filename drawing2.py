print('*** Fun with Drawing ***')
num = int(input('Enter input : '))
for y in range(2*num-2,-1*(2*num-1),-1) :
    for x in range(-1*(2*num-2),2*num-1,1) :
       if abs(x) <= abs(y) : print('#',end="") if y % 2 == 0 else print(".",end="")
       else : print('#',end="") if x % 2 == 0 else print(".",end="")
    print("\n",end='')