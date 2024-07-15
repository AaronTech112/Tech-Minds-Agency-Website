from datetime import datetime
import pytz

# Get the current time in the USA
usa_tz = pytz.timezone('America/New_York')
current_time = datetime.now(usa_tz).strftime("%H:%M:%S")

print("Current time in USA (New York) is:", current_time)