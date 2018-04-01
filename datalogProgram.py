from adxl345 import ADXL345
import datetime
import time

adxl345 = ADXL345()
file =open("log8.txt","w")
    
axes = adxl345.getAxes(True)
print "ADXL345 on address 0x%x:" % (adxl345.address)
print ("   x = %.3fG" % ( axes['x'] ))
print ( "   y = %.3fG" % ( axes['y'] ))
print ("   z = %.3fG" % ( axes['z'] ))

status=True

while status:
    axes = adxl345.getAxes(True)
    x=( axes['x'])
    y=( axes['y'])
    z=( axes['z'] )
    X=str(x)
    Y=str(y)
    Z=str(z)
    log=str(datetime.datetime.utcnow())
    data= log+','+X+','+Y+','+Z+'\n'
    #data= i+','+X +'\n'
    print (data)
    file.write(str(data))
    time.sleep(0.1)
file.close();
