print ("Selin Kovaç 150406011 HM#1")
import math  
def Distance(x1,y1,x2,y2):  
     dist = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)  
     return dist  
print "Please calculate the distance between given points"

print "SK1= (2,3)"
print "SK2= (6,7)"
print "the distance between SK1 and SK2:", Distance(2,3,6,7)
print "SK3= (0,7)"
print "SK4= (0,5)"
print "the distance between SK3 and SK4:",Distance(0,7,0,5)
print "SK5= (3,0)"
print "SK6= (3,0)"
print "the distance between SK5 and SK6:",Distance(3,0,3,0)
print "SK7= (6,0)"
print "SK8= (3,0)"
print "the distance between SK7 and SK8:",Distance(6,0,3,0)

