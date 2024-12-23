# code here
from machine import PWM, Pin,ADC
import time
import utime
from lib.dcmotor import DCMotor
from lib.servo import Servo
from lib.ota import OTA

# initialize OTA

ota_updater = OTAUpdater("Orange_AB2F", "6mE8R3iBhD4M", firmware_url, "boot.py")
ota_updater.download_and_install_update_if_available()


# Initialize Pins


#water_level = ADC(Pin(25, Pin.IN))
m1_1 = Pin(4, Pin.OUT)
m1_2 = Pin(5, Pin.OUT)
m1_en = PWM(Pin(32), freq=1000)
m2_1 = Pin(22, Pin.OUT)
m2_2 = Pin(23, Pin.OUT)
m2_en = PWM(Pin(33), freq=1000)
r_motor = DCMotor(m1_1, m1_2, m1_en)
l_motor = DCMotor(m2_1, m2_2, m2_en)
pump = Pin(19, Pin.OUT) # 19 to 13
servo = Servo(pin=13)
l_sensor = ADC(Pin(26, Pin.IN))
c_sensor = ADC(Pin(14, Pin.IN)) ## change 
r_sensor = ADC(Pin(27, Pin.IN))

l_sensor.atten(ADC.ATTN_11DB)
c_sensor.atten(ADC.ATTN_11DB)
r_sensor.atten(ADC.ATTN_11DB)

l_sensor.width(ADC.WIDTH_12BIT)
c_sensor.width(ADC.WIDTH_12BIT)
r_sensor.width(ADC.WIDTH_12BIT)


#water_level.atten(ADC.ATTN_11DB)
#water_level.width(ADC.WIDTH_12BIT)





servo.move(0)
time.sleep(1)
servo.move(90)

def Feedback():
    valR = r_sensor.read()
    valL = l_sensor.read()
    valC = c_sensor.read()
    
    if (valC < valR and valC < valL):

        TurnForward()
    elif (valR < valC and valR < valL):

        TurnLeft()
    elif (valL < valC and valL < valR):

        TurnRight()
    elif (valC == 4095 and valL == 4095 and valR == 4095):
        TurnStop()
    else:
        pass
        
    #check_fire()




def CheckTank():
    
    val = water_level.read()
    
    if val < 1500:
        print("Fill The Tank!")
    

def MovementOfServo():
    
    servo.move(45)
    time.sleep(0.5)
    servo.move(135)
    time.sleep(0.5)
    
    

    

# functions

def TurnLeft():
    
    # Make Robot To Go To Left Drive
    r_motor.forward(100)
    l_motor.stop()
    
def TurnRight():
    # Make Robot To Go To Right Drive
    l_motor.forward(100)
    r_motor.stop()
    
def TurnForward():
    # Make Robot To Go To Forward
    l_motor.forward(100)
    r_motor.forward(100)

def TurnStop():
    # Make Robot To Stop From Motion
    l_motor.stop()
    r_motor.stop()

def StartPumpWater():
    # Make Robot Pump Water on Fire
    pump.on()
    MovementOfServo()
    pass

def StopPumpWater():
    pump.off()
    # Make Robot Stop Pump Water
    pass

def check_fire():
    
    #check from where fire -> which sensor that close to near fire to take command
    c_read = c_sensor.read()
    l_read = l_sensor.read()
    r_read = r_sensor.read()
    if (c_read < 100 or l_read < 100 or r_read < 100):     
        print("Fire near!!!!", c_read, r_read, l_read)
        TurnStop()
        StartPumpWater()
    else:
        StopPumpWater()




while True:
    
    valR = r_sensor.read()
    valL = l_sensor.read()
    valC = c_sensor.read()
    
    if (valC < valR and valC < valL):

        TurnForward()
    elif (valR < valC and valR < valL):

        TurnLeft()
    elif (valL < valC and valL < valR):

        TurnRight()
    elif (valC == 4095 and valL == 4095 and valR == 4095):
        TurnStop()
    else:
        TurnStop()
        
    check_fire()
    time.sleep(0.00001)

 

    
 



