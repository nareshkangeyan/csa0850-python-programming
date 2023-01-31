def countstrings(n, start):
   
    
    if n == 0:
        return 1
    cnt = 0
     
    
    for i in range(start, 5):
       
       
        cnt += countstrings(n - 1, i)
    return cnt
     
def countVowelStrings(n):
   
    return countstrings(n, 0)
 
n = roman = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}

print(countVowelStrings(n))
