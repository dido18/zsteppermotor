# ustep
# Created at 2020-05-20 06:26:57.434174
import streams
import sfw
import gc
import timers


@native_c("upulse",["upulse.c"])
def upulse(pin, us, n_pulse):
    pass


pinMode(D23, OUTPUT)
digitalWrite(D23, LOW)

streams.serial()

while True:
    try:
        
        res = system_fr(D23, 20,15)
        
    except Exception as e:
        print(e)
    
    sleep(2000)
    sfw.kick()
    print('.')