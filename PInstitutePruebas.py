hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))


mins = mins + round(dura/60)
hour = hour + round(mins/60)
print(str(hour) + ":" + str(mins))

