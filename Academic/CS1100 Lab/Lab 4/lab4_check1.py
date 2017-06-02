from PIL import Image
im2x2 = Image.new('RGB', (512,512))
ca = 'ca.jpg'
capt = Image.open(ca)
capt.show()