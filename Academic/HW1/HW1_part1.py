import math as m
jupiter_diameter = 88846
jupiter_distance = 483632000
jupiter_volume = (4/3)* m.pi*((jupiter_diameter/2)**3)

earth_diameter = 7926
earth_distance = 92957100
earth_volume = (4/3)* m.pi*((earth_diameter/2)**3)


sun_diameter = 864938
sun_volume = (4/3)* m.pi*((sun_diameter/2)**3)

speed_light = 186000
print('Sun-to-Jupiter radius ratio:', round(sun_diameter/jupiter_diameter,2))
print('Sun-to-Earth radius ratio:', round(sun_diameter/earth_diameter,2))
print('Jupiter-to-Earth radius ratio:', round(jupiter_diameter/earth_diameter,2),'\n')
print('Jupiter-to-Earth Sun distance ratio:', round(jupiter_distance/earth_distance,2))
print('Sun-to-Jupiter volume ratio:', round(sun_volume/jupiter_volume,2))
print('Sun-to-Earth volume ratio:', round(sun_volume/earth_volume,2))
print('Jupiter-to-Earth volume ratio:', round(jupiter_volume/earth_volume,2),'\n')
print('Sun to Earth light travel time in minutes:', round((earth_distance/speed_light/60),2))
print('Sun to Jupiter light travel time in minutes:', round((jupiter_distance/speed_light/60),2))


