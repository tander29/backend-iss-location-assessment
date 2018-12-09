#!/usr/bin/env python2


import requests
import time


def get_people_in_space():
    # payload = {}
    r = requests.get('http://api.open-notify.org/astros.json')
    r = r.json()
    print 'Total poeple in space:', r['number']
    for people in r['people']:
        print people['name'] + ' is on spaceship ' + people['craft']


def get_coordinates_of_iss():
    r = requests.get('http://api.open-notify.org/iss-now.json')
    r = r.json()
    current_time = r['timestamp']
    latitude = r['iss_position']['latitude']
    longitude = r['iss_position']['longitude']
    converted_time = time.strftime(
        "%D %H:%M", time.localtime((int(current_time))))
    print ('Time(Military): {}, Latitude: {}, Longitude: {}'.format(
        converted_time, latitude, longitude))


def main():
    # get_people_in_space()
    get_coordinates_of_iss()


if __name__ == "__main__":
    main()
