hour,min = map(int, input().split())
add = int(input())
min = min+add
hour2 = min//60
hour = hour+hour2
min2 = min-hour2*60
if(hour>=24):
    hour = hour-24
print(hour,min2)