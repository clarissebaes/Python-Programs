mins = float(input("Minutes ==> "))
print(round(mins))
secs = float(input("Seconds ==> "))
print(round(secs))
miles = float(input("Miles ==> "))
print(miles,"\n")

total_secs = (mins*60 +secs)
pace_secs = (total_secs/miles)
pace_mins = int(pace_secs//60)
final_sec = int(pace_secs%60)

hours = (total_secs/(60**2))
speed = round(miles/hours,2)

print('Pace is', pace_mins, 'minutes and', final_sec, 'seconds per mile.')
print('Speed is', speed, 'miles per hour.') 

