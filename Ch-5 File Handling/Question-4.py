f=open(r'C:\Users\Rehber Singh\Desktop\Ch-5 File Handling\poem.txt','r')

def counter(words):
    counter_1 = 0
    counter_2 = 0
    n = len(words)
    for i in range(n):
        if words[i]== 'to':
            counter_1 += 1
        elif words[i] == 'the':
            counter_2 += 1
    return counter_1,counter_2
to = 0
the = 0
while True:
    words = f.readline().split()
    if words == []:
        break
    else:
        a,b=counter(words)
        to += a
        the += b
print('The count of "to" in file is', to)
print('The count of "the" in file is', the)

     



