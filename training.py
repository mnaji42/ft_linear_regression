#!/Applications/Python3.8
# -*-coding:Utf-8 -*

import sys, pickle

learn_rate = 0.1

def training(X, Y):
	
	#Transform all price and mileage between 0 and 1:
	mileage = [float(X[i])/max(X) for i in range(len(X))]
	price = [float(Y[i])/max(Y) for i in range(len(Y))]

	#Gradient descent:
	m = len(mileage)
	t0 = 0.0
	t1 = 0.0
	grad_t1 = 0.0

	while grad_t1 != sum(((t0 + mi * t1 - pi) * mi) for mi, pi in list(zip(mileage, price))):
		grad_t0 = sum((t0 + mi * t1 - pi) for mi, pi in list(zip(mileage, price)))
		grad_t1 = sum(((t0 + mi * t1 - pi) * mi) for mi, pi in list(zip(mileage, price)))
		t0 = t0 - (learn_rate * ((1.0 / m) * grad_t0))
		t1 = t1 - (learn_rate * ((1.0 / m) * grad_t1))

	#Retransform all price and mileage
	t0 = t0 * max(Y)
	t1 = t1 * (max(Y) / max(X))

	return [t0, t1]

if __name__ == "__main__":

	if len(sys.argv) != 2:
		print("Usage : python3 training.py [data_file]")
	else:
		with open(sys.argv[1], "r") as f:
			data = f.readlines()
			i = 1
			try:
				header = data[0].strip().split(",")
				if header[0] != "km" or header[1] != "price":
					raise NameError
				X = []
				Y = []
				while i < len(data):
					data[i] = data[i].strip()
					data[i] = data[i].split(",")
					X.append(int(data[i][0]))
					Y.append(int(data[i][1]))
					assert X[i - 1] >= 0 and Y[i - 1] >= 0
					i += 1
			except AssertionError:
				print("A price or a kilometer can't be negativ")
			except:
				print("Your file is not well formated you must write only numbers like this:\nkm,price\n[kilometer1],[price1]\n[kilometer2],[price2]\n[kilometer3],[price3]\n[kilometer4],[price4]")
			else:
				print("training...")
				[t0, t1]= training(X, Y)
				print("training success with theta_0 = {} and theta_1 = {}".format(t0, t1))
				with open("theta", "wb") as f:
					pickle.Pickler(f).dump([t0, t1])
				print("File theta save with success")
