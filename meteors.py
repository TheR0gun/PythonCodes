import math
import requests

nasa=requests.get('https://data.nasa.gov/resource/gh4g-9sfh.json')
nasa_data=nasa.json()

def calc_dist(lat1,lon1,lat2,lon2):
   lat1= math.radians(lat1)
   lon1= math.radians(lon1)
   lat2= math.radians(lat2)
   lon2= math.radians(lon2)
   h= math.sin( (lat2- lat1) /2)**2 + \
   math.cos(lat1) * \
   math.cos(lat2) * \
   math.sin( (lon2 - lon1) /2) **2

   return 6372.8 * 2 *math.asin(math.sqrt(h))
my_loc=(42.023347,-88.124555)

for meteor in nasa_data:
	if not ('reclat' in meteor and 'reclong' in meteor): continue
	meteor['distance'] = calc_dist(float(meteor['reclat']), float(meteor['reclong']),my_loc[0],my_loc[1])

def get_dist(meteor):
	return meteor.get('distance',math.inf)

nasa_data.sort(key=get_dist)
print(nasa_data[0])
print(len(nasa_data))
print(len([m for m in nasa_data if 'distance' not in m]))
