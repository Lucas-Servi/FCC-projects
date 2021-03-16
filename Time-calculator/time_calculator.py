def add_time(start, duration, today=""):
    starttime = start.split()
    time = starttime[0].split(":")
    timeMod = starttime[1]
    timeAdd = duration.split(":")
    sum_time = [int(time[0]) + int(timeAdd[0]), int(time[1]) + int(timeAdd[1])]
    DoW= ("monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday")
  
    while sum_time[1] > 60:
        sum_time[0] +=1
        sum_time[1] -= 60
  
    days =0
    while sum_time[0] >= 12:
        if timeMod == 'PM':
            sum_time[0] -= 12
            days += 1
            timeMod = 'AM'
        elif timeMod == 'AM':
            sum_time[0] -= 12
            timeMod = 'PM'
    if sum_time[0] == 0: sum_time[0] = 12
            
    if today.lower() in DoW:
        i=0
        for day in DoW:
            if today.lower() == day:
                break
            i+=1

    if sum_time[1] < 10: sum_time[1]="0"+str(sum_time[1])
    
    #Same day and no today
    if days == 0 and today == "":
        return str(sum_time[0])+ ":"+str(sum_time[1]) + " " + timeMod
    
    #Same day and today
    elif today.lower() in DoW and days == 0:
        return str(sum_time[0])+ ":"+str(sum_time[1]) + " " + timeMod + ", " + today.capitalize()
    
    #1 day and no today
    elif days == 1 and today == "":
        return str(sum_time[0])+ ":"+str(sum_time[1]) + " " + timeMod + " (next day)"
    
    #1 day and today
    elif days == 1 and today.lower() in DoW:
        if i == 6: i=-1
        return str(sum_time[0])+ ":"+str(sum_time[1]) + " " + timeMod + ", "+ DoW[i+1].capitalize() + " (next day)"
    
    #2+ days and no today    
    elif days > 1 and today == "":
        return str(sum_time[0])+ ":"+str(sum_time[1]) + " " + timeMod + " (" + str(days)+ " days later)"
    
    else:
        i = i + (days % 7)
        if i>6: i-=7
        return str(sum_time[0])+ ":"+str(sum_time[1]) + " " + timeMod + ", "+ DoW[i].capitalize() + " ("+ str(days) +" days later)"
