from machine import Pin, Timer, PWM
from rp2 import PIO, asm_pio

@asm_pio()    
def PIO_COUNTER():
    mov(x,0)  # Initialize x to be 0
    label('loop')
    mov(isr,x)  # Move the value of x to isr
    wait(0,pin,0)  # Wait for a low signal on the pin
    wait(1,pin,0)  # Wait for a high signal on the pin
    jmp(x_dec,'loop')  # Jump to 'loop' label if x is not zero
    jmp('loop')  # Jump to 'loop' label

counter = 0
secFlag = False
pulsePerSecond = 0

def GetPulse(timer):
    global counter
    global secFlag
    global pulsePerSecond
    sm0.exec('push()')  # Execute push instruction on StateMachine sm0
    _tcount = sm0.get()  # Get the value from StateMachine sm0
    pulsePerSecond = counter - _tcount  # Calculate the difference between the current counter value and the previous counter value
    counter = _tcount  # Update the counter value
    secFlag = True  # Set secFlag to True

pwm = PWM(Pin(14))
pwm.freq(25_000_000)  # Set PWM frequency to 25MHz
pwm.duty_u16(32768)  # Set PWM duty cycle to 50%

sm0 = rp2.StateMachine(0)
sm0.init(PIO_COUNTER, freq=125_000_000, in_base=Pin(15, Pin.IN))  # Initialize StateMachine sm0 with PIO_COUNTER program and 125MHz frequency
sm0.active(1)  # Activate StateMachine sm0

timer = Timer()
timer.init(freq=1.0, mode=Timer.PERIODIC, callback=GetPulse)  # Initialize timer with 1Hz frequency and GetPulse callback function

try:
    while True:
        if secFlag:
            p = pulsePerSecond
            if p < 0:
                p = p + 2**32  # Handle overflow if p is negative
            print(p)  # Print pulse count per second
            secFlag = False  # Reset secFlag
except KeyboardInterrupt:
    pass  # Handle keyboard interrupt
