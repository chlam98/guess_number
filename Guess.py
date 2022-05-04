import random

def getInputFromUser():
    guess_number = 0
    while True:
        try:
            guess_number = int(input("Enter a number to guess"))
        except:
            print("Please enter a number in correct form again")
        else:
            break
    return guess_number

def startGuessing():
    secret_number = random.randint(1, 100)
    guess_count = 0;
    while True:
        guess_number = getInputFromUser()
        guess_count += 1
        if guess_number == secret_number:
            print(" You have guessed it right, the secret number is {} ".format(secret_number))
            break
        else:
            print("You have guessed it wrong, you have entered {} ".format(guess_number))
            # you need to tell people whether entered number is smaller or larger than secret number.
            if guess_number < secret_number:
                print("The entered number is smaller than the secret number")
            else:
                print("The entered number is larger than the secret number")


    print("You have guessed {} times and the secret number is {} ".format(guess_count, secret_number))

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    startGuessing()