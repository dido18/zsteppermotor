###############################################################################
#  Stepper motor
###############################################################################
import streams
import adc
import sfw
import gc

stepPin =  D23
dirPin =  D22

thunbVrx =  A4
thunbVry =  A7

pinMode(dirPin, OUTPUT)
pinMode(stepPin, OUTPUT)
digitalWrite(stepPin, LOW)
   
streams.serial()

@native_c("upulse",["upulse.c"])
def upulse(pin, us, n_pulse):
    pass


def get_x():
    x = adc.read(thunbVrx) 
    print(x)
    return x

def get_y():
    y =  adc.read(thunbVry) # values from 0 to 4095
    print(y)
    return y

# read mid-point x and y values 
def calibrate():
    global mid_x, mid_y
    mid_x = get_x()
    mid_y = get_y()


# read x and y values and return a direction
def get_direction(thr=.2):
    x = get_x()
    y = get_y()
        
    m_x = abs(x-mid_x)/mid_x
    m_y = abs(y-mid_y)/mid_y
    
    if m_x < thr and m_y < thr:
        return 'center'
    
    if m_x > m_y:
        if x > mid_x:
            return 'right'
        else:
            return 'left'
    else:
        if y > mid_y:
            return 'down'
        else:
            return 'up'
# Function for reading the Potentiometer
def speedUp():
  yDelay =  get_y() # values from 0 to 4095
  newDelay = map(yDelay, 0, 4095, 500, 4000) # Convrests the read values of the potentiometer from 0 to 4095 into desireded delay values (500 to 4000)
  return newDelay 

def map( x, in_min,  in_max,  out_min, out_max):
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min;

# calibrate the thumbstick 
calibrate()

while True:
    try:
        delay = speedUp()
        print(delay)
        upulse(stepPin, delay, 200)
        sleep(2)
        #dir = get_direction()
        
        #if dir == "right":
        #    print("To rigth")
        #    digitalWrite(dirPin, HIGH)
        #if dir == "left":
        #    print("To left")
        #    digitalWrite(dirPin, LOW) 
        #if dir == "down":
        #    print("To down")
        #    digitalWrite(dirPin, LOW) 
        #if dir == "up":
        #    print("To up")
        #    digitalWrite(dirPin, HIGH)
        
        #if dir == "center":
        #  print("No move...")
        #else:
          #upulse(stepPin, 500, 20)
          #digitalWrite(stepPin,HIGH)
          #sleep(1) 
          #digitalWrite(stepPin,LOW)
          #sleep(1)
            
    except Exception as e:
        print(e)
