import random


# A function that mix all the characters from a string
def mix(test):
    random.shuffle(test)
    return ''.join(test)


password_length = int(input('Type the password length that you need: '))
while password_length < 0:
    password_length = int(input('Please insert a valid password length (bigger than 0): '))


letter = []
# Create random letters
for i in range(1, password_length + 1):
    letter.insert(i, chr(random.randint(65, 90)))


# Create a random password mixing all the characters
password = mix(letter)
print(password)
