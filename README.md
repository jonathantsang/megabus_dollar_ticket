## Megabus Dollar Fare Lookup
To find $1 MegaBus tickets

1. open chrome web browser
2. search the megabus tickets for any date or location
3. once the search result page finished loading
4. enable web developer mode
5. click on "Network" tab
6. on the megabus result page, click on any date to make a new request
7. under the developer window, find something like this:
https://ca.megabus.com/journey-planner/api/journeys?originId=145&destinationId=427&departureDate=2018-01-08&totalPassengers=1&concessionCount=0&nusCount=0&days=1
8. Under originId and destinationId you can find your cities and the number Megabus represents them as.

## TODO
1. do it for more days than just starting today
2. figure out how to get locations
3. error handling
4. url argument library
5. clean up scaper
