from sense_hat import SenseHat
from time import sleep
sense = SenseHat()

r = (255, 0, 0)
g = (0, 255, 0)
b = (0, 0, 255)
k = (0, 0, 0)
w = (255, 255, 255)
c = (0, 255, 255)
y = (255, 255, 0)
o = (255, 128, 0)
n = (255, 128, 128)
p = (128, 0, 128)
d = (255, 0, 128)
l = (128, 255, 128)

rmon4 = [k, k, k, w, w, w, k, k,
         k, k, w, w, w, w, w, k,
         k, k, w, w, w, w, w, k,
         w, w, w, w, w, w, w, w,
         k, k, k, k, k, k, k, k,
         c, k, k, c, k, k, c, k,
         k, k, k, k, k, k, k, k,
         k, c, k, k, c, k, k, c
]	
sense.set_pixels(rmon4)	
A = input("Enter rain or thunder to shw the aimation:\n")
if (A=="rain"):
    r = (255, 0, 0)
    g = (0, 255, 0)
    b = (0, 0, 255)
    k = (0, 0, 0)
    w = (255, 255, 255)
    c = (0, 255, 255)
    y = (255, 255, 0)
    o = (255, 128, 0)
    n = (255, 128, 128)
    p = (128, 0, 128)
    d = (255, 0, 128)
    l = (128, 255, 128)

    rmon5 = [k, k, k, w, w, w, k, k,
            k, k, w, w, w, w, w, k,
            k, k, w, w, w, w, w, k,
            w, w, w, w, w, w, w, w,
            c, k, k, c, k, k, c, k,
            k, k, k, k, k, k, k, k,
            k, c, k, k, c, k, k, c,
            k, k, k, k, k, k, k, k
    ]	
    r = (255, 0, 0)
    g = (0, 255, 0)
    b = (0, 0, 255)
    k = (0, 0, 0)
    w = (255, 255, 255)
    c = (0, 255, 255)
    y = (255, 255, 0)
    o = (255, 128, 0)
    n = (255, 128, 128)
    p = (128, 0, 128)
    d = (255, 0, 128)
    l = (128, 255, 128)

    rmon4 = [k, k, k, w, w, w, k, k,
            k, k, w, w, w, w, w, k,
            k, k, w, w, w, w, w, k,
            w, w, w, w, w, w, w, w,
            k, k, k, k, k, k, k, k,
            c, k, k, c, k, k, c, k,
            k, k, k, k, k, k, k, k,
            k, c, k, k, c, k, k, c
    ]
    i=-100
    while i<10:
        sense.set_pixels(rmon5)
        sleep(0.2)
        sense.set_pixels(rmon4)
        sleep(0.2) 	       
        i+=1
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		