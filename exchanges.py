def exchanges(arr):
    if len(arr)==1:
        return [arr] 
    else:
        a=arr[0] 
        p=exchanges(arr[1:]) 
        r=[]  
        for pp in p: 
            for i in range(len(pp)):
                tmp=pp[0:i]+[a]+pp[i:]
                r.append(tmp)
            r.append(pp+[a])    
        return r
 
n=int(input("Введите количество элементов списка от 1 до: "))        
print(exchanges([i for i in range(1,n+1)]))