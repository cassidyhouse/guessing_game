import random

cpuNum = random.randint(1, 10)

userNum = int(raw_input("Enter a number between 1 and 10: "))

guessList = []

while cpuNum != userNum:
	if cpuNum == userNum:
		pass

	elif cpuNum < userNum:
		print "Your guess is too high! Guess again"
		userNum = int(raw_input("Enter another guess: "))
		guessList.append(userNum)

	elif cpuNum > userNum:
		print "Your guess is too low! Guess again"
		userNum = int(raw_input("Enter another guess: "))
		guessList.append(userNum)

	else:
		print "Hmm, that guess returned an error."


print "Yay! You guessed correctly!"
guessListcount = len(guessList)
print "You made %d incorrect guesses before guessing correctly! Not bad!" % guessListcount
print cpuNum
print userNum