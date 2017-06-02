
import panoramio as pan

urls = pan.getPhotos('Eiffel Paris France',5) # Return 5 pictures of Eiffel Tower 
im = pan.openphoto(urls[0]) # Open the first image URL
im.show()

im2 = pan.openphoto(urls[2]) # Open the first image URL
im2.show()
