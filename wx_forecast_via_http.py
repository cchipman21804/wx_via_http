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
# rooturl = "http://tgftp.nws.noaa.gov/data/observations/metar/decoded/"
# kged = "KGED.TXT"
# ksby = "KSBY.TXT"
# kwal = "KWAL.TXT"
# koxb = "KOXB.TXT"

rooturl = "https://tgftp.nws.noaa.gov/data/forecasts/state/"
inlandSussex = "de/dez003.txt"
delawareBeaches = "de/dez004.txt"
easternShoreMD = "md/mdz003.txt"
marylandBeaches = "md/mdz025.txt"
easternshoreVA = "va/vaz099.txt"

# Prepare menu selection loop
validInput = False
while validInput == False:
    print("\nZONE AREA WEATHER FORECASTS\n")
    print("1 ... Inland Sussex County, DE --- (DEZ003)")
    print("2 ... Delaware Beaches ----------- (DEZ004)")
    print("3 ... Wicomico County, Maryland -- (MDZ003)")
    print("4 ... Maryland Beaches ----------- (MDZ025)")
    print("5 ... Accomack County, Virginia -- (VAZ099)")
#    print("2 ... Wicomico Regional Airport, Salisbury, Wicomico County, MD")
#    print("3 ... Wallops Flight Facility, Wallops Island, Accomac County, VA")
#    print("n ... Ocean City Municipal Airport, Ocean City, Worcester County, MD")
    airport = input("\nPlease select a zone # or 'e' to EXIT: ")

# Uncomment to debug:
#    print(airport)
#    print(f"Length: {len(airport)}")
#    print(type(airport))

# Evaluate menu selection
    if airport == '1':
        url = rooturl + inlandSussex
        validInput = True  # leave while loop

    elif airport == '2':
        url = rooturl + delawareBeaches
        validInput = True

    elif airport == '3':
        url = rooturl + easternShoreMD
        validInput = True  # leave while loop

    elif airport == '4':
        url = rooturl + marylandBeaches
        validInput = True

    elif airport == '5':
        url = rooturl + easternshoreVA
        validInput = True  # leave while loop

#     elif airport == '4':
#        url = rooturl + koxb
#        validInput = True  # leave while loop

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

# Uncomment to debug:
# wxdata = str(respdata)
# print(wxdata)

# print(respdata)
# print(type(respdata))

# Returns decimal ASCII codes of those specific bytes
# print(respdata[0])
# print(respdata[1])
# print(respdata[2])

# Returns length of http data in bytes
# print(f"\n{len(respdata)} bytes")

# Returns status of forecast file object
# print(f"forecast file: {forecast}")

# Open forecast.txt file, write the data byte by byte into forecast file & close the file
forecast = open ("/Users/kb3pm/forecast.txt",'wb')
forecast.write(respdata)
forecast.close()
exit(0)


# Find constant strings in observational weather data text and obtain index numbers to extract substrings
# Observation Date Stamp:
# localDateStartIdx = wxdata.find("EDT") - 24
# localDateEndIdx = wxdata.find("EDT") - 12
# localDate = wxdata[localDateStartIdx:localDateEndIdx]

# Uncomment to debug:
# print("\n")
# print(wxdata)
# print("\n")
# print(f"{header}")
