f=open(r'C:\Users\Rehber Singh\Desktop\Ch-5 File Handling\contacts.txt','r')
g=open(r'C:\Users\Rehber Singh\Desktop\Ch-5 File Handling\contacts.csv','w')

for i in range(2):
    words = f.readline().split()
    str= words[0]+','+words[1]
    g.write(str)
    g.write('\n')
f.close()
g.close()