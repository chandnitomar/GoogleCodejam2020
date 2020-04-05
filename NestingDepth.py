import numpy as np
def check(string) : 
    p = set(string) 
    s = {0, 1} 
    if s == p or p == {0} or p == {1}: 
        return 1
    else : 
        return 0

def binarystring(s):
    i=0
    while i<len(s):
        #print("i at start:",i)
        if s[i] == 1 and(i+1)<len(s) and s[i+1] == 0:
            #print("if")
            s[i] = "(1)"
           # print("i in if:",i)
        #print(" ",s[i],s[i+1],i,len(s))
        elif (s[i] == 1) and ((i+1)<len(s)) and (s[i+1] == 1) :
            #print("elif")
            s[i] = "(1"
            #print("i in elif: ",i)
            while  (i+1)<len(s) and s[i+1] !=0 :
                i+=1
                #print("i in while: ",i)
            s[i] = "1)"
            i+=1
        elif s[len(s)-1] == 1:
            s[len(s)-1] = "(1)"
        else:
            i+=1
        #print("i at last: ",i)
        
    listToStr = ''.join([str(elem) for elem in s]) 
    return listToStr

def lhs(s,temp,maxpos,paranthesis):
    if(temp-2 == -2):
        temp_to_return = temp
        for i in range(s[temp]):
            s[temp] = "("+str(s[temp])+")"
            paranthesis -= 1
        return s,temp_to_return
    else:
        while (temp-2)>-1 and s[temp-2] <= s[temp-1]:
            temp -= 1
        temp_to_return = temp
        temp = temp -1
        while (temp < maxpos and paranthesis>0):
            """temp_next_arg= s[temp+1]"""
            arg = int(s[temp])
            temp_arg = arg
            
            for i in range(temp_arg):
                s[temp] = "("+str(s[temp])
                paranthesis -= 1
            nex_arg = temp+1
            while nex_arg<= maxpos and paranthesis>0:
                temp_next_arg = s[nex_arg]
                for nex in range(s[nex_arg]-temp_arg):
                    temp_arg = temp_next_arg
                    s[nex_arg] = "("+str(s[nex_arg])
                    paranthesis -= 1
                nex_arg += 1
                
            temp = nex_arg
        return s,temp_to_return

def rhs(s,temp,maxpos,paranthesis):
    if(temp+2 == len(s)+1 ):
        if(s[temp-1] < s[temp]):
             temp_to_return = temp
             dup_stemp = s[temp]
             s[temp] = ""
             for i in range(dup_stemp):
                s[temp] = s[temp]+")"
                paranthesis -= 1
             return s,temp_to_return
            
        else:
            temp_to_return = temp
            for i in range(s[temp]):
                s[temp] = "("+str(s[temp])+")"
                paranthesis -= 1
            return s,temp_to_return
             
    else:
        while (temp+2)<len(s)+1 and s[temp+2] <= s[temp+1]:
            temp += 1
        temp_to_return = temp
        temp = temp +1
        while (temp > maxpos and paranthesis>0):
            """temp_next_arg= s[temp+1]"""
            print("Here temp is: ",temp)
            arg = int(s[temp])
            temp_arg = arg
            s[temp] = " "
            for i in range(temp_arg):
                s[temp] = s[temp]+")"
                paranthesis -= 1
            nex_arg = temp-1
            while nex_arg>= maxpos and paranthesis>0:
                temp_next_arg = int(s[nex_arg])
                s[nex_arg] = " "                
                for nex in range(temp_next_arg-temp_arg):
                    temp_arg = temp_next_arg
                    s[nex_arg] = s[nex_arg]+")"
                    paranthesis -= 1
                nex_arg -= 1
                
            temp = nex_arg
        return s,temp_to_return

def decimalstring(s):
    print("hi there")
    dup_s = s.copy()
    print("dup_s:",dup_s)
    maxpos = s.index(max(s))
    temp = maxpos
    paranthesis = max(s)
    print("Parathesis: ",paranthesis)
    modified_s = []
    temp_returned = 0
    modified_s_rhs=[]
    temp_returned_rhs=0 
    modified_s,temp_returned = lhs(s,temp,maxpos,paranthesis)
    print("yeh 4 hona chahiye tha: ",modified_s[temp_returned-2])
    print("modified_s:",modified_s)
    print("temp_returned: ",temp_returned)
    if(temp_returned-2 != -1):
        modified_s,temp_returned = lhs(modified_s,temp_returned-2,temp_returned-2,modified_s[temp_returned-2])
    print("dup_s:",dup_s)
    modified_s_rhs,temp_returned_rhs = rhs(dup_s,temp,maxpos,paranthesis)
    if(temp_returned+2 != len(s)+1):
        modified_s,temp_returned = rhs(modified_s_rhs,temp_returned_rhs+2,temp_returned+2,modified_s_rhs[temp_returned_rhs+2])
    print("modified_s_rhs:",modified_s_rhs)
    print("temp_returned_rhs: ",temp_returned_rhs)
    
    print(modified_s)
    listToStr = ''.join([str(elem) for elem in modified_s]) 
    return listToStr
        
        



result = []
while True:
    testcases = int(input())
    if 1<=testcases and testcases<=100:
        break

for i in range(0,testcases):
    while True:
        s = list(map(int,list(input())))
        if 1<=len(s) and len(s)<=100:
            break
    print(s)
    checked = check(s)
    s_dash = " "
    #print(checked)
    if checked == 1:
        #print("hi")
        s_dash = binarystring(s)
        #print(s_dash)
    elif checked ==0 :
        s_dash = decimalstring(s)
        print(s_dash)
    temp = [0,0]
    temp[0] = i+1
    temp[1] = s_dash
    result.append(temp)



result_arr = np.array(result)
for k in result_arr:
    for l in range(len(k)):
        print("Case #"+str(k[0])+": "+k[1])
        break 


