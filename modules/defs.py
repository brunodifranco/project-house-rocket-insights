import time
from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent='geo_api_exe')

def get_adress(x):
   index, row = x
   time.sleep(1) # Tempo entre uma requisição e outra, para não sobrecarregar a API
   response = geolocator.reverse(row['query']) # Passa a query
   address = response.raw['address'] # Chamada API

   try: # Pega os valores da requisição e retorna       
       road = address['road'] if 'road' in address else 'NA'
       house_number = address['house_number'] if 'house_number' in address else 'NA'
       
       return road, house_number
   except:
       return None, None