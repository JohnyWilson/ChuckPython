# Guess secret number over iterations



try:
    x = int(raw_input("Guess a number: "))
except:
    print "The number entered is invalid. Please try again"
    exit()

High_end = 100; Low_end = 0

while True:
    Guess = (High_end+Low_end)/2; print('Is your secret number '+ str(Guess) + '?')
    response = (raw_input('Enter your response: '))
    if response == "h":
        High_end = Guess
    elif response == "l":
        Low_end = Guess
    elif response == "c":
        print('Game over. Your secret number was: ' + str(Guess))
        break
    else:
        print("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")