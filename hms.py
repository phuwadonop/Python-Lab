print("*** Converting hh.mm.ss to seconds ***")
lst_input = [int(e) for e in input("Enter hh mm ss : ").split()]
hh,mm,ss = lst_input
str_hh = str_mm = str_ss = ''

if hh < 0 or hh != int(hh) : print('hh(%d) is invalid!' %hh)
elif mm < 0 or mm > 59 or mm != int(mm) : print('mm(%d) is invalid!' %mm)
elif ss < 0 or ss > 59 or ss != int(ss) : print('ss(%d) is invalid!' %ss)

else :
    int_ans = (hh*3600) + (mm*60) + ss
    strIntAns = str(int_ans)
    ls = []
    numCout = 0
    for i in range(len(strIntAns) - 1,-1,-1):
        ls.append(strIntAns[i])
        numCout += 1
        if numCout == 3 and i != 0 : 
            ls.append(',') 
            numCout = 0
    ls.reverse()
    strIntAns = ""
    for ele in ls : strIntAns += ele

    str_ans = '{}:{}:{} = {} seconds'
    if hh < 10 : str_hh = "0" + str(hh)
    else : str_hh = str(hh)
    if mm < 10 : str_mm = "0" + str(mm)
    else : str_mm = str(mm)
    if ss < 10 : str_ss = "0" + str(ss)
    else : str_ss = str(ss)

    print(str_ans.format(str_hh,str_mm,str_ss,strIntAns))

