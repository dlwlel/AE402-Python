n=int(input('how many people are in your class'))
score=[]
name=[]
lowest=('100')
highest=('0')
highestname=""
lowestname=""
summath=('0')
for i in range(0,2*n):
    mathname=(input(""))
    mathscore=int(input("name and score"))
    name.append(mathname)
    print(score)
    if i%2==1:
        score[i]=int(score[i])
        summath=summath+score
        if highest<score[i]:
            highest=score[i]
        lowest=mathscore
            lowestname=mathname
            print('lowest', 'lowestname')
            print('highest', 'highestname')
            print('average',summath/n)
            