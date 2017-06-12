import random

print("Hello, what is you favoirte number?")
number = input()

print("Your favorite number is " + number)

minNumber = 1
maxNumber = 100

magicNumber = random.randint(minNumber, maxNumber)

message = "This magic number is between {0} and {1}"
print(message.format(minNumber, maxNumber))

found = False

while not found:
    print('Guess what it is?')
    guess = int(input())
    if guess == magicNumber:
        found = True
    if guess < magicNumber:
        print('To low')
    if guess > magicNumber:
        print('To high')



print("You got it!")
