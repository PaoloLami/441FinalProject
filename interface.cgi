#!/usr/bin/python37all
#Paolo Lami, ENME441 Lab5

import cgi
import stepper

#Get data from html
data = cgi.FieldStorage()
angle = data.getvalue('angle')

#Write in file depending on which submission was selected

#If an angle was submitted, write the angle
if ('move' in data): 
  with open('angle.txt', 'w') as f:
    f.write(str(angle)) 

#If the reset button was submitted, set angle to 0
elif ('zero' in data): 
  with open('angle.txt', 'w') as f: 
    f.write(str(0)) 

print('Content-type: text/html\n\n')
print('<html>')
print('<form action="/cgi-bin/interface.cgi" method="POST">')
print('<TH COLSPAN="4"><BR><H5>Angle Adjustment</H5>')
print('0 <input type="range" name="angle" min ="0" max="90" value ="45"/> 90 <br>')
print('<br> <input type="submit" name="move" value="angle">')
print('Reset angle to 0:<br>')
print('<input type="submit" name="zero" value="zero">')
print('</form>')