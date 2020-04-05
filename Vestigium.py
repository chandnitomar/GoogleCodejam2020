import numpy as np

def matrixinput(order):
    #print("Enter the entries in a single line (separated by space): ")    
     matrix = []  
     t = 0
     while (t<order): 
        t += 1
        flag = 0          
        #for i in range(order):
        a = list(map(int,input().strip().split()))[:order]
        if(len(a) < order):
                for i in range(0,order-len(a)):
                    a.append(0)
        for i in a:           
            if 1<=i and i<=order:                   
                continue
            else:
                flag = 1
                break
    
        if flag == 1:
            t -= 1
            continue
        else:
            matrix.append(a)
     return matrix

def same(x):
     count = 0
     for i in range(0,len(x)):
        for j in range(i+1,len(x)):
             if x[i] == x[j]:
                 count += 1
                 break
        if count > 0:
            break
     return count

    
while True:
    testcases = int(input())
    if 1<=testcases and testcases<=100:
        break
result = []

for i in range(0,testcases):
    while True:
        order = int(input())
        if 2<=order and order<=100:
            break
    matrix = matrixinput(order)
    #print(matrix)
    mx = np.array(matrix)
    tr = mx.trace()
    #print ("trace:",tr)
    rows = np.apply_along_axis(same,axis=1, arr = mx)
    #print("Rows ",rows,sum(rows))
    cols = np.apply_along_axis(same,axis=0, arr = mx)
    #print("Cols ",cols,sum(cols))
    temp = [0,0,0,0]
    temp[0] = i
    temp[1] = tr
    temp[2] = sum(rows)
    temp[3] = sum(cols)
    result.append(temp)

result_arr = np.array(result)
for k in result_arr:
    for l in range(len(k)):
        print("Case #"+str(k[0]+1)+": "+str(k[1])+" "+str(k[2])+" "+str(k[3]))
        break

