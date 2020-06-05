#!/Applications/Python3.8
# -*-coding:Utf-8 -*

import os, pickle

def errorKm(e):
	try:
		try:
			km = float(input(e))
		except ValueError:
			raise ValueError("You must enter a number :")
		if km < 0:
			raise ValueError("Your number must be strictly positif :")
	except ValueError as e:
		return errorKm(e)
	return km

if __name__ == "__main__":
	try:
		f = open("theta", "rb")
		if os.stat("theta").st_size == 0:
			raise ValueError("The file is empty")
		teta = pickle.Unpickler(f).load()
		f.close()
	except FileNotFoundError:
		print("You must training your program before ask a price")
		teta = [0, 0]
	except ValueError:
		f.close()
		print("There is no data in the file, please train your program before ask a Price")
		teta = [0, 0]
	
	try:
		try:
			km = float(input("how many kilometers has your car been :"))
		except ValueError:
			raise ValueError("You must enter a number :")
		if km < 0:
			raise ValueError("Your number must be strictly positif :")
	except ValueError as e:
		km = errorKm(e)
	
	print("The price of your car is", round((teta[0] + (teta[1] * km)),2), "dollars")
