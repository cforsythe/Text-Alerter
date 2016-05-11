import urllib
import json
import re

def directions(starting,destination):
    #starting="Monterey,ca" #get_starting()
    #destination="Hollister,ca" #get_destination()

    urllib.urlretrieve("https://maps.googleapis.com/maps/api/directions/json?origin="+starting+"&destination="+destination+"&key=AIzaSyDYEI9_pHILyfzxpL-vTSGLlrklfOlZzvc", "directions.json")

    with open('directions.json') as data_file:
        data = json.load(data_file)
    
    finaldir = ["Directions: "]

    if data["status"]=="ZERO_RESULTS":
        print("Invalid Address")
    else:
        length = len(data['routes'][0]['legs'][0]['steps'])

        for i in range(0,length):
            directions = data['routes'][0]['legs'][0]['steps'][i]['html_instructions']
            directions=directions.replace('</b>','')
            directions = directions.replace('<b>','')
            new = directions + " "
            finaldir.append(new)
    return finaldir