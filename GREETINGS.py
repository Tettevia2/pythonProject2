import datetime
now = datetime.datetime.now()
hour = now.hour

if hour < 12 :
    greeting = "Good morning"
elif hour < 18 :
    greeting = "Good afternoon"
else:
    greeting = "Good evening"
print("{}".format(greeting))



