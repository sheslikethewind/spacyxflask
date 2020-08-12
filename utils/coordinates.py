#! /usr/bin/env python
from geopy.geocoders import Nominatim

def get_coordinates(entities: list) -> list:
    cities_found = entities
    coordinates = []
    geolocator = Nominatim(user_agent="spaCy_cities_finder")
    
    for city in cities_found:
        location = geolocator.geocode(city)
        if location:
            coordinates.append([city, location.latitude, location.longitude])
    return coordinates
