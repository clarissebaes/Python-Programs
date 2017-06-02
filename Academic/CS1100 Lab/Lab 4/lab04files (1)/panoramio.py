""" 

    This module contains functions that are used to return pictures from a given location.

"""

import json
from urllib import request
import io
from PIL import Image

def getPhotos_box(min_long, min_lat, max_long, max_lat,num_photos=20):
    '''
        Get Photos takes the number of photos requested and four points:
        the the minimum longitude, the minimum lattitude, the maximum 
        longitude and the maximum lattitude. 
        Returns a list of URLs.
    '''
    # Initialize empty photos array
    photos = []

    # Set url with right variables. Currently handles number of photos,
    # with a min and max longitude and lattitude
    request_url = "http://www.panoramio.com/map/get_panoramas.php?set=public&from=0&to="\
            +str(num_photos)+"&minx="+str(min_long)+"&miny="+str(min_lat)\
            +"&maxx="+str(max_long)+"&maxy="+str(max_lat)+"&size=medium&mapfilter=true"
    # Query the API with a get request
    r = request.urlopen(request_url).read()
    # Decode the JSON. API returns a dictionary with 'count', 
    # 'has_more', 'map_location', and 'photos'
    data = json.loads(r.decode('utf-8'))
    photos_data = data["photos"]

    for photo in photos_data:
        photos.append(photo["photo_file_url"])
    # Return list of URLS
    return photos

def get_address(address):
    """ 
        Given an address string, it returns a tuple containing the lat/lon values 
        corresponding to the given address.

    """

    try:
        url = "http://nominatim.openstreetmap.org/"\
              "search?q=%s&format=json&polygon_geojson=1&addressdetails=0"
        address = address.replace(' ','+')
        
        x = request.urlopen(url%address).read()
        line = json.loads(x.decode('utf-8'))
        res = line[0]
        return float(res['lat']), float(res['lon'])
    except:
        return 0,0

def getPhotos(address,num_photos=20, increment=0.0025):
    """
        Wrapper around the Panaromio call, first finds the latitude and longitude
        of an address, and puts a box around it with the given increment.
        Larger increments are recommended for less popular places.

    """
    lat1, long1 = get_address(address)
    return tuple(getPhotos_box(long1-increment, lat1-increment,\
                         long1+increment, lat1+increment, num_photos))

def openphoto(url):
    ''' Take a URL and open it as an image and return the image'''
    file = request.urlopen(url)
    im_io = io.BytesIO(file.read())
    im = Image.open(im_io)
    return im


if __name__ == '__main__':

    #urls = getPhotos_box(-180,-90,180,90,20)
    #urls = getPhotos_box(2.35,48.85,3,49,5)
    #urls = getPhotos('Eiffel Tower Paris France',5)
    urls = getPhotos('Rensselaer Polytechnic Institute', 20, 0.01)

    print(urls)
    for url in urls:
        im = openphoto(url)
        im.show()
