import random

print("Hello, what is you favoirte number?")
number = input()

print("Your favorite number is "+number)

minNumber = 1
maxNumber = 100

magicNumber = random.randint(minNumber, maxNumber)

message = "This magic number is between (0) and (1)"
print(message.format(minNumber, maxNumber)
