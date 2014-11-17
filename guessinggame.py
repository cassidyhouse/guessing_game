import random
cpuNum = random.randint(1, 10)
print cpuNum
userNum = int(raw_input("Enter a number between 1 and 10: "))
guessList = []


def guess(userNum):
	if cpuNum == userNum:
		correct(guessList)

	elif cpuNum != userNum:
		while cpuNum != userNum:

			if cpuNum < userNum:
				print "Your guess is too high! Guess again"
				userNum = int(raw_input("Enter another guess: "))
				guessList.append(userNum)
				return correct(guessList)

			elif cpuNum > userNum:
				print "Your guess is too low! Guess again"
				userNum = int(raw_input("Enter another guess: "))
				guessList.append(userNum)
				return correct(guessList)

			else:
				print "Hmm, that guess returned an error."
	
	

def correct(guessList):
	guessListcount = len(guessList)

	print "Yay! You guessed correctly!"
	print "You made %d incorrect guesses before guessing correctly! Not bad!" % guessListcount
	again()
	
def again():
	again = raw_input("Would you like to play again? y/n?:  ")
	if again == "y":
		guess()
	else:
		print "Thanks for playing!"	

guess(userNum)



