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

NYC = datetime.now(tz=ZoneInfo('America/New_York'))
NewYorkCity = (NYC.strftime("%H:%M:%S on %B %d"))

LondonOffice = datetime.now(tz=ZoneInfo('Europe/London'))
London = (LondonOffice.strftime("%H:%M:%S on %B %d"))

# Print out to the screen the three branches and whether they are open or closed.
print("\nThe time at headquarters in Portland, Oregon, is currently: ", PortlandHour_Minute)
print("Portland HQ is ")

print("\nThe time in New York City is currently: ", NewYorkCity)
# print("The branch is NYC is ")

print("\nThe current time in London is: ", London)
# print("The London branch is ")

# HELPFUL LINK:   https://www.w3schools.com/python/python_datetime.asp