a=input("enter the month")
b=int(input("enter the date"))
if a in('jan','feb','mar'):
    season='summer'
elif a in('apr','may','jun'):
    season='spring'
elif a in('july','aug','sep'):
    season='autumn'
else:
    season='winter'
if(a=='march') and(b>20):
    season='summer'
elif(a=='june') and(b>21):
    season='spring'
elif(a=='sep')and (b>22):
    season='autumn'
elif(a=='dec')and(b>21):
    season='winter'
print("season is",season)
