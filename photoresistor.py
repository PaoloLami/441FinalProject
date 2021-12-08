import PCF8591 as PCF8591

sens = PCF8591(0x48)

light = sens.read(1)*10 #reads data from the photoresistor
print(light)