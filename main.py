import colorama

import time

print("Welcome to the \033[32mSEARCH FOR THE EVIL CEO\033[39m\nOnce upon a time an evil CEO took the money of his company, he has taken the money and hidden in his large mansion.\nWell what are you waiting for? Get seaarching!")


# part 1
user = 0
while user != 2:
	user = int(input("which floor would you like to look in   1, 2, 3? "))
	if user == 1 or user == 3:
		print("hmmm.... no sign of any mad CEO")
		continue
	elif user == 2:
		print("Hey! There is muddy boots all over the floor, lets look around this floor")
		break
	else:
		print("Detective! Now is not time to play silly games!")
		continue


# part 2

while user != 2:
	user = int(input("which area would you like to look in:  living room (1), office (2), bedroom area (3)? "))
	if user == 1 or user == 2:
		print("hmmm.... no sign of any mad CEO")
		continue
	elif user == 3:
		print("Hey! The mad CEO just entered here!")
		break
	else:
		print("Detective! Now is not time to play silly games!")
		continue

while user != 2:
	user = int(input("which room would you like to look in:   Clue: 0  | 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25.    [Gee how big is this place?!]   ? "))
	if user < 17 or user > 17 and user :
		print("hmmm.... no sign of any mad CEO")
		continue
	elif user == 17:
		print("Hey! The mad CEO just entered here!")
		break
	elif user == 0:
		print("what number is the age that")
	else:
		print("Detective! Now is not time to play silly games!")
		continue