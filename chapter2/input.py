str_seconds = input("Please enter the number of seconds you wish to convert")
total_secs = int(str_seconds)

days = total_secs//(3600*24)

hours = total_secs//3600

secs_stil_remaining = total_secs % 3600
minutes = secs_stil_remaining //60
secs_finally_remaining = secs_stil_remaining % 60

print("Days=", days, "Hrs=", hours, "mins=", minutes, "secs=", secs_finally_remaining)
