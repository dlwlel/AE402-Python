n=int(input("how many people are in class?"))
score=[]
highest=0
lowest=100
lowestname=""
highestname=""
summath=0
for i in range(n*2):
   mathscore=input("name and score?")
   score.append(mathscore)
   print(score)
   if i%2==1:
       score[i]=int(score[i])
       summath=summath+score[i]
       if highest<score[i]:
           highest=[i]
           highestname=score[i-1]
       if lowest>score[i]:
           lowest=score[i]
           lowestname=score[i-1]
print(highest,highestname)
print(lowest,lowestname)
print("average", summath/n)

