def ishappynumber(n):
    digit = sum = 0
    while(n>0):
        digit =n % 10
        sum = sum + (digit*digit)
        n = n//10
    return sum
num=int(input("enter a number:"))
result = num
while(result !=1 and result !=4):
    result=ishappynumber(result)
if(result == 1):
    print(num,"is a happy number!!!")
else:
    print(num,"is an unhappy number!!!")
