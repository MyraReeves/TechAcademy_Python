# STEP 308 = DATETIME CHALLENGE

# The Portland-based company you work for just opened two new branches. One is in New York City, the other in London. They need a very simple program to find out if the branches are open or closed. The hours of both branches are 9:00 a.m.-5:00 p.m. in their own time zone.

# Using IDLE, create a new file.

# Import the datetime module and any others to aid in time zone calculations.
import datetime
import zoneinfo
from datetime import datetime, timedelta, timezone
from zoneinfo import ZoneInfo

# Create a script that will find out the current times in the Portland HQ and NYC and London branches. Then, compare that time with each branch's hours to see if they are open or closed.
PortlandHQ = datetime.now()
PortlandHour_Minute = (PortlandHQ.strftime("%H:%M:%S on %B %d"))
Portland_AM_PM = (PortlandHQ.strftime("%I %p"))

NYC = datetime.now(tz=ZoneInfo('America/New_York'))
NewYorkCity = (NYC.strftime("%H:%M:%S on %B %d"))
NewYork_AM_PM = (NYC.strftime("%I %p"))

LondonOffice = datetime.now(tz=ZoneInfo('Europe/London'))
London = (LondonOffice.strftime("%H:%M:%S on %B %d"))
London_AM_PM = (LondonOffice.strftime("%I %p"))

# Calculating before 09 AM in each time zone or after 05PM in each time zone:
Portland_HourONLY = (PortlandHQ.strftime("%I %p"))
NYC_HourONLY = (NYC.strftime("%I %p"))
London_HourONLY = (LondonOffice.strftime("%I %p"))


for t in range(1, 8): Closed_before9AM = "CLOSED"
for t in range(9, 18): Open_between9and5 = "OPEN"
for t in range(17, 25): Closed_after5PM = "CLOSED"


# Loop to check for between 09 AM and 05 PM:
if PortlandHQ.strftime("%H") == t in range(1,9):
    print("Portland is CLOSED")
elif PortlandHQ.strftime("%H") == t in range(9,18):
    print("Portland is OPEN")
else:
    print("It is after 5pm in Portland")


if NYC.strftime("%H") == t in range(1,9):
    print("It is before 9am in New York")
elif PortlandHQ.strftime("%H") == t in range(9,18):
    print("New York is OPEN")
else:
    print("It is after 5pm in New York")





# Print out to the screen the three branches and whether they are open or closed.
print("\nAll of our branches are open from 9 AM to 5 PM in their respective time zones.")

print("\nOn a 24 hour clock, the time at headquarters in Portland, Oregon, is currently: ", PortlandHour_Minute)
print("Portland HQ is " + " now, because it is currently " + Portland_AM_PM + " there.")

print("\nOn a 24 hour clock, the time in New York City is currently: ", NewYorkCity)
print("The branch in NYC is " + " now, because it is currently " + NewYork_AM_PM + " there.")

print("\nThe current time in London is: ", London)
print("The London branch is " + " now, because it is currently " + London_AM_PM + " there.")

# HELPFUL LINK:   https://www.w3schools.com/python/python_datetime.asp