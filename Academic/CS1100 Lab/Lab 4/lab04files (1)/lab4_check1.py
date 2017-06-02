from PIL import Image
im2x2 = Image.new('RGB',(512,512))
ca = Image.open('ca.jpg')
im = Image.open('im.jpg')
hk = Image.open('hk.jpg')
bw = Image.open('bw.jpg')

ca.resize(256,256)
im.resize(256,256)
hk.resize(256,256)

bw.resize(256,256).show()