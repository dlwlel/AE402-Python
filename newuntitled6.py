import random
count=0
num=random.randint(1,10)
while count <5:
    guess=int(input('guess a number'))
    count=count=1
    if num==guess:
        print('correct')
        print('correct',count, 'times')
    elif guess>num:
        print('too big')
        print('wrong', count 'times')
    else:
        print('too small')
        print('wrong', count 'times')