# https://www.airnewzealand.co.nz/flights/en-nz/flights-from-auckland-to-wellington
# https://www.dthm4kaiako.ac.nz/resources/resource/74/csfg-ncea-guide-for-as91371-244/
import random
from time import sleep

# colouring
def rgb(r, g, b):
    return f"\033[38;2;{r};{g};{b}m"
Error = rgb(255,105,105)
white = rgb(255,255,255)

# stuff
# i get the number of steats from the boeing 787-8
num_full_seat = 0
num_full_seat = random.randint(0, 248)

# num_people_ask catch
def npa():
	print("We have",248-num_full_seat,"seats left ")
	while True:
		try:
			num_people = int(input("How many people are coming with you(including you)? "))	
			if num_people > 0 and num_people < 249 - num_full_seat:
				return num_people
				break
			else:
				print("exceeds the number of seats available")
		except ValueError:
			print("invald input")

# destination catch
def des():
	while True:
		try:
			destination = int(input("""Where are you traveling to?
1 for Hamilton($39.99), 2 for Rotorua($59.99), 3 for Auckland($54.99). """))	
			if destination == 1:
				destination_price = 40
				destination = "Hamilton"
				return destination_price,destination
				break
			elif destination == 2:
				destination_price = 60
				destination = "Rotorua"
				return destination_price,destination
				break
			elif destination == 3:
				destination_price = 55
				destination = "Auckland"
				return destination_price,destination
				break
			else:
				print("invald input")
		except ValueError:
			print("invald input")

# flight class catch
def seat():
	while True:
		try:
			fclass = int(input("""What class of flight would you like?
1 for first class(2x$), 2 for Business class(1.6x$), 3 for economy class(1.1x$). """))
			if fclass == 1:
				fclass = "First class"
				class_price = 2
				return class_price,fclass
				break
			elif fclass == 2:
				fclass = "Business class"
				class_price = 1.5
				return class_price,fclass
				break
			elif fclass == 3:
				fclass = "economy class"
				class_price = 1
				return class_price,fclass
				break
			else:
				print("invald input")
		except ValueError:
			print("invald input")

# welcome user
print(f"{white}Hello and welcome to Waikato airborn,")
name = input("What is your name? ")
print("Hello",name,"I hope you are having a good day. ")
num_people_ask = npa()
destination_price = des()
fclass = seat()
leave_day = input(f"""{Error}when do are you planing on departing? 
'today', 'tomorrow', or the 'day after'. {white}""")
leave_day = leave_day.strip().lower()
		
# seats left
num_full_seat += num_people_ask

# leaving logic
if leave_day == "today":
	leave_dayn = 1
elif leave_day == "tomorrow":
	leave_day_n = 2
elif leave_day == "day after":
	leave_day_n = 3

#full price
full_price = 0
def work(full_price, destination_price, num_people_ask, fclass, num_full_seat):
	full_price += (destination_price[0] * num_people_ask)
	full_price *= fclass[0]
	if num_full_seat > 75:
		full_price *= 1.2
	return full_price
	print(full_price)
work(full_price, destination_price, num_people_ask, fclass, num_full_seat)

# user data
print("""name:""",name,"""
Full steats:""",num_full_seat,"""
people""",num_people_ask,"""
destination:""",destination_price[1],"""
Seat Class:""",fclass[1],"""
full steats:""",num_full_seat,"""
Price:""",work(full_price, destination_price, num_people_ask, fclass, num_full_seat),"""
""")
