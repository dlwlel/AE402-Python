math=input("math percentage")
math=int(math)
english=input("english percentage")
english=int(english)
if not (math>=0 and math<=100):
    print("sike u got the wrong numba")
elif not (english>=0 and english<=100):
    print("sike u got the wrong numba")

if(math>=90 and english>=90):
    print("u get prize")
elif(math==100 or english==100):
    print("u still get prize")
else:
    print("ok")