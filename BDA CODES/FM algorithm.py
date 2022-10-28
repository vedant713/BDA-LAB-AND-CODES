stream=[1,2,3,4,5,6,4,2,5,9,1,6,3,7,1,2,2,4,2,1]
print('Using Flajolet Martin Algorithm:')
import time
start_time = time.time()

maxnum=0
for i in range(0,len(stream)):
    val= bin((1*stream[i] + 6) % 32)[2:]
    
    sum=0
    for j in range(len(val)-1,0,-1):
        
        if val[j]=='0':
            sum+=1
        else:
            break
    if sum>maxnum:
        maxnum=sum
        
print('distict elements', 2**maxnum)
print("--- %s seconds ---" % (time.time() - start_time))