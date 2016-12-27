import socket
HOST = '127.0.0.1'
PORT = 1234
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((HOST, PORT))
send = sock.send

def pixel(x,y,r,g,b,a=255):
    if a == 255:
        send('PX %d %d %02x%02x%02x\n' % (x,y,r,g,b))
    else:
        send('PX %d %d %02x%02x%02x%02x\n' % (x,y,r,g,b,a))

def rect(x,y,w,h,r,g,b):
    for i in xrange(x,x+w):
        for j in xrange(y,y+h):
            pixel(i,j,r,g,b)

#from PIL import Image
#def image(x,y,filename):
#    im = Image.open(filename).convert('RGB')
#    im.thumbnail((200,300), Image.ANTIALIAS)
#    _,_,w,h = im.getbbox()  
#    for x in xrange(w):
#        for y in xrange(h):
#            r,g,b = im.getpixel((x,y))
#            pixel(x,y,r,g,b)

for i in range(200, 300):
    pixel(i, i, 100, 255, 255, 255)
    pixel(300 - i, i, 100, 255, 255, 255)
