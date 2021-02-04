d={}
print('___________________')
print('HI')
file=input('dog.txt', 'w')
import os.path
d={}
def buildMenu():
    print('________')
    print('hi')
    print('__________')

while True:
    print('=>')
    print('1.choose a word')
    print('list the word')
    print('english translate chinese')
    print('chinese translate english')
    print('fun game')
    print('leave')
    
    sel=input('enter option')
    
    if sel=='1':
        while True:
            voc=input('add word(press 0 to leave):')
            if voc=='0':
                break 
            if voc not in d:
                    m=input('enter word')
                    d[voc]=m
            else: 
             print('word saved')
                elif sel=='2':
                    lk=sorted(d)
                    for item in lk:
                        print(item,'yes',d[item])
                    elif sel=='3':#english translate
                        voc=input('search english definition(press 0 to leave):')
                        if voc=='0':
                            break
                        if voc in d:
                            print(d[voc])
                        else:
                            print('my dictionary do  not have these words')
                        elif sel=='4': #chinese translate
                            got=False
                            ch=input('search english definition(press 0 to leave):')
                            if ch=='0'
                            break
                        for k.v in d.items():
                            if ch==v:
                                print(ch,'english definition',k)
                                got=True
                                if not got ='5'. #Try
                                score=0
                                print('total score is', len(d),'points')
                                for k,v in d.items():
                                    print(v,':')
                                    ans==k:
                                        score+=1
                                        print('coorect! you got', score,'points now')
                                    elif sel=='6'
                                    break 
                                else:
                                    print('wrong! you got', scpre, 'points now')
                                elif sel=='6'
                                break 
                            else:
                                print('incorrect, do it again')