import json
import os
import phonenumbers
from phonenumbers import carrier, geocoder
from opencage.geocoder import OpenCageGeocode
import folium
import webbrowser  # Import the webbrowser module

# Load configuration from config.json
with open('config.json', 'r') as config_file:
    config = json.load(config_file)

######################################
####### Config Includes ##############
######################################
number = config["number"]
key = config["key"]
save = config["save"]
######################################
####### Config Includes ##############
######################################

pepnumber = phonenumbers.parse(number)
location = geocoder.description_for_number(pepnumber, "en")

service_pro = phonenumbers.parse(number)
geocoder_instance = OpenCageGeocode(key)
query = str(location)
results = geocoder_instance.geocode(query)

lat = results[0]['geometry']['lat']
lng = results[0]['geometry']['lng']

myMap = folium.Map(location=[lat, lng], zoom_start=9)
folium.Marker([lat, lng], popup=location).add_to(myMap)

myMap.save(save)

print('''       ___             ___           _           
      / _ \___  ___   /   \___  __ _| | ___ _ __ 
     / /_\/ _ \/ _ \ / /\ / _ \/ _` | |/ _ \ '__|
    / /_\\\  __/ (_) / /_//  __/ (_| | |  __/ |   
    \____/\___|\___/___,' \___|\__,_|_|\___|_|   
      ''')
print("          ╔══════════════════════════════╗   ")
print(f"          ║   Location: {location}         ║   ")
print(f"          ║   Service: {carrier.name_for_number(service_pro, 'en')}           ║   ")
print(f"          ║   {lat, lng}   ║   ")
print("          ╚══════════════════════════════╝   ")
print()
print(f'          saved to {save}')

# Open the HTML file in the default web browser
webbrowser.open(save)
os.system('pause>null')