from machine import Pin
import utime
pir_sensor=Pin(28,Pin.IN)
led = Pin(15,Pin.OUT)
buzzer=Pin(16,Pin.OUT)
while True:
    if pir_sensor.value()==1:
        for i in range(50):
            led.toggle()
            buzzer.toggle()
            utime.sleep(0.1)
            
        else:
            led.value(0)
            buzzer.value(0)
    