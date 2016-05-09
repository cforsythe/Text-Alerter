'''https://maps.googleapis.com/maps/api/directions/json?origin=Boston,MA&destination=Concord,MA&waypoints=Charlestown,MA|Lexington,MA&key=AIzaSyDYEI9_pHILyfzxpL-vTSGLlrklfOlZzvc'''

import urllib
import json
import re

def get_starting():
    starting = raw_input('Enter your starting address: ')
    starting.replace(' ','+')
    print(starting)
    return starting

def get_destination():
    destination = raw_input('Enter your destination: ')
    destination.replace(' ','+')
    print(destination)
    return destination

def directions(starting,destination):
    #starting="Monterey,ca" #get_starting()
    #destination="Hollister,ca" #get_destination()

    urllib.urlretrieve("https://maps.googleapis.com/maps/api/directions/json?origin="+starting+"&destination="+destination+"&key=AIzaSyDYEI9_pHILyfzxpL-vTSGLlrklfOlZzvc", "directions.json")

    with open('directions.json') as data_file:
        data = json.load(data_file)
    
    str = ['Directions: \n']

    if data["status"]=="ZERO_RESULTS":
        print("Invalid Address")
    else:
        length = len(data['routes'][0]['legs'][0]['steps'])

        for i in range(0,length):
            directions = data['routes'][0]['legs'][0]['steps'][i]['html_instructions']
            directions=directions.replace('</b>','')
            directions = directions.replace('<b>','')
            new = directions + " "
            str.append(new)
    return str
#starting ="Monterey,ca"
#destination="Hollister,ca"
#str = directions(starting,destination)
#print(str)
