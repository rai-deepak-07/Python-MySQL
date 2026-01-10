import time

timestamp = time.strftime('%H')
timestamp=int(timestamp)
if(timestamp<12 and timestamp>0):
    greeting = "Good Morning"
elif (timestamp>=12 and timestamp<16):
    greeting = "Good Afternoon"
elif (timestamp>=16 and timestamp<24):
    greeting = "Good Evening"
else:
    greeting = "Good Morning"

name  = input("Enter Your Name:")
print("Hello {0}, {1}".format(name, greeting))