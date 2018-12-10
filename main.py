#!/usr/bin/env python2
# -*- coding: utf-8 -*-s


import requests
import time
import turtle


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
    latitude = r['iss_position']['latitude'].encode('ascii', 'ignore')
    longitude = r['iss_position']['longitude'].encode('ascii', 'ignore')
    converted_time = time.strftime(
        "%D %H:%M", time.localtime((int(current_time))))
    print ('Time(Military): {}, Latitude: {}, Longitude: {}'.format(
        converted_time, latitude, longitude))
    a = latitude
    b = longitude
    return (b, a)


def draw_iss():
    longitude, latitude = get_coordinates_of_iss()
    screen = turtle.Screen()
    screen.register_shape('./iss.gif')
    screen.setup(width=720, height=360, startx=0, starty=0)
    screen.bgpic('./map.gif')
    screen.setworldcoordinates(-180, -90, 180, 90)
    iss = turtle.Turtle()

    iss.shape('./iss.gif')
    iss.penup()
    print(longitude, latitude)
    iss.goto(float(longitude), float(latitude))
    draw_indy()
    turtle.done()


def draw_indy():
    indy_lat = 39.9784
    indy_lon = -89.1581
    data = {'lon': indy_lon, 'lat': indy_lat}
    r = requests.get('http://api.open-notify.org/iss-pass.json', params=data)
    r = r.json()
    timestamp = r['response'][0]['risetime']
    timestamp = time.strftime(
        "%D %H:%M", time.localtime((int(timestamp))))
    print(timestamp)
    indy = turtle.Turtle()
    indy.shape('circle')
    indy.color('yellow')
    indy.turtlesize(.5, .5, .5)
    indy.penup()
    indy.goto(indy_lon, indy_lat)
    indy.write(timestamp, move=False, align='left',
               font=('Arial', 8, 'normal'))
    indy.pendown()


def main():
    get_people_in_space()
    # get_coordinates_of_iss()
    draw_iss()


if __name__ == "__main__":
    main()
