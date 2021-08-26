print(" *** Wind classification *** ")


		# Speed (km/h)		ระดับพายุ
		# 0-51.99			Breeze
		# 52.00-55.99		Depression
		# 56.00-101.99	    Tropical Storm
		# 102.00-208.99	    Typhoon
		# >= 209			Super Typhoon


speed = float(input('Enter wind speed (km/h) : '))

if speed >= 0 and speed < 52 : print('Wind classification is Breeze.')
elif speed < 55.99 : print('Wind classification is Depression.')
elif speed < 102 : print('Wind classification is Tropical Storm.')
elif speed < 209 : print('Wind classification is Typhoon.')
else : print('Wind classification is Super Typhoon.')