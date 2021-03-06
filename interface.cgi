#!/usr/bin/python37all
#Paolo Lami and Jake Crossan, ENME441 Final Project

import cgi
import time

#Get data from html
data = cgi.FieldStorage()
angle = data.getvalue('angle')
power = data.getvalue('power')

#Write in file depending on which submission was selected

#If an angle was submitted, write the angle
if ('launch' in data): 
  with open('angle.txt', 'w') as f:
    f.write(str(angle)) 
  with open('power.txt','w') as f:
    f.write(str(power))
  time.sleep(4) 
  
  with open('angle.txt', 'w') as f: 
    f.write(str(0)) 
  with open('power.txt', 'w') as f: 
    f.write(str(0))  


#If the turn off button was submitted, set angle to 0
elif ('off' in data): 
  with open('angle.txt', 'w') as f: 
    f.write(str(0)) 
  with open('power.txt', 'w') as f: 
    f.write(str(0)) 

print('Content-type: text/html\n\n')
print('<html>')
print('<form action="/cgi-bin/interface.cgi" method="POST">')
print('<h1 ALIGN="CENTER">Pong Playing Robot</h1><p ALIGN="CENTER">')
print('Instructions: Select angle of launch (0-90) and power (Low, Medium, High) before launching the ball.<br></br>')
print('<TABLE BORDER="5"    WIDTH="50%"   CELLPADDING="4" CELLSPACING="3">')
print('<TR><TH COLSPAN="4"><BR><H3>Launcher</H3></TH></TR>')
print('<TR style="height:100px"> <TH COLSPAN="4"><BR><H5>Angle Adjustment:</H5>')
print('0 <input type="range" name="angle" min ="0" max="90"') 
print('oninput="this.nextElementSibling.value = this.value"/>') 
print('<output>45</output><br><H5>Power:</H5>')
print('Low <input type="range" name="power" min ="1" max="3"/> High <br></TH> </TR>')
print('<TR ALIGN="CENTER" style="height:100px">')
print('<TD><img src="https://atlas-content-cdn.pixelsquid.com/stock-images/red-plastic-cup-n1KXoxC-600.jpg" alt="Red Cup"') 
print('width="80" height="80"><br>Target<br></TD></TR></TABLE><br></br>')
print('<input type="submit" name = "launch" value="Launch">')
print('<br></br>')
print('If you wish to turn off the game, click the button below:<br></br>')
print('<input type="submit" name = "off" value="Turn Off">')
print('</form>')