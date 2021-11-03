from turtle import *
import json
import turtle
import time
import urllib.request
screen = turtle.Screen()
while True:
    url = "http://api.open-notify.org/iss-now.json"
    response = urllib.request.urlopen(url)
    result = json.loads(response.read())
    location = result["iss_position"]
    lat = float(location["latitude"])
    lon = float(location["longitude"])
    print("latitude: ", lat)
    print("longitude: ", lon)
    url = "http://api.open-notify.org/astros.json"
    response = urllib.request.urlopen(url)
    result = json.loads(response.read())






    screen.setup(720, 360)
    screen.setworldcoordinates(-180, -90, 180, 90)
    screen = turtle.Screen()
    image = r"H:\Yr 8\code club\iss-setup.gif"
    screen.bgpic(image)
    image2 = r"H:\Yr 8\code club\iss.gif"
    turtle.goto(lon, lat)
    screen.addshape(image2)
    turtle.shape(image2)
    turtle.setheading(90)
    turtle.goto(lon, lat)




