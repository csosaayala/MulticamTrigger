from machine import reset
from machine import Pin
import time

L0=Pin(0,Pin.OUT)
L1=Pin(1,Pin.OUT)
L2=Pin(2,Pin.OUT)
L3=Pin(3,Pin.OUT)
L4=Pin(4,Pin.OUT)
L5=Pin(5,Pin.OUT)
L6=Pin(6,Pin.OUT)
L7=Pin(7,Pin.OUT)
L8=Pin(8,Pin.OUT)
L9=Pin(9,Pin.OUT)
L10=Pin(10,Pin.OUT)
L11=Pin(11,Pin.OUT)
L12=Pin(12,Pin.OUT)
L13=Pin(13,Pin.OUT)
L14=Pin(14,Pin.OUT)
L15=Pin(15,Pin.OUT)
led=Pin(25,Pin.OUT)
NpbC=Pin(20,Pin.IN)
NpbN=Pin(21,Pin.IN)
Nf1 = Pin(16,Pin.OUT)
Ns1 = Pin(17,Pin.OUT)
Nf2 = Pin(18,Pin.OUT)
Ns2 = Pin(19,Pin.OUT)
tc=0.005
tn=0.010
interrupt_flagC=0
interrupt_flagN=0
debounce_time=0

LED=[L0,L1,L2,L3,L4,L5,L6,L7,L8,L9,L10,L11,L12,L13,L14,L15]
TRIG=[Nf1,Ns1,Nf2,Ns2]

def button_handlerC(irq):
    global interrupt_flagC, debounce_time    
    if time.ticks_ms()-debounce_time > 450:
        interrupt_flagC=1
        debounce_time=time.ticks_ms()
def button_handlerN(irq):
    global interrupt_flagN, debounce_time    
    if time.ticks_ms()-debounce_time > 450:
        interrupt_flagN=1
        debounce_time=time.ticks_ms()
        
NpbC.irq(trigger = Pin.IRQ_FALLING, handler = button_handlerC)
NpbN.irq(trigger = Pin.IRQ_FALLING, handler = button_handlerN)

def LedRunC():
    for led in LED:
        led.value(1)
        time.sleep(tc)
        
        if led == L3:
            led.value(1)
        elif led == L8:
            led.value(1)
        elif led == L13:
            led.value(1)
        else:
         led.value(0)

def LedRunN():
    for led in LED:
        led.value(1)
        time.sleep(tn)
        
        if led == L3:
            led.value(1)
        elif led == L8:
            led.value(1)
        elif led == L13:
            led.value(1)
        else:
         led.value(0)
         
def LedStop():
    for led in LED:
        led.value(0)
        
def TriggerC():
    Nf1.value(1)
    Ns1.value(1)
    time.sleep(0.105)
    Nf1.value(0)
    Ns1.value(0)
    LedRunC()
    
def TriggerN():   
    Ns2.value(1)
    Nf2.value(1)
    time.sleep(0.100)
    Ns2.value(0)             
    Nf2.value(0)
    LedRunN()
    
while True:
    if interrupt_flagC is 1:
        print(interrupt_flagC)
        interrupt_flagC=0
        print("Canon")
        print(interrupt_flagC)
        TriggerC()
        LedStop()
     
    elif interrupt_flagN is 1:
        print(interrupt_flagN)
        interrupt_flagN=0
        print("Nikon")
        print(interrupt_flagN)
        TriggerN()
        LedStop()

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        