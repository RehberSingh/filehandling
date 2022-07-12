from pickle import *

f=open(r'C:\Users\Rehber Singh\Desktop\Ch-5 File Handling\sports.dat','wb')
n=int(input('Enter the no. of Participants'))

for i in range(n):
    event=input('Enter the name of the event')
    participant = input('Enter the name of the participant')
    str= event + ' ~ ' + participant
    dump(str,f)
    print(str)
f.close()

g=open(r'C:\Users\Rehber Singh\Desktop\Ch-5 File Handling\athletics.dat','wb')
f=open(r'C:\Users\Rehber Singh\Desktop\Ch-5 File Handling\sports.dat','rb')
for i in range(3):
    words = load(f).split('~')
    print(words)
    if words[0]=='Cricket ':
        dump(words[1],g)
        

