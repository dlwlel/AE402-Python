import random
condition=0
num=random.randint(1,20)
while condition<5:
    guess=int(input('guess the number'))
    if num==guess:
        print('correct')
        condition=6
    elif(num!=guess):
            print('incorrect')
            condition=condition+1
    elif(condition==5):
        print('u lose')
    