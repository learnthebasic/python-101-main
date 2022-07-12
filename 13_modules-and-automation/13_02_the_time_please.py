# Use a built-in Python module to tell you the current date and time.
# Research online, so you can print it in a readable manner.

import datetime as dt

now = dt.datetime.now()

date = now.strftime("%y-%m-%d")
time = now.strftime("%H:%M:%S")

print("today date is {a:}. Time now is {b:}".format(a=date,b=time))