import serial
from serial.tools import list_ports

VID_Ser = "2341"
PID_Ser = "0043" #Uno

device_list = list_ports.comports()

for device in device_list:
    if (device.vid != None or device.pid != None):
        if ('{:04X}'.format(device.vid) == VID_Ser and
            '{:04X}'.format(device.pid) == PID_Ser):
            port_Ser = device.device
            print(port_Ser)

ser_Ser = serial.Serial(baudrate=9600, timeout=0.1)
ser_Ser.port = port_Ser

try:
    ser_Ser.open()
except:
    print("Serial Port not connect")
    
    
    
try:    
    if ser_Ser.inWaiting():
        tmpstr = (ser_Ser.readline())
        print(tmpstr)
        try:
            strtmp = tmpstr.decode()
            #strData = strtmp.split(",")  
            
            
        except:
            print("Error Read Serial Port")     
            ser_Ser.close()
            try:
                ser_Ser.open()
            except:
                print("Serial Port not connect")
except:
    # print("Error Read Pump")        
    a=1

