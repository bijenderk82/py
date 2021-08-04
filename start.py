 import random
 num = random.randint
 num = random.randint(1,100)
 while True:
	print("guess a number between 1 and 100!")
	guess = input()
	i = int(guess)
	if i == num:
		print("you guess right!!!")
		break
	elif i < num:
		print("try higher")
	elif i > num:
		print("try lower")