#! /usr/bin/env python
from geopy.geocoders import Nominatim

def get_nominatim_coordonates(entities: list) -> list:
    cities_found = entities
    coordonates = []
    geolocator = Nominatim(user_agent="spaCy_cities_finder")
    
    for city in cities_found:
        location = geolocator.geocode(city)
        if location:
            coordonates.append([city, location.latitude, location.longitude])
    return coordonates
