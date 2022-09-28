import time
from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent='geo_api_exe')

def get_adress(x):
   index, row = x
   time.sleep(1) 
   response = geolocator.reverse(row['query']) # query
   address = response.raw['address'] # API call

   try:     
       road = address['road'] if 'road' in address else 'NA' # getting the road info
       house_number = address['house_number'] if 'house_number' in address else 'NA' # getting the house number info
       
       return road, house_number
   except:
       return None, None
