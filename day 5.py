def length(str):
    lis = list(str.split(" "))
    return len(lis[-1])
 
 

str = "ashwin is a good boy"
print("The length of last word is",length(str))

