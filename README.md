## Megabus Dollar Fare Lookup
To find $1 MegaBus tickets

1. Open chrome
2. Search the megabus tickets for any date or location
3. Wait for search result page to finish loading
4. Enable web developer mode
5. Click on "Network" tab
6. On the megabus result page, click on any date to make a new request
7. Under the developer window, find something like this:
https://ca.megabus.com/journey-planner/api/journeys?originId=145&destinationId=427&departureDate=2018-01-08&totalPassengers=1&concessionCount=0&nusCount=0&days=1
8. Under originId and destinationId you can find your cities and the number Megabus represents them as.

## Known cities ids

- AUSTIN = 320
- HOUSTON = 318 (NOTE: Houston has THREE different megabus stops all classified as Houston (but very far apart) so if it is $1, it may be wildly different)
- DALLAS = 317
- SAN_ANTONIO = 321

## TODO
1. do it for more days than just starting today
2. figure out how to get locations
3. error handling
4. url argument library
5. clean up scaper
