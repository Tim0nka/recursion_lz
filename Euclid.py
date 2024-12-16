def gcd(x, y): 
    if(y == 0):  
        return x  
    else: 
        return gcd(y, x % y) 
x =int(input("Введите число ")) 
y =int(input("Введите число: ")) 
num = gcd(x, y)  
print("НОД: ") 
print(num)