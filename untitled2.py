grade=int(input("How many grades do you have"))
gradelist=[]
for i in range(0,grade):
   gradelist.append(int(input("what are your grades")))
gradelist.sort(reverse=True)
print(gradelist)