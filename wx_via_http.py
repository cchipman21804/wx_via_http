import urllib.request

# The following URL contains information regarding general access to data and products:
# https://www.weather.gov/tg/general

# The following URL contains guidelines for anonymous FTP access:
# https://www.weather.gov/tg/datahelp

# The following URL contains Email access procedures for the FTP Gateway:
# https://www.weather.gov/tg/ftpmail

# The following URL contains the latest tabular text forecast for Salisbury, MD:
# https://tgftp.nws.noaa.gov/data/forecasts/state/md/mdz003.txt

# The following URL contains the latest tabular text forecast for Georgetown, DE:
# https://tgftp.nws.noaa.gov/data/forecasts/state/de/dez003.txt

# The following URL contains the latest observations for Delaware Coastal Airport (KGED):
# http://tgftp.nws.noaa.gov/data/observations/metar/decoded/KGED.TXT

# The following URL contains the latest observations for Wicomico Regional Airport (KSBY):
# http://tgftp.nws.noaa.gov/data/observations/metar/decoded/KSBY.TXT

# The following URL contains the latest observations for Ocean City Municipal Airport (KOXB):
# http://tgftp.nws.noaa.gov/data/observations/metar/decoded/KOXB.TXT

# The following URL contains the latest observations for Wallops Flight Facility (KWAL):
# http://tgftp.nws.noaa.gov/data/observations/metar/decoded/KWAL.TXT

# Future (BIG) Project - extract dry bulb temperature, dew point, relative humidity data to retrieve outdoor air enthalpy
# from psychrometric chart lookup table
# lookup dryBulbTemp as dictionary key for 2D tuple
# lookup dewPoint in element 0 of 2D tuple
# retrieve enthalpy in element 1 of 2D tuple
# HUNDREDS OF DATA POINTS

# Concatenate rooturl and airport code to obtain full url
rooturl = "http://tgftp.nws.noaa.gov/data/observations/metar/decoded/"
kged = "KGED.TXT"
ksby = "KSBY.TXT"
kwal = "KWAL.TXT"
koxb = "KOXB.TXT"

# Ocean City Airport does not have temperature, dew point, & RH data
# koxb = "KOXB.TXT"

# Prepare menu selection loop
validInput = False
while validInput == False:
    print("\nLOCAL WEATHER OBSERVATIONS\n")
    print("1 ... Delaware Coastal Airport, Georgetown, Sussex County, DE")
    print("2 ... Wicomico Regional Airport, Salisbury, Wicomico County, MD")
    print("3 ... Wallops Flight Facility, Wallops Island, Accomac County, VA")
    print("4 ... Ocean City Municipal Airport, Ocean City, Worcester County, MD")
    #    print("n ... Ocean City Municipal Airport, Ocean City, Worcester County, MD")
    airport = input("\nPlease select an area wx forecast or 'e' to EXIT: ")

# Uncomment to debug:
#    print(airport)
#    print(f"Length: {len(airport)}")
#    print(type(airport))

# Evaluate menu selection
    if airport == '1':
        url = rooturl + kged
        validInput = True  # leave while loop

    elif airport == '2':
        url = rooturl + ksby
        validInput = True  # leave while loop

    elif airport == '3':
        url = rooturl + kwal
        validInput = True  # leave while loop

    elif airport == '4':
        url = rooturl + koxb
        validInput = True  # leave while loop

#    elif airport == 'n':
#       url = xxxxurl
#       validInput = True  # leave while loop


    elif airport.lower() == 'e':
        # Exit to Operating System
        print("\n")
        exit(0)

    else: validInput = False

# Perform http GET request for weather data
req = urllib.request.Request(url)
resp = urllib.request.urlopen(req)
respdata = resp.read()
wxdata = str(respdata)

# Find constant strings in observational weather data text and obtain index numbers to extract substrings

# Observation Date Stamp:
localDateStartIdx = wxdata.find("EDT") - 24
localDateEndIdx = wxdata.find("EDT") - 12
localDate = wxdata[localDateStartIdx:localDateEndIdx]

# Location Header:
headerStartIdx = 2
headerEndIdx = localDateStartIdx - 6
header = wxdata[headerStartIdx:headerEndIdx]

# Observation Time Stamp:
localTimeStartIdx = wxdata.find("EDT") - 9
localTimeEndIdx = wxdata.find("EDT") + 3
localTime = wxdata[localTimeStartIdx:localTimeEndIdx]

# Wind Speed:
windSpeedStartIdx = wxdata.find("Wind: ")
windSpeedEndIdx = wxdata.find("Visibility: ") - 4
windSpeed = wxdata[windSpeedStartIdx:windSpeedEndIdx]

# Visibility:
visibilityStartIdx = wxdata.find("Visibility: ")
visibilityEndIdx = wxdata.find("Sky conditions: ") - 4
visibility = wxdata[visibilityStartIdx:visibilityEndIdx]

# Sky Conditions:
skyCondxStartIdx = wxdata.find("Sky conditions: ")
skyCondxEndIdx = wxdata.find("Temperature: ") - 2
skyCondx = wxdata[skyCondxStartIdx:skyCondxEndIdx]

# Weather?

# Temperature:
temperatureStartIdx = wxdata.find("Temperature: ")
temperatureEndIdx = wxdata.find("Dew Point: ") - 2
temperature = wxdata[temperatureStartIdx:temperatureEndIdx]

# Dew Point:
dewPointStartIdx = wxdata.find("Dew Point: ")
dewPointEndIdx = wxdata.find("Relative Humidity: ") - 2
dewPoint = wxdata[dewPointStartIdx:dewPointEndIdx]

# Relative Humidity:
rhStartIdx = wxdata.find("Relative Humidity: ")
rhEndIdx = wxdata.find("Pressure (altimeter): ") - 2
relativeHumidity = wxdata[rhStartIdx:rhEndIdx]

# Pressure:
pressureStartIdx = wxdata.find("Pressure (altimeter): ")
pressureEndIdx = wxdata.find(" hPa)") + 5
pressure = wxdata[pressureStartIdx:pressureEndIdx]

# Obtain indices for:
# Pressure tendency:
pressureTendencyStartIdx = wxdata.find("Pressure tendency: ")
pressureTendencyEndIdx = wxdata.find("ob: ") - 2
pressureTendency = wxdata[pressureTendencyStartIdx:pressureTendencyEndIdx]

# Uncomment wxdata to debug:
# print("\n")
# print(wxdata)
# print("\n")

print(f"{header}")
print(f"{localDate}")
print(f"{localTime}")
print(f"{windSpeed}")
print(f"{visibility}")
print(f"{skyCondx}")
print(f"{temperature}")
print(f"{dewPoint}")
print(f"{relativeHumidity}")
print(f"{pressure}")
print(f"{pressureTendency}")
# print("\n")
