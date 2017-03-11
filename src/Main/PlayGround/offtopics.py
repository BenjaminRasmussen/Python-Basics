import math
from matplotlib import pyplot
##drawing a circle
x = []
y = []
tan = []
count = []
##found that putting epsion to pi or pi/2 makes the spirals straight.
##  While making epison > 1 makes the spiral more traditional
epsion = math.pi
i = 0.0
while i < 361:
    ##At this point i said fuck it and made a sprial instead.
    i+= epsion
    x.append(math.cos(i))
    y.append(math.sin(i))
    print ("ENTITLED: " + str(i))
##pyplot.title("Floating point numbers" + " - Epsion: " + str(epsion))
pyplot.scatter(x,y)
pyplot.show()

##Using integer to generate the spiral will show how inaccurate integer math is compared to float math
## when using decimal numbers or just general simulation
j = int
v = []
w = []
for j in range(1, 361, 1):
    v.append(math.cos(j)*j)
    w.append(math.sin(j)*j)
    print (j)
##pyplot.title("Integer - Epsion : 1")
##pyplot.plot(v,w)
pyplot.show()