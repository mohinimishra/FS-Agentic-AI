# Build a smart smart thermostat alert System
# If the "device_status" is "active"  
    # And temp > 35 - Warn High Temprature Alert 
#If device is "off"
    # return "Device is Offline"

device_status = "active"
temp = 30

if device_status == "active":
    if temp >35:
        print(f"High Alert Temprature is above 35% C")
    else:
        print(f"Normal Temprature")
else:
    print(f"Device is Offline")
    