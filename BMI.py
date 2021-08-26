h,w = input('Enter your High and Weight : ').split()

h = float(h)
w = float(w)

BMI =  w/(h*h)

if BMI < 18.50 : print('Less Weight')
elif BMI < 23 : print('Normal Weight')
elif BMI < 25 : print('Morethan Normal Weight')
elif BMI < 30 : print('Getting fat')
else : print('Fat')