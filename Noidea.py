nm = input().split() 
main_lst = input().split()
A = set(input().split())
B = set(input().split())

happiness = 0
for e in main_lst :

    if e in A : happiness = happiness + 1
    if e in B : happiness = happiness - 1

print(happiness)