# STEP 308 = DATETIME CHALLENGE

# The Portland-based company you work for just opened two new branches. One is in New York City, the other in London. They need a very simple program to find out if the branches are open or closed. The hours of both branches are 9:00 a.m.-5:00 p.m. in their own time zone.

# Using IDLE, create a new file.

# Import the datetime module and any others to aid in time zone calculations.
import datetime
from datetime import datetime
from zoneinfo import ZoneInfo

# Create a script that will find out the current times in the Portland HQ and NYC and London branches.
PortlandHQ = datetime.now()
PortlandHour_Minute = (PortlandHQ.strftime("%H:%M:%S on %B %d"))
Portland_AM_PM = (PortlandHQ.strftime("%#I %p"))            # In Windows specifically, the # symbol strips any leading zeros from before the hour.


NYC = datetime.now(tz=ZoneInfo('America/New_York'))
NewYorkCity = (NYC.strftime("%H:%M:%S on %B %d"))
NewYork_AM_PM = (NYC.strftime("%#I %p"))            # If working in Linux, a - symbol is needed instead of the # , but that - symbol would throw an error in Windows.

LondonOffice = datetime.now(tz=ZoneInfo('Europe/London'))
London = (LondonOffice.strftime("%H:%M:%S on %B %d"))
London_AM_PM = (LondonOffice.strftime("%#I %p"))




# Compare each branch's current time to their operating hours to see if they are open or closed by checking for if between 9 AM and 5 PM:
if int(PortlandHQ.strftime("%H")) < 9:
    Port_open_close = "CLOSED"
elif int(PortlandHQ.strftime("%H")) >= 18:
    Port_open_close = "CLOSED"
else:
    Port_open_close = "OPEN"


if int(NYC.strftime("%H")) < 9:
    NYC_open_close = "CLOSED"
elif int(NYC.strftime("%H")) >= 18:
    NYC_open_close = "CLOSED"
else:
    NYC_open_close = "OPEN"


if int(LondonOffice.strftime("%H")) < 9:
    London_open_close = "CLOSED"
elif int(NYC.strftime("%H")) >= 18:
    London_open_close = "CLOSED"
else:
    London_open_close = "OPEN"





# Print out to the screen the three branches and whether they are open or closed.
print("\nAll of our branches are open from 9 AM to 5 PM in their respective time zones.")

print("\nOn a 24 hour clock, the time at headquarters in Portland, Oregon, is currently: ", PortlandHour_Minute)
print("Portland HQ is " + Port_open_close + " now, because it is currently " + Portland_AM_PM + " there.")

print("\nOn a 24 hour clock, the time in New York City is currently: ", NewYorkCity)
print("The branch in New York City is " + NYC_open_close + " now, because it is currently " + NewYork_AM_PM + " there.")

print("\nOn a 24 hour clock, the current time in London is: ", London)
print("The London branch is " + London_open_close + " now, because it is currently " + London_AM_PM + " there.")

# HELPFUL LINK:   https://www.w3schools.com/python/python_datetime.asp