file=open('10.jpg',"rb")
img=file.read()
file.close()
file=open("1-.jpg", "wb")
file.write(img)
file.close()
          
