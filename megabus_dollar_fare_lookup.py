#!/usr/bin/env python3.4
# -*- coding: utf-8 -*-
import datetime
#import scrapy
import json
import sys
# import os
import calendar
# bypass megabus cloudflare protection
import cloudscraper

TO_WRITE = {}

STCATHARINES = 427
TORONTO      = 145
AUSTIN = 320
HOUSTON = 318

DEBUG = "&totalPassengers=1&concessionCount=0&nusCount=0&otherDisabilityCount=0&wheelchairSeated=0&pcaCount=0&days=1"

def get_data(orig, dest, departDate):

    """
    example link
    https://us.megabus.com/journey-planner/api/journeys?
    originId=320&destinationId=318&departureDate=2022-05-02&totalPassengers=1&concessionCount=0&nusCount=0
    &otherDisabilityCount=0&wheelchairSeated=0&pcaCount=0&days=1
    """
    # arguments for link
    args = {"originId": "320",
            "destinationId": "318",
            "totalPassengers": "1"
            }
    url = "https://us.megabus.com/journey-planner/api/journeys?originId={}&destinationId={}&departureDate={}".format(orig,dest,departDate) + DEBUG
    # url = 'https://ca.megabus.com/journey-planner/api/journeys?originId={}&destinationId={}&departureDate={}&totalPassengers=1&concessionCount=0&nusCount=0&days=1'.format(orig, dest, departDate)

    scraper = cloudscraper.create_scraper()  # returns a CloudScraper instance
    price_json = json.loads(scraper.get(url).text)

    # journeys = price_json['dates'][0]['journeys'] ##obselete on 9/15/2017
    journeys = price_json['journeys']

    return journeys

def print_cheap_trips(journeys):
    for j in journeys:
        price = j['price']
        date = j['departureDateTime']
        date_str = date.split('T')[0]
        time_str = date.split('T')[1]

        time = datetime.datetime.strptime(time_str, "%H:%M:%S")
        time_str = time.strftime("%I:%M %p")

        date_split = date_str.split('-')
        day = datetime.date(year =int(date_split[0]),
                            month=int(date_split[1]),
                            day  =int(date_split[2]))
        week_day = day.weekday()

        if price < 5:
            deal = "{} {} = ${}  {}".format(date_str, time_str, price, calendar.day_name[week_day])
            print(deal)
            TO_WRITE[date_str] = deal


def search_ticket(days_from_today, orig, dest):
    today = datetime.date.today()

    for day in range(days_from_today):
        date = today + datetime.timedelta(day)

        journeys = get_data(orig, dest, str(date))
        print_cheap_trips(journeys)

# write to a file for lookup
def write_file():
    with open("times.txt", 'w') as f:
        for key, value in TO_WRITE.items():
            f.write('%s:%s\n' % (key, value))

print("==== From Austin to HOUSTON: ====")
search_ticket(days_from_today = 120,
              orig            = AUSTIN,
              dest            = HOUSTON)

write_file()

input("Press enter to exit ;)")
