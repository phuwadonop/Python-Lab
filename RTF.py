print('*** Rabbit & Turtle ***')
d,Vr,Vt,Vf = input('Enter Input : ').split()
d = float(d)
Vr = float(Vr)
Vt = float(Vt)
Vf = float(Vf)

if d > 5000 or Vf > 5000 or Vt > 5000 or Vr > 5000 or Vr > Vt or Vf < Vt or Vf < Vr :
    print('Input incorrect. please enter input again !')

else :
    df = Vf * (d/(Vt-Vr))
    print('%.2f'%df)